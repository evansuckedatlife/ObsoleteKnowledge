# BUILD-ORDER — the work queue

Ordered queue of everything left to build. Work top to bottom. This file plus `AGENTS.md` is all you need.

## How to run (recursion loop)

Repeat until no `- [ ]` boxes remain:

1. **Re-read `AGENTS.md` and this file first** (every iteration). A long autonomous run drifts off-format; a quick re-read each time is what keeps the output consistent — do not skip it.
2. Find the **first unchecked** `- [ ]` item below. Note whether it is marked **⭐** — if so it is **Tier 1 (Cornerstone)** and gets the deep treatment in `AGENTS.md` §2b (long summary, 8–14 grouped clues, a `## context` section, 6–10 connections). Unmarked = Tier 2 (standard).
3. Build it following `AGENTS.md`:
   - **Hub node** (Phase 0, all Tier 1): create the single node file `concepts/<folder>/<slug>.md` with `lists: []`. Wire its `connections` to existing nodes.
   - **List** (Phase 1+): create every member node under `concepts/<folder>/`, then the MOC `lists/<slug>.md`. Dedup first — never duplicate an existing basename; add the list to a shared node's `lists:` instead. Even in a Tier-2 list, give the 1–3 keystone members Tier-1 depth.
4. Run the validation in `AGENTS.md` §6 (or `python _scratch/validate.py`). If it reports errors, fix them — do **not** check the box until it's clean (0 errors).
5. Tick the box here (`- [ ]` → `- [x]`) and add a `✅ ` to the same topic's line in `index.md`.
6. Commit: `git add -A && git commit -m "Build <topic>"`. (Commit per item so progress is resumable and reviewable.)
7. Go to step 1.

Rules that never bend: original content only (no NAQT prose), one node per entity with a globally-unique basename, `read: false`. Accuracy over invention — if unsure of a fact, state it less precisely. Spot-checkpoint: pause for human review after each full category.

**Legend:** ⭐ = Tier-1 Cornerstone (deep treatment). All Phase-0 hub nodes are Tier 1.

**Scope:** 187 unique NAQT topics (17 built, 31 ⭐ Tier-1) + 23 hub nodes (all Tier 1).

---

## Phase 0 — Hub nodes (build first: they knit the existing web together)

Single nodes, not lists. The Greek Olympian gods especially are referenced by dozens of existing hero/monster nodes but don't exist yet.

- [x] `concepts/mythology/` — [[zeus]] — king of the Olympian gods — referenced everywhere
- [x] `concepts/mythology/` — [[athena]] — goddess of wisdom & war
- [x] `concepts/mythology/` — [[apollo]] — god of the sun, music, prophecy
- [x] `concepts/mythology/` — [[aphrodite]] — goddess of love
- [x] `concepts/mythology/` — [[the-trojan-war]] — the war the Trojan/Greek hero lists orbit
- [x] `concepts/mythology/` — [[the-iliad]] — Homer's epic of the Trojan War
- [x] `concepts/mythology/` — [[the-odyssey]] — Homer's epic of Odysseus' return
- [x] `concepts/mythology/` — [[the-aeneid]] — Virgil's epic of Aeneas
- [x] `concepts/mythology/` — [[round-table]] — the fellowship of Arthur's knights
- [x] `concepts/mythology/` — [[holy-grail]] — the object of the Arthurian quest
- [x] `concepts/mythology/` — [[book-of-the-dead]] — Egyptian funerary text
- [x] `concepts/mythology/` — [[pharaoh]] — Egyptian god-king institution
- [x] `concepts/religion/` — [[trimurti]] — Hindu triad: Brahma, Vishnu, Shiva
- [x] `concepts/religion/` — [[mahabharata]] — Hindu epic containing the Bhagavad Gita
- [x] `concepts/religion/` — [[ramayana]] — Hindu epic of Rama
- [x] `concepts/religion/` — [[jesus]] — central figure of Christianity / the NT
- [x] `concepts/religion/` — [[judaism]] — the tradition the Hebrew-Bible/holiday/lifecycle lists orbit
- [x] `concepts/religion/` — [[torah]] — the first five books / core of Judaism
- [x] `concepts/religion/` — [[gospels]] — the four NT accounts of Jesus
- [x] `concepts/religion/` — [[crucifixion]] — the death of Jesus
- [x] `concepts/religion/` — [[exodus]] — the departure from Egypt under Moses
- [x] `concepts/religion/` — [[buddhism]] — tradition founded by Siddhartha Gautama
- [x] `concepts/religion/` — [[temple-in-jerusalem]] — First & Second Temples

> After Phase 0, also consider the rest of the Twelve Olympians (hera, poseidon, ares, artemis, hephaestus, hermes, demeter, dionysus, hades, hestia) as a node cluster.

## Phase 1 — Religion  (`concepts/religion/`)  ·  9/9 built

- [x] [[biblical-sayings]] — Biblical sayings
- [x] [[hebrew-bible-characters]] — characters in the Hebrew Bible
- [x] [[founders-of-religious-traditions]] — founders of religious traditions
- [x] [[hindu-heroes]] — Hindu gods and heroes
- [x] [[jewish-holidays]] — Jewish holidays
- [x] [[jewish-lifecycle-events]] — Jewish lifecycle events
- [x] [[new-testament-characters]] — New Testament characters
- [x] [[popes]] — popes
- [x] [[religious-texts]] — religious texts

## Phase 2 — Mythology  (`concepts/mythology/`)  ·  7/7 built

- [x] [[arthurian-characters]] — Arthurian characters
- [x] [[egyptian-deities]] — Egyptian deities
- [x] [[greek-heroes]] — Greek heroes
- [x] [[greek-mythological-monsters]] — Greek mythological monsters
- [x] [[mortal-women-in-greek-myth]] — mortal women in Greek myth
- [x] [[norse-gods]] — Norse gods
- [x] [[trojan-war-heroes]] — Trojan War heroes

## Phase 3 — Science  (`concepts/science/`)  ·  3/25 built

- [x] [[20th-century-physicists]] — 20th-century physicists
- [x] [[active-volcanoes]] — active volcanoes
- [x] [[phyla]] — animal phyla
- [x] ⭐ [[chemical-elements]] — chemical elements
- [ ] [[chemistry-lab-techniques]] — chemistry lab techniques
- [ ] [[circuit-components]] — circuit components
- [ ] ⭐ [[classes-of-particles]] — classes of particles
- [ ] [[computer-components]] — computer components
- [ ] ⭐ [[quantum-mechanics-concepts]] — concepts from quantum mechanics
- [ ] [[plant-distinctions]] — distinctions among types of plants
- [ ] [[dwarf-planets-comets-and-asteroids]] — dwarf planets, comets, and asteroids
- [ ] ⭐ [[enzymes]] — enzymes
- [ ] [[functional-groups]] — functional groups
- [ ] [[geologic-time-periods]] — geologic time periods
- [ ] [[moons]] — moons
- [ ] [[nobel-prize-winners-in-medicine]] — Nobel Prize winners in physiology or medicine
- [ ] ⭐ [[organelles]] — organelles
- [ ] [[organic-reactions]] — organic reactions
- [ ] ⭐ [[programming-terms]] — programming terms
- [ ] [[rocket-scientists]] — rocket scientists
- [ ] [[rocks-and-minerals]] — rocks and minerals
- [ ] [[scientific-experiments]] — scientific experiments
- [ ] [[scientific-scales]] — scientific scales
- [ ] [[space-missions]] — space missions
- [ ] [[techniques-in-biotechnology]] — techniques in biotechnology

## Phase 4 — Mathematics  (`concepts/mathematics/`)  ·  0/6 built

- [ ] [[classifications-of-functions]] — classifications of mathematical functions
- [ ] [[geometric-curves]] — geometric curves
- [ ] ⭐ [[calculus-ideas]] — ideas from calculus
- [ ] ⭐ [[mathematicians]] — mathematicians
- [ ] [[statements-about-prime-numbers]] — statements about prime numbers
- [ ] [[computation-types]] — types of computation problems

## Phase 5 — Literature  (`concepts/literature/`)  ·  0/23 built

- [ ] [[20th-century-newbery-medal-winners]] — 20th-century Newbery Medal winners
- [ ] [[african-american-authors]] — African-American authors
- [ ] [[american-plays]] — American plays
- [ ] [[ancient-greek-plays]] — ancient Greek plays
- [ ] [[authors-of-speculative-fiction]] — authors of speculative fiction
- [ ] [[charles-dickens-characters-not-protagonists]] — Charles Dickens characters who aren’t protagonists
- [ ] [[charles-dickens-novels]] — Charles Dickens novels
- [ ] [[japanese-authors]] — Japanese authors
- [ ] [[jewish-american-authors]] — Jewish-American authors
- [ ] [[latin-american-authors]] — Latin American authors
- [ ] ⭐ [[modernist-authors]] — modernist authors
- [ ] [[non-shakespeare-classical-english-dramas]] — non-Shakespeare classical English dramas
- [ ] [[plot-twists]] — plot twists
- [ ] [[postmodern-authors]] — postmodern authors
- [ ] [[shakespearean-speeches]] — Shakespearean speeches, monologues, and soliloquies
- [ ] ⭐ [[shakespearean-villains]] — Shakespearean villains
- [ ] ⭐ [[short-story-authors]] — short story authors
- [ ] [[translations]] — translations and translators
- [ ] [[works-by-dostoevsky]] — works by Fyodor Dostoevsky
- [ ] [[works-by-irish-authors]] — works by Irish authors
- [ ] [[works-of-horror-fiction]] — works of horror fiction
- [ ] [[works-of-mystery-and-detective-fiction]] — works of mystery and detective fiction
- [ ] [[works-of-russian-short-fiction]] — works of Russian short fiction

## Phase 6 — History  (`concepts/history/`)  ·  2/54 built

- [ ] [[20th-century-african-leaders]] — 20th-century African leaders
- [ ] [[20th-century-middle-eastern-leaders]] — 20th-century Middle Eastern leaders
- [ ] [[african-american-civil-rights-leaders]] — African-American civil rights leaders
- [ ] [[american-murders-and-murderers]] — American murders and murderers
- [ ] [[american-third-parties]] — American third parties
- [ ] [[american-warships]] — American warships
- [ ] ⭐ [[ancient-empires]] — ancient empires of the Mediterranean and Near East
- [ ] [[ancient-greek-places]] — ancient Greek places
- [ ] ⭐ [[assassinations]] — assassinations
- [ ] [[aviators]] — aviators
- [ ] [[battles-of-the-ancient-world]] — battles of the ancient world
- [ ] [[black-american-legislators]] — Black American legislators
- [x] ⭐ [[british-monarchs]] — British monarchs
- [ ] [[british-prime-ministers]] — British prime ministers
- [ ] [[british-reform-movements]] — British reform movements
- [ ] [[world-war-ii-pacific-campaigns]] — campaigns in the Pacific Theater of World War II
- [ ] ⭐ [[chinese-dynasties]] — Chinese dynasties
- [ ] ⭐ [[civil-war-battles]] — Civil War battles
- [ ] [[countries-once-known-by-different-names]] — countries once known by different names
- [ ] ⭐ [[elections]] — elections
- [ ] [[european-royal-families]] — European royal families
- [ ] [[explorers]] — explorers
- [ ] [[feminists]] — feminists
- [ ] [[historical-fashions]] — historical fashions
- [ ] [[indigenous-peoples]] — indigenous peoples
- [ ] [[kings-of-france]] — kings of France
- [ ] [[magazines-from-american-history]] — magazines from American history
- [ ] ⭐ [[massacres]] — massacres
- [ ] [[medieval-battles]] — medieval battles
- [ ] [[medieval-islamic-dynasties]] — medieval Islamic dynasties
- [ ] [[mexican-leaders]] — Mexican leaders
- [ ] [[modern-speeches]] — modern speeches
- [ ] [[napoleonic-battles]] — Napoleonic battles
- [ ] [[native-american-peoples]] — Native American peoples
- [ ] [[people-from-the-french-revolution]] — people from the French Revolution
- [ ] [[peoples-of-the-early-middle-ages]] — peoples of the early Middle Ages
- [ ] [[plagues-and-pandemics]] — plagues and pandemics
- [ ] [[presidential-inaugurations]] — presidential inaugurations
- [ ] [[presidential-scandals]] — presidential scandals
- [ ] [[revolutionary-war-battles]] — Revolutionary War battles
- [ ] [[revolutionary-war-generals]] — Revolutionary War generals
- [x] ⭐ [[roman-emperors]] — Roman emperors
- [ ] ⭐ [[russian-tsars]] — Russian tsars
- [ ] [[secretaries-of-state]] — Secretaries of State
- [ ] [[south-american-political-leaders]] — South American political leaders
- [ ] [[spies]] — spies
- [ ] ⭐ [[supreme-court-cases]] — Supreme Court cases
- [ ] [[supreme-court-cases-2]] — Supreme Court cases
- [ ] [[supreme-court-cases-concerned-with-african-americans]] — Supreme Court cases concerned with African-Americans
- [ ] [[supreme-court-cases-involving-lgbt-rights]] — Supreme Court cases involving LGBT+ rights
- [ ] ⭐ [[treaties]] — treaties
- [ ] [[vice-presidents-who-never-became-president]] — vice presidents who never became president
- [ ] ⭐ [[world-war-ii-battles]] — World War II battles
- [ ] [[worlds-fairs]] — world's fairs

## Phase 7 — Music and Auditory Art  (`concepts/music/`)  ·  0/15 built

- [ ] [[20th-century-composers]] — 20th-century composers
- [ ] [[american-composers]] — American composers
- [ ] [[arias]] — arias
- [ ] [[early-20th-century-european-composers]] — early-20th-century European composers
- [ ] [[jazz-musicians]] — jazz musicians
- [ ] [[music-theory-terms]] — music theory terms
- [ ] [[musicals-part-1]] — musicals
- [ ] [[musicals-part-2]] — musicals
- [ ] [[non-western-classical-music-traditions]] — non-western classical music traditions
- [ ] ⭐ [[operas]] — operas
- [ ] [[piano-sonatas]] — piano sonatas
- [ ] [[pre-1700-composers]] — pre-1700 composers
- [ ] ⭐ [[romantic-era-composers]] — Romantic-era composers
- [ ] ⭐ [[works-by-beethoven]] — works by Ludwig van Beethoven
- [ ] ⭐ [[works-by-mozart]] — works by Mozart

## Phase 8 — Performance  (`concepts/performance/`)  ·  0/3 built

- [ ] [[ballets]] — ballets
- [ ] [[ballets-2]] — ballets
- [ ] [[choreographers]] — choreographers

## Phase 9 — Visual Art  (`concepts/visual-art/`)  ·  0/11 built

- [ ] [[20th-century-paintings]] — 20th-century paintings
- [ ] [[architects]] — architects
- [ ] [[art-museums]] — art museums
- [ ] [[baroque-painters]] — baroque painters
- [ ] [[dutch-paintings]] — Dutch paintings
- [ ] [[early-20th-century-art-movements]] — early 20th-century art movements
- [ ] [[french-directors]] — French directors
- [ ] [[photography-pioneers]] — photography pioneers
- [ ] [[sculptors]] — sculptors
- [ ] [[skyscrapers]] — skyscrapers
- [ ] [[works-by-leonardo-da-vinci]] — works by Leonardo da Vinci

## Phase 10 — Geography  (`concepts/geography/`)  ·  0/6 built

- [ ] [[african-bodies-of-water]] — African bodies of water
- [ ] [[asian-rivers]] — Asian rivers
- [ ] [[deserts]] — deserts
- [ ] [[mountains]] — mountains
- [ ] [[north-american-rivers]] — North American rivers
- [ ] [[western-european-rivers]] — western European rivers

## Phase 11 — Social Science  (`concepts/social-science/`)  ·  0/9 built

- [ ] [[accents-and-dialects-of-english]] — accents and dialects of English
- [ ] [[anthropologists]] — anthropologists
- [ ] [[archaeological-sites]] — archaeological sites
- [ ] ⭐ [[economic-concepts]] — economic concepts
- [ ] [[economists]] — economists
- [ ] [[linguists]] — linguists
- [ ] [[psychological-experiments]] — psychological experiments and studies
- [ ] ⭐ [[psychologists]] — psychologists
- [ ] [[unique-languages]] — unique languages

## Phase 12 — Philosophy  (`concepts/philosophy/`)  ·  0/2 built

- [ ] ⭐ [[ancient-philosophers]] — ancient philosophers
- [ ] ⭐ [[schools-of-western-philosophy]] — schools of Western philosophy

## Phase 13 — Popular Culture  (`concepts/pop-culture/`)  ·  0/7 built

- [ ] [[classic-american-television-series]] — classic American television series
- [ ] [[landmark-20th-century-american-sitcoms]] — landmark 20th-century American sitcoms
- [ ] [[modern-board-games]] — modern board games
- [ ] [[pre-1960s-movies]] — pre-1960s movies
- [ ] [[sandbox-and-open-world-video-games]] — sandbox and open-world video games
- [ ] [[silent-films]] — silent films
- [ ] [[video-game-series]] — video game series

## Phase 14 — Sports  (`concepts/sports/`)  ·  0/6 built

- [ ] [[21st-century-quarterbacks]] — 21st-century quarterbacks
- [ ] [[golfers]] — golfers
- [ ] [[hockey-hall-of-famers]] — Hockey Hall of Famers
- [ ] [[new-york-yankees]] — New York Yankees
- [ ] [[olympics]] — Olympics
- [ ] [[tennis-players]] — tennis players

## Phase 15 — Miscellaneous  (`concepts/misc/`)  ·  0/4 built

- [ ] [[common-mistakes]] — common mistakes
- [ ] [[common-mistakes-2]] — common mistakes
- [ ] [[new-year-celebrations]] — new-year celebrations
- [ ] [[quintuples]] — quintuples

