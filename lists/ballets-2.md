---
type: list
category: performance
read: false
---

# ballets

The ballets most worth knowing for quiz bowl.

## nodes

- [[appalachian-spring|Appalachian Spring]] — Appalachian Spring is a one-act ballet choreographed by Martha Graham in 1944 to a new score by Aaron Copland, celebrating…
- [[cinderella-prokofiev|Cinderella (Prokofiev)]] — Prokofiev's Cinderella is a full-length fairy-tale ballet, choreographed first by Konstantin Sergeyev in 1945 for the Kirov…
- [[don-quixote|Don Quixote]] — Don Quixote is a comic ballet choreographed by Marius Petipa in 1869, adapting Cervantes' novel of a delusional Spanish…
- [[la-bayadere|La Bayadère]] — La Bayadère is a full-length ballet choreographed by Marius Petipa in 1877, set in ancient India and centered on a doomed…
- [[la-sylphide|La Sylphide]] — La Sylphide is a two-act Romantic-era ballet choreographed by Filippo Taglioni in 1832, featuring his daughter Marie Taglioni…
- [[petrushka|Petrushka]] — Petrushka is a one-act ballet by Igor Stravinsky and Michel Fokine, premiered in 1911 by the Ballets Russes, based on a…
- [[pulcinella|Pulcinella]] — Pulcinella is a one-act ballet choreographed by Léonide Massine in 1920 for the Ballets Russes, with music by Igor Stravinsky…
- [[romeo-and-juliet-ballet|Romeo and Juliet]] — Prokofiev's Romeo and Juliet is a full-length ballet adapting Shakespeare's tragic play, choreographed in multiple versions…
- [[spartacus|Spartacus]] — Spartacus is a full-length Soviet ballet choreographed by Yuri Grigorovich in 1968, set to Aram Khachaturian's monumental score.
- [[the-firebird|The Firebird]] — The Firebird is a one-act ballet by Igor Stravinsky and Michel Fokine, premiered in 1910 by the Ballets Russes, drawing on…

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
