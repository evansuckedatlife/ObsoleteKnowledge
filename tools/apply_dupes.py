#!/usr/bin/env python3
"""Apply adjudicated duplicate-name verdicts.

`tools/consolidate.py` finds names claimed by two or more nodes. A model then
decides, per name, whether the two nodes are one subject under variant slugs
(`merge`) or two subjects that happen to share a name (`narrow`). This applies
those verdicts.

It is the destructive step, so the model's verdict is not trusted on its own.
Three guards run first, and each can override the model:

  A. read:   a node the user has actually read is never deleted. Full stop.

  B. subject the survivor must ALREADY CLAIM the victim's article title -- the
             victim's H1 is identical to the survivor's, or appears verbatim in
             the survivor's `defines`/`aliases`. If it does not, the two files
             are about different things and the merge is DOWNGRADED to a narrow.
             This is what separates `torah`/`pentateuch` (torah already claims
             "Pentateuch" -- one article) from `babylon`/`babylonian-empire`
             (the city does not claim the empire -- two articles), which the
             model called the same way.

  C. direction  the node named after itself wins: the one whose basename is the
             slugified form of its own first `defines` value. The model twice
             picked the wrong survivor -- `magellan` over `ferdinand-magellan`,
             `prussian-empire` over `prussia` -- and both times the loser was
             the node whose filename matched its own title.

A merge then: folds the victim's `defines` and `lists` into the survivor,
rewrites every `[[victim]]` in the vault to `[[survivor]]`, repoints list
files, and deletes the victim.

A narrow only drops the contested strings from one node's `defines`.

Afterwards `read:` and `tour_order` are re-read on every surviving touched file
and the run aborts if either moved.

Usage:
    python tools/apply_dupes.py --verdicts _scratch/dupe_verdicts.json --dry-run
    python tools/apply_dupes.py --verdicts _scratch/dupe_verdicts.json
"""

from __future__ import annotations

import argparse
import collections
import io
import json
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
    """Compare titles the way a reader would.

    Case and punctuation blind, and blind to a leading article -- "The Olympic
    Games" and "Olympic Games" are one subject, and an exact compare on the
    first `defines` value is what let that pair through as two nodes.
    Consensus's own rules take the same view: a player "will not be penalized
    if they add, remove, or change the leading article of a title."
    """
    s = re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()
    return re.sub(r"^(?:the|a|an)\s+", "", s)


def title_of(text: str) -> str:
    m = H1.search(frontier.FRONTMATTER.sub("", text, count=1))
    return m.group(1) if m else ""


def claims(fm: dict) -> set:
    out = set()
    for key in ("defines", "aliases"):
        for v in frontier.as_list(fm.get(key)):
            out.add(norm(str(v)))
    return out


def set_key(path: str, key: str, values: list) -> None:
    """Rewrite one frontmatter key to a flow-style list, preserving CRLF.

    Handles both flow (`key: [a, b]`) and block style, because Obsidian
    rewrites flow to block on every save and the vault contains both.
    """
    text = read(path)
    m = frontier.FRONTMATTER.match(text)
    if not m:
        return
    nl = "\r\n" if "\r\n" in text else "\n"
    lines = m.group(1).split(nl)
    start = next((i for i, l in enumerate(lines)
                  if l.startswith(key + ":")), None)
    if start is None:
        return
    end = start + 1
    while end < len(lines) and lines[end].lstrip().startswith("- "):
        end += 1
    rendered = f"{key}: [" + ", ".join(
        f'"{v}"' if any(c in v for c in ',:[]"') else v for v in values) + "]"
    if lines[start:end] == [rendered]:
        return
    lines[start:end] = [rendered]
    write(path, text[: m.start(1)] + nl.join(lines) + text[m.end(1):])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verdicts", required=True)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with io.open(os.path.join(ROOT, args.verdicts), encoding="utf-8") as fh:
        verdicts = json.load(fh)

    data = frontier.build(ROOT)
    nodes = data["nodes"]

    cache = {}

    def load(slug):
        if slug not in cache:
            p = os.path.join(ROOT, nodes[slug]["path"])
            t = read(p)
            cache[slug] = (p, t, frontier.parse_frontmatter(t), title_of(t))
        return cache[slug]

    # ---- collapse to distinct pairs, then run the guards -------------------
    pairs, narrows = {}, []
    skipped = collections.Counter()
    notes = []

    for d in verdicts:
        v = d.get("verdict")
        if v == "narrow":
            for n in d.get("narrow") or []:
                if n.get("slug") in nodes and n.get("drop"):
                    narrows.append((n["slug"], n["drop"]))
            continue
        if v != "merge":
            skipped["left alone by the model"] += 1
            continue
        keep = d.get("keep")
        for away in d.get("merge_away") or []:
            if keep not in nodes or away not in nodes or keep == away:
                skipped["endpoint is not a node"] += 1
                continue
            pairs.setdefault(tuple(sorted((keep, away))), (keep, away, d))

    print(f"{len(verdicts)} verdicts -> {len(pairs)} distinct merge pairs, "
          f"{len(narrows)} narrows")

    merges = []
    for keep, away, d in pairs.values():
        kp, kt, kfm, ktitle = load(keep)
        ap_, at, afm, atitle = load(away)

        # C. direction -- the node named after itself wins.
        def self_named(slug, fm):
            first = (frontier.as_list(fm.get("defines")) or [""])[0]
            return frontier.slugify(str(first)) == slug

        k_self, a_self = self_named(keep, kfm), self_named(away, afm)
        if a_self and not k_self:
            notes.append(f"direction flipped: keep {away}, not {keep} "
                         f"({away} is named after its own title)")
            keep, away = away, keep
            kp, kt, kfm, ktitle = load(keep)
            ap_, at, afm, atitle = load(away)

        # A. read: -- never delete the user's reading progress.
        if str(afm.get("read")).lower() == "true":
            if str(kfm.get("read")).lower() != "true":
                notes.append(f"direction flipped: {away} is read, {keep} is not")
                keep, away = away, keep
                kp, kt, kfm, ktitle = load(keep)
                ap_, at, afm, atitle = load(away)
            else:
                skipped["both nodes are read"] += 1
                continue
        if str(afm.get("read")).lower() == "true":
            skipped["victim is read"] += 1
            continue

        # B0. the leading-article trap. Ignoring "The" makes "The Birds" and
        # "Birds" look like one subject; they are a Hitchcock film and a class
        # of animal. When the article is the ONLY difference, require the two
        # nodes to agree on category before believing they are the same thing.
        if (norm(atitle) == norm(ktitle)
                and atitle.strip().lower() != ktitle.strip().lower()
                and afm.get("category") != kfm.get("category")):
            notes.append(f"DOWNGRADED to narrow: {keep} and {away} differ only "
                         f"by a leading article but sit in different "
                         f"categories ({kfm.get('category')} vs "
                         f"{afm.get('category')}) -- different subjects")
            skipped["article-only match across categories"] += 1
            continue

        # B. subject -- does the survivor already claim the victim's title?
        if norm(atitle) != norm(ktitle) and norm(atitle) not in claims(kfm):
            notes.append(f"DOWNGRADED to narrow: {keep} ('{ktitle}') does not "
                         f"claim '{atitle}' -- different subjects")
            contested = [d.get("name", "")]
            drop = [s for s in frontier.as_list(afm.get("defines"))
                    if norm(str(s)) in {norm(c) for c in contested}]
            if drop:
                narrows.append((away, drop))
            skipped["downgraded to narrow (different subjects)"] += 1
            continue

        merges.append((keep, away))

    for n in notes:
        print(f"  {n}")
    for why, n in skipped.most_common():
        print(f"  skipped {n}: {why}")
    print(f"\n{len(merges)} merges survive the guards")
    for k, a in merges:
        print(f"    keep {k:<28} <- {a}")

    if args.dry_run:
        print("\n[dry run] nothing written")
        return

    # ---- snapshot read:/tour_order on every file we are about to touch -----
    before = {s: (load(s)[2].get("read"), load(s)[2].get("tour_order"))
              for s in nodes}
    victims = {a for _, a in merges}

    # ---- apply merges -----------------------------------------------------
    for keep, away in merges:
        kp, kt, kfm, _ = load(keep)
        ap_, at, afm,_ = load(away)

        defines = frontier.as_list(kfm.get("defines"))
        have = {norm(str(x)) for x in defines}
        for extra in frontier.as_list(afm.get("defines")) + [away]:
            if norm(str(extra)) not in have:
                defines.append(str(extra))
                have.add(norm(str(extra)))
        set_key(kp, "defines", [str(x) for x in defines])

        # Inherit the victim's list memberships -- but only those the list
        # file actually records. A membership that lives only in the victim's
        # frontmatter would otherwise transfer to the survivor and leave it
        # claiming a list it does not appear in, which is exactly the
        # asymmetry check_symmetry.py exists to catch.
        lists = [frontier.link_basename(x)
                 for x in frontier.as_list(kfm.get("lists"))]
        for extra in frontier.as_list(afm.get("lists")):
            b = frontier.link_basename(extra)
            if b in lists:
                continue
            lf = os.path.join(ROOT, "lists", b + ".md")
            if not os.path.exists(lf):
                continue
            members = set(frontier.WIKILINK.findall(read(lf)))
            if away in members or keep in members:
                lists.append(b)
        set_key(kp, "lists", [f"[[{b}]]" for b in lists])
        cache.pop(keep, None)

        os.unlink(ap_)

    # ---- repoint every reference to a deleted slug ------------------------
    rewritten = files_touched = 0
    if victims:
        alias = {a: k for k, a in merges}
        pat = re.compile(r"\[\[(" + "|".join(
            re.escape(v) for v in sorted(victims, key=len, reverse=True))
            + r")(?=[\]\|#])")
        for dirpath, _, names in os.walk(ROOT):
            if ".git" in dirpath or "_scratch" in dirpath:
                continue
            for name in names:
                if not name.endswith(".md"):
                    continue
                p = os.path.join(dirpath, name)
                t = read(p)
                new, n = pat.subn(lambda m: "[[" + alias[m.group(1)], t)
                if n:
                    write(p, new)
                    rewritten += n
                    files_touched += 1

    # ---- dedupe list files ------------------------------------------------
    # Repointing turns `[[bellini]]` into `[[vincenzo-bellini]]`, and the list
    # that carried both slugs now names the survivor twice. Nothing validates
    # this -- check_symmetry only asks that every member exist -- so a tour
    # would simply read the same node twice.
    dedup_lines = 0
    listdir = os.path.join(ROOT, "lists")
    for name in sorted(os.listdir(listdir)):
        if not name.endswith(".md"):
            continue
        p = os.path.join(listdir, name)
        t = read(p)
        m = frontier.FRONTMATTER.match(t)
        head, body = (t[:m.end()], t[m.end():]) if m else ("", t)
        nl = "\r\n" if "\r\n" in t else "\n"
        seen, out, dropped = set(), [], 0
        for line in body.split(nl):
            links = frontier.WIKILINK.findall(line)
            if len(links) == 1 and line.lstrip().startswith("-"):
                if links[0] in seen:
                    dropped += 1
                    continue
                seen.add(links[0])
            out.append(line)
        if dropped:
            write(p, head + nl.join(out))
            dedup_lines += dropped

    # ---- apply narrows ----------------------------------------------------
    narrowed = 0
    for slug, drop in narrows:
        if slug not in nodes or slug in victims:
            continue
        p = os.path.join(ROOT, nodes[slug]["path"])
        fm = frontier.parse_frontmatter(read(p))
        want = {norm(str(x)) for x in drop}
        defines = [str(x) for x in frontier.as_list(fm.get("defines"))]
        kept = [x for x in defines if norm(x) not in want]
        if not kept or kept == defines:
            continue          # never strip a node's last claim on any name
        set_key(p, "defines", kept)
        narrowed += 1

    print(f"\n{len(merges)} nodes deleted, {rewritten} links repointed across "
          f"{files_touched} files, {narrowed} nodes narrowed, "
          f"{dedup_lines} duplicate list entries removed")

    # ---- verify -----------------------------------------------------------
    after = frontier.build(ROOT)["nodes"]
    bad = []
    for slug, (was_read, was_order) in before.items():
        if slug in victims:
            continue
        if slug not in after:
            bad.append(f"{slug} vanished")
            continue
        fm = frontier.parse_frontmatter(read(os.path.join(ROOT, after[slug]["path"])))
        if fm.get("read") != was_read or fm.get("tour_order") != was_order:
            bad.append(f"{slug} read/tour_order moved")
    if bad:
        sys.exit(f"ABORT: {len(bad)} node(s) changed unexpectedly: "
                 f"{', '.join(bad[:8])}")

    total_read = sum(1 for s, m in after.items()
                     if str(frontier.parse_frontmatter(
                         read(os.path.join(ROOT, m["path"]))).get("read")).lower() == "true")
    print(f"read: and tour_order verified unchanged; read: total now {total_read}")

    out = subprocess.run(
        ["git", "-c", "core.quotepath=false", "status", "--porcelain"],
        capture_output=True, encoding="utf-8", cwd=ROOT).stdout
    deleted = [l for l in out.splitlines() if l.startswith(" D ")]
    print(f"git sees {len(deleted)} deletion(s)")


if __name__ == "__main__":
    main()
