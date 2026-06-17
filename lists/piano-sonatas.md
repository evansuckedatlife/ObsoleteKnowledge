---
type: list
category: music
read: false
---

# piano sonatas

The piano sonatas most worth knowing for quiz bowl.

## nodes

- [[appassionata-sonata|Appassionata Sonata]] — Ludwig van Beethoven's Piano Sonata No.
- [[moonlight-sonata|Moonlight Sonata]] — Ludwig van Beethoven's Piano Sonata No.
- [[piano-sonatas-mozart|Mozart piano sonatas]] — Wolfgang Amadeus Mozart composed 18 numbered piano sonatas between 1774 and 1789.

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
