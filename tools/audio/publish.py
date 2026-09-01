#!/usr/bin/env python3
"""Publish a built episode to Spotify as a private Personal Podcast.

One Spotify *show* per vault category, one *episode* per tour, one *chapter*
per node. Show ids and uploaded episode ids are recorded in state.json, so a
re-run skips anything already published and a rate limit or crash costs
nothing but the time already spent.

Usage:
    python tools/audio/publish.py --episode greek-heroes
    python tools/audio/publish.py --episode greek-heroes --keep-audio
    python tools/audio/publish.py --status
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from covers import make_cover  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = os.path.join(ROOT, "tools", "audio", "work")
STATE = os.path.join(ROOT, "tools", "audio", "state.json")

SHOW_BLURB = {
    "mythology": "Gods, heroes and monsters.",
    "history": "Leaders, wars, revolutions and empires.",
    "literature": "Authors, works and movements.",
    "science": "Physics, chemistry, biology and earth science.",
    "mathematics": "Theorems, structures and the people behind them.",
    "geography": "Rivers, mountains, deserts and nations.",
    "religion": "Traditions, texts and founders.",
    "philosophy": "Thinkers, schools and problems.",
    "visual-art": "Painters, sculptors, movements and museums.",
    "music": "Composers, works and theory.",
    "performance": "Ballet, opera, theatre and dance.",
    "pop-culture": "Film, television, games and the modern canon.",
    "social-science": "Psychology, economics, linguistics and anthropology.",
    "sports": "Athletes, tournaments and records.",
    "misc": "Everything that fits nowhere else.",
}


def cli() -> str:
    for cand in (
        shutil.which("save-to-spotify"),
        os.path.expanduser("~/AppData/Local/save-to-spotify/save-to-spotify.exe"),
    ):
        if cand and os.path.exists(cand):
            return cand
    sys.exit("save-to-spotify CLI not found")


def run(*argv, check=True) -> dict | str:
    proc = subprocess.run([cli(), *argv], capture_output=True, text=True)
    if check and proc.returncode != 0:
        sys.exit(f"save-to-spotify {' '.join(argv)} failed:\n{proc.stderr or proc.stdout}")
    out = (proc.stdout or "").strip()
    for line in reversed(out.splitlines()):
        line = line.strip()
        if line.startswith("{") or line.startswith("["):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue
    return out


def load_state() -> dict:
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as fh:
            return json.load(fh)
    return {"shows": {}, "episodes": {}}


def save_state(state: dict) -> None:
    with open(STATE, "w", encoding="utf-8", newline="\r\n") as fh:
        json.dump(state, fh, indent=2)


def dig(obj, *keys):
    for k in keys:
        if isinstance(obj, dict) and k in obj:
            return obj[k]
    if isinstance(obj, dict):
        for v in obj.values():
            if isinstance(v, (dict, list)):
                found = dig(v, *keys)
                if found:
                    return found
    if isinstance(obj, list):
        for v in obj:
            found = dig(v, *keys)
            if found:
                return found
    return None


def ensure_show(state: dict, category: str) -> str:
    if category in state["shows"]:
        return state["shows"][category]
    title = f"ObsoleteKnowledge — {category.replace('-', ' ').title()}"
    summary = SHOW_BLURB.get(category, "A guided tour of the collection.")
    cover = make_cover(category.replace("-", " ").title(),
                       os.path.join(WORK, "_covers", f"show-{category}.jpg"),
                       key=f"show:{category}")
    res = run("--json", "shows", "create", "--title", title, "--summary", summary,
              "--image", cover)
    show_id = dig(res, "id", "show_id", "uri")
    if not show_id:
        sys.exit(f"could not read a show id from: {res}")
    state["shows"][category] = show_id
    save_state(state)
    print(f"created show {title} -> {show_id}")
    return show_id


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--episode")
    ap.add_argument("--keep-audio", action="store_true",
                    help="keep the local mp3 after a confirmed upload")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    state = load_state()

    if args.status:
        print(json.dumps(state, indent=2))
        return
    if not args.episode:
        ap.error("need --episode or --status")

    epdir = os.path.join(WORK, args.episode)
    with open(os.path.join(epdir, "plan.json"), encoding="utf-8") as fh:
        plan = json.load(fh)
    mp3 = os.path.join(epdir, "episode.mp3")
    timeline = os.path.join(epdir, "timeline.json")
    if not os.path.exists(mp3):
        sys.exit(f"no audio at {mp3} — run build.py first")

    if args.episode in state["episodes"]:
        print(f"{args.episode} already published: {state['episodes'][args.episode]['episode_id']}")
        return

    show_id = ensure_show(state, plan["category"])
    summary = (f"{len(plan['nodes'])} topics: "
               + ", ".join(n["title"] for n in plan["nodes"][:12]))[:600]

    cover = os.path.join(epdir, "cover.jpg")
    if not os.path.exists(cover):
        cover = make_cover(plan["title"], cover, key=plan["episode_id"])

    print(f"uploading {args.episode} ({os.path.getsize(mp3) / 1e6:.1f} MB)...")
    res = run("--json", "--timeout", "10m", "upload", mp3,
              "--title", plan["title"], "--show-id", str(show_id),
              "--summary", summary, "--image", cover)
    episode_id = dig(res, "episode_id", "id", "uri")
    if not episode_id:
        sys.exit(f"could not read an episode id from: {res}")
    print(f"  episode {episode_id}")

    run("episodes", "status", str(episode_id), "--wait", "5m", check=False)

    if os.path.exists(timeline):
        run("timeline", "set", "--episode-id", str(episode_id),
            "--from-file", timeline, check=False)
        with open(timeline, encoding="utf-8") as fh:
            n = len(json.load(fh)["items"])
        print(f"  {n} chapters set")

    state["episodes"][args.episode] = {
        "episode_id": str(episode_id),
        "show_id": str(show_id),
        "title": plan["title"],
        "nodes": [n["slug"] for n in plan["nodes"]],
        "cache_keys": [n["cache_key"] for n in plan["nodes"]],
    }
    save_state(state)

    if not args.keep_audio:
        os.remove(mp3)
        print("  local mp3 removed (it lives in Spotify now; --keep-audio to retain)")

    print(f"done: {plan['title']} -> Spotify > Your Library")


if __name__ == "__main__":
    main()
