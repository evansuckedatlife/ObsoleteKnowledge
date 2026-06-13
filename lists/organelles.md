---
type: list
category: science
read: false
---

# organelles

The organelles most worth knowing for quiz bowl.

## nodes

- [[centriole|Centriole]] — Centrioles are cylindrical, membrane-free structures composed of nine triplets of microtubules arranged in a 9-fold symmetric…
- [[chloroplast|Chloroplast]] — Chloroplasts are large, membrane-bound organelles found in plant and algal cells that convert light energy into chemical…
- [[cilia|Cilia]] — Cilia and flagella are hair-like, motile projections that extend from the cell surface and generate movement through beating…
- [[endoplasmic-reticulum|Endoplasmic reticulum]] — The endoplasmic reticulum (ER) is a vast, interconnected membrane network that synthesizes and transports proteins and lipids…
- [[golgi-apparatus|Golgi apparatus]] — The Golgi apparatus is a membrane-bound organelle that modifies, packages, and ships proteins and lipids received from the…
- [[lysosome|Lysosome]] — Lysosomes are membrane-bound organelles filled with digestive enzymes (hydrolases) that break down cellular waste, damaged…
- [[mitochondria|Mitochondria]] — Mitochondria are the membrane-bound organelles responsible for cellular respiration, converting nutrients (glucose, fatty…
- [[nucleus|Nucleus]] — The nucleus is the membrane-bound organelle that contains and protects the cell's genetic material (DNA), serving as the…
- [[ribosome|Ribosome]] — Ribosomes are non-membrane-bound cellular machines that synthesize proteins by translating messenger RNA (mRNA) into chains of…
- [[vacuole|Vacuole]] — Vacuoles are large, membrane-bound compartments that store water, nutrients, ions, pigments, and waste products in plant and…

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
