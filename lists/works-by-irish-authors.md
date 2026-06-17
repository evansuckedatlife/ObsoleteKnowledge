---
type: list
category: literature
read: false
---

# works by Irish authors

The works by Irish authors most worth knowing for quiz bowl.

## nodes

- [[a-portrait-of-the-artist-as-a-young-man|A Portrait of the Artist as a Young Man]] — A Portrait of the Artist as a Young Man is James Joyce's 1916 semi-autobiographical novel chronicling the intellectual,…
- [[at-swim-two-birds|At Swim-Two-Birds]] — At Swim-Two-Birds is Flann O'Brien's 1939 satirical novel set in Dublin, following a unnamed undergraduate who writes a book…
- [[dracula|Dracula]] — Bram Stoker's 1897 novel is a masterwork of epistolary Gothic horror depicting the invasion of Victorian England by Count…
- [[dubliners|Dubliners]] — Dubliners is James Joyce's 1914 collection of 15 short stories set in Dublin, depicting the lives of middle-class Dubliners…
- [[gulliver-travels|Gulliver's Travels]] — Gulliver's Travels is Jonathan Swift's 1726 satirical voyage narrative, in which Lemuel Gulliver undertakes four journeys to…
- [[murphy-novel|Murphy]] — Murphy is Samuel Beckett's 1938 debut novel about Murphy, an Irishman in London who seeks to escape the world's chaos by…
- [[the-importance-of-being-earnest|The Importance of Being Earnest]] — The Importance of Being Earnest is Oscar Wilde's 1895 comedy of errors and witty repartee, in which two men invent fictional…
- [[the-picture-of-dorian-gray|The Picture of Dorian Gray]] — The Picture of Dorian Gray is Oscar Wilde's 1890 philosophical novel about Dorian Gray, a young man of exceptional beauty who…
- [[ulysses|Ulysses]] — Ulysses is James Joyce's 1922 modernist masterpiece, a revolutionary novel that follows Leopold Bloom through Dublin on June…
- [[waiting-for-godot|Waiting for Godot]] — Waiting for Godot is Samuel Beckett's 1952 play—originally written in French as En attendant Godot—in which two men, Vladimir…

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
