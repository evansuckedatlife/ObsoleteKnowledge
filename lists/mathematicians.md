---
type: list
category: mathematics
read: false
---

# mathematicians

The mathematicians most worth knowing for quiz bowl.

## nodes

- [[alan-turing|Alan Turing]] — British pioneer of computer science who defined the Turing machine, proved the undecidability of the halting problem, and broke the Enigma code.
- [[bernhard-riemann|Bernhard Riemann]] — German mathematician who developed Riemannian geometry, defined the Riemann integral, and formulated the Riemann hypothesis.
- [[carl-friedrich-gauss|Carl Friedrich Gauss]] — German "Prince of Mathematicians" who proved the Fundamental Theorem of Algebra, introduced modular arithmetic, and developed the normal distribution.
- [[euclid|Euclid]] — Ancient Greek mathematician who compiled and structured geometry in the 13 books of the Elements.
- [[gottfried-leibniz|Gottfried Leibniz]] — German polymath who independently co-developed calculus, introducing the standard d/dx and integral notation, and pioneered symbolic logic.
- [[henri-poincare|Henri Poincaré]] — French mathematician who founded algebraic topology, discovered deterministic chaos in the three-body problem, and formulated the Poincaré conjecture.
- [[isaac-newton|Isaac Newton]] — English scientist who independently co-developed calculus, formulated the laws of motion and universal gravitation, and designed the reflecting telescope.
- [[leonhard-euler|Leonhard Euler]] — Prolific Swiss mathematician who formalised function notation, introduced e and i, solved the Königsberg bridges problem, and discovered e^(iπ) + 1 = 0.
- [[pierre-de-fermat|Pierre de Fermat]] — French lawyer and mathematician who proposed Fermat's Last Theorem, co-developed analytic geometry, and pioneered probability theory.
- [[pythagoras|Pythagoras]] — Ancient Greek philosopher and mathematician whose followers integrated mysticism with numbers and who is credited with the right-triangle theorem.

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
