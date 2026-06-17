---
type: list
category: history
read: false
---

# European royal families

The European royal families most worth knowing for quiz bowl.

## nodes

- [[house-of-bourbon|House of Bourbon]] — The House of Bourbon rose to power in France in 1589 and became Europe's greatest dynasty of the 17th and 18th centuries,…
- [[house-of-habsburg|House of Habsburg]] — The House of Habsburg was one of Europe's most powerful and longest-reigning dynasties, ruling Austria, Spain, Hungary, and…
- [[house-of-hohenzollern|House of Hohenzollern]] — The House of Hohenzollern rose from minor German nobility to rule Prussia and, ultimately, a unified German Empire spanning…
- [[house-of-medici|House of Medici]] — The House of Medici rose from merchant banking to become the de facto rulers of Florence and one of Renaissance Europe's most…
- [[house-of-plantagenet|House of Plantagenet]] — The House of Plantagenet ruled England from 1154 to 1485, the longest-reigning English royal house.
- [[house-of-romanov|House of Romanov]] — The House of Romanov ruled Russia for over three centuries (1613–1918), transforming it from a provincial Muscovite state into…
- [[house-of-stuart|House of Stuart]] — The House of Stuart ruled Scotland from 1371 and inherited the English and Irish thrones in 1603, reigning until 1714.
- [[house-of-tudor|House of Tudor]] — The House of Tudor ruled England from 1485 to 1603, emerging from the chaos of the Wars of the Roses to establish one of…
- [[house-of-valois|House of Valois]] — The House of Valois ruled France from 1328 to 1589, presiding over some of medieval Europe's grandest and bloodiest…
- [[house-of-windsor|House of Windsor]] — The House of Windsor has ruled the United Kingdom and the Commonwealth since 1917, when the British royal family renamed…

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
