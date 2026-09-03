#!/usr/bin/env python3
"""Author frontier nodes with Gemini via the Antigravity CLI (`agy`).

Different shape from the Haiku subagent waves. In `agy -p` print mode there is
nobody to approve a permission prompt, so any tool call the model attempts is
auto-denied and the run returns *nothing at all*. So the model never touches
the filesystem: every input is fed inline, it replies with the finished node
markdown, and this script validates and writes the file.

That inversion is an improvement in one respect -- the model cannot damage the
vault, because it has no way to reach it.

Usage:
    python tools/agy_write.py --wave _scratch/waves/agy1.json --jobs 4
    python tools/agy_write.py --slugs biodiversity denmark --dry-run
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frontier  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGY = os.path.expanduser("~/AppData/Local/agy/bin/agy.exe")
EXEMPLAR = "concepts/mythology/perseus.md"
MODEL = "gemini-3.8-flash-high"

# Without this the model reaches for a shell on any non-trivial task and the
# headless run returns empty. See the gemini-bridge notes.
NO_TOOLS = (
    "Answer entirely in your reply text. Do NOT call any tool - no shell "
    "commands, no file reads, no file writes, no search. Everything you need "
    "is already in this message. There is nothing to run."
)


def sh(*argv, cwd=ROOT, timeout=600):
    return subprocess.run(list(argv), cwd=cwd, capture_output=True,
                          text=True, encoding="utf-8", errors="replace",
                          timeout=timeout)


def referring_context(slug: str, limit: int = 6) -> str:
    """How the vault actually uses this slug -- decides WHICH subject is meant."""
    out = sh("git", "grep", "-h", "-F", f"[[{slug}]]", "--", "concepts").stdout
    lines = []
    for line in out.splitlines():
        line = line.strip().lstrip("- ").strip()
        if 25 < len(line) < 400 and line not in lines:
            lines.append(line)
        if len(lines) >= limit:
            break
    return "\n".join(f"  - {l}" for l in lines) or "  (no prose context found)"


def build_prompt(slug: str, region: str, refs: int, menu: list[str],
                 exemplar: str, merge_regions: list[str]) -> str:
    merge_note = ""
    if merge_regions:
        merge_note = (
            f"\nThis concept is reached from several different areas of the "
            f"collection ({' + '.join(merge_regions)}), so give it deliberately "
            f"interdisciplinary connections that cross categories rather than "
            f"staying inside {region}.\n"
        )
    return f"""{NO_TOOLS}

You are writing one reference node for a personal quiz-bowl knowledge base. Output ONLY the finished markdown file content. No preamble, no explanation, no code fence. Start with the `---` of the frontmatter and stop at the end of the footer line.

# The node to write

Slug: `{slug}`  (category: {region}; {refs} existing notes link to it)

Here is how the collection actually refers to it. Write the subject these sentences mean, not whatever the bare word might suggest:

{referring_context(slug)}
{merge_note}
# Exact template to follow

Copy this structure byte-for-byte, changing only the content. Keep the frontmatter key order, the three dataviewjs blocks, the `<!-- footer -->` marker and the footer line:

{exemplar}

# Rules

- Frontmatter key order exactly: type, category, defines, related, requires, lists, tour_order, read
- `type` is one of: person, deity, hero, monster, work, text, event, place, concept, phrase, practice, holiday, term
- `category: {region}` · `lists: ["[[{region}-hubs]]"]` · `tour_order: 0` · `read: false`
- Footer line exactly: `Lists: [[{region}-hubs]] · Mark read: ` followed by the read-toggle code span from the template
- `defines`: the canonical display name plus genuine alternate names THIS node owns. Keep it tight; do not claim a name that clearly belongs to a different subject.
- `requires`: 1-3 more foundational slugs, chosen ONLY from the menu below
- `related`: 5-9 wikilink strings

## Body

`## summary` - 2-4 sentences: what it is, when and where, why it is worth knowing.
`## you gotta know` - 5-8 bullets, MOST RECOGNISABLE FIRST and most obscure last, one fact per bullet.
`## connections` - 5-8 bullets, each a `[[wikilink]]` plus a one-line reason.
`## see also` - one line of peer wikilinks joined by ` · `.

`**bold**` ONLY to introduce a term this node defines. `*italics*` for other emphasis and for key names and titles. Every reference to another node is a `[[wikilink]]`. Target 450-550 words of body prose.

## Linking

Prefer these real slugs - they exist in the collection. A few links to unwritten concepts are fine and expected, but most must come from here:

{', '.join(menu)}

Write accurate, verifiable, encyclopaedic content from your own general knowledge. Do not invent facts, dates or works.
"""


SECTIONS = ("## summary", "## you gotta know", "## connections", "## see also")


def clean(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:markdown)?\s*\n", "", text)
    text = re.sub(r"\n```\s*$", "", text)
    i = text.find("---")
    text = text[i:].strip() if i > 0 else text.strip()
    # Gemini leaves a run of blank lines after the H1; collapse any gap wider
    # than one blank line so new nodes match the rest of the vault.
    return re.sub(r"\n{3,}", "\n\n", text)


def validate(text: str, slug: str, region: str) -> list[str]:
    problems = []
    fm = frontier.parse_frontmatter(text)
    if not fm:
        return ["frontmatter does not parse"]
    if fm.get("read") is not False:
        problems.append(f"read={fm.get('read')!r}")
    if fm.get("category") != region:
        problems.append(f"category={fm.get('category')!r}")
    for s in SECTIONS:
        if s not in text:
            problems.append(f"missing {s}")
    if "<!-- footer -->" not in text:
        problems.append("missing footer marker")
    words = len(frontier.FRONTMATTER.sub("", text, count=1).split())
    if words < 300:
        problems.append(f"only {words} words")
    return problems


def author(job) -> dict:
    slug, region, refs, menu, exemplar, merges, dry = job
    path = os.path.join(ROOT, "concepts", region, f"{slug}.md")
    if os.path.exists(path):
        return {"slug": slug, "ok": False, "reason": "file already exists"}

    prompt = build_prompt(slug, region, refs, menu, exemplar, merges)
    try:
        proc = sh(AGY, "-p", prompt, "--model", MODEL, "--output-format", "text")
    except subprocess.TimeoutExpired:
        return {"slug": slug, "ok": False, "reason": "agy timed out"}

    body = clean(proc.stdout or "")
    if not body:
        return {"slug": slug, "ok": False,
                "reason": "empty reply (a tool call in headless mode returns nothing)",
                "stderr": (proc.stderr or "")[:200]}

    problems = validate(body, slug, region)
    if problems:
        return {"slug": slug, "ok": False, "reason": "; ".join(problems),
                "words": len(body.split())}

    if not dry:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\r\n") as fh:
            fh.write(body if body.endswith("\n") else body + "\n")
    return {"slug": slug, "ok": True, "words": len(body.split()),
            "path": os.path.relpath(path, ROOT).replace("\\", "/")}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--wave", help="wave JSON from tools/wave.py")
    ap.add_argument("--slugs", nargs="*", help="explicit slugs (needs --region)")
    ap.add_argument("--region", help="category when using --slugs")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(AGY):
        sys.exit(f"agy not found at {AGY}")

    with open(os.path.join(ROOT, EXEMPLAR), encoding="utf-8") as fh:
        exemplar = fh.read()

    jobs = []
    if args.wave:
        with open(args.wave, encoding="utf-8") as fh:
            wave = json.load(fh)
        for b in wave["batches"]:
            for s in b["slugs"]:
                jobs.append((s["slug"], b["region"], s["refs"], b["hub_menu"],
                             exemplar, s.get("merge_regions") or [], args.dry_run))
    elif args.slugs:
        if not args.region:
            ap.error("--slugs needs --region")
        data = frontier.build(ROOT)
        menu = sorted({s for s, n in data["nodes"].items()
                       if n["category"] == args.region})[:60]
        for s in args.slugs:
            jobs.append((s, args.region, 0, menu, exemplar, [], args.dry_run))
    else:
        ap.error("need --wave or --slugs")

    if args.limit:
        jobs = jobs[: args.limit]

    print(f"{len(jobs)} slug(s) via {MODEL}, {args.jobs} parallel"
          + (" [dry run]" if args.dry_run else ""))

    ok = fail = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for r in pool.map(author, jobs):
            if r["ok"]:
                ok += 1
                print(f"  OK   {r['slug']:<38} {r['words']} words")
            else:
                fail += 1
                print(f"  FAIL {r['slug']:<38} {r['reason']}")
    print(f"\n{ok} written, {fail} failed")


if __name__ == "__main__":
    main()
