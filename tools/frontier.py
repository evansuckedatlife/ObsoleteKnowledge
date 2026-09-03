#!/usr/bin/env python3
"""Alias-aware frontier map for the ObsoleteKnowledge vault.

A "frontier" target is a `[[wikilink]]` that resolves to nothing: no node file,
no list, no tour, and no `aliases:`/`defines:` entry on an existing node. Those
targets are the vault's own record of what it keeps reaching for but never
wrote, and they are the queue a BFS expansion wave works through.

Frontmatter is parsed with PyYAML, never with regex. Obsidian rewrites flow
style (`aliases: [x]`) into block style (`aliases:\\n  - x`) whenever it saves a
note, and a regex like `^aliases:\\s*(.*)$` silently swallows the first list
item because `\\s*` crosses the newline -- which drops the alias entirely on
single-alias nodes and makes an existing node look missing.

Usage:
    python tools/frontier.py                    # human-readable report
    python tools/frontier.py --json             # full machine-readable map
    python tools/frontier.py --json --min-refs 2
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required:  python -m pip install pyyaml")

FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n---", re.S)
# `[` must be excluded from the capture, not just `]`. A malformed nested link
# such as `[[['[[tidal-disruption` otherwise yields the target `[[tidal-...`,
# which propagates into the build queue and produces a file literally named
# `[[cold-war.md`.
WIKILINK = re.compile(r"\[\[([^\[\]\|#]+)")

# Root-level docs that are legitimate link targets but are not nodes.
ROOT_DOCS = {
    "index", "readme", "claude", "vision", "agents", "project", "build-order",
    "all", "read", "unread",
}


def read_text(path: str) -> str:
    """Read preserving line endings; every writer in this repo emits CRLF."""
    with open(path, encoding="utf-8", errors="replace", newline="") as fh:
        return fh.read()


def slugify(value) -> str:
    return str(value).strip().strip("\"'").lower().replace(" ", "-")


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return {}
    return data if isinstance(data, dict) else {}


def as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def link_basename(value) -> str:
    """`"[[a/b|C]]"` -> `b`. Frontmatter link refs and bare slugs both work."""
    raw = str(value).strip().strip("\"'")
    raw = raw.strip("[]")
    raw = raw.split("|")[0].split("#")[0]
    return slugify(raw.split("/")[-1])


def build(root: str) -> dict:
    join = lambda *p: os.path.join(root, *p)

    node_paths = sorted(glob.glob(join("concepts", "*", "*.md")))
    list_paths = sorted(glob.glob(join("lists", "*.md")))
    tour_paths = sorted(glob.glob(join("tours", "*.md")))

    nodes: dict[str, dict] = {}
    aliases: set[str] = set()

    for path in node_paths:
        slug = os.path.basename(path)[:-3]
        fm = parse_frontmatter(read_text(path))
        nodes[slug] = {
            "path": os.path.relpath(path, root).replace("\\", "/"),
            "category": fm.get("category") or "?",
            "type": fm.get("type") or "?",
            "lists": [link_basename(x) for x in as_list(fm.get("lists"))],
            "tour_order": fm.get("tour_order", 0),
            "read": bool(fm.get("read")),
        }
        for key in ("aliases", "defines"):
            for entry in as_list(fm.get(key)):
                token = slugify(entry)
                if token:
                    aliases.add(token)

    resolvable = set(nodes) | aliases | ROOT_DOCS
    resolvable |= {os.path.basename(p)[:-3].lower() for p in list_paths}
    resolvable |= {os.path.basename(p)[:-3].lower() for p in tour_paths}

    # Who points at what.
    inbound: dict[str, set[str]] = collections.defaultdict(set)
    regions: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)

    sources = node_paths + list_paths + [join("index.md")]
    for path in sources:
        if not os.path.exists(path):
            continue
        slug = os.path.basename(path)[:-3]
        category = nodes.get(slug, {}).get("category", "list")
        for target in WIKILINK.findall(read_text(path)):
            target = slugify(target.split("/")[-1])
            if target and target not in resolvable:
                inbound[target].add(slug)
                regions[target][category] += 1

    missing = []
    for target, srcs in inbound.items():
        spread = regions[target]
        # Deterministic owner: the category most of the referrers live in,
        # ties broken alphabetically so partitions are reproducible.
        owner = min(spread.items(), key=lambda kv: (-kv[1], kv[0]))[0]
        cats = sorted(c for c in spread if c != "list")
        missing.append({
            "slug": target,
            "refs": len(srcs),
            "owner": owner,
            "sources": sorted(srcs),
            "regions": dict(spread),
            "merge": len(cats) >= 2,          # two BFS trees touched here
            "merge_regions": cats if len(cats) >= 2 else [],
        })
    missing.sort(key=lambda m: (-m["refs"], m["slug"]))

    return {
        "root": os.path.abspath(root),
        "counts": {
            "nodes": len(nodes),
            "lists": len(list_paths),
            "tours": len(tour_paths),
            "aliases": len(aliases),
            "resolvable": len(resolvable),
            "missing_targets": len(missing),
            "dangling_refs": sum(m["refs"] for m in missing),
            "read": sum(1 for n in nodes.values() if n["read"]),
        },
        "categories": sorted({n["category"] for n in nodes.values()}),
        "nodes": nodes,
        "missing": missing,
    }


def report(data: dict, top: int) -> None:
    c = data["counts"]
    print(f"nodes {c['nodes']}  lists {c['lists']}  tours {c['tours']}  "
          f"aliases/defines {c['aliases']}  read {c['read']}")
    print(f"missing targets {c['missing_targets']}   dangling refs {c['dangling_refs']}")

    tiers = [(8, 10**6), (6, 7), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1)]
    print("\n tier   slugs     refs")
    for lo, hi in tiers:
        sel = [m for m in data["missing"] if lo <= m["refs"] <= hi]
        label = f"{lo}+" if hi > 1000 else (f"{lo}" if lo == hi else f"{lo}-{hi}")
        print(f"{label:>5} {len(sel):>7} {sum(m['refs'] for m in sel):>8}")

    merges = [m for m in data["missing"] if m["merge"]]
    print(f"\nmerge points (referenced from 2+ categories): {len(merges)}")
    for m in merges[:15]:
        print(f"  {m['refs']:>3}  {m['slug']:<34} {'+'.join(m['merge_regions'])}")

    print(f"\ntop {top} frontier targets:")
    for m in data["missing"][:top]:
        print(f"  {m['refs']:>3}  {m['slug']:<38} owner={m['owner']}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ap.add_argument("--json", action="store_true", help="emit the full map as JSON")
    ap.add_argument("--min-refs", type=int, default=0, help="drop targets below this ref count")
    ap.add_argument("--out", help="write JSON here instead of stdout")
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--no-nodes", action="store_true", help="omit the node table from JSON")
    args = ap.parse_args()

    data = build(args.root)
    if args.min_refs:
        data["missing"] = [m for m in data["missing"] if m["refs"] >= args.min_refs]
    if args.no_nodes:
        data.pop("nodes", None)

    if args.json or args.out:
        blob = json.dumps(data, indent=2, sort_keys=False)
        if args.out:
            with open(args.out, "w", encoding="utf-8", newline="\r\n") as fh:
                fh.write(blob)
            print(f"wrote {args.out}  ({len(blob):,} bytes)")
        else:
            print(blob)
    else:
        report(data, args.top)


if __name__ == "__main__":
    main()
