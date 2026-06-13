# generate-node

## Purpose

Produce one reference node — a self-contained fact card for a single entity (person, deity, hero, monster, work, text, event, place, concept, phrase, practice, holiday) that a reader can absorb in under a minute and mark read.

## When to invoke

- Authoring a new member of a list.
- On explicit request: *"add a node for X"*, *"write up X"*.

## Sourcing discipline — read first

- **NAQT is a topic map only.** You may use the *name* of the entity as scope (names are facts). You may **not** fetch, read, paste, or paraphrase NAQT's article prose. Their terms forbid putting their text into an LLM.
- Write **original** content from your own general knowledge, grounded in open reference sources (Wikipedia, Britannica, public-domain primary texts). If unsure of a specific fact, state it less precisely rather than invent it.
- Facts (dates, relationships, plot points, attributes) are free to use. Someone else's *sentences* are not — produce your own.

## Inputs

- The canonical name (and known aliases) of the entity.
- The list(s) it belongs to, and its `type` and `category`.
- The set of already-authored nodes (to wikilink correctly and avoid duplicate basenames).

## Rules

### Slug & frontmatter
- Slug: kebab-case of the common English name. Disambiguate generic names (`jewish-marriage`, not `marriage`; `john-the-apostle`, not `john`). The slug is the filename and the wikilink target; it must be globally unique by basename.
- `defines`: canonical name + every alias/alternate spelling this node owns.
- `related`: wikilinks to connected nodes (web edges, not prerequisites).
- `lists`: **every** list this entity belongs to (check for cross-list membership before writing).
- `type`, `category`, `read: false` as specified.

### summary
2–4 sentences. Identity + why-it-matters. The single highest-yield paragraph. Plain prose, *italics* for emphasis only.

### you gotta know
- 4–8 bullets, each one fact, ordered **most-recognisable → most-obscure**.
- *Italics* for key names, titles, terms. Never bold for emphasis.
- These are the identifying clues — the things that, heard in a question, should make this entity click.
- Concrete and specific: a named work, a number, a relationship, a famous line — not vague ("was important").

### connections
- Bulleted `[[wikilink]] — reason`. Link to family, rivals, teachers/students, same myth/event, cause/effect, the work they appear in.
- Dangling links (to unbuilt nodes) are expected and good — they mark the frontier. Prefer linking the *right* concept even if it isn't authored yet.

### see also
- One line of sibling wikilinks separated by ` · ` — usually peers from the same list.

### footer
Append exactly:
```
<!-- footer -->

---

Lists: [[list-a]] · [[list-b]] · Mark read: `INPUT[toggle:read]`
```

## Formatting invariants (validator-enforced)
- Bold = term introduction only (must be in `defines`). Emphasis uses italics.
- Every reference to another node is a wikilink.
- No `## Understood?` section; `read:` + the footer toggle are the only tracking.

## Quality checks before writing
1. **Sourcing** — no NAQT prose used; content is original and factual.
2. **Basename uniqueness** — the slug doesn't collide with an existing node.
3. **Membership** — `lists:` includes every list this entity belongs to; if it's shared, the node is authored once and linked from each.
4. **Clue quality** — every "you gotta know" bullet carries a specific, checkable fact, ordered recognisable-first.
5. **Connectivity** — at least 2–3 `connections`; wikilinks well-formed.
