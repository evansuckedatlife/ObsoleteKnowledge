---
type: list
category: science
read: false
---

# Animal Phyla

The primary taxonomic divisions of the animal kingdom, categorized by their structural body plans, embryonic development, and evolutionary histories.

## nodes

- [[porifera|Porifera]] — sponges; primitive sessile organisms lacking true tissues and organs, characterized by choanocytes.
- [[cnidaria|Cnidaria]] — jellyfish, corals, and anemones; characterized by stinging cnidocytes and alternating polyp/medusa stages.
- [[ctenophora|Ctenophora]] — comb jellies; marine invertebrates that move using comb rows of cilia and capture prey using sticky colloblasts.
- [[platyhelminthes|Platyhelminthes]] — flatworms; acoelomate triploblasts lacking circulatory systems, relying on diffusion.
- [[nematoda|Nematoda]] — roundworms; pseudocoelomates covered by a thick collagen cuticle that undergoes ecdysis.
- [[annelida|Annelida]] — segmented worms; coelomates characterized by body segments (metamerism) and chitinous setae.
- [[mollusca|Mollusca]] — snails, clams, and octopuses; characterized by a mantle, muscular foot, and rasping radula.
- [[arthropoda|Arthropoda]] — insects, arachnids, and crustaceans; characterized by a chitinous exoskeleton, segmented bodies, and jointed appendages.
- [[echinodermata|Echinodermata]] — starfish, sea urchins, and cucumbers; characterized by pentaradial symmetry and a water vascular system.
- [[chordata|Chordata]] — vertebrates, tunicates, and lancelets; defined by a notochord, dorsal hollow nerve cord, pharyngeal slits, and post-anal tail.

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
