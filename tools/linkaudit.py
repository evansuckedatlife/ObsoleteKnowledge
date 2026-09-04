#!/usr/bin/env python3
"""Measure how well the vault is actually wired together.

Four things, all exact -- no model needed:

  connectivity   nodes with no inbound links (orphans), and no outbound
  reach          size of the largest connected component; anything outside it
                 is unreachable by browsing, however good the note is
  interdisciplinary  share of links whose target sits in another category.
                 This is the vault's own stated health metric: a fact you can
                 reach from five directions is a fact you keep.
  thin           nodes with few resolving links, which are the real targets
                 for a link-filling pass

Usage:
    python tools/linkaudit.py
    python tools/linkaudit.py --json _scratch/linkaudit.json --thin 4
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build_graph(data):
    """Resolve every wikilink to a node slug, following aliases and defines."""
    nodes = data["nodes"]
    alias_to_node = {}
    for slug, meta in nodes.items():
        fm = frontier.parse_frontmatter(
            frontier.read_text(os.path.join(data["root"], meta["path"])))
        for key in ("aliases", "defines"):
            for v in frontier.as_list(fm.get(key)):
                alias_to_node.setdefault(frontier.slugify(v), slug)

    out = {s: set() for s in nodes}
    for slug, meta in nodes.items():
        text = frontier.read_text(os.path.join(data["root"], meta["path"]))
        body = frontier.FRONTMATTER.sub("", text, count=1)
        for raw in frontier.WIKILINK.findall(body):
            t = frontier.slugify(raw.split("/")[-1])
            tgt = t if t in nodes else alias_to_node.get(t)
            if tgt and tgt != slug:
                out[slug].add(tgt)
    return out


def components(out, nodes):
    """Undirected connected components."""
    adj = collections.defaultdict(set)
    for a, ts in out.items():
        for b in ts:
            adj[a].add(b)
            adj[b].add(a)
    seen, comps = set(), []
    for s in nodes:
        if s in seen:
            continue
        stack, comp = [s], []
        seen.add(s)
        while stack:
            cur = stack.pop()
            comp.append(cur)
            for nxt in adj[cur]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        comps.append(comp)
    return sorted(comps, key=len, reverse=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json")
    ap.add_argument("--thin", type=int, default=4,
                    help="nodes with fewer resolving links than this count as thin")
    args = ap.parse_args()

    data = frontier.build(ROOT)
    nodes = data["nodes"]
    out = build_graph(data)

    inbound = collections.Counter()
    for a, ts in out.items():
        for b in ts:
            inbound[b] += 1

    cross = same = 0
    per_region_cross = collections.Counter()
    per_region_total = collections.Counter()
    for a, ts in out.items():
        ca = nodes[a]["category"]
        for b in ts:
            if nodes[b]["category"] != ca:
                cross += 1
                per_region_cross[ca] += 1
            else:
                same += 1
            per_region_total[ca] += 1

    orphans = sorted(s for s in nodes if inbound[s] == 0)
    dead_ends = sorted(s for s in nodes if not out[s])
    thin = sorted((len(out[s]) + inbound[s], s) for s in nodes)
    comps = components(out, nodes)
    total_links = cross + same

    print(f"nodes {len(nodes)}   resolving links {total_links}")
    print()
    print("CONNECTIVITY")
    print(f"  orphans (nothing links in)   {len(orphans):>5}  "
          f"{100*len(orphans)/len(nodes):4.1f}%")
    print(f"  dead ends (links out to none){len(dead_ends):>5}  "
          f"{100*len(dead_ends)/len(nodes):4.1f}%")
    print(f"  connected components         {len(comps):>5}")
    print(f"  largest component            {len(comps[0]):>5}  "
          f"{100*len(comps[0])/len(nodes):4.1f}% of the vault")
    stranded = sum(len(c) for c in comps[1:])
    print(f"  stranded outside it          {stranded:>5}")
    print()
    print("INTERDISCIPLINARY")
    print(f"  cross-category links {cross:>6}  of {total_links}  "
          f"= {100*cross/total_links:4.1f}%")
    print("  by category (share of that category's links that leave it):")
    for r in sorted(per_region_total, key=lambda r: -per_region_total[r]):
        tot = per_region_total[r]
        print(f"    {r:<16} {per_region_cross[r]:>5} / {tot:<6} "
              f"{100*per_region_cross[r]/tot:5.1f}%")
    print()
    print(f"THIN NODES (fewer than {args.thin} links either way)")
    thin_list = [s for n, s in thin if n < args.thin]
    print(f"  {len(thin_list)} nodes")
    for n, s in thin[:12]:
        if n < args.thin:
            print(f"    {n}  {s} ({nodes[s]['category']})")

    if args.json:
        payload = {
            "totals": {"nodes": len(nodes), "links": total_links,
                       "cross": cross, "cross_pct": round(100*cross/total_links, 2),
                       "orphans": len(orphans), "dead_ends": len(dead_ends),
                       "components": len(comps), "largest": len(comps[0]),
                       "stranded": stranded},
            "orphans": orphans,
            "stranded": [s for c in comps[1:] for s in c],
            "thin": [{"slug": s, "links": n, "category": nodes[s]["category"]}
                     for n, s in thin if n < args.thin],
        }
        with open(os.path.join(ROOT, args.json), "w", encoding="utf-8",
                  newline="\r\n") as fh:
            json.dump(payload, fh, indent=1)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
