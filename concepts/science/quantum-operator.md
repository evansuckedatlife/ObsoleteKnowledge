---
type: concept
category: science
defines: ["Operator (quantum mechanics)", "operator"]
related: ["[[eigenvalue]]", "[[hamiltonian]]", "[[commutator]]"]
lists: ["[[quantum-mechanics-concepts]]"]
read: false
---

# Operator (quantum mechanics)

## summary

A *quantum operator* is a mathematical object that acts on a *wavefunction* to extract or represent observable information. Operators correspond to physical quantities (position, momentum, energy, angular momentum); when an operator acts on an eigenstate of that operator, it returns the eigenvalue—the observed value in a measurement. Operators are the bridge between the abstract wavefunction and measurable reality.

## you gotta know

- **Definition**: an operator  maps a wavefunction to another wavefunction; written as Â, Ô, etc., acting via Â ψ = φ
- **Observable and Hermitian**: operators corresponding to measurable quantities must be *Hermitian* (self-adjoint); this ensures eigenvalues are real and eigenstates form an orthonormal basis
- **Eigenvalue equation**: Â ψ_n = a_n ψ_n; if a measurement of Â is performed on ψ_n, the result is always a_n; eigenstates are the "eigenbases" for that observable
- **Common operators**: position x̂, momentum p̂ = -iℏ d/dx, kinetic energy T̂ = p̂²/2m, potential V̂(x), *Hamiltonian* Ĥ = T̂ + V̂ (total energy)
- **Commutation relations**: [Â, B̂] = AB - BA determines whether two observables can be simultaneously measured; [x̂, p̂] = iℏ is fundamental
- **Measurement outcome**: if ψ is a superposition of eigenstates, measurement yields one eigenvalue with probability given by the coefficient squared; the wavefunction then "collapses" to that eigenstate
- **Observables and expectation value**: ⟨Â⟩ = ∫ ψ* Â ψ d³r is the average outcome over many measurements

## context

Operators formalize the correspondence between mathematical objects (wavefunctions) and physical measurements. In the 1920s, Werner Heisenberg and Erwin Schrödinger developed operator formalisms (matrix mechanics and wave mechanics, respectively) that turned out to be mathematically equivalent. The *commutator* between operators reveals fundamental constraints—for instance, the fact that [x̂, p̂] ≠ 0 encodes the *uncertainty principle*. Operators are not merely computational tools; they encode the structure of quantum mechanics itself. The choice of which observable to measure is represented by which operator to apply, and the *spectrum* of eigenvalues is the set of possible outcomes.

## connections

- [[eigenvalue]] — measurement of an observable yields one of its eigenvalues; eigenstates correspond to definite measurement outcomes
- [[hamiltonian]] — the energy operator; its eigenvalues are the energy levels of the system, and its eigenspaces govern *Schrödinger equation* solutions
- [[commutator]] — [Â, B̂] quantifies whether two observables are compatible; vanishing commutator means simultaneous measurement is possible
- [[wavefunction]] — operators act on wavefunctions; the *Schrödinger equation* is an operator equation
- [[schrodinger-equation]] — iℏ ∂ψ/∂t = Ĥ ψ; the *Hamiltonian* operator drives time evolution
- [[uncertainty-principle]] — arises from non-zero commutators between conjugate observables (position–momentum, energy–time)
- [[quantum-spin]] — spin operators Ŝₓ, Ŝᵧ, Ŝz act on spin states; their commutation relations are [Ŝᵢ, Ŝⱼ] = iℏ εᵢⱼₖ Ŝₖ

## see also

- [[quantization]] · [[hilbert-space]] · [[werner-heisenberg]]

<!-- footer -->

---

Lists: [[quantum-mechanics-concepts]] · Mark read: `INPUT[toggle:read]`
