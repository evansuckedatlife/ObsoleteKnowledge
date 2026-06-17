---
type: list
category: science
read: false
---

# enzymes

The enzymes most worth knowing for quiz bowl.

## nodes

- [[amylase|Amylase]] — Amylase is a carbohydrate-digesting enzyme that catalyzes the hydrolysis of glycosidic bonds in starch and related…
- [[atp-synthase|ATP synthase]] — ATP synthase is a molecular turbine that harnesses proton gradients across membranes to drive ATP synthesis from ADP and…
- [[cas9|Cas9]] — Cas9 is an RNA-guided nuclease from the bacterial immune system that cleaves DNA at specific sequences defined by a guide RNA.
- [[catalase|Catalase]] — Catalase is an antioxidant enzyme found in nearly all aerobic organisms that catalyzes the rapid decomposition of hydrogen…
- [[dna-polymerase|DNA polymerase]] — DNA polymerase is the primary enzyme responsible for replicating DNA by synthesizing new strands in the 5' to 3' direction.
- [[pepsin|Pepsin]] — Pepsin is a serine protease secreted in the stomach that catalyzes the hydrolysis of peptide bonds in proteins, initiating…
- [[restriction-enzyme|Restriction enzyme]] — Restriction enzymes are bacterial nucleases that recognize and cleave DNA at specific palindromic sequences, typically 4–8 bp…
- [[reverse-transcriptase|Reverse transcriptase]] — Reverse transcriptase is an unusual polymerase that synthesizes DNA from an RNA template—the reverse of normal transcription.
- [[rna-polymerase|RNA polymerase]] — RNA polymerase catalyzes transcription—the synthesis of RNA from a DNA template strand in the 5' to 3' direction.
- [[rubisco|RuBisCO]] — RuBisCO (ribulose-1,5-bisphosphate carboxylase/oxygenase) is the most abundant enzyme on Earth and catalyzes the first…
- [[telomerase|Telomerase]] — Telomerase is a specialized reverse transcriptase that extends chromosome ends (telomeres) by repeatedly adding tandem DNA…

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
