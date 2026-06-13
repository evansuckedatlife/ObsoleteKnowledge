---
type: list
category: science
read: false
---

# classes of particles

The classes of particles most worth knowing for quiz bowl.

## nodes

- [[baryon|Baryon]] — Baryons are hadrons composed of three quarks held together by gluon exchange via the strong force.
- [[boson|Boson]] — Bosons are particles with integer spin (0, 1, 2, …) that obey Bose-Einstein statistics, allowing multiple identical particles…
- [[fermion|Fermion]] — Fermions are particles with half-integer spin (1/2, 3/2, …) that obey Fermi-Dirac statistics, including the Pauli exclusion…
- [[gauge-boson|Gauge boson]] — Gauge bosons (also vector bosons) are spin-1 bosons that mediate fundamental forces through gauge symmetry principles.
- [[gluon|Gluon]] — Gluons are massless gauge bosons that mediate the strong nuclear force by coupling to color charge.
- [[hadron|Hadron]] — Hadrons are composite particles made of quarks bound by gluon exchange through the strong nuclear force.
- [[lepton|Lepton]] — Leptons are fundamental fermions that do not participate in the strong nuclear force.
- [[meson|Meson]] — Mesons are hadrons composed of a quark-antiquark pair bound by gluon exchange.
- [[parton|Parton]] — Partons are the generic name for quarks and gluons that constitute hadrons, used when their exact identity or behavior within…
- [[quark|Quark]] — Quarks are fundamental fermions that carry color charge and are confined within hadrons via the strong nuclear force.

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
