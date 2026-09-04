#!/usr/bin/env python3
"""Turn classified quiz subjects into agy waves, ordered by what gets asked.

The vault grew as a humanities syllabus: 36.5% of it is history, religion,
mythology and philosophy. Consensus Trivia's published 2027 distribution gives
those areas 16.0%, and gives Popular Culture 23.0% -- where the vault sits at
6.9%. Reach For The Top's answer set says the same thing empirically: the
subjects it asks about and the vault lacks are Fortnite, Billie Eilish,
Christian Siriano and Franklin the Turtle, not more Byzantine emperors.

So the queue is not ordered by reference count like the BFS waves were. It is
ordered by DEFICIT -- how far each area sits below the share of real questions
it has to answer -- so that stopping early still leaves the highest-yield
subjects written.

Exact distribution-matching is deliberately not the target. Social Science is
5.9% of the vault against a 1.0% Consensus weight, and that one constraint
alone would demand a 32,000-node vault before the shares lined up. The goal is
answer coverage, not a pie chart.

Usage:
    python tools/consensus_wave.py --subjects _scratch/classified.json \
        --out _scratch/waves/consensus --per-wave 220
"""

from __future__ import annotations

import argparse
import collections
import io
import itertools
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier
import wave as wavelib
from rftt_topics import canon

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Consensus Trivia 2027 topic distribution, grouped as the vault categorises.
TARGET = {
    "Popular Culture":    (23.0, ["pop-culture", "sports"]),
    "Science & Math":     (17.5, ["science", "mathematics"]),
    "General Knowledge":  (16.0, ["misc"]),
    "Humanities":         (16.0, ["history", "religion", "mythology",
                                  "philosophy"]),
    "Contemporary World": (15.5, ["geography"]),
    "Arts":               (12.0, ["literature", "music", "visual-art",
                                  "performance"]),
    "Social Science":     (1.0,  ["social-science"]),
}


def deficits(counts: collections.Counter) -> dict:
    """Per-category priority: how far its AREA sits below its question share."""
    total = sum(counts.values()) or 1
    share = sum(t for t, _ in TARGET.values())
    out = {}
    for area, (target, cats) in TARGET.items():
        have = sum(counts[c] for c in cats)
        gap = (target / share) - (have / total)
        for c in cats:
            out[c] = gap
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--subjects", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--per-wave", type=int, default=220)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    with io.open(os.path.join(ROOT, args.subjects), encoding="utf-8") as fh:
        subjects = json.load(fh)

    data = frontier.build(ROOT)
    nodes = data["nodes"]

    # A slug merged away lives on as an alias; filtering on basenames alone
    # re-creates it and shadows the alias. Filter on everything resolvable.
    taken = {canon(s) for s in nodes}
    for slug, meta in nodes.items():
        fm = frontier.parse_frontmatter(
            frontier.read_text(os.path.join(ROOT, meta["path"])))
        for key in ("defines", "aliases"):
            for v in frontier.as_list(fm.get(key)):
                taken.add(canon(str(v)))

    counts = collections.Counter(m["category"] for m in nodes.values())
    prio = deficits(counts)

    fresh, dropped = [], collections.Counter()
    seen = set()
    for s in subjects:
        slug, cat = s.get("slug"), s.get("category")
        if not slug or not cat:
            dropped["incomplete"] += 1
            continue
        k = canon(slug)
        if k in taken:
            dropped["already in the vault"] += 1
            continue
        if k in seen:
            dropped["duplicate in the queue"] += 1
            continue
        seen.add(k)
        fresh.append({"slug": slug, "title": s.get("title", slug),
                      "category": cat, "refs": 0, "sources": [],
                      "regions": {}, "merge": False, "merge_regions": []})

    print(f"{len(subjects)} classified -> {len(fresh)} to write")
    for why, n in dropped.most_common():
        print(f"  dropped {n}: {why}")

    print("\npriority by area (deficit against the Consensus distribution):")
    for area, (target, cats) in sorted(
            TARGET.items(), key=lambda kv: -deficits(counts)[kv[1][1][0]]):
        have = sum(counts[c] for c in cats)
        pend = sum(1 for f in fresh if f["category"] in cats)
        print(f"  {area:<20} target {target:>5.1f}%   vault "
              f"{have * 100 / sum(counts.values()):>5.1f}%   queued {pend:>5}")

    fresh.sort(key=lambda f: (-prio.get(f["category"], 0), f["category"],
                              f["slug"]))
    if args.limit:
        fresh = fresh[:args.limit]

    outdir = os.path.join(ROOT, args.out)
    os.makedirs(outdir, exist_ok=True)
    menus = {}
    written = 0
    for i in range(0, len(fresh), args.per_wave):
        chunk = fresh[i:i + args.per_wave]
        batches = []
        for cat, items in itertools.groupby(
                sorted(chunk, key=lambda f: f["category"]),
                key=lambda f: f["category"]):
            items = list(items)
            if cat not in menus:
                menus[cat] = wavelib.hub_menu(data, cat)
            batches.append({"region": cat, "part": 1,
                            "dir": f"concepts/{cat}",
                            "hub_menu": menus[cat],
                            "slugs": items})
        path = os.path.join(outdir, f"wave_{i // args.per_wave:02d}.json")
        with io.open(path, "w", encoding="utf-8", newline="\r\n") as fh:
            json.dump({"selection": {"targets": len(chunk),
                                     "agents": len(batches)},
                       "merge_points": [], "batches": batches}, fh,
                      indent=1, ensure_ascii=False)
        written += 1

    claimed = [f["slug"] for f in fresh]
    assert len(claimed) == len(set(claimed)), "a slug was claimed twice"
    print(f"\nwrote {written} wave file(s) to {args.out}/ "
          f"({len(fresh)} subjects, {args.per_wave} per wave)")


if __name__ == "__main__":
    main()
