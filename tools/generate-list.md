# generate-list

## Purpose

Build a **list** — a map-of-content for one NAQT *You Gotta Know* topic — and author its member nodes. A list is the curation layer: it points at nodes, which live under `concepts/<category>/` and may be shared with other lists.

## When to invoke

- On request: *"build the X list"*, *"do the Norse gods"*.
- When scoping a new subject area.

## Inputs

- The list slug (matches the NAQT topic slug, e.g. `norse-gods`).
- The membership scope — the entity *names* under that topic (names are facts; NAQT prose is off-limits per `generate-node.md`).
- The existing `concepts/` tree (to detect shared members and avoid duplicate basenames).

## Rules

### Step 1 — Enumerate membership
List the well-known entities for the topic by name. NAQT's entry names may be used as the checklist.

### Step 2 — Resolve cross-list dedup (critical)
For each member, check whether a node already exists (it may be shared with another list — e.g. *Achilles* in both `greek-heroes` and `trojan-war-heroes`):
- **Exists** → do *not* create a second file (basename collision breaks Obsidian). Instead add this list to the existing node's `lists:` frontmatter.
- **New** → author it via `generate-node.md`, with `lists:` set to every list it belongs to.

When two lists are authored together, assign each shared node a single **owner** list (the one that creates the file); the other list only links to it.

### Step 3 — Author member nodes
Via `generate-node.md`, one file per entity under the correct `concepts/<category>/`.

### Step 4 — Write the list MOC
`lists/<slug>.md` from the template below.

### Step 5 — Update the index
In `index.md`, promote this topic from a dangling wikilink to a real `[[<slug>]]` link.

### Step 6 — Validate
Run `tools/validate-graph.md`.

## Output template

`````markdown
---
type: list
category: <category>
read: false
---

# <List Title>

One-sentence description of the topic and why it matters for quiz bowl.

## nodes

- [[node-a]] — one-line hint.
- [[node-b]] — one-line hint.

## progress

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
      - property: file.name
        direction: ASC
```
`````

`file.hasLink(this.file)` selects every node linking to this MOC (its members, via their `lists:` frontmatter). `lists.containsLinkTo(...)` is **not** a real Bases function — don't use it.

## Quality checks
1. **No duplicate basenames** — shared members are authored once and multi-linked.
2. **Membership sync** — every node listed in `## nodes` has this list in its `lists:` frontmatter, and vice versa.
3. **Index updated** — the topic is a live link in `index.md`.
4. **Progress base** — the `lists.containsLinkTo` filter matches this list.
