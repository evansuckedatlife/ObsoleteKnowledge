---
type: list
category: literature
read: false
---

# postmodern authors

The postmodern authors most worth knowing for quiz bowl.

## nodes

- [[david-foster-wallace|David Foster Wallace]] — David Foster Wallace (1962–2008) was an American novelist, essayist, and short-story writer who synthesized postmodern…
- [[don-delillo|Don DeLillo]] — Don DeLillo (b.
- [[italo-calvino|Italo Calvino]] — Italo Calvino (1923–1985) was an Italian writer whose playful, ingeniously structured novels pioneered narrative…
- [[jorge-luis-borges|Jorge Luis Borges]] — Jorge Luis Borges (1899–1986) was an Argentine writer and poet who revolutionised the short story by treating fiction as…
- [[joseph-heller|Joseph Heller]] — Joseph Heller (1923–1999) was an American novelist best known for Catch-22, a landmark anti-war satire that revolutionized…
- [[kurt-vonnegut|Kurt Vonnegut]] — Kurt Vonnegut was an American novelist and social critic whose darkly comic, science-inflected narratives interrogated war,…
- [[salman-rushdie|Salman Rushdie]] — Salman Rushdie (b.
- [[thomas-pynchon|Thomas Pynchon]] — Thomas Pynchon (b.
- [[vladimir-nabokov|Vladimir Nabokov]] — Vladimir Nabokov (1899–1977) was a Russian-American novelist and writer celebrated for his elaborate wordplay, psychological…
- [[zadie-smith|Zadie Smith]] — Zadie Smith (b.

## progress

Live read-status for this list (requires the **Bases** core plugin). Flip a node's `read` from its footer toggle and it moves here.

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
      - property: tour_order
        direction: ASC
      - property: file.name
        direction: ASC
```
