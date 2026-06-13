# AGENTS.md — Building ObsoleteKnowledge nodes

Antigravity (and other agents) auto-load this file. You are continuing work on **ObsoleteKnowledge**, an Obsidian knowledge vault: small atomic reference "nodes" woven into a wikilink web, with `read:` progress tracking. Your job is to **author new nodes and list pages** for topics from NAQT's *You Gotta Know* catalogue, matching the existing format **exactly**. Read `CLAUDE.md`, `VISION.md`, and `tools/generate-node.md` for the full design; this file is the quick operating guide.

---

## 0. The three rules you must never break

1. **Write original content only.** Do **not** fetch, paste, read, or paraphrase NAQT's article prose into yourself — their terms of use forbid putting their text into a language model, and copying their wording would create infringing content. Use NAQT **only as a scope checklist**: the topic title and the *names* of the ~10 entries (names are facts). Write every word yourself from general knowledge / open references (Wikipedia, Britannica, primary texts). If unsure of a fact, state it less precisely rather than invent it.
2. **One node per entity, globally-unique filename.** Obsidian resolves `[[wikilinks]]` by *basename* across the whole vault, so two files with the same name silently break every link to that name. Before creating a node, check whether it already exists (`ls concepts/**`). If a figure is shared between lists (e.g. *Achilles* is in both Greek heroes and Trojan War heroes), **do not make a second file** — instead add the new list to the existing node's `lists:` frontmatter and link to it.
3. **`read: false` always.** It is the single source of truth for progress. Never add a `## Understood?` section or any other tracking state.

---

## 1. Where files go

```
concepts/<category>/<slug>.md     # one fact-node per entity
lists/<slug>.md                   # one map-of-content (MOC) per NAQT topic
index.md                          # master catalogue of all 187 topics (the frontier)
```

`<category>` is a flat top-level subject. Use these folder names (kebab-case), matching `index.md`'s NAQT categories:

`mythology` · `religion` · `literature` · `history` · `geography` · `science` · `mathematics` · `social-science` · `philosophy` · `music` · `performance` · `visual-art` · `pop-culture` · `sports` · `misc`

The same string is the value of the `category:` frontmatter field.

`<slug>` = kebab-case of the common English name (`king-arthur`, `chemical-elements`). **Disambiguate generic names** so the basename is meaningful and unique: `jewish-marriage` not `marriage`, `john-the-apostle` not `john`, `book-of-job` not `job`.

---

## 2. Node template — copy this exactly

```markdown
---
type: <person | deity | hero | monster | work | text | event | place | concept | phrase | practice | holiday | element | species | term>
category: <one of the folder names above>
defines: [Canonical Name, Alias One, Alias Two]
related: ["[[slug-a]]", "[[slug-b]]"]
lists: ["[[list-slug]]"]
read: false
---

# Canonical Name

## summary

2–4 sentences: what/who it is, when and where, and why it is worth knowing. Plain prose; *italics* for emphasis only.

## you gotta know

4–8 bullets, each ONE fact, ordered **most-recognisable first → most-obscure last** (the order quiz-bowl giveaway clues run). *Italics* for key names, titles, dates, places. Be specific — a named work, a number, a relationship, a famous line — never vague ("was important").

- fact one
- fact two

## connections

How this node ties into the web. Each bullet is `[[slug]] — one-line reason`. Link to family, rivals, teachers/students, the same myth/event, cause/effect, the work it appears in. 2–5 links minimum. Linking to a node that doesn't exist yet is fine and encouraged — dangling links are the frontier.

- [[other-slug]] — why they're connected.

## see also

One line of sibling wikilinks separated by ` · ` — usually peers from the same list.

- [[peer-a]] · [[peer-b]] · [[peer-c]]

<!-- footer -->

---

Lists: [[list-slug]] · Mark read: `INPUT[toggle:read]`
```

Notes:
- Footer lists **every** list the node belongs to: `Lists: [[greek-heroes]] · [[trojan-war-heroes]] · Mark read: ...`.
- `defines` = the display name plus any aliases/alternate spellings the node owns.
- Read an existing node first as a style exemplar, e.g. `concepts/mythology/odin.md` or `concepts/religion/moses.md`.
- **Tier-1 (Cornerstone) nodes** add a `## context` section after `## you gotta know` (see Depth tiers below).

## 2b. Depth tiers — scale effort to importance

Not every node deserves equal effort. Match depth to how central the topic is. **Effort budget should flow to the major concepts**, not be spread evenly.

**Tier 1 — Cornerstone.** Civilization-level concepts and high-traffic hubs: `jesus`, `zeus`, `judaism`, `the-trojan-war`; and major lists/members like *programming terms*, *massacres*, *elections*, *chemical elements*, *Supreme Court cases*, *World War II battles*. Marked **⭐** in `BUILD-ORDER.md`. Give these the deep treatment:
- **summary:** a full paragraph (4–6 sentences) — identity, scope, and why it's pivotal.
- **you gotta know:** 8–14 bullets, and group them under `###` sub-headers when the material splits naturally (e.g. for `jesus`: `### life`, `### teachings`, `### death & resurrection`, `### influence`; for a battle: `### background`, `### the battle`, `### aftermath`).
- **`## context`** (Tier-1 only): one paragraph on broader significance — influence, legacy, why it recurs in quiz bowl and the wider culture.
- **connections:** 6–10 links, reaching across domains (a person → their works, era, rivals, the movement they belong to).

**Tier 2 — Standard.** Everything else (the default, and what the existing Mythology & Belief nodes are): summary 2–4 sentences, 4–8 clue bullets, 2–5 connections, no `## context`.

**Within any list,** even a Tier-2 list, give the 1–3 *keystone* members Tier-1 depth (e.g. in *operas*, *Carmen* and *The Magic Flute* get more than a minor entry). Use judgment: if a topic is obviously major but isn't marked ⭐, treat it as Tier 1 anyway. Better to over-invest in the famous than to pad the obscure.

## 3. List (MOC) template — copy this exactly

```markdown
---
type: list
category: <category>
read: false
---

# <List Title>

One sentence: what this topic covers and why it matters.

## nodes

- [[slug|Display Name]] — one-line hint.
- [[slug|Display Name]] — one-line hint.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
```

The `file.hasLink(this.file)` filter automatically shows every node whose `lists:` links to this MOC. (`lists.containsLinkTo(...)` is **not** a real Bases function — never use it.)

---

## 4. Formatting rules (strict)

- Wikilinks use the lowercase **slug**: `[[odin]]`, never `[[Odin]]`. For nicer display in lists, alias it: `[[odin|Odin]]`.
- `**bold**` is reserved for the node's own name/aliases (things in its `defines`). Use `*italics*` for all other emphasis and for key names inside clues. **Never bold for emphasis or clue labels.**
- `` `code` `` for literal tokens (transliterations, fixed notation).
- **YAML safety:** in `defines`, wrap any value containing an apostrophe, colon, or non-ASCII letter in double quotes — `defines: ["Qur'an", Koran]`, `defines: ["Baháʼu'lláh"]`.
- Obsidian rewrites inline frontmatter lists (`lists: ["[[x]]"]`) into block style when you edit a note. Both are valid; don't fight it. If you write tooling that reads frontmatter, parse real YAML, not regex.

---

## 5. Workflow to build one list

**Stay on-spec:** at the start of every item, **re-read this `AGENTS.md` and `BUILD-ORDER.md`** before writing. Over a long autonomous run your sense of the format drifts; a 10-second re-read prevents it. Also glance at one recent node you wrote to confirm you're still matching the template.

1. **Pick a frontier topic** — the first unchecked item in `BUILD-ORDER.md`. Check whether it's marked **⭐ (Tier 1)** and set your depth accordingly (§2b).
2. **Enumerate members** — the ~10 well-known entities for that topic. You may use NAQT's entry names as the checklist (names only).
3. **Dedup** — for each member, `ls concepts/<category>/` (and grep the vault) to see if a node already exists. If it does, add this list to that node's `lists:` and footer; do not duplicate. Otherwise author it from the node template.
4. **Write the MOC** at `lists/<slug>.md` from the list template, listing every member.
5. **Update `index.md`** — put a `✅ ` in front of that topic's `[[slug]]` entry (and add it to the "Built so far" section) so the catalogue reflects it.
6. **Validate** (section 6).

Aim for the same density and accuracy as the existing Mythology & Belief nodes. Quality bar: every "you gotta know" bullet carries a specific, checkable fact; at least 2–3 real connections per node; recognisable-first ordering; accuracy over invention. Work one list at a time; create the member nodes, then the MOC, then validate, then move on.

---

## 6. Validate before you finish

Check, across everything you wrote:
- **No duplicate basenames** anywhere in `concepts/` (list all `concepts/**/*.md` basenames, confirm no repeats).
- Every node has complete frontmatter (`type`, `category`, `defines`, `related`, `lists`, `read: false`) and ends with the `<!-- footer -->` block containing the `Mark read` toggle.
- Every node listed in a MOC's `## nodes` has that list in its `lists:` frontmatter, and vice versa (membership is symmetric).
- Wikilinks are well-formed; dangling links are OK (frontier) but intra-list links should resolve once the list is done.
- No `## Understood?` sections; no NAQT prose anywhere.

A quick Python check (PyYAML) that mirrors the project validator:

```python
import glob, os, yaml, collections
base=collections.Counter(os.path.splitext(os.path.basename(f))[0] for f in glob.glob("concepts/**/*.md",recursive=True))
print("DUP basenames:", [b for b,c in base.items() if c>1] or "none")
for f in glob.glob("concepts/**/*.md",recursive=True):
    t=open(f,encoding="utf-8").read(); fm=t[3:t.find("\n---",3)]
    d=yaml.safe_load(fm)
    for k in ("type","category","defines","lists","read"):
        if k not in d: print(f, "missing", k)
    if "<!-- footer -->" not in t: print(f, "no footer")
```

---

## 7. Reference exemplars

Read these before writing, to match voice and structure:
- `concepts/mythology/odin.md`, `concepts/mythology/medusa.md` (entities)
- `concepts/religion/moses.md`, `concepts/religion/quran.md` (people / texts)
- `lists/norse-gods.md` (a finished MOC)
- `CLAUDE.md` and `tools/generate-node.md` (the authoritative spec)

---

## 8. Suggested first targets (from the frontier)

High-value, well-bounded lists to start with — and natural cross-links into the existing Mythology & Belief web:

- **History:** `roman-emperors`, `british-monarchs`, `chinese-dynasties`, `ancient-empires`, `russian-tsars`, `popes`
- **Science:** `chemical-elements`, `organelles`, `phyla`, `moons`, `geologic-time-periods`
- **Literature:** `short-story-authors`, `shakespearean-villains`, `latin-american-authors`
- **Hub nodes** (currently high-inbound dangling links worth authoring as nodes, not lists): `the-trojan-war`, `the-iliad`, `the-odyssey`, `jesus`, `judaism`, `torah`, `pharaoh`, `zeus`, `the-twelve-olympians`. File these under the relevant category (e.g. `concepts/mythology/the-trojan-war.md`) with `lists: []` if they belong to no NAQT list.
