---
type: list
category: music
read: false
---

# 20th-century composers

The 20th-century composers most worth knowing for quiz bowl.

## nodes

- [[aaron-copland|Aaron Copland]] — Aaron Copland (1900–1990) was an American composer often referred to as the "Dean of American Composers." He is celebrated for…
- [[arnold-schoenberg|Arnold Schoenberg]] — Arnold Schoenberg (1874–1951) was an Austrian-born composer, music theorist, and painter who was one of the most radical and…
- [[benjamin-britten|Benjamin Britten]] — Benjamin Britten (1913–1976) was the preeminent English composer of the 20th century, revitalizing British opera and choral music.
- [[bela-bartok|Béla Bartók]] — Béla Bartók (1881–1945) was a Hungarian composer, pianist, and ethnomusicologist who was one of the most influential figures…
- [[charles-ives|Charles Ives]] — Charles Ives (1874–1954) was an American modernist composer who is now recognized as one of the first American composers of…
- [[dmitri-shostakovich|Dmitri Shostakovich]] — Dmitri Shostakovich (1906–1975) was a Soviet Russian composer and pianist who was one of the most celebrated and scrutinized…
- [[george-gershwin|George Gershwin]] — George Gershwin (1898–1937) was a monumental American composer and pianist who successfully bridged the gap between popular…
- [[igor-stravinsky|Igor Stravinsky]] — Igor Stravinsky (1882–1971) was a Russian-born composer, pianist, and conductor widely considered one of the most influential…
- [[john-cage|John Cage]] — John Cage (1912–1992) was an American composer, music theorist, philosopher, and artist who was a leading figure of the…
- [[maurice-ravel|Maurice Ravel]] — Maurice Ravel (1875–1937) was a French composer, pianist, and conductor who is widely regarded as one of France's greatest…
- [[sergei-prokofiev|Sergei Prokofiev]] — Sergei Prokofiev (1891–1953) was a Soviet and Russian composer, pianist, and conductor who was one of the major creators of…
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
