#!/usr/bin/env python3
"""Find nodes that should be merged away or rewritten, vault-wide.

Four kinds of dead weight accumulate when nodes are written in large automated
waves:

  duplicate   two nodes claiming the same name in `defines`/`aliases` --
              the classic variant-slug duplicate (algorithms / algorithm)
  shadowed    a node whose slug is also an alias on a DIFFERENT node, so the
              alias silently never resolves
  stub        real node, too thin to be worth reading
  vague       a slug that is a description rather than a subject, which is what
              the single-reference tail keeps producing

Reports only. Merging is a judgement call about which node keeps the inbound
links, so nothing is deleted here.

Usage:
    python tools/consolidate.py
    python tools/consolidate.py --json _scratch/consolidate.json
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier
import linkaudit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VAGUE = re.compile(
    r"-(themes?|influence|impact|legacy|overview|context|background|"
    r"significance|comparison|relations?|aspects?|elements?|features?|"
    r"characteristics|role|importance|effects?|uses?|types?|examples?)$"
)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json")
    ap.add_argument("--stub-words", type=int, default=280)
    args = ap.parse_args()

    data = frontier.build(ROOT)
    nodes = data["nodes"]
    out_edges = linkaudit.build_graph(data)
    inbound = collections.Counter()
    for a, ts in out_edges.items():
        for b in ts:
            inbound[b] += 1

    owns = collections.defaultdict(list)   # name -> [slug, ...]
    alias_of = {}                          # alias token -> owning slug
    words = {}
    for slug, meta in nodes.items():
        text = frontier.read_text(os.path.join(ROOT, meta["path"]))
        words[slug] = len(frontier.FRONTMATTER.sub("", text, count=1).split())
        fm = frontier.parse_frontmatter(text)
        for key in ("defines", "aliases"):
            for v in frontier.as_list(fm.get(key)):
                tok = frontier.slugify(v)
                owns[tok].append(slug)
                if key == "aliases":
                    alias_of[tok] = slug

    duplicates = []
    for name, slugs in owns.items():
        uniq = sorted(set(slugs))
        if len(uniq) > 1:
            ranked = sorted(uniq, key=lambda s: -inbound[s])
            duplicates.append({"name": name, "keep": ranked[0],
                               "merge": ranked[1:],
                               "inbound": {s: inbound[s] for s in ranked}})

    shadowed = [{"slug": s, "alias_on": alias_of[s], "inbound": inbound[s]}
                for s in nodes if s in alias_of and alias_of[s] != s]

    stubs = sorted(({"slug": s, "words": words[s], "category": nodes[s]["category"],
                     "inbound": inbound[s]}
                    for s in nodes if words[s] < args.stub_words),
                   key=lambda d: d["words"])

    vague = sorted(({"slug": s, "inbound": inbound[s],
                     "category": nodes[s]["category"]}
                    for s in nodes if VAGUE.search(s)),
                   key=lambda d: (d["inbound"], d["slug"]))

    print(f"vault: {len(nodes)} nodes")
    print()
    print(f"DUPLICATE names (one name claimed by 2+ nodes) : {len(duplicates)}")
    for d in sorted(duplicates, key=lambda d: -max(d["inbound"].values()))[:12]:
        others = ", ".join(f"{s}({d['inbound'][s]})" for s in d["merge"])
        print(f"    '{d['name']}'  keep {d['keep']}({d['inbound'][d['keep']]})  <- {others}")
    print()
    print(f"SHADOWED slugs (node exists AND is an alias elsewhere) : {len(shadowed)}")
    for s in shadowed[:10]:
        print(f"    {s['slug']} ({s['inbound']} in) is aliased on {s['alias_on']}")
    print()
    print(f"STUBS (< {args.stub_words} words) : {len(stubs)}")
    for s in stubs[:10]:
        print(f"    {s['words']:>4}w  {s['slug']} ({s['category']}, {s['inbound']} in)")
    print()
    print(f"VAGUE slugs (description, not subject) : {len(vague)}")
    for v in vague[:10]:
        print(f"    {v['slug']} ({v['category']}, {v['inbound']} in)")

    if args.json:
        with open(os.path.join(ROOT, args.json), "w", encoding="utf-8",
                  newline="\r\n") as fh:
            json.dump({"duplicates": duplicates, "shadowed": shadowed,
                       "stubs": stubs, "vague": vague}, fh, indent=1)
        print(f"\nwrote {args.json}")


if __name__ == "__main__":
    main()
