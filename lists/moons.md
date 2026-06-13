---
type: list
category: science
read: false
---

# moons

The moons most worth knowing for quiz bowl.

## nodes

- [[callisto|Callisto]] — Callisto is the outermost of Jupiter's four large Galilean moons and the third-largest moon in the solar system.
- [[charon|Charon]] — Charon is Pluto's largest moon and so massive relative to its primary that the two bodies orbit around a shared center of…
- [[deimos|Deimos]] — Deimos is the smaller and more distant of Mars's two natural satellites, discovered in 1877 by Asaph Hall.
- [[earth-moon|Earth's Moon]] — The Moon is Earth's only natural satellite, orbiting at an average distance of 384,400 km.
- [[enceladus|Enceladus]] — Enceladus is a small moon of Saturn famous for its dramatic water-ice geysers that erupt from its south polar region.
- [[europa|Europa]] — Europa is the fourth and smallest of Jupiter's four large Galilean moons, but its icy surface and compelling evidence of a…
- [[ganymede|Ganymede]] — Ganymede is the largest moon in the solar system and the second-largest Galilean moon of Jupiter.
- [[io|Io]] — Io is the innermost of Jupiter's four large Galilean moons, famous for being the most volcanically active body in the solar…
- [[phobos|Phobos]] — Phobos is the larger of Mars's two moons, orbiting much closer to the planet than any other known moon in the solar system.
- [[titan|Titan]] — Titan is Saturn's largest moon and the second-largest moon in the solar system, remarkable for being the only moon with a…
- [[triton|Triton]] — Triton is Neptune's largest moon, famous for orbiting retrograde—backward relative to Neptune's rotation.

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
