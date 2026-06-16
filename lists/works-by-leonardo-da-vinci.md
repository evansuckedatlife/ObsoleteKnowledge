---
type: list
category: visual-art
read: false
---

# works by Leonardo da Vinci

The works by Leonardo da Vinci most worth knowing for quiz bowl.

## nodes

- [[annunciation|Annunciation]] — Leonardo's Annunciation, painted circa 1472–1475 in Florence, depicts the angel Gabriel approaching the Virgin Mary to…
- [[codex-leicester|Codex Leicester]] — The Codex Leicester is a 36-page scientific and technical notebook compiled by Leonardo from 1506–1510, now held in the…
- [[lady-with-an-ermine|Lady with an Ermine]] — Lady with an Ermine is Leonardo's portrait of Cecilia Gallerani, the young mistress of Ludovico Sforza, Duke of Milan, painted…
- [[mona-lisa|Mona Lisa]] — The Mona Lisa is Leonardo's most celebrated portrait, painted circa 1503–1519, depicting Lisa Gherardini, a Florentine…
- [[salvator-mundi|Salvator Mundi]] — Salvator Mundi is a portrait of Christ holding a crystal orb, painted by Leonardo circa 1490s, in which Jesus gestures in…
- [[the-last-supper|The Last Supper]] — The Last Supper is Leonardo's monumental mural depicting Jesus' final meal with his apostles before the Crucifixion, painted…
- [[the-virgin-and-child-with-st-anne|The Virgin and Child with St. Anne]] — The Virgin and Child with St.
- [[virgin-of-the-rocks|Virgin of the Rocks]] — Virgin of the Rocks exists in two versions by Leonardo (circa 1483–1486 and 1495–1508), depicting the Virgin Mary in a rocky…
- [[vitruvian-man|Vitruvian Man]] — Vitruvian Man is Leonardo's iconic drawing from circa 1490 depicting a perfectly proportioned male figure superimposed on both…

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
      - property: file.name
        direction: ASC
```
