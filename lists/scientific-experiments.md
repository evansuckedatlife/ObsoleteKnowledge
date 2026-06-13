---
type: list
category: science
read: false
---

# scientific experiments

The scientific experiments most worth knowing for quiz bowl.

## nodes

- [[davisson-germer-experiment|Davisson–Germer Experiment]] — In 1927, Clinton Davisson and Lester Germer fired a beam of electrons at a nickel crystal and observed a diffraction pattern…
- [[double-slit-experiment|Double-Slit Experiment]] — Thomas Young's landmark 1801 experiment demonstrated that light behaves as a wave, not merely as particles, by passing it…
- [[hershey-chase-experiment|Hershey–Chase Experiment]] — In 1952, Alfred Hershey and Martha Chase used radioactive isotopes to label the DNA and protein components of bacteriophages…
- [[mendel-pea-plant-experiments|Mendel's Pea-Plant Experiments]] — Gregor Mendel, an Augustinian friar and botanist, conducted systematic breeding experiments on pea plants between 1856 and…
- [[meselson-stahl-experiment|Meselson–Stahl Experiment]] — In 1958, Matthew Meselson and Franklin Stahl grew bacteria in a medium containing a heavy isotope of nitrogen, then…
- [[michelson-morley-experiment|Michelson–Morley Experiment]] — In 1887, Albert Michelson and Edward Morley used an interferometer to measure whether Earth's motion through space could be…
- [[miller-urey-experiment|Miller–Urey Experiment]] — In 1952, Stanley Miller and Harold Urey simulated the early Earth's atmosphere and ocean in a closed flask, sparked it with…
- [[millikan-oil-drop-experiment|Millikan Oil-Drop Experiment]] — Between 1909 and 1916, Robert Millikan sprayed tiny oil droplets into an electric field and measured their fall velocity to…
- [[rutherford-gold-foil-experiment|Rutherford Gold-Foil Experiment]] — In 1909, Ernest Rutherford, Hans Geiger, and Ernest Marsden bombarded thin gold foil with alpha particles (helium nuclei) and…
- [[stern-gerlach-experiment|Stern–Gerlach Experiment]] — In 1922, Otto Stern and Walther Gerlach passed a beam of silver atoms through a non-uniform magnetic field and observed that…

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
