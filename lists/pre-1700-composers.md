---
type: list
category: music
read: false
---

# pre-1700 composers

The pre-1700 composers most worth knowing for quiz bowl.

## nodes

- [[claudio-monteverdi|Claudio Monteverdi]] — Claudio Monteverdi (1567–1643) was an Italian composer who bridged Renaissance and Baroque styles, fundamentally transforming…
- [[giovanni-gabrieli|Giovanni Gabrieli]] — Giovanni Gabrieli (c.
- [[giovanni-pierluigi-da-palestrina|Giovanni Pierluigi da Palestrina]] — Palestrina (c.
- [[guillaume-de-machaut|Guillaume de Machaut]] — Guillaume de Machaut (c.
- [[henry-purcell|Henry Purcell]] — Henry Purcell (1659–1695) was the greatest English Baroque composer, a master of dramatic expression and instrumental…
- [[hildegard-of-bingen|Hildegard of Bingen]] — Hildegard of Bingen (1098–1179) was a Benedictine abbess, mystic, theologian, and composer whose liturgical chants represent…
- [[josquin-des-prez|Josquin des Prez]] — Josquin des Prez (c.
- [[orlando-di-lasso|Orlando di Lasso]] — Orlando di Lasso (1532–1594) was a Franco-Flemish composer of extraordinary prolific genius and stylistic range, equally…
- [[thomas-tallis|Thomas Tallis]] — Thomas Tallis (c.
- [[william-byrd|William Byrd]] — William Byrd (1540–1623) was the preeminent English composer of the Tudor and early Stuart era, excelling equally in masses,…

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
