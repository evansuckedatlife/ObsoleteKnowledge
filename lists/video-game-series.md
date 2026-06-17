---
type: list
category: pop-culture
read: false
---

# video game series

The video game series most worth knowing for quiz bowl.

## nodes

- [[call-of-duty|Call of Duty]] — Call of Duty is an annual first-person shooter franchise launched by Activision in 2003, centered on modern military campaigns…
- [[final-fantasy|Final Fantasy]] — Final Fantasy is a multimedia role-playing game franchise debuted by Squaresoft in 1987, known for elaborate fantasy worlds,…
- [[halo|Halo]] — Halo is a science-fiction first-person shooter franchise launched by Bungie for Xbox in 2001, featuring the super-soldier…
- [[pokemon|Pokémon]] — Pokémon is a multimedia franchise launched by Nintendo and Game Freak in 1996, centered on capturing, training, and battling…
- [[sonic-the-hedgehog|Sonic the Hedgehog]] — Sonic the Hedgehog is Sega's flagship platformer franchise debuting in 1991, centered on a super-fast blue hedgehog racing…
- [[street-fighter|Street Fighter]] — Street Fighter is a fighting game franchise launched by Capcom in 1987, featuring hand-to-hand martial artists competing in…
- [[super-mario|Super Mario]] — Super Mario is Nintendo's flagship platformer franchise debuting in 1985, following the adventures of Mario, a plumber who…
- [[tetris|Tetris]] — Tetris is a Soviet-designed puzzle game released in 1984, built on the mechanic of rotating and dropping geometric tetrominoes…
- [[the-legend-of-zelda|The Legend of Zelda]] — The Legend of Zelda is Nintendo's action-adventure franchise debuting in 1986, centered on the hero Link as he battles the…
- [[the-sims|The Sims]] — The Sims is a life simulation game franchise debuted by Maxis in 2000, where players build and manage households of artificial…

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
