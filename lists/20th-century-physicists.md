---
type: list
category: science
read: false
---

# 20th-Century Physicists

The pioneering theoretical and experimental scientists who revolutionized our understanding of the physical universe by developing quantum mechanics, relativity, and nuclear physics.

## nodes

- [[max-planck|Max Planck]] — the father of quantum theory who resolved the ultraviolet catastrophe using energy quanta.
- [[albert-einstein|Albert Einstein]] — the creator of special and general relativity who explained the photoelectric effect.
- [[niels-bohr|Niels Bohr]] — the developer of the Bohr atomic model and primary philosopher of the Copenhagen interpretation.
- [[louis-de-broglie|Louis de Broglie]] — the discoverer of the wave nature of electrons who formulated matter-wave duality.
- [[werner-heisenberg|Werner Heisenberg]] — the developer of matrix mechanics and the uncertainty principle.
- [[erwin-schrodinger|Erwin Schrödinger]] — the developer of wave mechanics who formulated his eponymous wave equation and cat thought experiment.
- [[paul-dirac|Paul Dirac]] — the formulator of the relativistic wave equation who predicted the existence of antimatter.
- [[enrico-fermi|Enrico Fermi]] — the builder of the first nuclear reactor who co-developed Fermi-Dirac statistics and beta decay theory.
- [[richard-feynman|Richard Feynman]] — the developer of quantum electrodynamics and path integrals who invented Feynman diagrams.
- [[george-gamow|George Gamow]] — the Big Bang cosmologist who explained alpha decay using quantum tunneling and proposed triplet genetic codons.

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
