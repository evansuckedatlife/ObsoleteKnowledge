---
type: list
category: music
read: false
---

# operas

The operas most worth knowing for quiz bowl.

## nodes

- [[aida|Aida]] — Giuseppe Verdi's Aida (1871) is a grand opera in four acts set in ancient Egypt during a conflict with Ethiopia.
- [[boris-godunov|Boris Godunov]] — Modest Mussorgsky's Boris Godunov (1874) is a monumental Russian opera based on Alexander Pushkin's historical drama and…
- [[carmen|Carmen]] — Georges Bizet's Carmen (1875) is a four-act French opera that stands as one of the most popular and frequently performed works…
- [[don-giovanni|Don Giovanni]] — Wolfgang Amadeus Mozart's Don Giovanni (1787) is a two-act opera formally classified as a dramma giocoso (a blend of comedy…
- [[la-boheme|La bohème]] — Giacomo Puccini's La bohème (1896) is a four-act Italian opera that stands as one of the most beloved and frequently performed…
- [[madama-butterfly|Madama Butterfly]] — Giacomo Puccini's Madama Butterfly (1904) is a tragic three-act Italian opera set in Nagasaki, Japan.
- [[salome|Salome]] — Richard Strauss's Salome (1905) is a shocking, highly influential one-act German opera.
- [[the-barber-of-seville|The Barber of Seville]] — Gioachino Rossini's The Barber of Seville (1816) is a two-act opera buffa (comic opera) that stands as a masterpiece of the…
- [[the-marriage-of-figaro|The Marriage of Figaro]] — Wolfgang Amadeus Mozart's The Marriage of Figaro (1786) is a four-act opera buffa (comic opera) widely considered one of the…
- [[william-tell|William Tell]] — Gioachino Rossini's William Tell (1829) is a four-act French grand opera based on Friedrich Schiller's play Wilhelm Tell.

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
