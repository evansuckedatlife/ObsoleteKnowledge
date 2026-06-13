---
type: list
category: science
read: false
---

# Chemistry Lab Techniques

Common experimental methods and practices used to separate, purify, analyze, and quantify chemical substances.

## nodes

- [[chromatography|Chromatography]] — separates components of mixtures using a stationary phase and a mobile phase.
- [[distillation|Distillation]] — separates liquid mixtures based on differences in boiling points or volatile behaviors.
- [[titration|Titration]] — quantifies the concentration of an unknown analyte by adding a reactant of known concentration.
- [[calorimetry|Calorimetry]] — measures the heat flow and energy changes associated with chemical and physical processes.
- [[spectroscopy|Spectroscopy]] — analyzes the interaction between matter and electromagnetic radiation to determine structure and concentration.
- [[filtration|Filtration]] — separates solid particulate matter from a fluid using a porous physical barrier.
- [[centrifugation|Centrifugation]] — separates components of different densities using high-speed rotational force.
- [[recrystallization|Recrystallization]] — purifies solid organic compounds based on their temperature-dependent solubility.
- [[pipetting|Pipetting]] — transfers precise volumes of liquid reagents using volumetric, graduated, or micropipettes.
- [[electrolysis|Electrolysis]] — drives non-spontaneous redox reactions using a direct electric current.

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
