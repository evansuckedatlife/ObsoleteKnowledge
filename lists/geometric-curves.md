---
type: list
category: mathematics
read: false
---

# geometric curves

The geometric curves most worth knowing for quiz bowl.

## nodes

- [[cardioid|Cardioid]] — A cardioid is a heart-shaped curve traced by a point on the circumference of a circle rolling around another circle of the…
- [[catenary|Catenary]] — A catenary is the curve formed by a hanging chain or cable under its own weight, held fixed at both ends.
- [[circle|Circle]] — A circle is the set of all points in a plane equidistant from a fixed point called the center.
- [[conic-sections|Conic Sections]] — Conic sections are the curves produced when a plane intersects a double cone at various angles.
- [[cycloid|Cycloid]] — A cycloid is the curve traced by a point on the rim of a circle as it rolls along a straight line without slipping.
- [[ellipse|Ellipse]] — An ellipse is the set of all points in a plane such that the sum of distances to two fixed points (the foci) is constant.
- [[hyperbola|Hyperbola]] — A hyperbola is the set of all points in a plane such that the absolute difference of distances to two fixed points (the foci)…
- [[lemniscate|Lemniscate]] — A lemniscate is a figure-eight or infinity-shaped curve defined as the locus of points whose product of distances to two fixed…
- [[limacon|Limacon]] — A limacon (or limaçon, French for "snail") is a rose-like curve defined in polar coordinates, known for its variety of shapes…
- [[parabola|Parabola]] — A parabola is the set of all points in a plane equidistant from a fixed point (the focus) and a fixed line (the directrix).
- [[spiral|Spiral]] — A spiral is a curve that winds around a central point or axis, progressively getting closer to (or farther from) the center.
- [[witch-of-agnesi|Witch of Agnesi]] — The Witch of Agnesi is a smooth, bell-shaped curve with a centuries-long history of study, originating in Maria Agnesi's…

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
