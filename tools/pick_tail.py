#!/usr/bin/env python3
"""Select the worth-writing slugs from the single-reference frontier tail.

Above two references, a dangling slug is almost always a real concept the vault
keeps reaching for. At exactly one reference that stops being true: the tail is
mostly incidental phrasing lifted out of one sentence -- `1896-election` and
`1896-u-s-presidential-election` and `1892-u-s-presidential-election` as three
separate targets, or compounds like `1960s-counterculture-and-violence` that no
reference work would ever have an article for.

Writing that wholesale would bury 4,000 real nodes under near-duplicates. This
keeps the tail entries that look like canonical article titles and drops the
rest, reporting what it dropped and why so the judgement stays inspectable.

Usage:
    python tools/pick_tail.py --show-dropped
    python tools/pick_tail.py --out _scratch/tail_queue.json
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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# A decade or year in front of a common noun is a sentence fragment, not a
# title: 1920s-scandal, 1850s-american-politics, 1970s-television.
YEAR_QUALIFIED = re.compile(r"^\d{3,4}s?-")
# Trailing generic nouns that signal a description rather than a subject.
VAGUE_TAIL = re.compile(
    r"-(politics|america|american-politics|scandal|culture-and-\w+|"
    r"and-\w+|era-\w+|history|themes?|influence|impact|legacy|overview|"
    r"context|background|significance|comparison|relations?)$"
)
CONJUNCTION = re.compile(r"-(and|or|vs|versus|in|of|for|with)-")


VALID_SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def reasons(slug: str, tokens: list[str], sibling: str | None) -> str | None:
    if not VALID_SLUG.match(slug):
        return "not a clean slug"
    if not any(len(t) > 3 for t in tokens):
        return "no substantive word"
    if len(tokens) > 4:
        return "too many words to be an article title"
    if YEAR_QUALIFIED.match(slug) and len(tokens) > 2:
        return "year-qualified fragment"
    if VAGUE_TAIL.search(slug):
        return "descriptive tail, not a subject"
    if CONJUNCTION.search(slug) and len(tokens) > 3:
        return "compound phrase"
    if sibling:
        return f"near-duplicate of {sibling}"
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out")
    ap.add_argument("--show-dropped", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    data = frontier.build(ROOT)
    ones = [m for m in data["missing"] if m["refs"] == 1]
    resolvable = set(data["nodes"])

    # Token-set index so a longer slug whose words contain a shorter slug's
    # words is treated as the same subject stated at more length.
    by_tokens = {}
    for m in sorted(ones, key=lambda m: len(m["slug"])):
        key = frozenset(t for t in m["slug"].split("-") if len(t) > 2)
        by_tokens.setdefault(key, m["slug"])

    kept, dropped = [], []
    for m in ones:
        slug = m["slug"]
        tokens = [t for t in slug.split("-") if t]
        core = frozenset(t for t in tokens if len(t) > 2)

        sibling = None
        for key, owner in by_tokens.items():
            if owner != slug and key and key < core:
                sibling = owner
                break
        if sibling is None and slug in resolvable:
            sibling = slug

        why = reasons(slug, tokens, sibling)
        (dropped if why else kept).append((slug, m["owner"], why))

    print(f"{len(ones)} single-reference targets")
    print(f"  keep {len(kept)}   drop {len(dropped)}")
    counts = collections.Counter(w for _, _, w in dropped)
    for why, n in counts.most_common():
        print(f"    {n:>5}  {why}")

    if args.show_dropped:
        print("\nsample dropped:")
        for slug, _, why in dropped[:18]:
            print(f"    {slug:<44} {why}")
        print("\nsample kept:")
        for slug, region, _ in kept[:24]:
            print(f"    {slug:<44} {region}")

    if args.out:
        sel = kept[: args.limit] if args.limit else kept
        payload = collections.defaultdict(list)
        for slug, region, _ in sel:
            payload[region].append(slug)
        with open(os.path.join(ROOT, args.out), "w", encoding="utf-8", newline="\r\n") as fh:
            json.dump(dict(payload), fh, indent=1)
        print(f"\nwrote {args.out}: {sum(len(v) for v in payload.values())} slugs "
              f"across {len(payload)} regions")


if __name__ == "__main__":
    main()
