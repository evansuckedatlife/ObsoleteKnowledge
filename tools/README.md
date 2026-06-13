# Tools

Focused specs Claude follows when working in this vault. Each describes a capability's purpose, when to invoke it, and the rules it must satisfy. Invoke a tool by reading its spec and following it exactly, not by paraphrasing.

## Available

| Tool | Purpose | Invoked during |
|---|---|---|
| [generate-node.md](generate-node.md) | Author one reference node (`summary → you gotta know → connections → see also`) from open sources, never NAQT prose. | Adding any node. |
| [generate-list.md](generate-list.md) | Build a list MOC and its member nodes; resolve cross-list dedup and multi-membership. | Building a *You Gotta Know* topic. |
| [validate-graph.md](validate-graph.md) | Check basename uniqueness, wikilink integrity, dedup, frontier accuracy, formatting invariants. | After any edit. |

## Not yet built

- `promote-frontier.md` — turn a dangling wikilink that recurs often into an authored node, wiring its backlinks.
- `add-hubs.md` — author high-degree connective nodes (events, works, per-domain overviews) once the leaf nodes exist.
- `check-script.py` — deterministic, CI-runnable validation for when the graph outgrows a Claude-executed pass.

## The sourcing rule (applies to every tool)

NAQT is a **topic map only**. Never fetch, paste, or paraphrase NAQT article prose into a model or this repo. Write original content from general knowledge and open sources. Facts are free; expression is not.
