---
type: list
category: science
read: false
---

# Science hubs

Foundational structures, laws and systems the specific science nodes build on.

## nodes

- [[active-transport|Active Transport]] — Active transport is the cellular process of moving molecules across the cell membrane against their concentration gradient, from low to high concentra…
- [[alpha-particle|Alpha Particle]] — An alpha particle is a helium-4 nucleus consisting of two protons and two neutrons bound together, ejected from certain radioactive atoms during decay.
- [[angular-momentum|Angular Momentum]] — Angular momentum is the rotational analog of linear momentum—a conserved quantity measuring how much an object or system is rotating and how resistant…
- [[antimatter|Antimatter]] — Antimatter is the counterpart to ordinary matter, composed of antiparticles—particles with identical mass but opposite charge and quantum numbers to t…
- [[asaph-hall|Asaph Hall]] — Asaph Hall (1829–1907) was an American astronomer who discovered the two moons of Mars, Phobos and Deimos, in 1877 at the U.S.
- [[astrobiology|Astrobiology]] — Astrobiology is the multidisciplinary study of the conditions, origins, and distribution of life in the universe beyond Earth.
- [[asymptotic-freedom|Asymptotic Freedom]] — Asymptotic freedom is a property of quantum chromodynamics (QCD) in which the strength of the strong nuclear force between quarks decreases as they ar…
- [[atmosphere|Atmosphere]] — An atmosphere is a layer of gases surrounding a planet or moon, held in place by gravity.
- [[bacteriology|Bacteriology]] — Bacteriology is the branch of microbiology that studies bacteria—their structure, growth, reproduction, physiology, and role in human health and disea…
- [[birds|Birds]] — Birds (class Aves) are feathered, egg-laying vertebrates descended from theropod dinosaurs, representing a living lineage that survived the Cretaceous…
- [[buzz-aldrin|Buzz Aldrin]] — Buzz Aldrin (born 1930) is an American former astronaut and engineer who was the second person to walk on the Moon during Apollo 11 on July 21, 1969, …
- [[cancer|Cancer]] — Cancer is a disease characterized by uncontrolled cell growth and division resulting from mutations that disable tumor suppressors and activate oncoge…
- [[cell-cycle|Cell Cycle]] — The cell cycle is the regulated sequence of events by which a cell grows, replicates its DNA, and divides into daughter cells.
- [[cell-division|Cell Division]] — Cell division is the process by which a parent cell separates into two or more daughter cells, accomplished through mitosis (for somatic cells) or mei…
- [[chlorine|Chlorine]] — Chlorine (element 17, Cl) is a highly reactive halogen gas used extensively in industrial chemistry, disinfection, and everyday products.
- [[chromosome|Chromosome]] — Chromosomes are compact, thread-like structures made of tightly coiled DNA and proteins that package and organize a cell's genetic material.
- [[circuit-topology|Circuit Topology]] — Circuit topology describes the way components in an electrical circuit are connected — how nodes link together, which elements are in series or parall…
- [[codon|Codon]] — Codons are three-nucleotide sequences on messenger RNA (mRNA) that specify which amino acid should be added during protein synthesis, or signal the st…
- [[color-charge|Color Charge]] — Color charge is an abstract quantum property analogous to electric charge that quarks and gluons possess in quantum chromodynamics (QCD), the theory o…
- [[current-limiting|Current Limiting]] — Current limiting is the practice of restricting the maximum electrical current flowing through a component or circuit to safe levels, preventing damag…
- [[data-structure|Data Structure]] — Data structures are organized formats for storing and accessing data in memory, designed to enable efficient operations like searching, insertion, and…
- [[dna-ligase|DNA Ligase]] — DNA ligase is an enzyme that catalyzes the formation of phosphodiester bonds between the sugar-phosphate backbone of adjacent DNA fragments.
- [[electromagnetism|Electromagnetism]] — Electromagnetism is the unified theory of electricity and magnetism, formalized by James Clerk Maxwell in the 1860s.
- [[energy|Energy]] — Energy is the capacity of a system to do work or undergo change.
- [[gemstone|Gemstone]] — Gemstones are minerals or rocks prized for their beauty, rarity, and durability, commonly used in jewelry and ornamentation.
- [[gene|Gene]] — Genes are discrete functional units of DNA that encode instructions for building proteins or producing RNA molecules that cells need to function.
- [[gene-regulation|Gene Regulation]] — Gene regulation is the process by which cells control when, where, and how frequently genes are expressed, turning transcription and translation on or…
- [[genetics|Genetics]] — Genetics is the science of inheritance — how traits pass from parents to offspring and how variation arises within populations.
- [[hamiltonian|Hamiltonian]] — The Hamiltonian (denoted Ĥ) is the fundamental quantum mechanical operator representing the total energy of a system—kinetic plus potential energy.
- [[international-space-station|International Space Station]] — The International Space Station (ISS) is a modular research laboratory in low Earth orbit, continuously inhabited since November 2000.
- [[magnetic-field|Magnetic Field]] — A magnetic field is a vector field that exerts a force on moving electric charges and magnetic dipoles, analogous to how an electric field acts on sta…
- [[measurement|Measurement]] — In quantum mechanics, measurement refers to the act of observing or extracting information from a quantum system, which fundamentally alters its state.
- [[mutation|Mutation]] — A mutation is a permanent alteration in the DNA sequence of an organism, affecting one or more nucleotides.
- [[proton|Proton]] — Proton is a positively charged subatomic particle and one of the two main constituents of the atomic nucleus.
- [[scoville-scale|Scoville Scale]] — The Scoville scale is a measurement of the pungency (spiciness) of hot peppers and spicy foods, quantified in Scoville Heat Units (SHU).
- [[solar-system|Solar System]] — The Solar System is the gravitationally bound system comprising the Sun and all objects that orbit it, including eight major planets, their moons, ast…
- [[subsurface-ocean|Subsurface Ocean]] — A subsurface ocean is a body of liquid water hidden beneath the solid icy crust of a moon or planetary body.
- [[thermodynamics|Thermodynamics]] — Thermodynamics is the physics of heat, work, and energy transformation in macroscopic systems.
- [[trna|tRNA]] — Transfer RNA (tRNA) is a small RNA molecule that delivers amino acids to the ribosome during protein-synthesis.
- [[volcano|Volcano]] — A volcano is a geological opening in Earth's crust through which molten rock (magma), ash, gases, and rock fragments erupt onto the surface.

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
