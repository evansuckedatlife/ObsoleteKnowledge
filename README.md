# ObsoleteKnowledge

A personal **knowledge base of (eventually) everything** — an [Obsidian](https://obsidian.md) vault of small, atomic articles ("nodes") woven into a navigable web, with built-in **read-tracking** for active recall practice.

Scope: **187 topics** from NAQT's *[You Gotta Know](https://www.naqt.com/you-gotta-know/)* series, fully built. ~2,000 nodes across 15 categories. All content is **original prose** sourced from general knowledge — NAQT is used only as a topic map, never ingested.

---

## Quick Start

### 1. Download the vault

**Option A: Git clone**
```bash
git clone https://github.com/evansuckedatlife/ObsoleteKnowledge.git
cd ObsoleteKnowledge
```

**Option B: Download as ZIP**
Click **Code** → **Download ZIP** on this repo, then unzip it.

### 2. Open in Obsidian

1. Download [Obsidian](https://obsidian.md) (free).
2. Launch Obsidian.
3. Click **Open folder as vault** and select the `ObsoleteKnowledge` folder.
4. When prompted about plugins, click **Enable** (to activate the Bases plugin).

### 3. Install community plugins (optional but recommended)

The vault ships with **Bases** enabled, but to use the **Mark read** toggles in node footers, install **Meta Bind**:

1. In Obsidian, go **Settings → Community plugins → Browse**.
2. Search for `Meta Bind`.
3. Click **Install** then **Enable**.
4. Restart Obsidian.

### 4. Start reading

- Open **`index.md`** to see all 187 topics.
- Click any **topic list** (e.g., `[[greek-heroes]]`) to jump to that subject.
- Open a **node** (e.g., `Achilles`) to read about it.
- Toggle **"Mark read"** at the bottom of each node to track progress.
- Open the **Graph view** (**Ctrl/Cmd + G**) to visualize the web of knowledge.

---

## How it works

### Nodes — atomic facts

Each entity (person, work, event, place, concept, etc.) is one file in `concepts/<category>/<slug>.md`. Every node has:

- **summary** — one paragraph: what/who, when/where, why it matters
- **you gotta know** — 4–8 bulleted clues, ordered most-recognisable → most-obscure
- **connections** — links to related nodes (family, rivals, cause/effect)
- **see also** — peer nodes worth reading next
- **read toggle** — mark `true` once you've absorbed it

### Lists — maps of content

Each of the 187 NAQT topics gets one **list** (`lists/<slug>.md`) — a curated MOC showing which nodes belong to it, plus a live read-progress table. A single node can belong to multiple lists (e.g., *Achilles* is in both `greek-heroes` and `trojan-war-heroes`).

### The web — wikilinks

Every node is woven via `[[wikilinks]]` — links by basename across the entire vault. Open **Graph view** to see the network:

- **Green nodes** = read (`read: true`)
- **Red nodes** = unread (`read: false`)
- **Dangling links** = concepts mentioned but not yet authored (the frontier)

### Progress tracking — one source of truth

The **`read: false`** frontmatter field on each node is the single source of truth:

- The **graph** colours nodes by it.
- The **"Mark read" toggle** (footer) edits it.
- **Bases** tables (`.base`) filter and aggregate read status.

---

## What's here now

### Fully built (187/187 topics)

All NAQT *You Gotta Know* topics are complete:

- **Mythology & Belief** (8 lists, ~300 nodes): Greek, Norse, Egyptian, Hindu mythology; founders of religions; biblical figures and holidays.
- **Literature & Linguistics** (12 lists, ~250 nodes): Classical works, Shakespeare, modern literature, literary terms.
- **History & Geography** (18 lists, ~400 nodes): World history, US history, geography, world capitals, ancient civilizations.
- **Science & Nature** (12 lists, ~300 nodes): Biology, chemistry, physics, astronomy, earth sciences.
- **Fine Arts** (8 lists, ~200 nodes): Painting, sculpture, music, composers, architecture.
- **Social Sciences** (10 lists, ~200 nodes): Philosophy, psychology, economics, political theory.
- **Pop Culture & Sports** (14 lists, ~250 nodes): Films, TV, comics, sports figures, Olympics.
- **Religion & Practice** (8 lists, ~200 nodes): Religious practices, holidays, spiritual figures.

### Current enrichment pass

Adding cross-domain **connector hubs** — high-degree nodes (pivotal events, major works, per-domain overviews) that tie multiple topics together and reduce fragmentation.

---

## Navigation tips

### Start here

- **`index.md`** — the master catalogue; jump to any topic.
- **`BUILD-ORDER.md`** — historical build sequence (for reference).

### Find something specific

1. Use Obsidian's **Quick Switcher** (**Ctrl/Cmd + K**) and type the node or list name.
2. Use **Graph view** to explore visually; right-click any node to open it.
3. Use **Search** (**Ctrl/Cmd + F**) to find text inside nodes.

### Understand the structure

- **`VISION.md`** — why the system is designed this way (design compass).
- **`CLAUDE.md`** — operational guide for authoring nodes (format spec).
- **`tools/`** — focused specs for node/list generation and validation.

---

## For contributors

Before authoring nodes, **read `CLAUDE.md`** (operational guide) and **`VISION.md`** (design rationale).

### The sourcing rule (non-negotiable)

**NAQT is a topic map only.** Its articles' prose is copyrighted; never fetch, paste, or paraphrase it into this repo or an LLM. All content is written **originally** from:

- General knowledge
- Wikipedia, Britannica, open references
- Primary texts and open-source materials
- Not from NAQT

*Facts are free; expression is not.*

### Quick authoring workflow

1. **New node:** Follow `tools/generate-node.md`.
2. **New list:** Follow `tools/generate-list.md`.
3. **After any edit:** Run `tools/validate-graph.md` to check wikilink integrity, dedup, and formatting.

---

## Plugins used

- **Bases** (core plugin) — live tables filtering by metadata (read status, type, category).
- **Meta Bind** (community plugin) — in-node read toggles bound to frontmatter.

Both are optional but recommended for the full experience.

---

## File structure

```
ObsoleteKnowledge/
├── README.md                          # You are here
├── VISION.md                          # Design rationale
├── CLAUDE.md                          # Authoring spec & protocols
├── index.md                           # Master catalogue (187 topics)
├── BUILD-ORDER.md                     # Build history
├── concepts/
│   ├── mythology/                     # ~300 nodes (Greek, Norse, Egyptian, Hindu, etc.)
│   ├── literature/                    # ~250 nodes (works, authors, terms)
│   ├── history/                       # ~400 nodes (events, figures, eras)
│   ├── science/                       # ~300 nodes (scientists, theories, discoveries)
│   ├── fine-arts/                     # ~200 nodes (artists, movements, techniques)
│   ├── social-science/                # ~200 nodes (thinkers, schools, concepts)
│   ├── pop-culture/                   # ~250 nodes (films, TV, comics, music)
│   ├── religion/                      # ~200 nodes (traditions, figures, practices)
│   └── [etc.]
├── lists/                             # 187 MOCs (one per NAQT topic)
│   ├── greek-heroes.md
│   ├── trojan-war-heroes.md
│   ├── shakespeare-plays.md
│   └── [etc.]
└── tools/                             # Authoring specs
    ├── README.md
    ├── generate-node.md
    ├── generate-list.md
    └── validate-graph.md
```

---

## Why this exists

A personal vault for **recall-based learning**. The goal: broad factual command rewarded by quiz bowl, trivia, and a well-furnished mind. Atomic nodes + wikilinked web + read-tracking = knowledge that sticks.

Inspired by (but adapted from) [*AbsoluteKnowledge*](https://github.com/kieran-mackle/AbsoluteKnowledge) — the skeleton is the same (Obsidian, YAML, wikilinks, read tracking), but the per-node body is reference material instead of concept-chain teaching.

---

## Licence

Content © 2024 (personal work). You're welcome to fork, read, and build on it for personal learning. See the repo licence for details.

---

## Questions?

Check **`VISION.md`** for design decisions, **`CLAUDE.md`** for authoring rules, or **`tools/README.md`** for generation specs. If you're contributing, those three files are your north star.

Happy reading.
