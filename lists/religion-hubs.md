---
type: list
category: religion
read: false
---

# Religion hubs

Traditions, movements and ideas that the specific figures and texts belong to.

## nodes

- [[bible|Bible]] — The Bible is the central sacred text of Christianity, comprising the Hebrew Bible (also called the Old Testament) and the New Testament.
- [[counter-reformation|Counter-Reformation]] — The Counter-Reformation (16th–17th centuries) was the Catholic Church's comprehensive response to the Protestant Reformation, combining internal Churc…
- [[gospel-of-john|Gospel of John]] — The Gospel of John (or Fourth Gospel) is the final of the four canonical Gospels in the New Testament, traditionally attributed to John the Apostle.
- [[laozi|Laozi]] — Laozi (literally "Old Master") is the legendary author traditionally credited with composing the Tao Te Ching, the foundational text of Taoism and phi…
- [[st-peters-basilica|St. Peter's Basilica]] — St.

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
