---
type: concept
category: science
defines:
  - Commutator
related: ["[[quantum-operator]]", "[[uncertainty-principle]]", "[[eigenvalue]]"]
requires: []
lists:
  - "[[quantum-mechanics-concepts]]"
tour_order: 0
read: true
---

# Commutator

## summary

The *commutator* of two *quantum operators* Â and B̂ is defined as [Â, B̂] = ÂB̂ - B̂Â; it measures whether the two operators commute (i.e., whether applying them in different orders yields the same result). A zero commutator means the observables can be simultaneously measured with arbitrary precision; a nonzero commutator signals a fundamental trade-off governed by the *uncertainty principle*.

## you gotta know

- **Definition**: [Â, B̂] = ÂB̂ - B̂Â; if [Â, B̂] = 0, the operators commute and are compatible observables
- **Incompatible observables**: nonzero [Â, B̂] implies the observables cannot both have definite values simultaneously; measurement of one disturbs the other
- **Canonical commutation relation**: [x̂, p̂] = iℏ is the bedrock of quantum mechanics; all other commutation relations follow from it
- **Spin commutation**: [Ŝᵢ, Ŝⱼ] = iℏ εᵢⱼₖ Ŝₖ; the three spin components do not commute, so spin along different axes cannot be simultaneously measured
- **Shared eigenbasis**: if [Â, B̂] = 0, the operators have a common set of eigenstates; simultaneous measurement yields well-defined pairs of eigenvalues
- **Anticommutator**: {Â, B̂} = ÂB̂ + B̂Â is sometimes used; in fermion algebras (Grassmann variables), anticommutation reflects *Pauli exclusion principle*
- **Poisson bracket analog**: commutators are the quantum version of Poisson brackets in classical mechanics; [Â, B̂] ↔ {A, B}_PB/iℏ

## context

Commutators are central to the structure of quantum mechanics, encoding the non-classical behavior of nature. The fact that [x̂, p̂] = iℏ (not zero) was the key insight that forced physicists in the 1920s to abandon the idea that a particle has both a definite position and momentum. Werner Heisenberg's *uncertainty principle* is a direct consequence: Δx Δp ≥ ℏ/2 follows from the non-zero commutator. In more abstract terms, commutation relations define the algebra of a quantum system; different algebras correspond to different physical systems. Lie algebras (where [, ] is antisymmetric) govern symmetries and conservation laws. The vanishing or nonvanishing of a commutator is not merely a computational detail—it determines what can and cannot be known about a system.

## connections

- [[quantum-operator]] — commutators are defined between operators; they determine operator compatibility and simultaneous measurability
- [[uncertainty-principle]] — the uncertainty relation ΔÂ ΔB̂ ≥ |⟨[Â, B̂]⟩|/2 is a direct consequence of nonzero commutators
- [[eigenvalue]] — if [Â, B̂] = 0, Â and B̂ share eigenstates; measuring both yields well-defined eigenvalue pairs
- [[hamiltonian]] — the *Hamiltonian* Ĥ commutes with itself; [Ĥ, Ĥ] = 0 ensures energy is conserved, and eigenstates of Ĥ are stationary states
- [[quantum-spin]] — spin operators exhibit the canonical commutation algebra; [Ŝᵢ, Ŝⱼ] encodes angular momentum addition rules
- [[schrodinger-equation]] — rewritten as i ℏ dÂ/dt = [Â, Ĥ], it relates operator time-evolution to commutation with the *Hamiltonian*
- [[pauli-exclusion-principle]] — fermionic creation/annihilation operators satisfy anticommutation relations {â, â†} = 1, enforcing the exclusion principle

## see also

- [[quantization]] · [[hilbert-space]] · [[werner-heisenberg]]

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
