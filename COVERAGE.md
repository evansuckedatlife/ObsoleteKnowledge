# Coverage — what this vault can actually answer

Node count is a vanity metric. The number that predicts match performance is
**what share of real questions the vault can answer**, and it is measurable,
because Reach For The Top packs come with their answer set.

Measured 2026-09-04 against 32 RFTT Senior Packs (2022–23) and the published
[Consensus Trivia 2027 topic distribution](https://www.consensustrivia.com/resources.html).

---

## The headline

| | |
|---|---|
| nodes | 5,519 |
| distinct RFTT subjects covered | **694 of 2,810 — 24.7%** |
| RFTT answer slots covered (weighted by how often asked) | **932 of 3,057 — 30.5%** |

Reading the entire vault today answers **just under a third** of a real pack.
That is the honest starting point, and the gap is not obscurity — it is
*subject area*.

## Why: the vault is a humanities syllabus, and the competitions are not

The vault was scoped to NAQT, an American quiz-bowl circuit with a heavy
academic distribution. Consensus publishes what it actually asks:

| area | Consensus 2027 | vault | verdict |
|---|---|---|---|
| Popular Culture | **23.0%** | 6.9% | **3.3× under** |
| General Knowledge | **16.0%** | 2.8% | **5.7× under** |
| Contemporary World | 15.5% | 7.5% | 2.1× under |
| Science & Math | 17.5% | 15.7% | about right |
| Arts | 12.0% | 24.7% | 2.1× **over** |
| Humanities | 16.0% | **36.5%** | 2.3× **over** |
| Social Science | 1.0% | 5.9% | 5.9× **over** |

Popular Culture is the single largest slice of a Consensus tournament —
Sports 4.5%, Popular Music 4.5%, Movies 4.0%, Television 3.5%, Video Games
2.5%, Popular Literature 2.0%. The vault gives that whole 23% about one node
in fourteen.

General Knowledge is the second-worst: Language 4.0%, Food & Drink 2.0%,
Games & Hobbies 2.0%, Brands & Products 1.5%, Culture & Traditions 1.5%,
Fashion 1.0%. The vault has essentially none of it.

Meanwhile History alone is 28% of the vault against a 12% weight.

RFTT's answer set says the same thing independently. The subjects it asks
about that the vault lacks are *Fortnite*, *Billie Eilish*, *Christian
Siriano*, *Margot Robbie*, *Franklin the Turtle*, *BMW*, *Intel*, *pho*,
*Afrikaans*, *caribou* — not more Byzantine emperors.

## What "balanced" would cost, and why that is the wrong target

Matching the distribution exactly, without deleting anything, is impossible at
a sane size. Social Science is 5.9% of the vault against a 1.0% weight, and
that one constraint alone forces a **32,000-node** vault before the shares line
up.

So the target is not the pie chart. It is coverage:

> **Writing the 2,088 RFTT subjects the vault is missing takes answer-slot
> coverage from 30.5% to ~98% of a real pack.**

That is roughly the volume already written in a single session. It is the
highest-value work available, and it is finite.

## How the queue is ordered

`tools/consensus_wave.py` orders by **deficit** — how far each area sits below
the share of real questions it must answer — not by reference count like the
BFS waves. Popular Culture and General Knowledge go first. History and
Literature get nothing. Stopping early therefore still leaves the
highest-yield subjects written.

## The one thing coverage does not buy

Consensus rules let players buzz before the question ends, and give three
seconds after it. Fast reactions only convert to points if you recognise the
*early* clue — and quiz questions are written hard-clue-first, giveaway-last.

Every node's `you gotta know` section is ordered the other way: most
recognisable first, most obscure last (`CLAUDE.md`). That is the right order
for *learning* a subject and the wrong order for *buzzing* on it. The deep
clues that appear early in a question are buried at the bottom of the list, and
in the audio tours they arrive last.

Fixing that is a re-ordering, not a rewrite — the content already exists. It is
not yet done, and it is the largest remaining gain that is not about writing
more nodes.

---

## Reproducing these numbers

```bash
python tools/rftt_topics.py --dir <pack folder> --out _scratch/rftt_gap.json
python tools/rftt_filter.py --gap _scratch/rftt_gap.json \
    --out _scratch/rftt_candidates.json
python tools/consensus_wave.py --subjects _scratch/classified.json \
    --out _scratch/waves/consensus
```

Sourcing, unchanged and non-negotiable: the packs are copyrighted. Only the
**answer names** are read — facts, not expression. No question text enters a
model or this repo. See `VISION.md`.
