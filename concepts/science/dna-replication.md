---
type: term
category: science
defines: ["DNA replication", "semiconservative replication"]
related: ["[[dna]]", "[[dna-polymerase]]", "[[cell-cycle]]", "[[mitosis]]", "[[dna-helicase]]"]
requires: ["[[dna]]", "[[enzyme]]"]
lists: []
tour_order: 2
read: false
---

# DNA Replication


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

*DNA replication* is the process by which a cell duplicates its entire genome before cell division. The two strands of the DNA double helix separate, and each serves as a template for a new complementary strand, producing two identical DNA molecules — each containing one original strand and one newly synthesized strand. This *semiconservative* mechanism ensures high fidelity and allows each daughter cell to inherit an exact copy of the parent's genetic code.

## you gotta know

### The Semiconservative Mechanism
- The double helix unwinds; the two strands separate and each serves as a template for a new complementary strand.
- Result: two DNA molecules, each with one original (parental) strand and one new strand — the hallmark of semiconservative replication.
- This was proven by *Meselson and Stahl* in 1958 using nitrogen isotopes to track parental vs. newly synthesized strands.
- The mechanism ensures fidelity: mispairing or errors are rare because the template strand enforces correct base pairing.

### Key Machinery
- *DNA helicase* unwinds the double helix, breaking hydrogen bonds between base pairs and creating a replication fork.
- *Primase* synthesizes short RNA primers (~10 nucleotides), required because DNA polymerase cannot initiate synthesis de novo.
- *DNA polymerase III* (in prokaryotes) or *Pol ε and Pol δ* (in eukaryotes) catalyzes phosphodiester bond formation, adding nucleotides in the 5' to 3' direction.
- *DNA ligase* seals nicks between Okazaki fragments and primers to produce a continuous strand.
- *Topoisomerase* relieves tension created by unwinding, preventing the molecule from supercoiling into a knot.

### The Leading and Lagging Strands
- The *leading strand* is synthesized continuously in the 5' to 3' direction (same direction as helicase movement) by a single polymerase.
- The *lagging strand* runs 3' to 5' relative to helicase motion, so it is synthesized discontinuously as short *Okazaki fragments* (1000–2000 nucleotides in eukaryotes, 1000–2000 in prokaryotes), each with its own primer.
- Primers are later removed and gaps filled by polymerase; DNA ligase seals the fragments into a continuous strand.

### Timing and Regulation
- Replication occurs during the *S phase* (synthesis phase) of the cell cycle in eukaryotes.
- Multiple replication origins (in eukaryotes, ~50,000 to 100,000) ensure the entire genome is replicated in ~8 hours; prokaryotes typically have one origin.
- *Checkpoint controls* monitor replication fidelity and completeness; if errors are detected, the cell cycle halts or apoptosis is triggered.

### Accuracy and Error Correction
- DNA polymerase has 3' to 5' exonuclease activity (proofreading), removing mismatched nucleotides; error rate ~1 per 10^10 bases.
- *Mismatch repair* systems correct errors that escape proofreading, reducing overall error rate to ~1 per 10^10 bases per cell division.
- Despite high fidelity, replication errors accumulate over many divisions, contributing to mutation and evolution.

## context

DNA replication is one of the most accurate and complex processes in the cell. Its fidelity is essential: errors in replication can lead to mutations that cause cancer, genetic diseases, or cell death. The process involves dozens of proteins working in concert, and its regulation is intricately tied to the cell cycle — cells don't divide unless DNA is completely and accurately replicated. Understanding replication has been central to molecular biology since the discovery of the double helix; Meselson and Stahl's elegant isotope experiment remains one of biology's most beautiful proofs. DNA replication also underpins biotechnology: PCR artificially harnesses the replication machinery to amplify DNA exponentially, making replication a cornerstone of molecular diagnostics, forensics, and genetic engineering.

## connections

- [[dna]] — the substrate and target of replication.
- [[dna-polymerase]] — catalyzes the synthesis of new DNA strands.
- [[dna-helicase]] — unwinds the double helix to expose the template.
- [[primase]] — synthesizes the RNA primers that initiate synthesis.
- [[dna-ligase]] — seals the nicks between DNA fragments.
- [[cell-cycle]] — replication occurs during S phase; checkpoint controls ensure accuracy.
- [[mitosis]] — follows DNA replication to distribute copies to daughter cells.
- [[mutation]] — errors in replication, despite high fidelity, are a source of mutations.
- [[pcr]] — artificially harnesses replication machinery for exponential DNA amplification.

## see also

- [[dna]] · [[dna-polymerase]] · [[cell-cycle]] · [[mutation]]

<!-- crosslinks -->
```dataviewjs
dv.view("_dv/crosslinks")
```
<!-- /crosslinks -->

<!-- tournav -->
```dataviewjs
dv.view("_dv/tournav")
```
<!-- /tournav -->

<!-- footer -->

---

Lists: Mark read: `INPUT[toggle:read]`
