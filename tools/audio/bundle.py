#!/usr/bin/env python3
"""Resolve a tour (or a whole category) into an ordered, narratable bundle.

Membership and ordering mirror `_dv/tourpage.js` exactly, because that is what
the vault shows you in Obsidian:

    normal tour   members = nodes whose `lists` contains the tour slug,
                            sorted by `tour_order` ascending
    <cat>-core    members = nodes in that category with empty/absent `lists`

Emits a plan.json per episode listing each node, its speakable text, and the
cache key for its narration. Long tours are split into parts so an episode
stays a listenable length rather than a seven-hour slog.

Usage:
    python tools/audio/bundle.py --tour greek-heroes
    python tools/audio/bundle.py --category mythology
    python tools/audio/bundle.py --list-tours
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import frontier  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = os.path.join(ROOT, "tools", "audio", "work")
CACHE = os.path.join(ROOT, "tools", "audio", ".cache", "narration")

MAX_NODES_PER_EPISODE = 18

FENCE = re.compile(r"```.*?```", re.S)
HTML_COMMENT = re.compile(r"<!--.*?-->", re.S)
INLINE_FIELD = re.compile(r"`INPUT\[[^\]]*\]`")
WIKILINK_PIPED = re.compile(r"\[\[([^\]\|#]+)\|([^\]]+)\]\]")
WIKILINK_BARE = re.compile(r"\[\[([^\]\|#]+)\]\]")
MD_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
EMPHASIS = re.compile(r"(\*\*|\*|`)")


def speakable(text: str) -> str:
    """Markdown node body -> plain prose a narrator can read.

    Everything Obsidian-specific comes out: frontmatter, dataviewjs and base
    fences, the HTML section markers, the Meta Bind read toggle, and the
    footer (which is navigation, not content).
    """
    body = frontier.FRONTMATTER.sub("", text, count=1)

    marker = body.find("<!-- footer -->")
    if marker != -1:
        body = body[:marker]

    body = FENCE.sub("", body)
    body = HTML_COMMENT.sub("", body)
    body = INLINE_FIELD.sub("", body)

    body = WIKILINK_PIPED.sub(r"\2", body)
    body = WIKILINK_BARE.sub(lambda m: m.group(1).replace("-", " "), body)
    body = MD_LINK.sub(r"\1", body)
    body = EMPHASIS.sub("", body)

    # Drop the see-also line: it is a bare list of peer links, useless aloud.
    out, skip = [], False
    for line in body.splitlines():
        low = line.strip().lower()
        if low.startswith("#"):
            skip = low.lstrip("# ").startswith("see also")
        if not skip:
            out.append(line)

    body = "\n".join(out)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def cache_key(slug: str, clean: str) -> str:
    """Content-addressed: edit a node and only that node re-narrates."""
    return hashlib.sha256(f"{slug}\n{clean}".encode("utf-8")).hexdigest()[:32]


def title_of(text: str, slug: str) -> str:
    m = re.search(r"^#\s+(.+)$", frontier.FRONTMATTER.sub("", text, count=1), re.M)
    return m.group(1).strip() if m else slug.replace("-", " ").title()


def tour_members(data: dict, tour: str) -> list[str]:
    nodes = data["nodes"]
    if tour.endswith("-core"):
        category = tour[: -len("-core")]
        members = [s for s, n in nodes.items()
                   if n["category"] == category and not n["lists"]]
    else:
        members = [s for s, n in nodes.items() if tour in n["lists"]]

    def order(slug):
        raw = nodes[slug]["tour_order"]
        try:
            return (int(raw), slug)
        except (TypeError, ValueError):
            return (0, slug)

    return sorted(members, key=order)


def build_episodes(data: dict, tour: str) -> list[dict]:
    members = tour_members(data, tour)
    if not members:
        return []

    entries = []
    for slug in members:
        meta = data["nodes"][slug]
        text = frontier.read_text(os.path.join(data["root"], meta["path"]))
        clean = speakable(text)
        if len(clean.split()) < 40:
            continue
        key = cache_key(slug, clean)
        entries.append({
            "slug": slug,
            "title": title_of(text, slug),
            "path": meta["path"],
            "category": meta["category"],
            "words": len(clean.split()),
            "cache_key": key,
            "cached": os.path.exists(os.path.join(CACHE, key + ".txt")),
            "clean": clean,
        })

    chunks = [entries[i : i + MAX_NODES_PER_EPISODE]
              for i in range(0, len(entries), MAX_NODES_PER_EPISODE)]

    episodes = []
    pretty = tour.replace("-", " ")
    for idx, chunk in enumerate(chunks, 1):
        suffix = f" — Part {idx}" if len(chunks) > 1 else ""
        episodes.append({
            "tour": tour,
            "part": idx,
            "parts": len(chunks),
            "episode_id": f"{tour}-p{idx}" if len(chunks) > 1 else tour,
            "title": pretty[:1].upper() + pretty[1:] + suffix,
            "category": chunk[0]["category"],
            "nodes": chunk,
            "words": sum(e["words"] for e in chunk),
        })
    return episodes


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tour")
    ap.add_argument("--category")
    ap.add_argument("--list-tours", action="store_true")
    ap.add_argument("--root", default=ROOT)
    args = ap.parse_args()

    data = frontier.build(args.root)

    tours = sorted(
        os.path.basename(p)[:-3]
        for p in os.listdir(os.path.join(args.root, "tours"))
        if p.endswith(".md") and p != "INDEX.md"
    )

    if args.list_tours:
        for t in tours:
            n = len(tour_members(data, t))
            if n:
                print(f"{n:>4}  {t}")
        return

    if args.category:
        targets = [t for t in tours
                   if any(data["nodes"][s]["category"] == args.category
                          for s in tour_members(data, t)[:1])]
    elif args.tour:
        targets = [args.tour]
    else:
        ap.error("need --tour, --category or --list-tours")

    os.makedirs(WORK, exist_ok=True)
    os.makedirs(CACHE, exist_ok=True)

    total = 0
    for tour in targets:
        for ep in build_episodes(data, tour):
            out = os.path.join(WORK, ep["episode_id"])
            os.makedirs(out, exist_ok=True)
            with open(os.path.join(out, "plan.json"), "w", encoding="utf-8", newline="\r\n") as fh:
                json.dump(ep, fh, indent=2)
            missing = sum(1 for n in ep["nodes"] if not n["cached"])
            mins = ep["words"] / 150.0
            print(f"{ep['episode_id']:<44} {len(ep['nodes']):>3} nodes  "
                  f"{ep['words']:>6} words  ~{mins:>5.1f} min  "
                  f"{missing} to narrate")
            total += 1
    print(f"\n{total} episode plan(s) in {os.path.relpath(WORK, args.root)}")


if __name__ == "__main__":
    main()
