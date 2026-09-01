---
type: list
category: performance
read: false
---

# Performance hubs

Forms and traditions behind the individual productions and performers.

## nodes

- [[musical-theatre|Musical Theatre]] — Musical theatre is a theatrical form that synthesizes dramatic narrative, music, choreography, and elaborate spectacle into a live performance.

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
