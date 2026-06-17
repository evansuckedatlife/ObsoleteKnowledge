---
type: concept
category: science
defines: ["Pauli exclusion principle"]
related: ["[[quantum-spin]]", "[[fermion]]", "[[wavefunction]]"]
requires: ["[[quantum-mechanics]]"]
lists: ["[[quantum-mechanics-concepts]]"]
tour_order: 1
read: false
---

# Pauli exclusion principle


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The Pauli exclusion principle states that no two identical *fermions* can occupy the same *quantum state* simultaneously. This foundational constraint explains why matter has *bulk*, why atoms don't collapse, and why electrons fill atomic shells in discrete layers rather than all crowding the ground state.

## you gotta know

- **Core statement**: Two identical fermions cannot share all four quantum numbers (*n*, *l*, *m_l*, *m_s*)
- **Fermions vs. bosons**: applies only to fermions (electrons, protons, neutrons, quarks); *bosons* (photons, gluons) can occupy the same state
- **Spin antisymmetry**: the total *wavefunction* must be antisymmetric under particle exchange; spatial part may be symmetric if spin part is antisymmetric, and vice versa
- **Shell structure**: electrons fill atomic orbitals level-by-level because once an orbital is "full," the next electron must jump to a higher energy level—this creates chemistry
- **Degeneracy pressure**: in matter, fermions resist compression; as density increases, available quantum states fill up and the system must go to higher energies, creating outward pressure; crucial in neutron stars and white dwarfs
- **Consequences**: periodic table structure, electrical conductivity, magnetism, and the stability of ordinary matter

## context

Wolfgang Pauli proposed this principle in 1925, initially to explain the structure of atomic spectra. Unlike Coulomb repulsion (which *pushes* electrons apart electromagnetically), the exclusion principle is a purely quantum mechanical effect—it emerges from the requirement that the total wavefunction be antisymmetric under particle exchange. This is intimately tied to *quantum-spin*: an electron's spin state is part of its complete quantum description. The principle is not a force in the classical sense; rather, it is a constraint on the set of allowed *quantum states* that a system of identical particles can occupy. This mathematical structure underpins the entire edifice of atomic physics, materials science, and the existence of stable, large-scale matter.

## connections

- [[quantum-spin]] — spin labels one of the four quantum numbers; the antisymmetry requirement links spin and spatial wavefunction symmetry
- [[fermion]] — electrons and quarks are fermions; the principle defines their collective behavior
- [[wavefunction]] — the principle is expressed as a requirement on wavefunction symmetry under particle exchange
- [[quantum-operator]] — occupation numbers and creation/annihilation operators in second quantization directly encode the exclusion principle
- [[schrodinger-equation]] — multi-particle solutions must respect antisymmetry; this constrains which solutions are physical
- [[uncertainty-principle]] — related: the exclusion principle can be understood as a consequence of position–momentum uncertainty pushing particles apart in phase space
- [[standard-model]] — fermions in the Standard Model (quarks, leptons) are subject to Pauli exclusion; bosons mediate forces

## see also

- [[quantum-entanglement]] · [[hilbert-space]] · [[erwin-schrodinger]]

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

Lists: [[quantum-mechanics-concepts]] · Mark read: `INPUT[toggle:read]`
