---
type: list
category: geography
read: false
---

# Asian rivers

The Asian rivers most worth knowing for quiz bowl.

## nodes

- [[brahmaputra-river|Brahmaputra River]] — The Brahmaputra River is a major river of South Asia flowing approximately 2,896 kilometers (1,800 miles) from its source in…
- [[euphrates-river|Euphrates River]] — The Euphrates River is the longest river in southwestern Asia, flowing approximately 2,760 kilometers (1,715 miles) from its…
- [[ganges-river|Ganges River]] — The Ganges River is the holiest river in Hinduism and the lifeblood of northern India, flowing approximately 2,525 kilometers…
- [[indus-river|Indus River]] — The Indus River is one of the world's major rivers, flowing approximately 3,180 kilometers (1,976 miles) from the Tibetan…
- [[irrawaddy-river|Irrawaddy River]] — The Irrawaddy River (also spelled Ayeyarwady) is Myanmar's most important river, flowing approximately 2,170 kilometers (1,348…
- [[jordan-river|Jordan River]] — The Jordan River is the world's lowest river, flowing approximately 251 kilometers (156 miles) southward from the mountains of…
- [[mekong-river|Mekong River]] — The Mekong River is Southeast Asia's longest and most important river, flowing approximately 4,350 kilometers (2,703 miles)…
- [[tigris-river|Tigris River]] — The Tigris River is one of the two great rivers of ancient Mesopotamia, flowing approximately 1,900 kilometers (1,180 miles)…
- [[yangtze-river|Yangtze River]] — The Yangtze River is the longest river in Asia and the third longest in the world, flowing approximately 3,915 kilometers…
- [[yellow-river|Yellow River]] — The Yellow River, or Huang He, is the second-longest river in Asia and historically the most dangerous, flowing approximately…

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
