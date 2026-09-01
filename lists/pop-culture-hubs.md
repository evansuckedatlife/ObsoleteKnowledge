---
type: list
category: pop-culture
read: false
---

# Pop Culture hubs

Formats, genres and phenomena the individual titles belong to.

## nodes

- [[nintendo|Nintendo]] — Nintendo is a Japanese entertainment company founded in 1889 that evolved into one of the world's most influential video game publishers.
- [[science-fiction-television|Science-Fiction Television]] — Science-fiction television encompasses TV series that explore speculative futures, alternate realities, or scientific premises as central to their nar…
- [[television-drama|Television Drama]] — Television drama represents narrative-driven TV series built around character arcs, ongoing conflicts, and serialized storytelling rather than comedy …
- [[worker-placement-mechanics|Worker-Placement Mechanics]] — Worker-placement mechanics represent a core board game system in which players assign limited agent tokens (often representing workers, officials, or …

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
