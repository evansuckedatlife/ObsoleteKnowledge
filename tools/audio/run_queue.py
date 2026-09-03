#!/usr/bin/env python3
"""Render and publish a queue of episodes, one at a time.

This replaces a shell `while read` loop, which produced three separate bugs:
Python's text-mode write turned the queue's newlines into CRLF so every path
had a trailing carriage return; the inner `python` inherited the loop's stdin
and ate queue lines, turning `african-american-...` into `can-american-...`;
and piping to `tail` was accidentally the only thing making the loop wait for
a render to finish. Doing it in one process removes all three.

Usage:
    python tools/audio/run_queue.py --queue _scratch/build_queue.txt
    python tools/audio/run_queue.py --queue q.txt --limit 5 --no-publish
"""

from __future__ import annotations

import argparse
import io
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WORK = os.path.join(HERE, "work")


def run(argv, timeout=None):
    """Always detach stdin: a child that inherits it can eat the queue."""
    return subprocess.run(
        argv, cwd=ROOT, stdin=subprocess.DEVNULL,
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        timeout=timeout,
    )


def last_meaningful(text: str) -> str:
    for line in reversed((text or "").splitlines()):
        line = line.strip()
        if len(line) > 12 and not line.startswith(("File \"", "  ", "~", "^")):
            return line[:160]
    return "(no output)"


def renders_running() -> int:
    ps = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         "(Get-CimInstance Win32_Process -Filter \"Name like 'python%'\" | "
         "Where-Object { $_.CommandLine -like '*audio*build.py*' }).Count"],
        capture_output=True, text=True, stdin=subprocess.DEVNULL,
    ).stdout.strip()
    try:
        return int(ps)
    except ValueError:
        return -1


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--queue", required=True)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--no-publish", action="store_true")
    ap.add_argument("--keep-audio", action="store_true", default=True)
    args = ap.parse_args()

    with io.open(os.path.join(ROOT, args.queue), encoding="utf-8") as fh:
        queue = [l.strip() for l in fh if l.strip()]
    if args.limit:
        queue = queue[: args.limit]

    todo = [e for e in queue
            if not os.path.exists(os.path.join(WORK, e, "episode.mp3"))]
    print(f"{len(queue)} queued, {len(todo)} to render", flush=True)

    built = published = failed = 0
    started = time.time()

    for i, ep in enumerate(todo, 1):
        mp3 = os.path.join(WORK, ep, "episode.mp3")
        wav = os.path.join(WORK, ep, "episode.wav")

        n = renders_running()
        if n > 1:
            print(f"!! {n} renders already running - stopping so they do not "
                  f"stack and exhaust memory", flush=True)
            break

        print(f"[{i}/{len(todo)}] {ep}", flush=True)
        proc = run([sys.executable, os.path.join(HERE, "build.py"),
                    "--episode", ep])
        if not os.path.exists(mp3):
            failed += 1
            print(f"    FAILED: {last_meaningful(proc.stdout + proc.stderr)}",
                  flush=True)
            if os.path.exists(wav):
                os.remove(wav)
            continue

        built += 1
        print(f"    {last_meaningful(proc.stdout)}", flush=True)
        if os.path.exists(wav):
            os.remove(wav)

        if not args.no_publish:
            pub = run([sys.executable, os.path.join(HERE, "publish.py"),
                       "--episode", ep] + (["--keep-audio"] if args.keep_audio else []))
            out = pub.stdout or ""
            if pub.returncode == 2 or "RATE LIMITED" in out:
                print("    rate limited - stopping. Re-run later, or "
                      "`publish.py --pending` to drain.", flush=True)
                break
            if "done:" in out:
                published += 1
            else:
                print(f"    publish: {last_meaningful(out + pub.stderr)}", flush=True)

        mins = (time.time() - started) / 60
        print(f"    ({built} built, {published} published, {failed} failed, "
              f"{mins:.0f} min elapsed)", flush=True)

    print(f"\n{built} built, {published} published, {failed} failed")


if __name__ == "__main__":
    main()
