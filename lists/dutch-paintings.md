---
type: list
category: visual-art
read: false
---

# Dutch paintings

The Dutch paintings most worth knowing for quiz bowl.

## nodes

- [[girl-with-a-pearl-earring|Girl with a Pearl Earring]] — Johannes Vermeer's circa 1665 Girl with a Pearl Earring depicts an unknown young woman in exotic turban and luminous pearl…
- [[self-portrait-with-two-circles|Self-Portrait with Two Circles]] — Rembrandt's Self-Portrait with Two Circles, painted in 1665 near the end of his life, shows the aging artist standing before a…
- [[the-anatomy-lesson-of-dr-tulp|The Anatomy Lesson of Dr. Tulp]] — Rembrandt's 1632 The Anatomy Lesson of Dr.
- [[the-arnolfini-portrait|The Arnolfini Portrait]] — Jan van Eyck's 1434 The Arnolfini Portrait depicts a wealthy merchant and his wife in an elaborately furnished domestic…
- [[the-garden-of-earthly-delights|The Garden of Earthly Delights]] — Hieronymus Bosch's monumental triptych The Garden of Earthly Delights, painted circa 1490–1510, presents a fantastical…
- [[the-hunters-in-the-snow|The Hunters in the Snow]] — Pieter Bruegel the Elder's 1565 Hunters in the Snow depicts a winter landscape with hunters and dogs returning from the field,…
- [[the-milkmaid|The Milkmaid]] — Vermeer's The Milkmaid, painted circa 1658–1660, shows a domestic servant pouring milk into a bowl with such concentration and…
- [[the-night-watch|The Night Watch]] — The Night Watch, Rembrandt's monumental 1642 group portrait, depicts an Amsterdam militia company mustering in a shadowed…
- [[the-potato-eaters|The Potato Eaters]] — Vincent van Gogh's 1885 The Potato Eaters, painted in Nuenen in northern Brabant, depicts a family of peasants gathered around…
- [[view-of-delft|View of Delft]] — Vermeer's View of Delft, painted circa 1660–1661, is his only known cityscape—a serene panorama of Delft's skyline reflected…

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
