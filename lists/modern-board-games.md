---
type: list
category: pop-culture
read: false
---

# modern board games

The modern board games most worth knowing for quiz bowl.

## nodes

- [[agricola|Agricola]] — Agricola is a worker-placement board game designed by Uwe Rosenberg and released in 2007, where players manage family farms…
- [[carcassonne|Carcassonne]] — Carcassonne is a tile-placement board game designed by Klaus Teuber and released in 2000, named after a walled medieval town…
- [[codenames|Codenames]] — Codenames is a word-association party game designed by Vladimír Chvátal and released in 2015, where two competing teams race…
- [[dominion|Dominion]] — Dominion is a deck-building board game designed by Donald X.
- [[pandemic|Pandemic]] — Pandemic is a cooperative board game designed by Matt Leacock and released in 2008 where players assume roles of…
- [[puerto-rico|Puerto Rico]] — Puerto Rico is a worker-placement and trading game designed by Andreas Seyfarth and released in 2002, where players develop…
- [[scythe|Scythe]] — Scythe is a worker-placement and asymmetric game designed by Jamey Stegmaier and released in 2016, set in an alternate-history…
- [[settlers-of-catan|Settlers of Catan]] — Settlers of Catan is a foundational modern board game designed by Klaus Teuber and released in Germany in 1995 (as Die Siedler…
- [[ticket-to-ride|Ticket to Ride]] — Ticket to Ride is a railroad route-building board game designed by Alan R.
- [[wingspan|Wingspan]] — Wingspan is a card-driven engine-building game designed by Elizabeth Hargrave and released in 2019, where players attract…

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
