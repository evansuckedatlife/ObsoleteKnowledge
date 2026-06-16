---
type: list
category: music
read: false
---

# American composers

The American composers most worth knowing for quiz bowl.

## nodes

- [[aaron-copland|Aaron Copland]] — Aaron Copland (1900–1990) was an American composer often referred to as the "Dean of American Composers." He is celebrated for…
- [[arnold-schoenberg|Arnold Schoenberg]] — Arnold Schoenberg (1874–1951) was an Austrian-born composer, music theorist, and painter who was one of the most radical and…
- [[charles-ives|Charles Ives]] — Charles Ives (1874–1954) was an American modernist composer who is now recognized as one of the first American composers of…
- [[george-gershwin|George Gershwin]] — George Gershwin (1898–1937) was a monumental American composer and pianist who successfully bridged the gap between popular…
- [[john-cage|John Cage]] — John Cage (1912–1992) was an American composer, music theorist, philosopher, and artist who was a leading figure of the…
- [[john-coolidge-adams|John Coolidge Adams]] — John Coolidge Adams (b.
- [[leonard-bernstein|Leonard Bernstein]] — Leonard Bernstein (1918–1990) was a towering American composer, conductor, author, and pianist who was one of the most…
- [[philip-glass|Philip Glass]] — Philip Glass (b.
- [[samuel-barber|Samuel Barber]] — Samuel Barber (1910–1981) was an American composer of orchestral, choral, and dramatic music who was one of the most…
- [[stephen-sondheim|Stephen Sondheim]] — Stephen Sondheim (1930–2021) was a legendary American composer and lyricist who is widely regarded as the most important and…

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
