---
type: list
category: mathematics
read: false
---

# mathematicians

The mathematicians most worth knowing for quiz bowl.

## nodes

- [[alan-turing|Alan Turing]] — Alan Turing (1912–1954) was a British mathematician, logician, and computer scientist who formalised the concepts of algorithm…
- [[bernhard-riemann|Bernhard Riemann]] — Bernhard Riemann (1826–1866) was a German mathematician who made groundbreaking contributions to analysis, number theory, and…
- [[carl-friedrich-gauss|Carl Friedrich Gauss]] — Carl Friedrich Gauss (1777–1855) was a German mathematician and astronomer whose contributions span number theory, statistics,…
- [[euclid|Euclid]] — Euclid (c.
- [[gottfried-leibniz|Gottfried Leibniz]] — Gottfried Leibniz (1646–1716) was a German polymath—mathematician, philosopher, physicist, logician, and diplomat—who…
- [[henri-poincare|Henri Poincaré]] — Henri Poincaré (1854–1912) was a French mathematician, theoretical physicist, and philosopher of science, often described as…
- [[isaac-newton|Isaac Newton]] — Isaac Newton (1642–1727) was an English mathematician, physicist, and astronomer whose Principia Mathematica (1687) founded…
- [[leonhard-euler|Leonhard Euler]] — Leonhard Euler (1707–1783) was a Swiss mathematician and physicist whose prolific output—roughly one paper per week for 56…
- [[pierre-de-fermat|Pierre de Fermat]] — Pierre de Fermat (1607–1665) was a French lawyer and mathematician whose work in number theory, calculus, and probability was…
- [[pythagoras|Pythagoras]] — Pythagoras (c.

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
