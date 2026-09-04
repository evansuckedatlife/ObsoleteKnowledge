#!/usr/bin/env python3
"""Resolve a fresh wave's `defines` collisions against the existing vault.

A newly written node routinely claims a name an existing node already owns.
Two different things cause that, and they need opposite treatment:

  the node IS the existing node under a variant slug -- `hobbit` beside
  `the-hobbit`, `jrr-tolkien` beside `j-r-r-tolkien`. Delete the new file and
  alias its slug onto the survivor so existing links still resolve.

  the node is a DIFFERENT subject that reached across and claimed someone
  else's name -- `franklin-the-turtle` claiming "Franklin", `secretariat`
  claiming "Big Red". Keep it, drop the offending `defines` entries.

Telling them apart by "is the primary defines value already owned?" is not
enough, and the failure is not hypothetical: `joker` was deleted and aliased
onto `nikola-jokic`, because "The Joker" is Jokic's nickname. The Batman
villain became a basketball player, and `[[joker]]` resolved to him.

So a merge additionally requires the two nodes to carry the SAME ARTICLE
TITLE, compared case-, punctuation- and leading-article-blind. `hobbit` and
`the-hobbit` are both "The Hobbit"; `joker` is "Joker" and `nikola-jokic` is
"Nikola Jokic", so that pair narrows instead. Deliberately stricter than
tools/apply_dupes.py, which may also merge on a defines match -- that one
applies verdicts a model reasoned about, this one auto-deletes unreviewed
files, so it only acts on the unambiguous case.

Only ever deletes files that are UNTRACKED in git.

Usage:
    python tools/resolve_collisions.py --dry-run
    python tools/resolve_collisions.py
"""

from __future__ import annotations

import argparse
import glob
import io
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H1 = re.compile(r"^#\s+(.+?)\s*$", re.M)


def read(p):
    with io.open(p, encoding="utf-8", newline="") as fh:
        return fh.read()


def write(p, t):
    with io.open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(t)


def norm(s: str) -> str:
    s = re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()
    return re.sub(r"^(?:the|a|an)\s+", "", s)


def title_of(text: str) -> str:
    m = H1.search(frontier.FRONTMATTER.sub("", text, count=1))
    return m.group(1) if m else ""


def edit_fm_line(path, prefix, render):
    text = read(path)
    m = frontier.FRONTMATTER.match(text)
    nl = "\r\n" if "\r\n" in text else "\n"
    out, done = [], False
    for line in m.group(1).split(nl):
        if line.startswith(prefix) and not done:
            out.append(render(line))
            done = True
            continue
        out.append(line)
    if not done:
        return False
    write(path, text[: m.start(1)] + nl.join(out) + text[m.end(1):])
    return True


def add_aliases(path, tokens):
    """Insert after the defines BLOCK, not the defines LINE.

    Obsidian rewrites flow YAML to block style on save, and inserting after
    the `defines:` line lands the new key between the key and its own items.
    """
    text = read(path)
    m = frontier.FRONTMATTER.match(text)
    nl = "\r\n" if "\r\n" in text else "\n"
    lines = m.group(1).split(nl)
    fm = frontier.parse_frontmatter(text)
    existing = [str(x) for x in frontier.as_list(fm.get("aliases"))]
    rendered = "aliases: [" + ", ".join(dict.fromkeys(existing + tokens)) + "]"
    if fm.get("aliases") is not None:
        lines = [rendered if l.startswith("aliases:") else l for l in lines]
    else:
        i = next(i for i, l in enumerate(lines) if l.startswith("defines:"))
        j = i + 1
        while j < len(lines) and lines[j].lstrip().startswith("- "):
            j += 1
        lines.insert(j, rendered)
    write(path, text[: m.start(1)] + nl.join(lines) + text[m.end(1):])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    out = subprocess.run(
        ["git", "-c", "core.quotepath=false", "status", "--porcelain"],
        capture_output=True, encoding="utf-8", cwd=ROOT).stdout
    new = {os.path.normpath(l[3:].strip().strip('"'))
           for l in out.splitlines()
           if l.startswith("?? concepts/") and l.endswith(".md")}
    allp = [os.path.normpath(p)
            for p in glob.glob(os.path.join(ROOT, "concepts", "*", "*.md"))]
    allp = [os.path.relpath(p, ROOT) for p in allp]
    by_slug = {os.path.basename(p)[:-3]: p for p in allp}

    owner = {}
    for p in allp:
        if p in new:
            continue
        fm = frontier.parse_frontmatter(read(os.path.join(ROOT, p)))
        for key in ("defines", "aliases"):
            for v in frontier.as_list(fm.get(key)):
                owner.setdefault(frontier.slugify(v),
                                 os.path.basename(p)[:-3])

    merged = narrowed = refused = 0
    for p in sorted(new):
        full = os.path.join(ROOT, p)
        slug = os.path.basename(p)[:-3]
        text = read(full)
        fm = frontier.parse_frontmatter(text)
        vals = [str(v) for v in frontier.as_list(fm.get("defines"))]
        if not vals:
            continue
        clash = [v for v in vals if frontier.slugify(v) in owner]
        if not clash:
            continue

        primary = owner.get(frontier.slugify(vals[0]))
        same_subject = False
        if primary and primary in by_slug:
            keep_path = os.path.join(ROOT, by_slug[primary])
            keep_text = read(keep_path)
            same_subject = norm(title_of(text)) == norm(title_of(keep_text))
            # The leading-article rule makes "The Birds" and "Birds" identical,
            # and they are a Hitchcock film and a class of animal. When the
            # article is the only difference, require the categories to agree.
            if (same_subject
                    and title_of(text).strip().lower()
                    != title_of(keep_text).strip().lower()
                    and fm.get("category")
                    != frontier.parse_frontmatter(keep_text).get("category")):
                same_subject = False
                print(f"kept     {slug:<36} differs from {primary} only by a "
                      f"leading article, but across categories")
            if not same_subject:
                refused += 1
                print(f"kept     {slug:<36} '{title_of(text)}' is not "
                      f"'{title_of(read(keep_path))}' ({primary})")

        if same_subject:
            before = frontier.parse_frontmatter(read(keep_path))
            if args.dry_run:
                print(f"would merge {slug:<33} -> {primary}")
                merged += 1
                continue
            os.remove(full)
            add_aliases(keep_path, [slug])
            after = frontier.parse_frontmatter(read(keep_path))
            assert before.get("read") == after.get("read"), primary
            assert before.get("tour_order") == after.get("tour_order"), primary
            print(f"merged   {slug:<36} -> {primary}")
            merged += 1
        else:
            kept = ([v for v in vals if frontier.slugify(v) not in owner]
                    or [slug.replace("-", " ").title()])
            if not args.dry_run:
                edit_fm_line(full, "defines:",
                             lambda _l: "defines: [" + ", ".join(kept) + "]")
            print(f"narrowed {slug:<36} dropped {clash}")
            narrowed += 1

    print(f"\n{merged} merged, {narrowed} narrowed"
          + (f", {refused} merge(s) refused on a title mismatch" if refused
             else "")
          + (" [dry run]" if args.dry_run else ""))


if __name__ == "__main__":
    main()
