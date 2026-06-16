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

**Scope:** 187 unique NAQT topics (171 built, 31 ⭐ Tier-1) + 23 hub nodes (all Tier 1).

---

## Phase 0 — Hub nodes (build first: they knit the existing web together)

Single nodes, not lists. The Greek Olympian gods especially are referenced by dozens of existing hero/monster nodes but don't exist yet.

- [ ] `concepts/mythology/` — [[zeus]] — king of the Olympian gods — referenced everywhere
- [ ] `concepts/mythology/` — [[athena]] — goddess of wisdom & war
- [ ] `concepts/mythology/` — [[apollo]] — god of the sun, music, prophecy
- [ ] `concepts/mythology/` — [[aphrodite]] — goddess of love
- [ ] `concepts/mythology/` — [[the-trojan-war]] — the war the Trojan/Greek hero lists orbit
- [ ] `concepts/mythology/` — [[the-iliad]] — Homer's epic of the Trojan War
- [ ] `concepts/mythology/` — [[the-odyssey]] — Homer's epic of Odysseus' return
- [ ] `concepts/mythology/` — [[the-aeneid]] — Virgil's epic of Aeneas
- [ ] `concepts/mythology/` — [[round-table]] — the fellowship of Arthur's knights
- [ ] `concepts/mythology/` — [[holy-grail]] — the object of the Arthurian quest
- [ ] `concepts/mythology/` — [[book-of-the-dead]] — Egyptian funerary text
- [ ] `concepts/mythology/` — [[pharaoh]] — Egyptian god-king institution
- [ ] `concepts/religion/` — [[trimurti]] — Hindu triad: Brahma, Vishnu, Shiva
- [ ] `concepts/religion/` — [[mahabharata]] — Hindu epic containing the Bhagavad Gita
- [ ] `concepts/religion/` — [[ramayana]] — Hindu epic of Rama
- [ ] `concepts/religion/` — [[jesus]] — central figure of Christianity / the NT
- [ ] `concepts/religion/` — [[judaism]] — the tradition the Hebrew-Bible/holiday/lifecycle lists orbit
- [ ] `concepts/religion/` — [[torah]] — the first five books / core of Judaism
- [ ] `concepts/religion/` — [[gospels]] — the four NT accounts of Jesus
- [ ] `concepts/religion/` — [[crucifixion]] — the death of Jesus
- [ ] `concepts/religion/` — [[exodus]] — the departure from Egypt under Moses
- [ ] `concepts/religion/` — [[buddhism]] — tradition founded by Siddhartha Gautama
- [ ] `concepts/religion/` — [[temple-in-jerusalem]] — First & Second Temples

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

## Phase 3 — Science  (`concepts/science/`)  ·  25/25 built

- [x] [[20th-century-physicists]] — 20th-century physicists
- [x] [[active-volcanoes]] — active volcanoes
- [x] [[phyla]] — animal phyla
- [x] ⭐ [[chemical-elements]] — chemical elements
- [x] [[chemistry-lab-techniques]] — chemistry lab techniques
- [x] [[circuit-components]] — circuit components
- [x] ⭐ [[classes-of-particles]] — classes of particles
- [x] [[computer-components]] — computer components
- [x] ⭐ [[quantum-mechanics-concepts]] — concepts from quantum mechanics
- [x] [[plant-distinctions]] — distinctions among types of plants
- [x] [[dwarf-planets-comets-and-asteroids]] — dwarf planets, comets, and asteroids
- [x] ⭐ [[enzymes]] — enzymes
- [x] [[functional-groups]] — functional groups
- [x] [[geologic-time-periods]] — geologic time periods
- [x] [[moons]] — moons
- [x] [[nobel-prize-winners-in-medicine]] — Nobel Prize winners in physiology or medicine
- [x] ⭐ [[organelles]] — organelles
- [x] [[organic-reactions]] — organic reactions
- [x] ⭐ [[programming-terms]] — programming terms
- [x] [[rocket-scientists]] — rocket scientists
- [x] [[rocks-and-minerals]] — rocks and minerals
- [x] [[scientific-experiments]] — scientific experiments
- [x] [[scientific-scales]] — scientific scales
- [x] [[space-missions]] — space missions
- [x] [[techniques-in-biotechnology]] — techniques in biotechnology

## Phase 4 — Mathematics  (`concepts/mathematics/`)  ·  6/6 built

- [x] [[classifications-of-functions]] — classifications of mathematical functions
- [x] [[geometric-curves]] — geometric curves
- [x] ⭐ [[calculus-ideas]] — ideas from calculus
- [x] ⭐ [[mathematicians]] — mathematicians
- [x] [[statements-about-prime-numbers]] — statements about prime numbers
- [x] [[computation-types]] — types of computation problems

## Phase 5 — Literature  (`concepts/literature/`)  ·  23/23 built

- [x] [[20th-century-newbery-medal-winners]] — 20th-century Newbery Medal winners
- [x] [[african-american-authors]] — African-American authors
- [x] [[american-plays]] — American plays
- [x] [[ancient-greek-plays]] — ancient Greek plays
- [x] [[authors-of-speculative-fiction]] — authors of speculative fiction
- [x] [[charles-dickens-characters-not-protagonists]] — Charles Dickens characters who aren’t protagonists
- [x] [[charles-dickens-novels]] — Charles Dickens novels
- [x] [[japanese-authors]] — Japanese authors
- [x] [[jewish-american-authors]] — Jewish-American authors
- [x] [[latin-american-authors]] — Latin American authors
- [x] ⭐ [[modernist-authors]] — modernist authors
- [x] [[non-shakespeare-classical-english-dramas]] — non-Shakespeare classical English dramas
- [x] [[plot-twists]] — plot twists
- [x] [[postmodern-authors]] — postmodern authors
- [x] [[shakespearean-speeches]] — Shakespearean speeches, monologues, and soliloquies
- [x] ⭐ [[shakespearean-villains]] — Shakespearean villains
- [x] ⭐ [[short-story-authors]] — short story authors
- [x] [[translations]] — translations and translators
- [x] [[works-by-dostoevsky]] — works by Fyodor Dostoevsky
- [x] [[works-by-irish-authors]] — works by Irish authors
- [x] [[works-of-horror-fiction]] — works of horror fiction
- [x] [[works-of-mystery-and-detective-fiction]] — works of mystery and detective fiction
- [x] [[works-of-russian-short-fiction]] — works of Russian short fiction

## Phase 6 — History  (`concepts/history/`)  ·  54/54 built

- [x] [[20th-century-african-leaders]] — 20th-century African leaders
- [x] [[20th-century-middle-eastern-leaders]] — 20th-century Middle Eastern leaders
- [x] [[african-american-civil-rights-leaders]] — African-American civil rights leaders
- [x] [[american-murders-and-murderers]] — American murders and murderers
- [x] [[american-third-parties]] — American third parties
- [x] [[american-warships]] — American warships
- [x] ⭐ [[ancient-empires]] — ancient empires of the Mediterranean and Near East
- [x] [[ancient-greek-places]] — ancient Greek places
- [x] ⭐ [[assassinations]] — assassinations
- [x] [[aviators]] — aviators
- [x] [[battles-of-the-ancient-world]] — battles of the ancient world
- [x] [[black-american-legislators]] — Black American legislators
- [x] ⭐ [[british-monarchs]] — British monarchs
- [x] [[british-prime-ministers]] — British prime ministers
- [x] [[british-reform-movements]] — British reform movements
- [x] [[world-war-ii-pacific-campaigns]] — campaigns in the Pacific Theater of World War II
- [x] ⭐ [[chinese-dynasties]] — Chinese dynasties
- [x] ⭐ [[civil-war-battles]] — Civil War battles
- [x] [[countries-once-known-by-different-names]] — countries once known by different names
- [x] ⭐ [[elections]] — elections
- [x] [[european-royal-families]] — European royal families
- [x] [[explorers]] — explorers
- [x] [[feminists]] — feminists
- [x] [[historical-fashions]] — historical fashions
- [x] [[indigenous-peoples]] — indigenous peoples
- [x] [[kings-of-france]] — kings of France
- [x] [[magazines-from-american-history]] — magazines from American history
- [x] ⭐ [[massacres]] — massacres
- [x] [[medieval-battles]] — medieval battles
- [x] [[medieval-islamic-dynasties]] — medieval Islamic dynasties
- [x] [[mexican-leaders]] — Mexican leaders
- [x] [[modern-speeches]] — modern speeches
- [x] [[napoleonic-battles]] — Napoleonic battles
- [x] [[native-american-peoples]] — Native American peoples
- [x] [[people-from-the-french-revolution]] — people from the French Revolution
- [x] [[peoples-of-the-early-middle-ages]] — peoples of the early Middle Ages
- [x] [[plagues-and-pandemics]] — plagues and pandemics
- [x] [[presidential-inaugurations]] — presidential inaugurations
- [x] [[presidential-scandals]] — presidential scandals
- [x] [[revolutionary-war-battles]] — Revolutionary War battles
- [x] [[revolutionary-war-generals]] — Revolutionary War generals
- [x] ⭐ [[roman-emperors]] — Roman emperors
- [x] ⭐ [[russian-tsars]] — Russian tsars
- [x] [[secretaries-of-state]] — Secretaries of State
- [x] [[south-american-political-leaders]] — South American political leaders
- [x] [[spies]] — spies
- [x] ⭐ [[supreme-court-cases]] — Supreme Court cases
- [x] [[supreme-court-cases-2]] — Supreme Court cases
- [x] [[supreme-court-cases-concerned-with-african-americans]] — Supreme Court cases concerned with African-Americans
- [x] [[supreme-court-cases-involving-lgbt-rights]] — Supreme Court cases involving LGBT+ rights
- [x] ⭐ [[treaties]] — treaties
- [x] [[vice-presidents-who-never-became-president]] — vice presidents who never became president
- [x] ⭐ [[world-war-ii-battles]] — World War II battles
- [x] [[worlds-fairs]] — world's fairs

## Phase 7 — Music and Auditory Art  (`concepts/music/`)  ·  8/15 built

- [x] [[20th-century-composers]] — 20th-century composers
- [x] [[american-composers]] — American composers
- [ ] [[arias]] — arias
- [x] [[early-20th-century-european-composers]] — early-20th-century European composers
- [ ] [[jazz-musicians]] — jazz musicians
- [ ] [[music-theory-terms]] — music theory terms
- [ ] [[musicals-part-1]] — musicals
- [ ] [[musicals-part-2]] — musicals
- [ ] [[non-western-classical-music-traditions]] — non-western classical music traditions
- [x] ⭐ [[operas]] — operas
- [x] [[piano-sonatas]] — piano sonatas
- [ ] [[pre-1700-composers]] — pre-1700 composers
- [x] ⭐ [[romantic-era-composers]] — Romantic-era composers
- [x] ⭐ [[works-by-beethoven]] — works by Ludwig van Beethoven
- [x] ⭐ [[works-by-mozart]] — works by Mozart

## Phase 8 — Performance  (`concepts/performance/`)  ·  1/3 built

- [x] [[ballets]] — ballets
- [ ] [[ballets-2]] — ballets
- [ ] [[choreographers]] — choreographers

## Phase 9 — Visual Art  (`concepts/visual-art/`)  ·  11/11 built

- [x] [[20th-century-paintings]] — 20th-century paintings
- [x] [[architects]] — architects
- [x] [[art-museums]] — art museums
- [x] [[baroque-painters]] — baroque painters
- [x] [[dutch-paintings]] — Dutch paintings
- [x] [[early-20th-century-art-movements]] — early 20th-century art movements
- [x] [[french-directors]] — French directors
- [x] [[photography-pioneers]] — photography pioneers
- [x] [[sculptors]] — sculptors
- [x] [[skyscrapers]] — skyscrapers
- [x] [[works-by-leonardo-da-vinci]] — works by Leonardo da Vinci

## Phase 10 — Geography  (`concepts/geography/`)  ·  6/6 built

- [x] [[african-bodies-of-water]] — African bodies of water
- [x] [[asian-rivers]] — Asian rivers
- [x] [[deserts]] — deserts
- [x] [[mountains]] — mountains
- [x] [[north-american-rivers]] — North American rivers
- [x] [[western-european-rivers]] — western European rivers

## Phase 11 — Social Science  (`concepts/social-science/`)  ·  9/9 built

- [x] [[accents-and-dialects-of-english]] — accents and dialects of English
- [x] [[anthropologists]] — anthropologists
- [x] [[archaeological-sites]] — archaeological sites
- [x] ⭐ [[economic-concepts]] — economic concepts
- [x] [[economists]] — economists
- [x] [[linguists]] — linguists
- [x] [[psychological-experiments]] — psychological experiments and studies
- [x] ⭐ [[psychologists]] — psychologists
- [x] [[unique-languages]] — unique languages

## Phase 12 — Philosophy  (`concepts/philosophy/`)  ·  2/2 built

- [x] ⭐ [[ancient-philosophers]] — ancient philosophers
- [x] ⭐ [[schools-of-western-philosophy]] — schools of Western philosophy

## Phase 13 — Popular Culture  (`concepts/pop-culture/`)  ·  0/7 built

- [ ] [[classic-american-television-series]] — classic American television series
- [ ] [[landmark-20th-century-american-sitcoms]] — landmark 20th-century American sitcoms
- [ ] [[modern-board-games]] — modern board games
- [ ] [[pre-1960s-movies]] — pre-1960s movies
- [ ] [[sandbox-and-open-world-video-games]] — sandbox and open-world video games
- [ ] [[silent-films]] — silent films
- [ ] [[video-game-series]] — video game series

## Phase 14 — Sports  (`concepts/sports/`)  ·  6/6 built

- [x] [[21st-century-quarterbacks]] — 21st-century quarterbacks
- [x] [[golfers]] — golfers
- [x] [[hockey-hall-of-famers]] — Hockey Hall of Famers
- [x] [[new-york-yankees]] — New York Yankees
- [x] [[olympics]] — Olympics
- [x] [[tennis-players]] — tennis players

## Phase 15 — Miscellaneous  (`concepts/misc/`)  ·  4/4 built

- [x] [[common-mistakes]] — common mistakes
- [x] [[common-mistakes-2]] — common mistakes
- [x] [[new-year-celebrations]] — new-year celebrations
- [x] [[quintuples]] — quintuples

