#!/usr/bin/env python3
"""Give newly written BFS hub nodes a home of their own.

`_dv/tourpage.js` defines a `<category>-core` tour as *nodes in that category
with an empty or absent `lists`*. BFS hub nodes are written with `lists: []`,
so left alone every one of them silently joins its category's core tour --
`history-core` was already drifting 147 -> 159 partway through the first wave,
and a thousand new nodes would bury the curated spine entirely and turn one
"tour" into twenty hours of audio.

So each new node joins `<category>-hubs` instead: a real list MOC plus a tour
note, built from the vault's own templates. The core spine stays exactly as it
was, and the connective tissue becomes its own readable (and narratable) path.

Only ever touches files that are UNTRACKED in git -- i.e. written by the wave
that just ran. Never a tracked node, because tracked nodes carry the user's
`read:` progress.

Usage:
    python tools/hubify.py --dry-run
    python tools/hubify.py
"""

from __future__ import annotations

import argparse
import os
import re
import glob
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BLURB = {
    "history": "The connective tissue of the history collection: eras, institutions, movements and forces the other nodes keep reaching for.",
    "geography": "Continents, regions and physical features that the rest of the geography collection is described against.",
    "literature": "Genres, movements and traditions that give the individual authors and works their context.",
    "science": "Foundational structures, laws and systems the specific science nodes build on.",
    "mathematics": "The underlying objects and ideas the individual theorems and figures depend on.",
    "mythology": "Places, cycles and concepts that recur across the individual myths.",
    "religion": "Traditions, movements and ideas that the specific figures and texts belong to.",
    "philosophy": "Branches, problems and positions the individual philosophers argue about.",
    "music": "Forms, eras and concepts underlying the individual composers and works.",
    "performance": "Forms and traditions behind the individual productions and performers.",
    "visual-art": "Movements, media and institutions the individual artists and works sit within.",
    "pop-culture": "Formats, genres and phenomena the individual titles belong to.",
    "social-science": "Concepts and frameworks the individual studies and thinkers apply.",
    "sports": "Competitions, structures and concepts the individual athletes compete within.",
    "misc": "Cross-cutting concepts that belong to no single field.",
}

LIST_TEMPLATE = """---
type: list
category: {category}
read: false
---

# {title}

{blurb}

## nodes

{members}

## progress

Live read-status for this list (requires the **Bases** core plugin). Flip a node's `read` from its footer toggle and it moves here.

```base
filters:
  and:
    - file.hasLink(this.file)
views:
  - type: table
    name: Progress
    order:
      - file.name
      - read
      - type
    sort:
      - property: read
        direction: ASC
      - property: tour_order
        direction: ASC
      - property: file.name
        direction: ASC
```
"""

TOUR_TEMPLATE = """---
type: tour
category: {category}
read: false
---

# Tour — {title}

A foundations-first reading path. **Continue** jumps to your next unread node; each node has a Next ▶ link to flow through, and a Foundations box that checks what you still need to read first.

```dataviewjs
dv.view("_dv/tourpage", {{list: "{slug}", core: false, category: "{category}"}})
```
"""


def untracked_nodes() -> list[str]:
    # core.quotepath=false, or git escapes any non-ASCII path into a quoted
    # octal form ("concepts/literature/julio-cort\303\241zar.md") that never
    # matches a real file -- which silently dropped that node from its list
    # and failed check_symmetry.
    out = subprocess.run(
        ["git", "-c", "core.quotepath=false", "status", "--porcelain"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
    ).stdout
    paths = []
    for line in out.splitlines():
        if line.startswith("?? concepts/") and line.endswith(".md"):
            paths.append(line[3:].strip().strip('"'))
    return sorted(paths)


def newline_of(text: str) -> str:
    return "\r\n" if "\r\n" in text else "\n"


def set_lists(path: str, slug: str, dry: bool) -> bool:
    """Rewrite only the empty `lists:` line, leaving every other byte alone."""
    full = os.path.join(ROOT, path)
    with open(full, encoding="utf-8", newline="") as fh:
        text = fh.read()

    m = frontier.FRONTMATTER.match(text)
    if not m:
        return False
    fm = m.group(1)
    nl = newline_of(text)

    lines = fm.split(nl) if nl in fm else fm.split("\n")
    for i, line in enumerate(lines):
        if not line.startswith("lists:"):
            continue
        value = line[len("lists:"):].strip()
        # Only claim a node that is genuinely unassigned; never overwrite a
        # real list membership.
        if value not in ("", "[]"):
            return False
        if value == "" and i + 1 < len(lines) and lines[i + 1].lstrip().startswith("- "):
            return False
        lines[i] = f'lists: ["[[{slug}]]"]'
        break
    else:
        return False

    new_fm = nl.join(lines)
    updated = text[: m.start(1)] + new_fm + text[m.end(1):]

    # Footer carries list membership too; keep the two in step.
    updated = updated.replace(
        "Lists:  · Mark read:", f"Lists: [[{slug}]] · Mark read:"
    )
    if "Lists: [[" not in updated:
        updated = re.sub(
            r"(?m)^Lists:.*?· Mark read:", f"Lists: [[{slug}]] · Mark read:", updated
        )

    if not dry:
        with open(full, "w", encoding="utf-8", newline="") as fh:
            fh.write(updated)
    return True


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    new = untracked_nodes()
    if not new:
        print("no untracked nodes — nothing to do")
        return

    by_cat: dict[str, list[str]] = {}
    for path in new:
        by_cat.setdefault(path.split("/")[1], []).append(path)

    changed = 0
    for category, paths in sorted(by_cat.items()):
        for path in paths:
            if set_lists(path, f"{category}-hubs", args.dry_run):
                changed += 1

    # Build each list from what the nodes actually DECLARE, not from which
    # folder they sit in. A node may legitimately belong to several lists
    # (romance and typography are both pop-culture and literature hubs), and
    # a folder-based build silently drops the extra memberships, which then
    # fails check_symmetry.
    membership: dict[str, list[str]] = {}
    for path in new:
        declared = frontier.as_list(
            frontier.parse_frontmatter(frontier.read_text(os.path.join(ROOT, path))).get("lists")
        )
        slugs = [frontier.link_basename(x) for x in declared]
        slugs = [s for s in slugs if s.endswith("-hubs")]
        if not slugs:
            slugs = [f"{path.split('/')[1]}-hubs"]
        for s in slugs:
            membership.setdefault(s, []).append(path)

    for slug, paths in sorted(membership.items()):
        category = slug[: -len("-hubs")]

        members = []
        for path in sorted(paths):
            node = os.path.basename(path)[:-3]
            text = frontier.read_text(os.path.join(ROOT, path))
            title = node.replace("-", " ")
            mt = re.search(r"^#\s+(.+)$",
                           frontier.FRONTMATTER.sub("", text, count=1), re.M)
            if mt:
                title = mt.group(1).strip()
            ms = re.search(r"##\s+summary\s*\n+(.+?)(?:\n\n|\Z)", text, re.S)
            hint = ""
            if ms:
                hint = re.sub(r"[*`\[\]]", "", ms.group(1)).strip().split(". ")[0]
                hint = hint[:150] + ("…" if len(hint) > 150 else ".")
            members.append(f"- [[{node}|{title}]] — {hint}")

        title = f"{category.replace('-', ' ').title()} hubs"
        list_path = os.path.join(ROOT, "lists", f"{slug}.md")
        tour_path = os.path.join(ROOT, "tours", f"{slug}.md")

        # Merge by node slug, never by whole line. The rendered hint drifts
        # between runs (summary edits, ellipsis vs full stop), so a line-level
        # set-union silently duplicates every member on a re-run.
        entries: dict[str, str] = {}
        if os.path.exists(list_path):
            prev = frontier.read_text(list_path)
            for line in re.findall(r"^- \[\[.+$", prev, re.M):
                key = re.match(r"^- \[\[([^\]\|]+)", line)
                if key:
                    entries[key.group(1).strip()] = line
        for line in members:
            key = re.match(r"^- \[\[([^\]\|]+)", line)
            if key:
                entries[key.group(1).strip()] = line       # newest wins
        # Drop members whose node no longer exists: duplicates get deleted and
        # aliased onto a survivor after a wave, and a stale entry would leave
        # the MOC pointing at nothing.
        alive = {os.path.basename(p)[:-3]
                 for p in glob.glob(os.path.join(ROOT, "concepts", "*", "*.md"))}
        merged = [entries[k] for k in sorted(entries) if k in alive]

        print(f"{slug:<26} {len(paths):>4} new  ->  {len(merged)} members")
        if args.dry_run:
            continue

        with open(list_path, "w", encoding="utf-8", newline="\r\n") as fh:
            fh.write(LIST_TEMPLATE.format(
                category=category, title=title,
                blurb=BLURB.get(category, "Connective nodes for this field."),
                members="\n".join(merged)))
        if not os.path.exists(tour_path):
            with open(tour_path, "w", encoding="utf-8", newline="\r\n") as fh:
                fh.write(TOUR_TEMPLATE.format(
                    category=category, title=title, slug=slug))

    print(f"\n{changed} node(s) assigned to <category>-hubs"
          + (" (dry run)" if args.dry_run else ""))


if __name__ == "__main__":
    main()
