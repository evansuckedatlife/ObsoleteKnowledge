---
type: list
category: literature
read: false
---

# Elizabethan playwrights

Shakespeare's contemporaries and rivals on the Elizabethan and Jacobean stage.

## nodes

- [[christopher-marlowe|Christopher Marlowe]] — Christopher Marlowe (1564–1593) was an English dramatist and poet who, though he died at 29 under mysterious circumsta…
- [[ben-jonson|Ben Jonson]] — Ben Jonson (1572–1637) was an English dramatist, poet, and literary critic who was Shakespeare's contemporary and riva…

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
