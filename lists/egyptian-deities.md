---
type: list
category: mythology
read: false
---

# Egyptian deities

The major gods of ancient Egypt and the Osiris myth at the center of their religion.

## nodes

- [[amon|Amon]] — The hidden king of the gods and chief deity of the New Kingdom, Amon was originally a local Theban god who rose to supreme…
- [[anubis|Anubis]] — The jackal-headed god of mummification, embalming, and the dead, Anubis was the divine mortician who first mummified Osiris.
- [[aten|Aten]] — The sun disk elevated to supreme and sole divinity by the pharaoh Akhenaten, Aten represented an unprecedented theological…
- [[hathor|Hathor]] — The goddess of love, beauty, fertility, and joy, Hathor was also a protective cosmic force depicted as a cow or as a woman…
- [[horus|Horus]] — The falcon-headed god of the sky and rightful heir to Egypt's throne, Horus was born to Isis after his father Osiris's death.
- [[isis|Isis]] — The goddess of magic, motherhood, and devotion, Isis used her supernatural powers to resurrect her murdered husband Osiris and…
- [[maat|Ma'at]] — The goddess and abstract principle of truth, justice, cosmic order, and balance, Ma'at represented the fundamental laws…
- [[nephthys|Nephthys]] — The goddess of the boundaries, mourning, and hidden things, Nephthys was the sister of Osiris and Isis and wife of Set.
- [[osiris|Osiris]] — The god of the afterlife, resurrection, and fertility, Osiris was murdered by his jealous brother Set but restored to life by…
- [[ptah|Ptah]] — The creator god of craftsmen and artisans, Ptah brought the world into being through his thoughts and words rather than…
- [[ra|Ra]] — The sun god and supreme deity of ancient Egypt, Ra travels across the sky in his solar barque each day and through the…
- [[set|Set]] — The god of chaos, desert, and violence, Set murdered his brother Osiris in a power struggle but was ultimately defeated by…
- [[thoth|Thoth]] — The ibis-headed god of wisdom, writing, and cosmic order, Thoth served as the divine scribe and record-keeper of the gods.

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
