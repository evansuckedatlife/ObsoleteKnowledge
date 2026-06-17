---
type: list
category: science
read: false
---

# 20th-century physicists

The 20th-century physicists most worth knowing for quiz bowl.

## nodes

- [[albert-einstein|Albert Einstein]] — A German-born theoretical physicist, Albert Einstein is widely considered one of the two pillars of modern physics alongside…
- [[enrico-fermi|Enrico Fermi]] — An Italian-American physicist, Enrico Fermi is widely known as the "architect of the nuclear age" for his work in both…
- [[erwin-schrodinger|Erwin Schrödinger]] — An Austrian-Irish theoretical physicist, Erwin Schrödinger developed wave mechanics, a formulation of quantum mechanics based…
- [[george-gamow|George Gamow]] — A Soviet-American theoretical physicist and cosmologist, George Gamow was a key developer of the Big Bang theory.
- [[louis-de-broglie|Louis de Broglie]] — A French physicist and aristocrat, Louis de Broglie proposed the radical theory that all matter possesses wave-like properties.
- [[max-planck|Max Planck]] — A German theoretical physicist, Max Planck is widely regarded as the founder of quantum mechanics.
- [[niels-bohr|Niels Bohr]] — A Danish physicist, Niels Bohr made foundational contributions to understanding atomic structure and quantum mechanics.
- [[paul-dirac|Paul Dirac]] — An English theoretical physicist, Paul Dirac made fundamental contributions to the early development of both quantum mechanics…
- [[richard-feynman|Richard Feynman]] — An American theoretical physicist, Richard Feynman was one of the most brilliant and colorful scientists of the 20th century.
- [[werner-heisenberg|Werner Heisenberg]] — A German theoretical physicist, Werner Heisenberg was a key pioneer of quantum mechanics.

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
