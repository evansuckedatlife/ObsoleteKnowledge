# ObsoleteKnowledge

A personal **knowledge base of (eventually) everything** — an [Obsidian](https://obsidian.md) vault of small, atomic articles ("nodes") woven into a navigable web, with built-in **read-tracking** so you can see what you've internalised and what's left.

It is modelled on the structure of the *AbsoluteKnowledge* learning vault, but adapted from inevitability-style teaching to **reference knowledge**: each node is a self-contained fact card you can read in under a minute.

The starting corpus is scoped to the topics in NAQT's *[You Gotta Know](https://www.naqt.com/you-gotta-know/)* series — the canonical "what every quiz-bowl player should know" catalogue (175 lists). NAQT is used **only as a topic map** (which subjects to cover); **all node content is written originally** from general knowledge and open sources. No NAQT article text is reproduced here — per their terms of use, their prose is neither ingested by a model nor stored in this repo.

## How it works

- **Nodes** live in `concepts/<category>/<name>.md` — one file per person, work, event, place, deity, concept, or phrase. Wikilink resolution is by basename across the whole vault, so every node name is globally unique.
- **The web** is built from `[[wikilinks]]`: every node's `## connections` section links to the other nodes it relates to. Open the **graph view** to see the whole web.
- **Lists** (`lists/<slug>.md`) are maps-of-content — one per *You Gotta Know* topic. A node can belong to several lists at once via its `lists:` frontmatter (e.g. *Achilles* is in both `greek-heroes` and `trojan-war-heroes`).
- **Progress tracking** is the `read:` frontmatter boolean on every node — the single source of truth.
  - The **graph view** colours nodes green when `read: true`, red when `read: false`.
  - `Read.base` / `Unread.base` / `All.base` give live tables (require the **Bases** core plugin).
  - Each node footer has a `Mark read` toggle (requires the **Meta Bind** community plugin) bound to the same `read:` field.
- **`index.md`** is the master catalogue of all 175 NAQT topics. Built lists are live links; unbuilt ones are dangling links — that dangling set *is* the to-do frontier, visible for free in the graph.

## What's built so far

The **Mythology & Belief** branch — 15 lists, ~150 nodes:

- *Mythology:* greek-heroes · trojan-war-heroes · mortal-women-in-greek-myth · greek-mythological-monsters · norse-gods · egyptian-deities · hindu-heroes · arthurian-characters
- *Belief:* founders-of-religious-traditions · religious-texts · hebrew-bible-characters · new-testament-characters · biblical-sayings · jewish-holidays · jewish-lifecycle-events

The other 160 topics appear in `index.md` as the frontier.

## Plugins

- **Bases** (core) — powers the read/unread tables.
- **Meta Bind** (community) — powers the in-node `read` toggles. Install via *Settings → Community plugins*.

## For Claude / contributors

`CLAUDE.md` is the operational guide (formats, protocols, the node template). `VISION.md` records *why* the system is shaped this way. `tools/` holds the focused specs Claude follows when authoring nodes, building lists, and validating the graph.
