---
type: list
category: science
read: false
---

# distinctions among types of plants

The distinctions among types of plants most worth knowing for quiz bowl.

## nodes

- [[angiosperms|Angiosperms]] — Angiosperms are the flowering plants — the most diverse and ecologically dominant plant group today — characterized by seeds…
- [[bryophytes|Bryophytes]] — Bryophytes are the simplest land plants — mosses, liverworts, and hornworts — lacking vascular tissue (xylem and phloem).
- [[dicots|Dicots]] — Dicots are flowering plants with two cotyledons (seed leaves), comprising roughly 70% of angiosperm diversity.
- [[gymnosperms|Gymnosperms]] — Gymnosperms are seed-bearing plants whose seeds develop naked — exposed directly to the air rather than enclosed in a fruit.
- [[monocots|Monocots]] — Monocots are flowering plants with a single cotyledon (seed leaf), comprising roughly 30% of angiosperm diversity.
- [[non-vascular-plants|Non-vascular plants]] — Non-vascular plants are plants that lack xylem and phloem — the specialized conducting tissues that characterize vascular plants.
- [[phloem|Phloem]] — Phloem is the vascular tissue that transports sugars, amino acids, and other organic compounds produced by photosynthesis…
- [[pterophytes|Pterophytes]] — Pterophytes (ferns and allies) are the first plants to evolve true vascular tissue, enabling them to grow tall and colonize…
- [[vascular-plants|Vascular plants]] — Vascular plants are plants that possess specialized conducting tissues — xylem and phloem — enabling them to transport water,…
- [[xylem|Xylem]] — Xylem is the vascular tissue in plants that transports water and dissolved minerals upward from the roots to the leaves and stems.

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
