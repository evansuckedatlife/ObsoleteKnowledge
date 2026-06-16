---
type: list
category: music
read: false
---

# Romantic-era composers

The Romantic-era composers most worth knowing for quiz bowl.

## nodes

- [[franz-liszt|Franz Liszt]] — Franz Liszt (1811–1886) was a Hungarian composer, teacher, and the most celebrated piano virtuoso of the 19th century.
- [[pyotr-ilyich-tchaikovsky|Pyotr Ilyich Tchaikovsky]] — Pyotr Ilyich Tchaikovsky (1840–1893) was the first Russian composer to achieve international renown, writing some of the most…
- [[richard-wagner|Richard Wagner]] — Richard Wagner (1813–1883) was a revolutionary German composer, conductor, and theatre director who fundamentally transformed…

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
