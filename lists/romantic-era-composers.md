---
type: list
category: music
read: false
---

# Romantic-era composers

The Romantic-era composers most worth knowing for quiz bowl.

## nodes

- [[antonin-dvorak|Antonín Dvořák]] — Antonín Dvořák (1841–1904) was a Czech composer who achieved international fame by integrating Czech and Slavic folk rhythms…
- [[felix-mendelssohn|Felix Mendelssohn]] — Felix Mendelssohn (1809–1847) was a German composer, pianist, and conductor of the early Romantic period.
- [[franz-liszt|Franz Liszt]] — Franz Liszt (1811–1886) was a Hungarian composer, teacher, and the most celebrated piano virtuoso of the 19th century.
- [[franz-schubert|Franz Schubert]] — Franz Schubert (1797–1828) was an Austrian composer who bridged the late Classical and early Romantic eras.
- [[giuseppe-verdi|Giuseppe Verdi]] — Giuseppe Verdi (1813–1901) was the dominant composer of 19th-century Italian opera and a national icon of the Italian…
- [[hector-berlioz|Hector Berlioz]] — Hector Berlioz (1803–1869) was a French Romantic composer, conductor, and critic who made monumental contributions to modern…
- [[johannes-brahms|Johannes Brahms]] — Johannes Brahms (1833–1897) was a German composer, pianist, and conductor who was one of the leading musicians of the Romantic…
- [[pyotr-ilyich-tchaikovsky|Pyotr Ilyich Tchaikovsky]] — Pyotr Ilyich Tchaikovsky (1840–1893) was the first Russian composer to achieve international renown, writing some of the most…
- [[richard-wagner|Richard Wagner]] — Richard Wagner (1813–1883) was a revolutionary German composer, conductor, and theatre director who fundamentally transformed…
- [[robert-schumann|Robert Schumann]] — Robert Schumann (1810–1856) was a German composer, pianist, and one of the most influential music critics of the Romantic era.

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
