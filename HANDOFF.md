# Handoff — ObsoleteKnowledge, 2026-09-04

State at commit `f930f2e7`. Working tree clean, `main` in sync with origin.

---

## Where things stand

| | |
|---|---|
| nodes | **5,410** (2,408 at session start) |
| `read:` | **69** — unchanged through every wave. This is the number to protect. |
| graph | **1 connected component, 100% of the vault.** 0 stranded, 0 dead ends, 220 orphans (4.1%) |
| interdisciplinary | **19.9%** of links cross a category (was ~1% originally, 10.2% mid-session) |
| frontier | 2,970 unresolved targets, 3,241 dangling refs |
| validators | `_scratch/validate.py` and `_scratch/check_symmetry.py` both clean |

**Buzzer podcast** — 66 episodes in the private Spotify library, 59 in the public feed at
`https://evansuckedatlife.github.io/buzzer/feed.xml`. 140 mp3s rendered locally,
**74 built but not yet uploaded** (Spotify's per-account cap). Audio is hosted as GitHub
Release assets, not in the repo — Pages caps a published site at 1 GB and this collection
passes that around 110 episodes.

Nothing is running. `agy` quota is available.

---

## Three queues, ready to go

```bash
# 1. Canadian / RFTT gap — 125 of 128 classified subjects unwritten. HIGHEST VALUE.
#    The vault was NAQT-scoped (American); RFTT is Canadian and asks about
#    Alberta and Nova Scotia constantly. See "RFTT" below.

# 2. Tail expansion — 2,034 filtered slugs remain
python tools/agy_write.py --wave <wave.json> --jobs 5 --bundle 4

# 3. Audio backlog — 74 rendered episodes waiting on the upload cap
python tools/audio/publish.py --pending
python tools/audio/run_queue.py --queue _scratch/build_queue.txt --no-publish
python tools/audio/feed.py --out ../buzzer \
    --base-url https://evansuckedatlife.github.io/buzzer \
    --email exhu2009@gmail.com --push
```

---

## The rules that matter

**1. `read:` is the user's real reading progress. Never let a model edit an existing node.**
Two separate waves destroyed or reset it. The pattern that works: agents **return data**,
a script applies it. `tools/apply_links.py` is the reference implementation — it rewrites
exactly one frontmatter line, then re-reads every touched file and aborts if any `read:`
or `tour_order` moved.

**2. Sourcing is non-negotiable.** NAQT and Reach For The Top packs are both copyrighted.
Their *questions* are their expression and never enter a model or the repo. Only answer
names — facts — are taken, and every node is written originally. See `VISION.md`.

**3. Run the collision audit after every wave.** The duplicate rate climbs as the vault
fills: ~1% in the ≥2-reference waves, ~4% in tail tranche 1, ~10% by tranche 2. The failure
mode is synonyms, which no slug filter can catch — `clock-arithmetic` beside
`modular-arithmetic`, `age-of-fishes` beside `devonian-period`. Each is a reasonable title
in isolation; they are only duplicates relative to what already exists.

**4. Commit after every wave.** A prior incident lost ~550 uncommitted nodes.
`git fetch && git rebase origin/main` first — the user edits README from another machine.

---

## Tooling

| tool | what it does |
|---|---|
| `tools/frontier.py` | alias-aware frontier map; the BFS queue |
| `tools/wave.py` | partitions the frontier into disjoint agent batches |
| `tools/agy_write.py` | writes nodes via `agy` + Gemini, bundled |
| `tools/hubify.py` | puts new nodes in `<category>-hubs` lists |
| `tools/linkaudit.py` | orphans, components, cross-category share |
| `tools/enrich_targets.py` | work list of orphaned / thin / insular nodes |
| `tools/apply_links.py` | applies verified links, guarding `read:` |
| `tools/consolidate.py` | duplicate names, shadowed slugs, stubs |
| `tools/rftt_topics.py` | RFTT answer set → topic map |
| `tools/pick_tail.py` | filters the single-reference tail |
| `tools/audio/*` | bundle → narrate → build → publish → feed |

---

## Gotchas — each of these cost real time

**Frontmatter**
- Parse with **PyYAML, never regex**. Obsidian rewrites flow style to block on every save,
  and `^aliases:\s*(.*)$` lets `\s*` cross the newline, swallowing the first list item.
  That silently erased aliases and made existing nodes look missing.
- Inserting a key after the `defines:` *line* breaks **block-style** YAML — it lands between
  the key and its own items. Insert after the block.
- The vault is committed **CRLF** with `.gitattributes` pinning it. Writing LF rewrites whole
  files in git's eyes and hides real changes.

**Windows**
- `os.execv` does **not** replace the process. It spawns a child and the parent exits
  immediately, so a caller not holding a pipe sees the script "finish" in milliseconds while
  the real work runs detached. This stacked a dozen 1 GB renders and exhausted RAM; ONNX
  then reported `bad allocation`, which reads like a model fault. **Spawn and wait.**
- Killing a background shell does **not** kill its Python child. Interrupted batches leak
  ~1 GB renders. Check with:
  `Get-CimInstance Win32_Process -Filter "Name like 'python%'" | Where-Object { $_.CommandLine -like '*build.py*' }`
- `subprocess.run(text=True)` decodes with the locale codec (cp1252) and mangles the em dash
  in `ObsoleteKnowledge — Mythology`. Pass `encoding="utf-8"` or match-by-title dedup fails
  and creates duplicate shows.
- Always force UTF-8 on stdout. A chapter title carrying `U+02BC` (Baháʼu'lláh) crashed a
  *progress print* after a completed 20-minute render.
- Python text-mode writes turn `\n` into `\r\n`. A queue file written that way gave every
  shell-loop entry a trailing CR and produced 482 silent "failures".
- A child inheriting a `while read` loop's stdin **eats queue lines** —
  `african-american-...` became `can-american-...`. Use `stdin=DEVNULL`.
- Colon-mangled path spills: an unquoted Windows path used as a literal filename lands in the
  repo root. Happened three times; now gitignored.

**Models**
- `agy -p` has nobody to approve a permission prompt, so **any tool call returns nothing at
  all**. Feed everything inline. The upside: the model cannot damage the vault.
- Quota is the binding cost, not tokens. Bundling 4 related slugs per call cut input roughly
  in half — over half of each prompt was the exemplar and hub menu, re-sent per slug.
- A two-string schema does not stop a model putting both strings in one field. 99 of 352
  verified links came back as `sweatt-v-painter_united-states` in the `slug` field.
- Filter new slugs against **aliases and defines**, not just node basenames. A slug merged
  away lives on as an alias; a basename-only filter re-creates it and shadows the alias.

**Audio**
- `--json` goes **before** the subcommand.
- Covers are mandatory on every show and episode.
- Chapters: ≥2, first at exactly 0, ≥5 s apart, all starts < duration. Nothing server-side
  validates this — `build.py` asserts it.
- Kokoro RTF ≈ 0.4 uncontended (not 1.5 — that was measured under load). Throttled to
  3 threads it takes ~21% of the machine instead of ~59%.
- `kokoro-onnx` 0.4.7 sends `speed` as int32 where the model wants float; patched at runtime,
  not in the venv, which `tts setup` would overwrite.

---

## RFTT — the biggest open opportunity

32 Senior Packs (2022-23) in `Downloads/2022-23-…/2022-23`. Extracted as a **topic map only**:
3,054 answers → 2,848 distinct subjects, **539 already in the vault, 2,309 not**.

The gap is overwhelmingly **Canadian**, because the vault was scoped to an American
competition:

| asked | subject |
|---|---|
| 8× | Nova Scotia |
| 7× | Alberta |
| 4× | British Columbia · Manitoba · Saskatchewan · Calgary |
| 3× | Ontario · Quebec · Yukon · PEI · Montreal · Winnipeg |

`_scratch/rftt_classified.json` holds 128 classified subjects; **125 are unwritten**.

Note: half the packs mark answers `A.` rather than `A:`. Missing that undercounts by ~60%.

---

## Open decisions for Evan

1. **Consensus** — no material exists locally. The "update modern sections in prep for
   Consensus" work is unscoped without it, and its format shouldn't be guessed at.
2. **Is Buzzer actually live on Spotify?** It does not appear in catalog search. The feed is
   healthy and serving. Only the Creators dashboard can distinguish "still indexing" from
   "submission incomplete".
3. **129 duplicate names** in `_scratch/consolidate.json` — most need `defines` narrowed
   rather than merging (`rome` the city vs `roman-empire` are genuinely different nodes that
   both claim the name). A few, like `torah`/`pentateuch`, are true merges.
4. **Gemini's house style** — its nodes run ~560 words against Haiku's ~420, and twice as
   densely linked. Better for recall, visibly different from the 3,720 Haiku nodes.
5. `consolidate.py`'s "vague slug" heuristic **over-fires** — it flags `photoelectric-effect`
   and `blood-type`, which are real subjects. Treat that column as a prompt to look, not a
   verdict.
