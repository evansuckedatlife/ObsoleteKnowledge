---
type: list
category: visual-art
read: false
---

# Visual Art hubs

Movements, media and institutions the individual artists and works sit within.

## nodes

- [[botticelli|Botticelli]] — Sandro Botticelli (1445–1510) was a Florentine painter whose elegant, decorative style defined the early Italian Renaissance.
- [[modern-architecture|Modern Architecture]] — Modern architecture refers to the design movement and building practices of the 20th and 21st centuries that abandoned historical ornament in favour o…
- [[renaissance-religious-art|Renaissance Religious Art]] — Renaissance religious art represents the synthesis of Christian devotional imagery with the revolutionary techniques and humanist philosophy of the 15…

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
