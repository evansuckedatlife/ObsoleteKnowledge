# ObsoleteKnowledge — Claude Instructions

This repo is a personal knowledge base: an Obsidian vault of atomic reference nodes woven into a web, with read-tracking. The design rationale lives in `VISION.md` — read it before any structural change. This file is the **operational** guide: the formats, protocols, and checks you follow when working here.

---

## Summary

- **Nodes** are the atomic unit — one markdown file per entity (person, deity, hero, monster, work, text, event, place, concept, phrase). They live in `concepts/<category>/<name>.md` and form a **web** via `[[wikilinks]]`, resolved by basename across all subfolders.
- **Lists** (`lists/<slug>.md`) are maps-of-content — one per NAQT *You Gotta Know* topic. A node belongs to one or more lists via its `lists:` frontmatter. Lists are the curation layer; nodes are reused across them.
- **`index.md`** is the master catalogue of all 175 NAQT topics. Unbuilt topics are dangling wikilinks — the to-do frontier.
- The format is Obsidian-native: YAML frontmatter for metadata, `[[wikilinks]]` for the web, `read:` boolean for progress.
- **Sourcing rule (non-negotiable):** NAQT is a *topic map only*. Never fetch, paste, ingest, or paraphrase NAQT article prose — their terms forbid putting their text into an LLM. Write **original** content from general knowledge, grounded in open sources (Wikipedia, Britannica, primary texts). Facts are free; expression is not.

---

## Authoring format

Every node file follows this template exactly:

`````markdown
---
type: <person | deity | hero | monster | work | text | event | place | concept | phrase | practice | holiday>
category: <mythology | religion | literature | science | history | fine-arts | geography | social-science | pop-culture | sports>
defines: [canonical-name, alias1, alias2]
related: ["[[node-a]]", "[[node-b]]"]
lists: ["[[list-slug]]"]
read: false
---

# Display Name

## summary

One short paragraph (2–4 sentences) establishing identity: *what / who it is, when and where, and why it is worth knowing.* This is the "if you remember one thing" layer. Plain prose; *italics* for emphasis.

## you gotta know

The buzz-worthy identifying clues — what a quiz-bowl player must be able to recall. Bulleted, ordered **most-recognisable first → deepest/most-obscure last** (mirrors how questions go from hard clues to giveaways). Each bullet is one fact. Use *italics* for key names, titles, and terms. Aim for 4–8 bullets.

## connections

How this node ties into the rest of the web. Each bullet is a `[[wikilink]]` + a one-line reason. Link generously to other nodes (family, rivals, same myth, teacher/student, cause/effect). Links to concepts not yet authored are fine — they render as dangling links and mark the frontier.

- [[related-node]] — why they're connected.

## see also

Sibling nodes worth reading next — usually peers from the same list. A single line of wikilinks separated by ` · `.

- [[peer-a]] · [[peer-b]] · [[peer-c]]

<!-- footer -->

---

Lists: [[list-slug]] · Mark read: `INPUT[toggle:read]`
`````

**Tracking:** the `read: false` frontmatter field is the single source of truth for whether the node has been internalised. Flip it to `true` after reading. The graph view colours by it; `Read.base`/`Unread.base` aggregate it; the footer `INPUT[toggle:read]` (Meta Bind plugin) is a second editing surface bound to the *same* field — never a parallel state. Never add a `## Understood?` checkbox.

**Footer:** introduced by the literal `<!-- footer -->` marker so it is idempotently regenerable. It carries the node's list memberships (as wikilinks) and the read toggle. No prev/next nav — lists are unordered reference sets, not sequenced courses, so there is no `seq` field.

### Formatting rules — strict

- `**bold**` is reserved for **term introduction** — a name or term this node is the canonical home for (it must appear in this node's `defines`). Never bold for emphasis or for clue labels.
- `*italic*` is the default for emphasis, key names/titles inside clues, and within-prose highlights.
- `` `code` `` for literals (dates in a fixed notation, transliterations, file/term tokens).
- All references to other nodes use wikilinks: `[[medusa]]`, not "Medusa".
- `defines` is bare strings — the canonical name plus any aliases/alternate spellings the node owns (drives wikilink resolution and dedup).
- `related` is wikilink strings — the web edges. Not a prerequisite DAG; just "is connected to."
- `lists` is wikilink strings — every NAQT list this node belongs to. A shared node (e.g. a figure in two lists) lists **all** of them.
- `read` is a boolean — always authored as `false`.

Every list file (`lists/<slug>.md`) follows this template:

`````markdown
---
type: list
category: <category>
read: false
---

# <List Title>

One-sentence description of what this topic covers and why it matters for quiz bowl.

## nodes

The members of this list. Each is a wikilink; unbuilt members are dangling (the frontier).

- [[node-a]] — one-line hint.
- [[node-b]] — one-line hint.

## progress

Live read-status table for this list's nodes (requires the **Bases** core plugin).

```base
filters:
  and:
    - lists.containsLinkTo(this.file.asLink())
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
      - property: file.name
        direction: ASC
```

## source

Scoped from NAQT's *You Gotta Know* topic [`<slug>`](https://www.naqt.com/you-gotta-know/<slug>.html). Content authored originally; NAQT used as topic map only.
`````

---

## Protocols

### "Build the list X" — the list protocol *(primary entry point)*

1. Confirm `lists/<slug>.md` does not already exist (or offer to extend it).
2. Determine the membership: the well-known entities under that topic. NAQT's entry **names** may be used as the scope checklist (names are facts) — but **never** read NAQT's prose into the model.
3. Resolve cross-list overlaps: if a member already exists as a node (shared with another list), **do not duplicate** — add this list to that node's `lists:` frontmatter and link to it. Wikilinks resolve by basename, so duplicate basenames are forbidden.
4. Author each new member node via the node protocol below.
5. Write `lists/<slug>.md` from the list template; add the slug to `index.md` (promote it from dangling to a real link).
6. Run `tools/validate-graph.md`.

### "Add node X" — the node protocol

1. Pick the canonical slug (kebab-case of the common English name; disambiguate generic names, e.g. `jewish-marriage`, `john-the-apostle`).
2. Choose `type` and `category`. Set `lists:` to every list X belongs to.
3. Write `summary` → `you gotta know` → `connections` → `see also` from the template, sourced originally (open sources, not NAQT prose).
4. Wikilink every other node referenced. Dangling links to unbuilt concepts are expected and good.
5. Append the `<!-- footer -->` block.
6. Validate.

### "Check the graph" — the validation protocol

Invoke `tools/validate-graph.md`.

---

## Tools

| Tool | When |
|---|---|
| [tools/generate-node.md](tools/generate-node.md) | Authoring a node. Defines the sourcing discipline and the section rules. |
| [tools/generate-list.md](tools/generate-list.md) | Building a list MOC and its member nodes; resolving cross-list dedup. |
| [tools/validate-graph.md](tools/validate-graph.md) | After any edit; checks wikilink/basename integrity, dedup, frontier accuracy. |

---

## When in doubt

Read `VISION.md`. The sourcing rule is the one inviolable constraint — when unsure whether something is "facts" (free) or "NAQT's expression" (off-limits), default to writing it yourself from scratch.
