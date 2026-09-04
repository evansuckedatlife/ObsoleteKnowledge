#!/usr/bin/env python3
"""Build the work list for a cross-category link-enrichment pass.

Targets, in priority order:
  orphans   nothing links in, so they are unreachable by browsing
  thin      almost no links either way
  insular   in a category whose links overwhelmingly stay inside it

Each target carries its own summary (so an agent can judge what it is) and a
menu of real slugs from OTHER categories (so proposals can actually resolve).

Agents return proposals as DATA and never edit a file: in-place rewrites by
earlier waves clobbered `read:`, which is the user's real reading progress.

Usage:
    python tools/enrich_targets.py --out _scratch/enrich.json --limit 400
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier
import linkaudit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def summary_of(text: str) -> str:
    m = re.search(r"##\s+summary\s*\n+(.+?)(?:\n\n|\n##)", text, re.S)
    if not m:
        return ""
    s = re.sub(r"[*`]", "", m.group(1))
    s = re.sub(r"\[\[([^\]\|#]+)(\|[^\]]+)?\]\]", lambda x: x.group(1).replace("-", " "), s)
    return " ".join(s.split())[:320]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=400)
    ap.add_argument("--batch", type=int, default=12)
    args = ap.parse_args()

    data = frontier.build(ROOT)
    nodes = data["nodes"]
    out_edges = linkaudit.build_graph(data)

    inbound = collections.Counter()
    for a, ts in out_edges.items():
        for b in ts:
            inbound[b] += 1

    # How insular is each category? Drives which categories to pull FROM.
    cross = collections.Counter()
    total = collections.Counter()
    for a, ts in out_edges.items():
        ca = nodes[a]["category"]
        for b in ts:
            total[ca] += 1
            if nodes[b]["category"] != ca:
                cross[ca] += 1
    insularity = {c: 1 - (cross[c] / total[c] if total[c] else 0) for c in total}

    scored = []
    for slug, meta in nodes.items():
        deg = len(out_edges[slug]) + inbound[slug]
        own_cross = sum(1 for t in out_edges[slug]
                        if nodes[t]["category"] != meta["category"])
        # orphans first, then thin, then insular nodes in insular categories
        priority = (0 if inbound[slug] == 0 else
                    1 if deg < 4 else
                    2 if own_cross == 0 else 3)
        if priority == 3:
            continue
        scored.append((priority, -insularity.get(meta["category"], 0), deg, slug))

    scored.sort()
    picked = [s for _, _, _, s in scored[: args.limit]]

    # Hub menu per category: the most-linked nodes OUTSIDE it, so proposals
    # are cross-category by construction and land on real, central targets.
    by_cat = collections.defaultdict(list)
    for slug in nodes:
        by_cat[nodes[slug]["category"]].append(slug)
    ranked = sorted(nodes, key=lambda s: -inbound[s])
    menus = {}
    for cat in by_cat:
        others = [s for s in ranked if nodes[s]["category"] != cat][:70]
        menus[cat] = others

    batches = []
    for i in range(0, len(picked), args.batch):
        chunk = picked[i: i + args.batch]
        cat = nodes[chunk[0]]["category"]
        batches.append({
            "menu": menus[cat],
            "targets": [{
                "slug": s,
                "category": nodes[s]["category"],
                "inbound": inbound[s],
                "outbound": len(out_edges[s]),
                "summary": summary_of(frontier.read_text(
                    os.path.join(ROOT, nodes[s]["path"]))),
                "existing": sorted(out_edges[s])[:10],
            } for s in chunk],
        })

    payload = {"count": len(picked), "batches": batches,
               "insularity": {k: round(v, 3) for k, v in sorted(insularity.items())}}
    with open(os.path.join(ROOT, args.out), "w", encoding="utf-8", newline="\r\n") as fh:
        json.dump(payload, fh, indent=1)

    kinds = collections.Counter(
        "orphan" if inbound[s] == 0 else
        ("thin" if len(out_edges[s]) + inbound[s] < 4 else "insular") for s in picked)
    print(f"{len(picked)} targets in {len(batches)} batches -> {args.out}")
    print("  " + ", ".join(f"{k}={v}" for k, v in kinds.most_common()))
    print("  most insular categories: " + ", ".join(
        f"{c}={insularity[c]:.0%}" for c in sorted(insularity, key=insularity.get,
                                                    reverse=True)[:5]))


if __name__ == "__main__":
    main()
