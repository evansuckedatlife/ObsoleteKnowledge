---
type: list
category: music
read: false
---

# American Composers

A collection of the most significant American classical and theatrical composers who defined the country's unique musical identity in the 20th century.

## nodes

- [[george-gershwin|George Gershwin]] — Fused classical music with jazz rhythms and Tin Pan Alley songs.
- [[aaron-copland|Aaron Copland]] — Crafted the populist "American sound" with open harmonies and folk hymns.
- [[leonard-bernstein|Leonard Bernstein]] — Charismatic conductor and composer of *West Side Story* and *Candide*.
- [[arnold-schoenberg|Arnold Schoenberg]] — Radical Austrian serialist who emigrated to the U.S. and taught in Los Angeles.
- [[philip-glass|Philip Glass]] — Minimalist pioneer who composed *Einstein on the Beach* and *Koyaanisqatsi*.
- [[samuel-barber|Samuel Barber]] — Neo-Romantic composer of the deeply emotional *Adagio for Strings*.
- [[charles-ives|Charles Ives]] — Early experimentalist who integrated polytonality and hymn quotations while working in insurance.
- [[john-cage|John Cage]] — Avant-garde revolutionary who composed the silent *4'33"* and invented the prepared piano.
- [[john-coolidge-adams|John Coolidge Adams]] — Post-minimalist composer of historical operas like *Nixon in China*.
- [[stephen-sondheim|Stephen Sondheim]] — Complex lyricist and composer who transformed modern musical theater with *Sweeney Todd*.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
