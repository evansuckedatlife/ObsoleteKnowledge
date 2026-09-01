#!/usr/bin/env python3
"""Partition the frontier into disjoint BFS writer assignments.

Each frontier target is owned by exactly one category region (computed in
frontier.py as the category most of its referrers live in, ties broken
alphabetically). Batches are cut inside a region, so two writer agents can
never be handed the same slug and cannot collide on a file.

Emits JSON suitable for passing straight to the Workflow tool as `args`.

Usage:
    python tools/wave.py --min-refs 3 --batch 10 --out _scratch/wave1.json
    python tools/wave.py --min-refs 2 --max-refs 2 --batch 12 --limit 320
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier  # noqa: E402

# Slugs that look like concepts but are structural noise: pluralisation
# artefacts, section labels, and other tokens no node should be created for.
JUNK = re.compile(
    r"^(untitled|index|tbd|todo|n-a|na|none|null|etc|and|the|see-also|"
    r"more|other|others|various|misc|example|examples|note|notes)$"
)


def hub_menu(data: dict, category: str, per_cat: int = 28, global_n: int = 34) -> list[str]:
    """Real, existing slugs a writer may safely link to.

    Without this menu, past waves wasted 50-75% of their links on slugs that
    do not exist. Ranked by inbound links so the menu is the graph's actual
    connective tissue, not an arbitrary sample.
    """
    nodes = data["nodes"]
    inbound = collections.Counter()
    for slug, meta in nodes.items():
        try:
            text = frontier.read_text(os.path.join(data["root"], meta["path"]))
        except OSError:
            continue
        for target in frontier.WIKILINK.findall(text):
            target = frontier.slugify(target.split("/")[-1])
            if target in nodes:
                inbound[target] += 1

    same = [s for s, _ in inbound.most_common() if nodes[s]["category"] == category][:per_cat]
    cross = [s for s, _ in inbound.most_common()
             if nodes[s]["category"] != category and s not in same][:global_n]
    return same + cross


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--min-refs", type=int, default=2)
    ap.add_argument("--max-refs", type=int, default=10**6)
    ap.add_argument("--batch", type=int, default=10, help="slugs per writer agent")
    ap.add_argument("--limit", type=int, default=0, help="cap total slugs this wave")
    ap.add_argument("--max-agents", type=int, default=0, help="cap writer agents this wave")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    data = frontier.build(args.root)
    nodes = data["nodes"]

    targets = [
        m for m in data["missing"]
        if args.min_refs <= m["refs"] <= args.max_refs
        and not JUNK.match(m["slug"])
        and m["owner"] != "list"           # referred to only from list MOCs
        and 2 <= len(m["slug"]) <= 60
    ]
    if args.limit:
        targets = targets[: args.limit]

    by_region: dict[str, list] = collections.defaultdict(list)
    for t in targets:
        by_region[t["owner"]].append(t)

    menus = {cat: hub_menu(data, cat) for cat in by_region}

    batches = []
    for region in sorted(by_region, key=lambda r: -len(by_region[r])):
        items = by_region[region]
        for i in range(0, len(items), args.batch):
            chunk = items[i : i + args.batch]
            batches.append({
                "region": region,
                "part": i // args.batch + 1,
                "dir": f"concepts/{region}",
                "hub_menu": menus[region],
                "slugs": [{
                    "slug": t["slug"],
                    "refs": t["refs"],
                    "sources": t["sources"][:8],
                    "regions": t["regions"],
                    "merge": t["merge"],
                    "merge_regions": t["merge_regions"],
                } for t in chunk],
            })

    # Interleave regions so concurrent agents span different categories: the
    # BFS trees advance in parallel rather than finishing one region at a time.
    batches.sort(key=lambda b: (b["part"], b["region"]))
    if args.max_agents:
        batches = batches[: args.max_agents]

    claimed = [s["slug"] for b in batches for s in b["slugs"]]
    assert len(claimed) == len(set(claimed)), "partition is not disjoint"

    merges = [t for t in targets if t["merge"]]
    payload = {
        "generated_from": {
            "nodes": data["counts"]["nodes"],
            "read": data["counts"]["read"],
            "missing_targets": data["counts"]["missing_targets"],
            "dangling_refs": data["counts"]["dangling_refs"],
        },
        "selection": {
            "min_refs": args.min_refs, "max_refs": args.max_refs,
            "targets": len(targets), "claimed": len(claimed),
            "agents": len(batches), "batch": args.batch,
        },
        "merge_points": [
            {"slug": t["slug"], "refs": t["refs"], "regions": t["merge_regions"]}
            for t in merges
        ],
        "batches": batches,
    }

    with open(args.out, "w", encoding="utf-8", newline="\r\n") as fh:
        json.dump(payload, fh, indent=2)

    print(f"wrote {args.out}")
    print(f"  targets {len(targets)}  claimed {len(claimed)}  agents {len(batches)}")
    print(f"  merge points in this wave: {len(merges)}")
    dist = collections.Counter(b["region"] for b in batches)
    print("  agents per region: " + ", ".join(f"{k}={v}" for k, v in sorted(dist.items())))


if __name__ == "__main__":
    main()
