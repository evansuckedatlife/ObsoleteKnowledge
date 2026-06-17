---
type: list
category: science
read: false
---

# dwarf planets, comets, and asteroids

The dwarf planets, comets, and asteroids most worth knowing for quiz bowl.

## nodes

- [[ceres|Ceres]] — Ceres is a dwarf planet in the asteroid belt between Mars and Jupiter, and the largest body in that region.
- [[comet-67p|Comet 67P]] — Comet 67P/Churyumov-Gerasimenko is a small periodic comet notable for being the first comet to be orbited and studied at close…
- [[comet-shoemaker-levy-9|Comet Shoemaker-Levy 9]] — Comet Shoemaker-Levy 9 is the first and only comet known to have impacted a planet in recorded history.
- [[eris|Eris]] — Eris is a dwarf planet in the outer solar system, slightly more distant and marginally more massive than Pluto.
- [[hale-bopp|Hale-Bopp]] — Comet Hale-Bopp is one of the brightest and most spectacularly active comets of the modern era, discovered independently in…
- [[halley-comet|Halley's Comet]] — Halley's Comet is the most famous periodic comet in human history, visible from Earth roughly every 75 to 76 years.
- [[pluto|Pluto]] — Pluto is a dwarf planet and the prototype of a new class of icy solar-system bodies orbiting beyond Neptune.
- [[theia|Theia]] — Theia is a hypothesized Mars-sized protoplanet that is believed to have collided with the proto-Earth roughly 4.5 billion…
- [[vesta|Vesta]] — Vesta is the second-most-massive body in the asteroid belt and a prototype of the differentiated asteroid — a small planetary…

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
