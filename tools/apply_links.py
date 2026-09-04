#!/usr/bin/env python3
"""Apply verified cross-category links to nodes' `related:` frontmatter.

This is the only step in the enrichment pass that touches existing notes, so
it is deliberately narrow: it rewrites exactly one frontmatter line per node
and nothing else. Earlier waves that let a model edit notes in place destroyed
`read:`, the user's real reading progress, which is why the agents only ever
propose and this applies.

Guards:
  - both endpoints must exist as real node files
  - a link already present is skipped, not duplicated
  - `read:` and `tour_order` are compared before and after on every file and
    the run aborts if either moves
  - CRLF is preserved; the vault is committed CRLF and an LF rewrite would
    show as a whole-file diff and hide what actually changed

Usage:
    python tools/apply_links.py --links _scratch/links.json --dry-run
    python tools/apply_links.py --links _scratch/links.json
"""

from __future__ import annotations

import argparse
import collections
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_RELATED = 14        # keep frontmatter readable


def read(p):
    with io.open(p, encoding="utf-8", newline="") as fh:
        return fh.read()


def write(p, t):
    with io.open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(t)


def set_related(path: str, targets: list[str]) -> bool:
    """Rewrite only the `related:` line. Returns False if nothing changed."""
    text = read(path)
    m = frontier.FRONTMATTER.match(text)
    if not m:
        return False
    nl = "\r\n" if "\r\n" in text else "\n"
    lines = m.group(1).split(nl)

    start = next((i for i, l in enumerate(lines) if l.startswith("related:")), None)
    if start is None:
        return False
    end = start + 1
    while end < len(lines) and lines[end].lstrip().startswith("- "):
        end += 1

    rendered = "related: [" + ", ".join(f'"[[{t}]]"' for t in targets) + "]"
    if lines[start:end] == [rendered]:
        return False
    lines[start:end] = [rendered]
    write(path, text[: m.start(1)] + nl.join(lines) + text[m.end(1):])
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--links", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with open(os.path.join(ROOT, args.links), encoding="utf-8") as fh:
        links = json.load(fh)

    data = frontier.build(ROOT)
    nodes = data["nodes"]

    def repair(s: str, t: str) -> str:
        """Recover a source slug the model packed the pair into.

        Some verifiers ignored the field contract and returned the whole edge
        in `slug` -- `sweatt-v-painter_united-states`, `19th-century-france:
        industrial-revolution`, `20th-century-writers -> poetry`. The `target`
        field stayed correct in every case, so stripping the target off the
        end recovers the real source.
        """
        if s in nodes:
            return s
        for sep in ("_", ":", " -> ", " → ", "->", "→", "-"):
            head = s.split(sep + t)[0] if (sep + t) in s else None
            if head and head.strip(" _:->→") in nodes:
                return head.strip(" _:->→")
        for sep in (" -> ", " → ", "->", "→", ":", "_"):
            if sep in s:
                head = s.split(sep)[0].strip()
                if head in nodes:
                    return head
        return s

    by_slug = collections.defaultdict(list)
    dropped = collections.Counter()
    recovered = 0
    for l in links:
        s, t = l.get("slug"), l.get("target")
        if s and t and s not in nodes:
            fixed = repair(s, t)
            if fixed != s:
                recovered += 1
                s = fixed
        if s not in nodes:
            dropped["source not a node"] += 1
            continue
        if t not in nodes:
            dropped["target not a node"] += 1
            continue
        if s == t:
            dropped["self-link"] += 1
            continue
        if nodes[s]["category"] == nodes[t]["category"]:
            dropped["same category"] += 1
            continue
        by_slug[s].append(t)

    print(f"{len(links)} verified links -> {len(by_slug)} nodes to touch")
    if recovered:
        print(f"  recovered {recovered} source slug(s) the verifier packed "
              f"the whole edge into")
    for why, n in dropped.most_common():
        print(f"  dropped {n}: {why}")

    before = {}
    changed = added = 0
    for slug, targets in sorted(by_slug.items()):
        path = os.path.join(ROOT, nodes[slug]["path"])
        fm = frontier.parse_frontmatter(read(path))
        before[slug] = (fm.get("read"), fm.get("tour_order"))

        existing = [frontier.link_basename(x)
                    for x in frontier.as_list(fm.get("related"))]
        merged = list(dict.fromkeys(existing + [t for t in targets
                                                if t not in existing]))
        new_count = len([t for t in targets if t not in existing])
        if not new_count:
            continue
        if len(merged) > MAX_RELATED:
            merged = merged[:MAX_RELATED]

        if args.dry_run:
            changed += 1
            added += new_count
            continue
        if set_related(path, merged):
            changed += 1
            added += new_count

    print(f"\n{added} links added across {changed} nodes"
          + (" [dry run]" if args.dry_run else ""))

    if args.dry_run:
        return

    bad = []
    for slug, (was_read, was_order) in before.items():
        fm = frontier.parse_frontmatter(read(os.path.join(ROOT, nodes[slug]["path"])))
        if fm.get("read") != was_read or fm.get("tour_order") != was_order:
            bad.append(slug)
    if bad:
        sys.exit(f"ABORT: read/tour_order changed on {len(bad)} node(s): "
                 f"{', '.join(bad[:8])}")
    print("read: and tour_order verified unchanged on every touched node")


if __name__ == "__main__":
    main()
