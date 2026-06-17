# ObsoleteKnowledge

A personal Obsidian "knowledge of everything" vault — atomic reference nodes
woven into a wikilinked web, with read-tracking. Scope is NAQT's *You Gotta
Know* catalogue (187 topics), all built. Content is original prose (Haiku-
authored); NAQT is used only as a topic map, never ingested.

## Structure
- `concepts/<category>/<slug>.md` — one fact-node per entity
- `lists/<slug>.md` — map-of-content per NAQT topic
- `index.md` — master catalogue · `BUILD-ORDER.md` — build queue
- `AGENTS.md` / `CLAUDE.md` / `VISION.md` — authoring spec

## Status
- 187/187 NAQT topics · ~2,000 nodes · 15 categories complete
- Enrichment pass adding cross-domain connector hubs underway

## Node format
`type` / `category` / `defines` / `related` / `lists` / `read:` frontmatter;
sections: summary → you gotta know → connections → see also; footer Mark-read toggle.

## Sourcing rule (non-negotiable)
NAQT is a topic map only — its prose is never fetched into an LLM or stored.
All content is written originally from general knowledge.
```
