---
type: list
category: mathematics
read: false
---

# geometric curves

The geometric curves most worth knowing for quiz bowl.

## nodes

- [[cardioid|Cardioid]] — A heart-shaped curve traced by a point on a circle rolling around another circle of equal radius.
- [[catenary|Catenary]] — The curve formed by a hanging chain or cable under its own weight, held fixed at both ends.
- [[circle|Circle]] — The set of all points in a plane equidistant from a fixed point called the center.
- [[cycloid|Cycloid]] — The curve traced by a point on the rim of a circle rolling along a straight line.
- [[ellipse|Ellipse]] — The set of all points in a plane such that the sum of distances to two fixed foci is constant.
- [[hyperbola|Hyperbola]] — The set of all points in a plane such that the absolute difference of distances to two fixed foci is constant.
- [[lemniscate|Lemniscate of Bernoulli]] — A figure-eight shaped algebraic curve defined by the product of distances to two foci.
- [[parabola|Parabola]] — The set of all points in a plane equidistant from a fixed focus and a fixed directrix.
- [[sine-curve|Sine curve]] — The symmetric, periodic wave shape traced by the trigonometric sine function.
- [[spiral|Spiral of Archimedes]] — A curve that winds around a central point, progressively getting farther away at a constant rate.

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
