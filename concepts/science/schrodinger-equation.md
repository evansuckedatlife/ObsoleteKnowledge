---
type: concept
category: science
defines: ["Schrödinger equation"]
related: ["[[wavefunction]]", "[[hamiltonian]]", "[[quantum-operator]]"]
lists: ["[[quantum-mechanics-concepts]]"]
read: false
---

# Schrödinger equation

## summary

The *Schrödinger equation* is the fundamental differential equation governing the time evolution of a *wavefunction* in quantum mechanics. In its time-dependent form, iℏ ∂ψ/∂t = Ĥ ψ, it is the quantum analog of Newton's laws; the time-independent version determines the *energy levels* of a system and is solved to find stationary states with definite energy.

## you gotta know

- **Time-dependent form**: iℏ ∂ψ/∂t = Ĥ ψ; describes how ψ(r,t) evolves, given the *Hamiltonian* Ĥ (total energy operator)
- **Time-independent form**: Ĥ ψ(r) = E ψ(r); an eigenvalue equation; solutions are stationary states with definite energy E; ψ_E(r,t) = ψ(r) e^(−iEt/ℏ)
- **Deterministic evolution**: the equation is fully deterministic between measurements; given ψ at t=0 and knowing Ĥ, the future ψ(t) is completely determined
- **Reversible**: the equation is unitary and reversible; time-reversal symmetry holds (with caveats for open systems and decoherence)
- **Hamiltonian structure**: Ĥ = −ℏ²/(2m) ∇² + V(r) combines kinetic energy (∇² term) and potential energy V(r); solving it requires knowing V
- **Boundary conditions**: ψ must vanish (or stay finite) at infinity; normalization ∫|ψ|² = 1 further constrains solutions
- **Physical interpretation**: energy eigenvalues are the only outcomes of energy measurement; a superposition collapses to one eigenstate upon measurement

## context

Erwin Schrödinger derived this equation in 1926, providing the wave-mechanical formulation of quantum mechanics (equivalent to Heisenberg's matrix mechanics). It is not derived from first principles but rather postulated as a fundamental law of nature. The equation works brilliantly for non-relativistic particles; a relativistic version (the *Dirac equation*) extends it to high-speed particles and incorporates spin. The *Schrödinger equation* is reversible, yet quantum measurements appear irreversible—this is the *measurement problem*, unresolved today. The equation assumes the Hamiltonian is time-independent; if V changes with time, perturbation theory or other techniques become necessary. Despite its age (nearly 100 years), the *Schrödinger equation* remains the workhorse of atomic, molecular, and condensed-matter physics.

## connections

- [[wavefunction]] — the *Schrödinger equation* is an operator equation acting on ψ; its solutions are the allowed wavefunctions
- [[hamiltonian]] — the energy operator Ĥ determines the dynamics; its eigenvalues and eigenstates directly solve the time-independent version
- [[quantum-operator]] — the equation is written in terms of operators (kinetic and potential); solving it requires operator algebra
- [[eigenvalue]] — energy eigenvalues of Ĥ are the allowed energy levels; eigenstates are stationary states with definite energy
- [[commutator]] — the equation can be rewritten as i ℏ dÂ/dt = [Â, Ĥ], relating operator time-evolution to commutation with Ĥ
- [[uncertainty-principle]] — the equation's solutions reflect the trade-off between position and momentum uncertainty encoded in [x̂, p̂] = iℏ
- [[quantum-spin]] — a relativistic extension (Dirac equation) incorporates spin naturally; the non-relativistic *Schrödinger equation* treats spin separately

## see also

- [[paul-dirac]] · [[superposition]] · [[quantization]] · [[erwin-schrodinger]]

<!-- footer -->

---

Lists: [[quantum-mechanics-concepts]] · Mark read: `INPUT[toggle:read]`
