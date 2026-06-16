---
type: list
category: music
read: false
---

# 20th-Century Composers

A collection of the most influential classical composers of the 20th century who revolutionized musical structure, tonality, and composition.

## nodes

- [[igor-stravinsky|Igor Stravinsky]] — Russian modernist composer of *The Rite of Spring* and pioneer of polytonality and neoclassicism.
- [[arnold-schoenberg|Arnold Schoenberg]] — Austrian pioneer of atonality and developer of the twelve-tone serial technique.
- [[benjamin-britten|Benjamin Britten]] — English composer of *Peter Grimes* and *The Young Person's Guide to the Orchestra*.
- [[aaron-copland|Aaron Copland]] — Populist American composer of *Appalachian Spring* and *Fanfare for the Common Man*.
- [[sergei-prokofiev|Sergei Prokofiev]] — Soviet Russian composer of *Peter and the Wolf* and the ballet *Romeo and Juliet*.
- [[dmitri-shostakovich|Dmitri Shostakovich]] — Soviet Russian composer of 15 symphonies who walked a tightrope under Stalin's regime.
- [[bela-bartok|Béla Bartók]] — Hungarian ethnomusicologist and composer of *Concerto for Orchestra*.
- [[charles-ives|Charles Ives]] — American modernist pioneer of polytonality who worked in the insurance industry.
- [[maurice-ravel|Maurice Ravel]] — Meticulous French composer and master orchestrator of *Boléro*.
- [[george-gershwin|George Gershwin]] — American composer who fused classical music with jazz in *Rhapsody in Blue*.
- [[john-cage|John Cage]] — American avant-garde composer of the silent work *4'33"* and inventor of the prepared piano.
- [[sergei-rachmaninoff|Sergei Rachmaninoff]] — Russian late-Romantic virtuoso pianist and composer of *Piano Concerto No. 2*.

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
