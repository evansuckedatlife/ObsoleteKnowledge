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
MODEL = "gemini-3.8-flash-medium"

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


class QuotaExhausted(RuntimeError):
    """agy's per-account quota. Every remaining call will fail identically."""


DELIM = "===== NODE:"


def group_related(jobs, size):
    """Bundle slugs that the vault itself mentions together.

    Greedy: take the first unplaced slug, then pull in the slugs sharing the
    most referring nodes with it. Slugs listed side by side in one article's
    connections are genuinely the same neighbourhood, so the model writes them
    as a coherent set instead of in isolation -- and the shared preamble is
    sent once instead of N times.
    """
    remaining = list(jobs)
    bundles = []
    while remaining:
        seed = remaining.pop(0)
        group = [seed]
        seed_src = set(seed[6] or ())
        if size > 1 and remaining:
            scored = sorted(
                range(len(remaining)),
                key=lambda i: (-len(seed_src & set(remaining[i][6] or ())),
                               remaining[i][0]),
            )
            for i in sorted(scored[: size - 1], reverse=True):
                group.append(remaining.pop(i))
        bundles.append(group)
    return bundles


def build_bundle_prompt(group, exemplar):
    """One shared preamble, then N slug specs."""
    region = group[0][1]
    menu = group[0][3]
    specs = []
    for slug, _region, refs, _menu, _ex, merges, _src, _dry in group:
        merge_note = ""
        if merges:
            merge_note = (f"\n  This one is reached from {' + '.join(merges)}, so "
                          f"give it connections that cross categories.")
        specs.append(
            f"### `{slug}`  ({refs} existing notes link to it)\n"
            f"How the collection refers to it:\n{referring_context(slug)}{merge_note}"
        )

    return f"""{NO_TOOLS}

You are writing {len(group)} reference nodes for a personal quiz-bowl knowledge base. They are closely related, so write them as a coherent set: cross-link them to each other where that is genuinely accurate.

# Output format

For EACH node, emit a line containing exactly:

{DELIM} <slug>

then the complete markdown file content for that slug, starting at its `---` frontmatter and ending at its footer line. No preamble, no commentary, no code fences. Emit all {len(group)} nodes, in the order given.

# The nodes to write

{chr(10).join(specs)}

# Exact template every node must follow

Copy this structure byte-for-byte, changing only the content. Keep the frontmatter key order, the three dataviewjs blocks, the `<!-- footer -->` marker and the footer line:

{exemplar}

# Rules (apply to every node)

- Frontmatter key order exactly: type, category, defines, related, requires, lists, tour_order, read
- `type` is one of: person, deity, hero, monster, work, text, event, place, concept, phrase, practice, holiday, term
- `category: {region}` · `lists: ["[[{region}-hubs]]"]` · `tour_order: 0` · `read: false`
- Footer line exactly: `Lists: [[{region}-hubs]] · Mark read: ` then the read-toggle code span from the template
- `defines`: the canonical display name plus genuine alternate names THIS node owns. Keep it tight — never claim a name that belongs to a different subject, and never give two of these nodes the same name.
- `requires`: 1-3 more foundational slugs chosen ONLY from the menu below
- `related`: 5-9 wikilink strings

## Body of each node

`## summary` — 2-4 sentences: what it is, when and where, why it is worth knowing.
`## you gotta know` — 5-8 bullets, MOST RECOGNISABLE FIRST and most obscure last, one fact per bullet.
`## connections` — 5-8 bullets, each a `[[wikilink]]` plus a one-line reason.
`## see also` — one line of peer wikilinks joined by ` · `.

`**bold**` ONLY to introduce a term that node defines. `*italics*` for other emphasis and for key names and titles. Every reference to another node is a `[[wikilink]]`. Target 450-550 words of body prose per node.

## Linking

Prefer these real slugs — they exist in the collection. A few links to unwritten concepts are fine, but most must come from here:

{', '.join(menu)}

Write accurate, verifiable, encyclopaedic content from your own general knowledge. Do not invent facts, dates or works.
"""


def split_bundle(text, slugs):
    """Split a bundled reply into per-slug markdown."""
    out = {}
    parts = re.split(rf"^{re.escape(DELIM)}\s*(\S+)\s*$", text, flags=re.M)
    # re.split with one group yields [pre, slug1, body1, slug2, body2, ...]
    for i in range(1, len(parts) - 1, 2):
        name = parts[i].strip().strip("`").removesuffix(".md")
        out[name] = parts[i + 1]
    if not out and len(slugs) == 1:
        out[slugs[0]] = text
    return out


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


def author_bundle(group) -> list[dict]:
    """Write every node in one bundle from a single agy call."""
    region, exemplar, dry = group[0][1], group[0][4], group[0][7]

    results, todo = [], []
    for g in group:
        if os.path.exists(os.path.join(ROOT, "concepts", g[1], f"{g[0]}.md")):
            results.append({"slug": g[0], "ok": False, "reason": "file already exists"})
        else:
            todo.append(g)
    if not todo:
        return results

    if len(todo) == 1:
        s = todo[0]
        prompt = build_prompt(s[0], s[1], s[2], s[3], exemplar, s[5])
    else:
        prompt = build_bundle_prompt(todo, exemplar)

    try:
        proc = sh(AGY, "-p", prompt, "--model", MODEL, "--output-format", "text",
                  timeout=1200)
    except subprocess.TimeoutExpired:
        return results + [{"slug": g[0], "ok": False, "reason": "agy timed out"}
                          for g in todo]

    combined = (proc.stdout or "") + "\n" + (proc.stderr or "")
    if "quota reached" in combined.lower() or "upgrade your subscription" in combined.lower():
        raise QuotaExhausted(combined.strip().splitlines()[0][:160])

    raw = proc.stdout or ""
    names = [g[0] for g in todo]
    pieces = split_bundle(raw, names) if len(todo) > 1 else {names[0]: raw}

    for g in todo:
        slug = g[0]
        body = clean(pieces.get(slug, ""))
        if not body:
            results.append({"slug": slug, "ok": False,
                            "reason": "absent from bundled reply"})
            continue
        problems = validate(body, slug, region)
        if problems:
            results.append({"slug": slug, "ok": False, "reason": "; ".join(problems)})
            continue
        if not dry:
            path = os.path.join(ROOT, "concepts", region, f"{slug}.md")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\r\n") as fh:
                fh.write(body if body.endswith("\n") else body + "\n")
        results.append({"slug": slug, "ok": True, "words": len(body.split())})
    return results


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--wave", help="wave JSON from tools/wave.py")
    ap.add_argument("--slugs", nargs="*", help="explicit slugs (needs --region)")
    ap.add_argument("--region", help="category when using --slugs")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--bundle", type=int, default=4,
                    help="slugs per agy call. The exemplar and hub menu are "
                         "over half of each prompt, so bundling closely related "
                         "slugs roughly halves input for the same output.")
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
                             exemplar, s.get("merge_regions") or [],
                             s.get("sources") or [], args.dry_run))
    elif args.slugs:
        if not args.region:
            ap.error("--slugs needs --region")
        data = frontier.build(ROOT)
        menu = sorted({s for s, n in data["nodes"].items()
                       if n["category"] == args.region})[:60]
        for s in args.slugs:
            jobs.append((s, args.region, 0, menu, exemplar, [], [], args.dry_run))
    else:
        ap.error("need --wave or --slugs")

    if args.limit:
        jobs = jobs[: args.limit]

    by_region = {}
    for j in jobs:
        by_region.setdefault(j[1], []).append(j)
    bundles = []
    for region_jobs in by_region.values():
        bundles.extend(group_related(region_jobs, args.bundle))

    print(f"{len(jobs)} slug(s) in {len(bundles)} bundle(s) of <={args.bundle} "
          f"via {MODEL}, {args.jobs} parallel"
          + (" [dry run]" if args.dry_run else ""), flush=True)

    ok = fail = 0
    quota = None
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = [pool.submit(author_bundle, b) for b in bundles]
        for fut in futures:
            try:
                batch = fut.result()
            except QuotaExhausted as exc:
                if quota is None:
                    quota = str(exc)
                    for other in futures:
                        other.cancel()
                continue
            except concurrent.futures.CancelledError:
                continue
            for r in batch:
                if r["ok"]:
                    ok += 1
                    print(f"  OK   {r['slug']:<38} {r['words']} words", flush=True)
                else:
                    fail += 1
                    print(f"  FAIL {r['slug']:<38} {r['reason']}", flush=True)

    print("")
    print(f"{ok} written, {fail} failed")
    if quota:
        print(f"QUOTA EXHAUSTED: {quota}")
        print(f"{len(jobs) - ok - fail} slug(s) not attempted. Nothing is lost: "
              f"re-run the same wave after the reset and it skips what exists.")
        sys.exit(2)


if __name__ == "__main__":
    main()
