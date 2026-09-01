#!/usr/bin/env python3
"""One command: vault tour -> chaptered private episode in your Spotify library.

Chains bundle -> build -> publish, skipping anything already done. The
narration step sits between bundle and build and needs a model, so it is not
run here: this reports exactly which nodes still need narrating and stops.

Usage:
    python tools/audio/run.py --tour greek-heroes
    python tools/audio/run.py --category mythology
    python tools/audio/run.py --category mythology --dry-run
    python tools/audio/run.py --all --limit 5
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WORK = os.path.join(HERE, "work")
CACHE = os.path.join(HERE, ".cache", "narration")
STATE = os.path.join(HERE, "state.json")

MIN_FREE_GB = 2.0


def sh(argv: list[str]) -> int:
    return subprocess.run(argv, cwd=ROOT).returncode


def published() -> set[str]:
    if not os.path.exists(STATE):
        return set()
    with open(STATE, encoding="utf-8") as fh:
        return set(json.load(fh).get("episodes", {}))


def free_gb() -> float:
    return shutil.disk_usage(ROOT).free / 1e9


def plans(selected: list[str]) -> list[dict]:
    out = []
    for name in selected:
        p = os.path.join(WORK, name, "plan.json")
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                out.append(json.load(fh))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--tour")
    g.add_argument("--category")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--voice", default="af_heart")
    ap.add_argument("--keep-audio", action="store_true")
    args = ap.parse_args()

    if free_gb() < MIN_FREE_GB:
        sys.exit(f"only {free_gb():.1f} GB free; need {MIN_FREE_GB} GB headroom for audio")

    # 1. Resolve tours into episode plans.
    bundle = [sys.executable, os.path.join(HERE, "bundle.py")]
    if args.tour:
        bundle += ["--tour", args.tour]
    elif args.category:
        bundle += ["--category", args.category]
    if not args.all and sh(bundle) != 0:
        sys.exit("bundle failed")
    if args.all:
        for cat in sorted({d.split(os.sep)[-1] for d in
                           os.listdir(os.path.join(ROOT, "concepts"))}):
            sh([sys.executable, os.path.join(HERE, "bundle.py"), "--category", cat])

    names = sorted(d for d in os.listdir(WORK)
                   if os.path.isdir(os.path.join(WORK, d)) and not d.startswith("_"))
    if args.tour:
        names = [n for n in names if n == args.tour or n.startswith(args.tour + "-p")]
    eps = plans(names)
    if args.limit:
        eps = eps[: args.limit]

    done = published()
    todo, needs_narration, already = [], [], []
    for ep in eps:
        if ep["episode_id"] in done:
            already.append(ep)
            continue
        missing = [n["slug"] for n in ep["nodes"]
                   if not os.path.exists(os.path.join(CACHE, n["cache_key"] + ".txt"))]
        (needs_narration if missing else todo).append((ep, missing))

    print()
    for ep, missing in needs_narration:
        print(f"  NARRATE  {ep['episode_id']:<40} {len(missing)} node(s) not yet narrated")
    for ep in already:
        print(f"  DONE     {ep['episode_id']:<40} already in Spotify")
    for ep, _ in todo:
        mins = ep["words"] / 150.0
        print(f"  READY    {ep['episode_id']:<40} {len(ep['nodes'])} chapters, ~{mins:.0f} min"
              f"  (~{mins * 1.5:.0f} min to synthesise)")

    if needs_narration:
        print(f"\n{len(needs_narration)} episode(s) need narration first. Narration is a model"
              f"\npass, not a script step — see tools/audio/README.md.")
    if not todo:
        print("\nnothing to build.")
        return
    if args.dry_run:
        total = sum(e["words"] for e, _ in todo) / 150.0
        print(f"\ndry run: {len(todo)} episode(s), ~{total:.0f} min of audio, "
              f"~{total * 1.5 / 60:.1f} h to synthesise. {free_gb():.1f} GB free.")
        return

    for ep, _ in todo:
        eid = ep["episode_id"]
        print(f"\n=== {eid} ===")
        if sh([sys.executable, os.path.join(HERE, "build.py"),
               "--episode", eid, "--voice", args.voice]) != 0:
            print(f"  build failed for {eid}; continuing")
            continue
        pub = [sys.executable, os.path.join(HERE, "publish.py"), "--episode", eid]
        if args.keep_audio:
            pub.append("--keep-audio")
        if sh(pub) != 0:
            print(f"  publish failed for {eid}; audio kept at "
                  f"{os.path.join(WORK, eid, 'episode.mp3')}")
            print("  re-run this command later to retry — nothing is lost")
            break

    print("\nOpen Spotify > Your Library > Podcasts & Shows.")


if __name__ == "__main__":
    main()
