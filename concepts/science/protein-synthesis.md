---
type: term
category: science
defines: ["Protein synthesis", Translation, Transcription]
related: ["[[rna]]", "[[mrna]]", "[[trna]]", "[[ribosome]]", "[[protein]]", "[[dna]]"]
requires: ["[[ribosome]]"]
lists: []
tour_order: 2
read: false
---

# Protein Synthesis


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

*Protein synthesis* is the process by which cells build proteins from amino acids, guided by genetic instructions encoded in DNA. It consists of two main stages: *transcription*, where RNA polymerase synthesizes mRNA from the DNA template; and *translation*, where ribosomes read the mRNA sequence and direct tRNA molecules to deliver amino acids in the correct order, forming a new protein chain. This process is universal across all life and is central to expressing genetic information.

## you gotta know

### Transcription
- *RNA polymerase* binds to a promoter region of DNA and synthesizes mRNA by reading the template strand in the 3' to 5' direction, building the mRNA strand 5' to 3'.
- The mRNA sequence is complementary to the template DNA strand (except uracil replaces thymine).
- In prokaryotes, transcription and translation are *coupled* — ribosomes begin translating while mRNA is still being transcribed.
- In eukaryotes, transcription occurs in the nucleus; the primary transcript (*pre-mRNA*) undergoes processing: a 5' cap and 3' poly-A tail are added, and *introns* are spliced out, leaving only *exons* in the mature mRNA.

### The Genetic Code
- The mRNA is read in codons (3-nucleotide sequences), each specifying one amino acid or a stop signal.
- There are 64 possible codons encoding 20 standard amino acids, so the code is *degenerate* — multiple codons encode the same amino acid, providing redundancy against mutations.
- The code is *universal* across almost all organisms, suggesting common evolutionary origin.
- Three codons (UAA, UAG, UGA) are stop signals; one codon (AUG) is the start signal and encodes methionine.

### Translation — Initiation
- A ribosome binds to the mRNA at the start codon (AUG); a special initiator tRNA carrying formyl-methionine (in prokaryotes) or methionine (in eukaryotes) pairs with the start codon.
- The ribosome has three tRNA-binding sites: the *A site* (aminoacyl, incoming), the *P site* (peptidyl, donor), and the *E site* (exit).

### Translation — Elongation
- An incoming tRNA molecule, charged with the amino acid corresponding to the current codon, enters the A site and base-pairs with the mRNA codon; the ribosome checks for correct pairing (*proofreading*).
- The ribosome catalyzes peptide bond formation between the growing protein chain (in the P site) and the incoming amino acid (in the A site); the rRNA is the actual catalyst.
- The ribosome translocates — moves one codon down the mRNA — shifting the tRNA from the A site to the P site and then to the E site (where it is released).
- This cycle repeats ~20 times per second in bacteria, ~2–8 times per second in eukaryotes.

### Translation — Termination
- When a stop codon (UAA, UAG, UGA) enters the A site, no tRNA matches it; instead, *release factors* recognize the stop codon and catalyze cleavage of the polypeptide from the tRNA in the P site.
- The ribosome, mRNA, and deacylated tRNA dissociate; the mRNA is recycled, and the newly synthesized protein folds (often with assistance from chaperones).

### Regulation
- Transcription can be turned on or off by *transcription factors* and chromatin remodeling.
- Translation can be regulated by the availability of tRNAs, by *microRNAs* (miRNAs) that block translation, or by other mechanisms.
- *Feedback inhibition*: if a protein product accumulates, it can inhibit transcription or translation of its own gene, preventing overproduction.

## context

Protein synthesis is the central execution of the genetic program. Every cell must synthesize thousands of different proteins, and each must be made at the right time, in the right amount, in the right place. The accuracy of the system is remarkable: the error rate in translation is ~1 per 10,000 amino acids in bacteria (one mistake per protein on average), balanced against the cost of proofreading. The discovery of mRNA and the cracking of the genetic code by Nirenberg, Matthaei, and others in the 1960s transformed biology; it showed that genetic information is written in a universal, decipherable code. Protein synthesis remains a prime target for antibiotics (many kill bacteria by blocking ribosomal function) and a frontier for synthetic biology (engineering ribosomes and tRNAs to incorporate non-standard amino acids). Understanding how cells translate DNA into proteins is essential to molecular biology, biochemistry, and modern medicine.

## connections

- [[dna]] — the source of genetic information; DNA is transcribed into RNA.
- [[rna]] — mRNA is synthesized from DNA and carries codons to the ribosome.
- [[mrna]] — the messenger molecule that specifies protein sequence.
- [[trna]] — brings amino acids to the ribosome; anticodon pairs with mRNA codon.
- [[ribosome]] — the molecular machine that catalyzes peptide bond formation during translation.
- [[protein]] — the product of protein synthesis.
- [[amino-acids]] — the substrates incorporated into the growing protein chain.
- [[rna-polymerase]] — synthesizes mRNA during transcription.
- [[genetic-code]] — the universal mapping of codons to amino acids.
- [[gene-regulation]] — controls transcription and translation rates.

## see also

- [[dna]] · [[rna]] · [[protein]] · [[ribosome]]

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
