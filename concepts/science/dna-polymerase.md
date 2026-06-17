---
type: term
category: science
defines: ["DNA polymerase"]
related: ["[[dna-replication]]", "[[dna]]"]
requires: ["[[enzyme]]", "[[protein]]", "[[dna]]"]
lists: ["[[enzymes]]"]
tour_order: 2
read: false
---

# DNA polymerase


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

DNA polymerase is the primary enzyme responsible for *replicating DNA* by synthesizing new strands in the 5' to 3' direction. It catalyzes the addition of nucleotides to a growing strand, requiring a primer and functioning with high fidelity through 3' to 5' exonuclease activity that removes mismatched bases. Multiple forms exist across organisms, each specialized for different replication contexts.

## you gotta know

- Catalyzes: phosphodiester bond formation between nucleotides in the 5' → 3' direction
- Requires: a primer (short RNA or DNA segment) to initiate synthesis; cannot start chains de novo
- Substrates: dNTPs (deoxyribonucleotide triphosphates) — energy from pyrophosphate release
- Proofreading: built-in 3' to 5' exonuclease activity checks and removes mismatches, yielding ~1 error per 10^10 bases
- Processivity: varies by polymerase type; can add 1–1000+ nucleotides before dissociating
- In *E. coli*: Pol I, II, III; Pol III is main replication enzyme; Pol I fills gaps left by primer removal
- In eukaryotes: Pol α-primase (starts), Pol δ (lagging strand), Pol ε (leading strand)

## context

DNA replication demands extraordinary accuracy to preserve genetic fidelity across cell divisions. DNA polymerase emerged as evolution's solution: a machine that both reads the template strand and verifies its own work in real time. The enzyme's inability to initiate chains without a primer (a feature rather than a bug) allows cells to recognize replication boundaries and control the process. Different polymerases evolved for different tasks—Pol III runs the bulk of replication in prokaryotes, while eukaryotic replication splits labor among polymerases for efficiency and quality control.

## connections

- [[dna]] — the substrate and template for replication.
- [[dna-replication]] — the process DNA polymerase orchestrates.
- [[pcr]] — artificially harnesses DNA polymerase for exponential amplification.
- [[rna-polymerase]] — analogous enzyme for transcription using RNA nucleotides.
- [[primase]] — synthesizes the primers that DNA polymerase extends.
- [[catalysis]] — the enzyme's mechanism of bond formation.
- [[active-site]] — where polymerase binds template and substrate.

## see also

- [[rna-polymerase]] · [[reverse-transcriptase]] · [[telomerase]]

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

Lists: [[enzymes]] · Mark read: `INPUT[toggle:read]`
