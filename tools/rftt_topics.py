#!/usr/bin/env python3
"""Extract the ANSWER SET from Reach For The Top packs as a topic map.

The packs are copyrighted ("2022 Reach For The Top Inc."), so this follows the
same rule the vault applies to NAQT: their *questions* are their expression and
are never read into a model or stored here. What gets taken is the list of
answers -- the names of the things asked about -- which are facts, and facts are
not copyrightable (Feist v. Rural).

So this reads only the `A:` lines, discards every question, and emits a list of
subjects. Nodes are then written originally from general knowledge, exactly as
for the NAQT-scoped material.

Nothing derived from the question text is written to the repo.

Usage:
    python tools/rftt_topics.py --dir <folder of packs> --out _scratch/rftt_topics.json
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import re
import subprocess
import sys
import tempfile

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Packs are inconsistent: some mark answers "A:", others "A."
ANSWER = re.compile(r"^\s*A[:.]\s*(.+?)\s*$", re.M)

# Answer lines carry adjudication furniture; strip it to get the bare subject.
PARENS = re.compile(r"\([^)]*\)")
BRACKETS = re.compile(r"\[[^\]]*\]")
PROMPTS = re.compile(
    r"\b(accept|or|prompt on|do not accept|also accept|either|both|"
    r"any of|reject)\b.*$", re.I)
UNDERLINE = re.compile(r"_+")

# Quiz answers include plenty of legitimate lowercase subjects (cesium,
# anthrax, foxglove), so the filter cannot just reject lowercase. It rejects
# answers that are not subjects at all: colours, weekdays, bare directions,
# yes/no. These are answers to questions, but nothing to write an article on.
STOP = {
    "yes", "no", "true", "false", "none", "all of them", "both",
    "red", "green", "blue", "yellow", "orange", "purple", "black", "white",
    "brown", "pink", "grey", "gray", "gold", "silver",
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
    "sunday", "north", "south", "east", "west", "left", "right", "up", "down",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "ten", "zero", "wings", "legs", "eyes", "head", "hand", "foot", "water",
    "air", "fire", "earth", "salt", "sugar", "milk", "bread", "the moon",
}


def clean_answer(raw: str) -> list[str]:
    """One answer line -> the subject name(s) it names."""
    s = BRACKETS.sub(" ", PARENS.sub(" ", raw))
    s = UNDERLINE.sub(" ", s)
    s = PROMPTS.sub(" ", s)
    s = s.replace("&", " and ")
    s = re.sub(r"[\"'`*]", "", s)
    parts = re.split(r"\s*(?:/|;|,\s+or\s+)\s*", s)
    out = []
    for p in parts:
        p = " ".join(p.split()).strip(" .:-")
        if not p or len(p) < 3 or len(p) > 60:
            continue
        if re.fullmatch(r"[\d\W]+", p):
            continue
        if p.lower() in STOP:
            continue
        out.append(p)
    return out[:2]


def extract(path: str) -> list[str]:
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
        txt = tmp.name
    try:
        subprocess.run(["pdftotext", "-layout", path, txt],
                       capture_output=True, check=False)
        with open(txt, encoding="utf-8", errors="replace") as fh:
            body = fh.read()
    finally:
        os.unlink(txt)
    answers = []
    for raw in ANSWER.findall(body):
        answers.extend(clean_answer(raw))
    return answers


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    pdfs = sorted(glob.glob(os.path.join(args.dir, "*.pdf")))
    if not pdfs:
        sys.exit(f"no PDFs under {args.dir}")

    counts = collections.Counter()
    for p in pdfs:
        for a in extract(p):
            counts[a] += 1
    print(f"{len(pdfs)} packs -> {sum(counts.values())} answers, "
          f"{len(counts)} distinct subjects")

    data = frontier.build(ROOT)
    resolvable = set(data["nodes"])
    for slug, meta in data["nodes"].items():
        fm = frontier.parse_frontmatter(
            frontier.read_text(os.path.join(ROOT, meta["path"])))
        for key in ("aliases", "defines"):
            for v in frontier.as_list(fm.get(key)):
                resolvable.add(frontier.slugify(v))

    have, missing = [], []
    for name, n in counts.most_common():
        slug = frontier.slugify(name)
        (have if slug in resolvable else missing).append(
            {"name": name, "slug": slug, "packs": n})

    print(f"  already in the vault : {len(have)}")
    print(f"  NOT in the vault     : {len(missing)}")
    print()
    print("top missing subjects (by how many packs asked about them):")
    for m in missing[:30]:
        print(f"    {m['packs']:>2}x  {m['name']}")

    with open(os.path.join(ROOT, args.out), "w", encoding="utf-8", newline="\r\n") as fh:
        json.dump({"packs": len(pdfs), "have": len(have),
                   "missing": missing}, fh, indent=1)
    print(f"\nwrote {args.out}")


if __name__ == "__main__":
    main()
