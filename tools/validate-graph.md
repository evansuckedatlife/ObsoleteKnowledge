# validate-graph

## Purpose

Enforce the vault's structural invariants: globally-unique basenames, clean wikilinks, correct dedup/multi-membership, frontier accuracy, and the formatting rules. At the current scale (~hundreds of nodes) this is a Claude-executed pass; graduate to a script when it stops scaling.

## When to invoke
- After authoring or editing any node or list.
- On request: *"check the graph"*, *"validate"*.

## Inputs
- All files under `concepts/` and `lists/`, plus `index.md`.
- For each node: frontmatter (`type`, `category`, `defines`, `related`, `lists`, `read`) and body (`summary`, `you gotta know`, `connections`, `see also`).

## Checks

Run all; report grouped by severity.

### 1. Basename uniqueness *(error)*
No two files anywhere in the vault share a basename. Obsidian resolves wikilinks by basename; a collision silently breaks links. This is the single most important check.

### 2. Membership consistency *(error)*
For every node, each list in its `lists:` frontmatter must list that node in its `## nodes` section, and every node listed in a list's `## nodes` must carry that list in its `lists:`. No drift.

### 3. Frontmatter completeness *(error)*
Every node has `type`, `category`, `read` (boolean, authored `false`), non-empty `defines`, and a `lists` list (may be empty only for hub nodes). Every list file has `type: list`.

### 4. Wikilink resolution *(info)*
For every `[[X]]` in a node body: if `concepts/**/X.md` or `lists/**/X.md` exists, fine; if not, it is a **dangling** link — info-level, the expected frontier (especially in `connections`). Report so they aren't forgotten; they are not failures.

### 5. Footer + tracking *(warning)*
Every node ends with the `<!-- footer -->` block carrying its `lists:` as wikilinks and the `INPUT[toggle:read]` line. No node contains a `## Understood?` section or any tracking state other than `read:`.

### 6. Formatting invariants *(error)*
- Bold (`**term**`) only for terms in the node's own `defines`. Bolded emphasis or clue labels are errors → switch to italics.
- References to other nodes are wikilinks, not bare text.

## Output template
```
Graph validation report — <N> nodes, <L> lists scanned

ERRORS (<M>)
- <file>: <description + fix>

WARNINGS (<M>)
- <file>: <description>

INFO (<M>)
- <file>: dangling [[X]] in connections (frontier)

SUMMARY
- <N> nodes, <L> lists, <E> web edges
- <M> errors, <M> warnings, <M> dangling
```
Zero errors ⇒ the graph is **valid**; warnings and dangling links are expected during active authoring.

## Quality checks before reporting
1. **Completeness** — scan every file, not a sample.
2. **Basename map** — build the full basename→path map first; that surfaces check 1 and 4 together.
3. **Actionable** — each finding names the file, the offending content, and the fix.
