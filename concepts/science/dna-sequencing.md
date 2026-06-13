---
type: practice
category: science
defines: [DNA sequencing, "gene sequencing"]
related: ["[[dna]]", "[[pcr]]", "[[gel-electrophoresis]]", "[[sanger-sequencing]]", "[[next-generation-sequencing]]"]
lists: ["[[techniques-in-biotechnology]]"]
read: false
---

# DNA Sequencing

## summary

**DNA sequencing** is the process of determining the precise order of nucleotide bases (A, T, G, C) along a DNA molecule. Modern sequencing underpins genomics, diagnostics, and evolutionary studies, with methods ranging from *Sanger sequencing* (single molecules, gold standard) to *next-generation sequencing* (millions of reads in parallel).

## you gotta know

- *Sanger sequencing* — the original method (1977); uses chain-terminating nucleotides (ddNTPs) to halt DNA synthesis at each base, generating a ladder of fragments differing by one base that are separated by gel or capillary electrophoresis.
- *Next-generation sequencing (NGS)* — massively parallel; DNA is fragmented, amplified on a chip or bead, and millions of reads are generated simultaneously, enabling whole-genome sequencing at lower cost per base.
- *Read length* matters — Sanger yields long, accurate reads (~1000 bp); NGS short-reads (~100–300 bp) or long-reads (10,000+ bp in newer tech) each suit different applications.
- *De novo assembly* — short reads from NGS must be computationally stitched together to reconstruct the original genome; existing reference genomes speed this step.
- *Error rates* — Sanger is ~1 error per 10,000 bases; NGS error rates vary by platform but are offset by coverage depth (reading the same region multiple times).
- Common for variant discovery, pathogen identification, cancer genomics, and microbiome studies.

## connections

- [[dna]] — the molecule being sequenced.
- [[pcr]] — typically used to amplify templates before sequencing.
- [[gel-electrophoresis]] — classical method for resolving Sanger sequencing ladder fragments.
- [[dna-polymerase]] — the enzyme that extends the DNA strand during sequencing reactions.
- [[human-genome-project]] — landmark effort that drove sequencing technology innovation.

## see also

- [[pcr]] · [[gel-electrophoresis]] · [[dna]]

<!-- footer -->

---

Lists: [[techniques-in-biotechnology]] · Mark read: `INPUT[toggle:read]`
