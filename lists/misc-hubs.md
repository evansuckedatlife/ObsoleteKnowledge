---
type: list
category: misc
read: false
---

# Misc hubs

Cross-cutting concepts that belong to no single field.

## nodes

- [[gilded-age|Gilded Age]] — The Gilded Age was the period of rapid industrialization and economic growth in the United States, roughly from the 1870s through the 1900s, marked by…
- [[mary-queen-of-scots|Mary Queen of Scots]] — Mary Queen of Scots was a Scottish monarch (1542–1587) and the tragic focal point of religious and political turmoil in Renaissance Britain.
- [[space-age|Space Age]] — The Space Age was a cultural and design movement spanning roughly the 1950s through 1970s, born from humanity's ventures into space exploration and Co…

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
