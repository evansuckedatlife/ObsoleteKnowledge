---
type: term
category: science
defines: ["Cas9", "CRISPR-Cas9"]
related: ["[[crispr]]", "[[dna]]"]
lists: ["[[enzymes]]"]
read: false
---

# Cas9

## summary

Cas9 is an RNA-guided nuclease from the bacterial immune system that cleaves DNA at specific sequences defined by a guide RNA. It has been adapted into a transformative gene-editing tool that precisely targets and cuts DNA for therapeutic and research applications.

## you gotta know

- Catalyzes: double-strand DNA cleavage 3–4 bp upstream of a PAM (protospacer adjacent motif, typically NGG in *Streptococcus pyogenes*)
- Guide RNA: synthetic 20 bp RNA sequence (CRISPR RNA, crRNA) directs Cas9 to specific genomic targets with perfect complementarity
- Mechanism: Cas9 searches DNA, unwinds it locally, and tests Watson-Crick base pairing; only when PAM is adjacent and guide RNA matches does the nuclease domain become active and cut both strands
- Cleavage products: blunt or sticky ends depending on variant; activates cellular DNA repair pathways
- Cell repair: non-homologous end joining (NHEJ) causes mutations and gene disruption; homology-directed repair (HDR) can insert new sequences
- CRISPR origin: bacterial defense against phages; invading DNA is incorporated as RNA guides to prevent future infection
- Delivery: requires methods to introduce Cas9 protein and guide RNA into cells (viral vectors, electroporation, nanoparticles)

## context

Cas9 revolutionized genetic engineering by providing a programmable, precise, and relatively simple way to edit the genome. Prior techniques (zinc-finger nucleases, TALENs) required protein engineering for each new target; Cas9 needs only a new 20 bp RNA guide. The technology's power lies in this programmability and its origin—it hijacks a natural bacterial immune system, proving that robust nuclease systems already exist in nature. Cas9 has enabled disease modeling, functional genomics at scale, and therapeutic applications including sickle cell and beta-thalassemia treatments now in clinical use. Ongoing refinements (high-fidelity variants, smaller orthologs, prime editing) further expand its capabilities and safety.

## connections

- [[crispr]] — the immune system from which Cas9 derives.
- [[dna]] — the substrate Cas9 cleaves.
- [[dna-polymerase]] — fills in gaps after Cas9 cleavage during HDR-mediated repair.
- [[restriction-enzyme]] — similarly cuts DNA at specific sequences; lacks guide RNA targeting.
- [[catalysis]] — the nuclease mechanism; metal ions (Mg²⁺) facilitate catalysis.

## see also

- [[crispr]] · [[restriction-enzyme]] · [[dna]]

<!-- footer -->

---

Lists: [[enzymes]] · Mark read: `INPUT[toggle:read]`
