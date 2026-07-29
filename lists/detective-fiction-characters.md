---
type: list
category: literature
read: false
---

# Detective fiction characters

The recurring detectives and companions who define the mystery genre.

## nodes

- [[sherlock-holmes|Sherlock Holmes]] — Sherlock Holmes is the fictional consulting detective created by Sir Arthur Conan Doyle, first appearing in A Study in…
- [[dr-watson|Dr. Watson]] — Dr.

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
