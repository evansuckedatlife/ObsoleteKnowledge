---
type: list
category: music
read: false
---

# early-20th-century European composers

The early-20th-century European composers most worth knowing for quiz bowl.

## nodes

- [[arnold-schoenberg|Arnold Schoenberg]] — Arnold Schoenberg (1874–1951) was an Austrian-born composer, music theorist, and painter who was one of the most radical and…
- [[bela-bartok|Béla Bartók]] — Béla Bartók (1881–1945) was a Hungarian composer, pianist, and ethnomusicologist who was one of the most influential figures…
- [[maurice-ravel|Maurice Ravel]] — Maurice Ravel (1875–1937) was a French composer, pianist, and conductor who is widely regarded as one of France's greatest…
- [[sergei-rachmaninoff|Sergei Rachmaninoff]] — Sergei Rachmaninoff (1873–1943) was a Russian composer, virtuoso pianist, and conductor who was one of the last great…

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
