# ObsoleteKnowledge — Vision

This file records the **why** behind the structural choices. `CLAUDE.md` is the operational guide — what to do. This is the design compass — why the system is shaped this way.

---

## What this repo is for

A durable, personal knowledge base aimed at *recall* — the kind of broad factual command rewarded by quiz bowl, trivia, and a generally well-furnished mind. The target outcome: open the vault, see at a glance what you know and don't, and read any node in under a minute to top up.

Two design moves fall out of that target:

1. **Atomic, durable nodes.** Every fact-cluster is its own file. Reviewing later means opening a file, not re-deriving anything. The unit is small enough to read in one sitting and be marked read honestly.
2. **A web, not a list.** Knowledge sticks when it's connected. Nodes link to nodes; the graph view makes the connectivity (and the gaps) visible. A fact you can reach from five directions is a fact you keep.

---

## Why it's adapted from AbsoluteKnowledge, not copied

AbsoluteKnowledge teaches *concepts* via "deterministic inevitability" — `forcing → mechanism → opens`, where each idea is *forced* by the prior. That schema is right for a prerequisite DAG (math → neural nets → transformers). It is wrong for **facts about the world**: there is no "problem that made *Zeus* inevitable." Zeus is not derived; he is *known*.

So we keep AbsoluteKnowledge's skeleton — Obsidian vault, YAML frontmatter, wikilink web, `read:` tracking, graph colouring, `.base` tables, MOC layer — and swap the per-node body for a **reference schema**: `summary → you gotta know → connections → see also`. The `requires` DAG becomes a flat `related` web (no prerequisite ordering); `courses` become `lists` (unordered topical collections); `seq` and prev/next nav are dropped because reference sets aren't walked in order.

---

## Why "you gotta know" ordering (recognisable first)

Within a node, clues are ordered most-recognisable → most-obscure. This mirrors how quiz-bowl questions are written (hard early clues, easy "giveaway" at the end) *read backwards* — so the learner front-loads the highest-yield identifier and only then layers depth. It also means a half-read node still leaves you with the fact most likely to come up.

---

## Why flat nodes under broad categories, not per-list folders

A figure like *Achilles* belongs to both `greek-heroes` and `trojan-war-heroes`. If folders were per-list, he'd need two files — and Obsidian resolves wikilinks by **basename**, so two `achilles.md` files would collide and break every `[[achilles]]` link in the vault. Therefore: **one node per entity, globally unique basename**, filed under a broad `category` (mythology, religion, …), with multi-list membership expressed in `lists:` frontmatter. The list a learner experiences is a MOC that *points at* nodes, not a folder that *owns* them — exactly the AbsoluteKnowledge concept/course split.

---

## Why NAQT is a topic map only

NAQT's *You Gotta Know* is the best-curated answer to "what's worth knowing" for this purpose, so it defines our **scope** — which topics, which entries. But each NAQT article's text is copyrighted and its usage note explicitly prohibits putting the article "into any large language model." We honour that exactly: their *prose* is never fetched into a model or stored here. We use only the *facts* — which are not copyrightable (Feist v. Rural) — and write every node from scratch against open sources. The selection of "which ten Norse gods" is a standard reference set, not NAQT's invention; the wording is ours. This keeps the vault clean to publish.

---

## Why `read:` is the single source of truth

One boolean, three surfaces: the graph colours by it, the `.base` tables filter on it, the Meta Bind footer toggle edits it. There is deliberately no second state (no `## Understood?` checkbox, no separate "in progress"). Multiple sources of truth drift; one does not. Marking a node read is a small honest act, and the green-vs-red graph is the dashboard.

---

## Open questions

- Should heavily-referenced hubs (the-trojan-war, the-iliad, a per-mythology overview) be authored as real nodes, or left dangling as frontier? Currently: list-MOCs are the hubs; other refs dangle.
- Granularity: when is something one node vs. several? (The "Osiris/Set family quarrel" — folded into the deity nodes, or its own node?)
- Should `related` edges be typed (rival / parent / teacher) rather than prose, so tools can traverse them?
- At ~100+ nodes, does validation need a deterministic script rather than a Claude-executed pass?
