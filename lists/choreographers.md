---
type: list
category: performance
read: false
---

# choreographers

The choreographers most worth knowing for quiz bowl.

## nodes

- [[agnes-de-mille|Agnes de Mille]] — Agnes de Mille was an American choreographer who invented the vocabulary of modern American musical theater by integrating…
- [[alvin-ailey|Alvin Ailey]] — Alvin Ailey was an American modern dancer and choreographer who founded the Alvin Ailey American Dance Theater, the most…
- [[bob-fosse|Bob Fosse]] — Bob Fosse was an American choreographer, dancer, and director who created a distinctive theatrical style blending jazz,…
- [[george-balanchine|George Balanchine]] — George Balanchine was a Russian-American choreographer who revolutionized ballet through speed, athleticism, and abstract…
- [[isadora-duncan|Isadora Duncan]] — Isadora Duncan was an American dancer and choreographer who single-handedly created modern dance by rejecting the rigid…
- [[jerome-robbins|Jerome Robbins]] — Jerome Robbins was an American choreographer and director who bridged classical ballet and Broadway, creating movement that…
- [[marius-petipa|Marius Petipa]] — Marius Petipa was a French-Russian choreographer who is the architect of classical ballet as we know it, having created the…
- [[martha-graham|Martha Graham]] — Martha Graham was an American modern dance pioneer who revolutionized dance by rejecting classical ballet's constraints and…
- [[merce-cunningham|Merce Cunningham]] — Merce Cunningham was an American modern dancer and choreographer who fundamentally redefined dance as an independent art form,…
- [[twyla-tharp|Twyla Tharp]] — Twyla Tharp is an American dancer and choreographer who seamlessly blended contemporary dance, ballet, and popular culture,…

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
