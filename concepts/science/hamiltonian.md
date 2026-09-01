---
type: concept
category: science
defines: [Hamiltonian, Hamiltonian operator]
related: ["[[quantum-operator]]", "[[schrodinger-equation]]", "[[eigenvalue]]", "[[energy]]", "[[commutator]]"]
requires: ["[[quantum-mechanics]]", "[[wavefunction]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Hamiltonian

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Hamiltonian** (denoted Ĥ) is the fundamental quantum mechanical operator representing the total energy of a system—kinetic plus potential energy. In quantum mechanics, the Hamiltonian governs time evolution via the *Schrödinger equation* and its eigenvalues yield the permissible energy levels. Understanding the Hamiltonian is central to solving any quantum problem, from the hydrogen atom to condensed-matter systems.

## you gotta know

- The Hamiltonian is a linear operator acting on the wavefunction; its form depends on the specific system (different Hamiltonians describe atoms, molecules, fields, etc.).
- The time-independent Schrödinger equation Ĥ|ψ⟩ = *E*|ψ⟩ is an eigenvalue equation where the Hamiltonian acts on eigenstates to yield energy eigenvalues—the measurable energy levels.
- Classical Hamiltonian mechanics in physics is reformulated quantum mechanically: classical variables become operators, and the classical Hamiltonian *H* (*p*, *q*) becomes the operator Ĥ by canonical quantization.
- The Hamiltonian for a particle in a box is Ĥ = *p*² / (2*m*), where *p* is momentum and *m* is mass; its eigenstates are standing waves with discrete energy levels.
- For hydrogen, the Hamiltonian includes kinetic energy of the electron and the Coulomb potential energy due to the nucleus; solving Ĥ|ψ⟩ = *E*|ψ⟩ yields orbitals and energy levels matching observation.
- Time evolution under a Hamiltonian is unitary: the time-dependent Schrödinger equation i*ℏ* d|ψ⟩/d*t* = Ĥ|ψ⟩ governs how quantum states change.
- The commutator [Ĥ, *O*] determines whether an observable *O* is conserved: if [Ĥ, *O*] = 0, the observable's expectation value is time-independent (a symmetry of the system).

## connections

- [[schrodinger-equation]] — the fundamental equation in which the Hamiltonian appears and governs quantum dynamics.
- [[quantum-operator]] — the broader category of quantum observables; the Hamiltonian is the energy operator.
- [[eigenvalue]] — the energy levels are eigenvalues of the Hamiltonian operator.
- [[commutator]] — used to assess whether quantities commute with the Hamiltonian and hence are conserved.
- [[quantum-mechanics]] — the framework in which the Hamiltonian is the central operator.
- [[energy]] — the physical quantity the Hamiltonian represents.

## see also

- [[schrodinger-equation]] · [[quantum-operator]] · [[eigenvalue]] · [[quantum-mechanics]]

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

Lists: [[science-hubs]] · Mark read: `INPUT[toggle:read]`
