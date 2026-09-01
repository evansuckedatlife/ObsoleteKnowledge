---
type: list
category: science
read: false
---

# Science hubs

Foundational structures, laws and systems the specific science nodes build on.

## nodes

- [[antimatter|Antimatter]] — Antimatter is the counterpart to ordinary matter, composed of antiparticles—particles with identical mass but opposite charge and quantum numbers to t…
- [[astrobiology|Astrobiology]] — Astrobiology is the multidisciplinary study of the conditions, origins, and distribution of life in the universe beyond Earth.
- [[cell-cycle|Cell Cycle]] — The cell cycle is the regulated sequence of events by which a cell grows, replicates its DNA, and divides into daughter cells.
- [[current-limiting|Current Limiting]] — Current limiting is the practice of restricting the maximum electrical current flowing through a component or circuit to safe levels, preventing damag…
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
