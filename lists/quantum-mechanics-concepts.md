---
type: list
category: science
read: false
---

# concepts from quantum mechanics

The concepts from quantum mechanics most worth knowing for quiz bowl.

## nodes

- [[bose-einstein-condensate|Bose–Einstein condensate]] — A Bose–Einstein condensate (BEC) is a state of matter in which a large fraction of bosonic particles occupy the same…
- [[commutator|Commutator]] — The commutator of two quantum operators Â and B̂ is defined as [Â, B̂] = ÂB̂ - B̂Â; it measures whether the two operators…
- [[quantum-operator|Operator (quantum mechanics)]] — A quantum operator is a mathematical object that acts on a wavefunction to extract or represent observable information.
- [[pauli-exclusion-principle|Pauli exclusion principle]] — The Pauli exclusion principle states that no two identical fermions can occupy the same quantum state simultaneously.
- [[quantization|Quantization]] — Quantization is the principle that physical observables—energy, angular momentum, charge—can only take on discrete, allowed…
- [[quantum-entanglement|Quantum entanglement]] — Quantum entanglement occurs when two or more particles share a [[wavefunction]] such that their quantum states are correlated…
- [[quantum-tunneling|Quantum tunneling]] — Quantum tunneling is the phenomenon where a particle penetrates a potential barrier even when its total energy is less than…
- [[schrodinger-equation|Schrödinger equation]] — The Schrödinger equation is the fundamental differential equation governing the time evolution of a wavefunction in quantum…
- [[quantum-spin|Spin]] — Spin is an intrinsic form of angular momentum carried by elementary particles—electrons, photons, quarks—that has no classical…
- [[superposition|Superposition]] — Superposition is the quantum principle that a system can exist simultaneously in multiple states or configurations, each with…
- [[uncertainty-principle|Uncertainty principle]] — The Heisenberg uncertainty principle states that certain pairs of physical observables—position and momentum, energy and…
- [[wave-particle-duality|Wave-particle duality]] — Wave-particle duality asserts that all matter and energy exhibit both wave and particle properties depending on how they are…
- [[wavefunction|Wavefunction]] — A wavefunction is a mathematical object, typically denoted ψ(r,t) or Ψ, that encodes the complete information about a quantum…

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
