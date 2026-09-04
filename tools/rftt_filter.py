#!/usr/bin/env python3
"""Cut pack furniture out of an extracted answer set before a model sees it.

`rftt_topics.py` takes every `A:` line, which means it also takes the things a
pack prints that are not subjects: round headers, list answers where one
question wanted four names, bare arithmetic, and the stray connective word.
Those are cheap to spot with rules and expensive to send to a model 2,000
times, so they are dropped here and the judgement calls are left to the model.

What is deliberately NOT filtered: lowercase common nouns. Quiz answers are
full of legitimate lowercase subjects -- cesium, anthrax, foxglove, tango --
and a case rule would throw all of them away.

Usage:
    python tools/rftt_filter.py --gap _scratch/rftt_gap3.json \
        --out _scratch/rftt_candidates.json
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Round headers, which always carry a point value or an explicit round word.
# A bare keyword list is far too eager: it ate "Game of Thrones", "Point Pelee
# National Park", "Half-Reaction" and "exclamation point" in order to catch two
# real headers, so the point value has to be part of the pattern.
FURNITURE = re.compile(
    r"^\d+\s*-?\s*point\b"
    r"|\b(?:snapout|jailbreak|blitz|toss-?up|tiebreak(?:er)?)\b"
    r"|\bend\s+round\b|\bround\s+(?:one|two|three|four|\d+)\b", re.I)

# "x = 0, 1, 2", "3/4", "1.5 million" -- values, not subjects.
NUMERIC = re.compile(r"^[\d\s\W]*$|^[a-z]\s*=|^\d+(\.\d+)?\s*(%|million|billion)?$", re.I)

# A single question that wanted several names back: "North, Saint, Chicago,
# Psalm". Three or more comma-separated pieces is a list, not a subject.
LIST_ANSWER = re.compile(r"^[^,]+(,[^,]+){2,}$")

# Connectives that survive when a compound answer is split badly.
STOPWORDS = {
    "and", "or", "the", "a", "an", "of", "in", "on", "at", "to", "for",
    "with", "by", "from", "as", "is", "was", "are", "were", "be", "been",
    "all", "both", "either", "neither", "any", "some", "none", "other",
    "same", "different", "true", "false", "more", "most", "less", "least",
    "house", "thing", "things", "person", "people", "place", "places",
    "word", "words", "name", "names", "number", "numbers", "letter",
    "letters", "colour", "color", "colours", "colors", "type", "types",
}


def junk(name: str) -> str | None:
    """Return the reason this is not a subject, or None to keep it."""
    s = name.strip()
    if len(s) < 3:
        return "too short"
    if FURNITURE.search(s):
        return "pack furniture"
    if NUMERIC.match(s):
        return "numeric value"
    if LIST_ANSWER.match(s):
        return "list answer"
    if s.lower() in STOPWORDS:
        return "stopword"
    if len(s.split()) > 8:
        return "sentence, not a name"
    if not re.search(r"[A-Za-z]", s):
        return "no letters"
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gap", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with io.open(os.path.join(ROOT, args.gap), encoding="utf-8") as fh:
        missing = json.load(fh)["missing"]

    kept, dropped = [], {}
    for m in missing:
        why = junk(m["name"])
        if why:
            dropped.setdefault(why, []).append(m["name"])
        else:
            kept.append(m)

    print(f"{len(missing)} missing -> {len(kept)} candidates")
    for why, names in sorted(dropped.items(), key=lambda kv: -len(kv[1])):
        print(f"  dropped {len(names):>4}: {why}   e.g. {names[0][:52]!r}")

    with io.open(os.path.join(ROOT, args.out), "w", encoding="utf-8",
                 newline="\r\n") as fh:
        json.dump(kept, fh, indent=1, ensure_ascii=False)
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
