---
type: list
category: music
read: false
---

# jazz musicians

The jazz musicians most worth knowing for quiz bowl.

## nodes

- [[billie-holiday|Billie Holiday]] — Billie Holiday was an American jazz vocalist whose intimate phrasing, emotional depth, and ability to convey profound…
- [[charles-mingus|Charles Mingus]] — Charles Mingus was an American jazz bassist, bandleader, and composer whose virtuosic bass playing and ambitious orchestral…
- [[charlie-parker|Charlie Parker]] — Charlie Parker was an American jazz saxophonist and composer whose rapid, harmonic innovations and technical brilliance…
- [[dizzy-gillespie|Dizzy Gillespie]] — Dizzy Gillespie was an American jazz trumpeter, bandleader, and composer whose harmonic innovations, technical virtuosity, and…
- [[duke-ellington|Duke Ellington]] — Duke Ellington was an American jazz composer, bandleader, and pianist whose sophisticated orchestrations, extended…
- [[ella-fitzgerald|Ella Fitzgerald]] — Ella Fitzgerald was an American jazz vocalist renowned for her exceptional vocal range, perfect intonation, and…
- [[john-coltrane|John Coltrane]] — John Coltrane was an American jazz saxophonist, bandleader, and composer whose harmonic innovations, spiritual searching, and…
- [[louis-armstrong|Louis Armstrong]] — Louis Armstrong was an American jazz trumpeter, vocalist, and composer whose innovative improvisational style and warm,…
- [[miles-davis|Miles Davis]] — Miles Davis was an American jazz trumpeter, bandleader, and composer whose restless innovation transformed jazz repeatedly…
- [[thelonious-monk|Thelonious Monk]] — Thelonious Monk was an American jazz pianist, bandleader, and composer whose angular compositions, percussive piano technique,…

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
