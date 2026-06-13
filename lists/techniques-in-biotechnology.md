---
type: list
category: science
read: false
---

# techniques in biotechnology

The techniques in biotechnology most worth knowing for quiz bowl.

## nodes

- [[crispr|CRISPR/Cas9]] — CRISPR/Cas9 is a genome-editing tool adapted from bacterial immune systems that uses a guide RNA to direct the Cas9 nuclease…
- [[dna-sequencing|DNA Sequencing]] — DNA sequencing is the process of determining the precise order of nucleotide bases (A, T, G, C) along a DNA molecule.
- [[elisa|ELISA (Enzyme-Linked Immunosorbent Assay)]] — ELISA is a biochemical assay for detecting and quantifying specific proteins or antigens in a sample using antibody-antigen…
- [[flow-cytometry|Flow Cytometry]] — Flow cytometry is an analytical method that counts and sorts individual cells or particles based on their size, granularity,…
- [[gel-electrophoresis|Gel Electrophoresis]] — Gel electrophoresis is a separation technique that forces charged molecules (DNA, RNA, or proteins) through a porous gel…
- [[molecular-cloning|Molecular Cloning]] — Molecular cloning is the process of isolating a DNA fragment of interest, inserting it into a vector (typically a plasmid),…
- [[northern-blotting|Northern Blotting]] — Northern blotting is a molecular technique for detecting and quantifying specific RNA molecules in a sample by separating…
- [[pcr|PCR (Polymerase Chain Reaction)]] — PCR is a laboratory method for exponentially amplifying specific DNA sequences by repeatedly cycling through temperatures that…
- [[southern-blotting|Southern Blotting]] — Southern blotting is a technique for detecting specific DNA sequences in a sample by fragmenting genomic DNA (usually with…
- [[western-blotting|Western Blotting]] — Western blotting is a method for detecting, identifying, and quantifying specific proteins in a sample by separating them by…

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
