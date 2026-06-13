---
type: list
category: science
read: false
---

# animal phyla

The animal phyla most worth knowing for quiz bowl.

## nodes

- [[annelida|Annelida]] — A phylum of invertebrate segmented worms including earthworms, leeches, and marine bristle worms, Annelida are coelomate…
- [[arthropoda|Arthropoda]] — Accounting for over 80% of all described animal species, Arthropoda is the largest and most ecologically diverse phylum on Earth.
- [[chordata|Chordata]] — Comprising all vertebrates (mammals, birds, reptiles, amphibians, and fish) alongside two invertebrate subphyla, Chordata is a…
- [[cnidaria|Cnidaria]] — A phylum of radially symmetrical aquatic animals including jellyfish, corals, sea anemones, and hydras, Cnidaria are…
- [[ctenophora|Ctenophora]] — A phylum of marine invertebrates commonly known as comb jellies, Ctenophora are characterized by rows of cilia that they use…
- [[echinodermata|Echinodermata]] — A phylum of marine deuterostomes including starfish, sea urchins, sand dollars, and sea cucumbers, Echinodermata are…
- [[mollusca|Mollusca]] — Comprising soft-bodied animals such as snails, clams, squids, and octopuses, Mollusca is the second-largest phylum of…
- [[nematoda|Nematoda]] — A highly diverse phylum of unsegmented, cylindrical invertebrates known as roundworms, Nematoda are pseudocoelomate protostomes.
- [[platyhelminthes|Platyhelminthes]] — A phylum of bilaterally symmetrical, unsegmented invertebrates known as flatworms, Platyhelminthes are acoelomate triploblasts.
- [[porifera|Porifera]] — An ancient phylum of aquatic multicellular organisms commonly known as sponges, Porifera are characterized by a lack of true…

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
