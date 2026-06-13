---
type: concept
category: science
defines: ["Wavefunction", "wave function"]
related: ["[[schrodinger-equation]]", "[[quantum-operator]]", "[[superposition]]"]
lists: ["[[quantum-mechanics-concepts]]"]
read: false
---

# Wavefunction

## summary

A *wavefunction* is a mathematical object, typically denoted ψ(r,t) or Ψ, that encodes the complete information about a *quantum system*. The square of its magnitude gives the *probability density* for finding a particle at a location; the wavefunction itself is complex-valued and carries both probability information and phase, the latter crucial to quantum interference and entanglement.

## you gotta know

- **Probability amplitude**: |ψ(r,t)|² is the probability density; ψ itself is a probability amplitude—a complex number whose squared magnitude yields a real probability
- **Superposition**: a wavefunction can be a linear combination of multiple basis states; the particle exists in all those states simultaneously until measured (the *measurement problem*)
- **Phase matters**: two wavefunctions differing only by a global phase (ψ vs. e^(iθ)ψ) are physically identical, but relative phases between components determine interference patterns
- **Normalization**: the integral of |ψ|² over all space equals 1; the wavefunction must be square-integrable (in the Hilbert space)
- **Time evolution**: governed by the *Schrödinger equation*; given ψ at t=0, the equation deterministically predicts ψ at all future times
- **Multi-particle case**: ψ(r₁, r₂, ..., r_N, t) lives in a high-dimensional configuration space; *Pauli exclusion principle* imposes antisymmetry on fermionic wavefunctions
- **Nodes and structure**: regions where ψ vanishes (nodes) indicate zero probability; the number and location of nodes encode energy and angular momentum information

## context

The wavefunction is the central object of quantum mechanics, introduced by Erwin Schrödinger in 1926. It is not directly observable—the *measurement problem* asks what ψ actually "is" before measurement. The Copenhagen interpretation holds that ψ represents our knowledge or tendency for an outcome, becoming definite only upon measurement (wave function *collapse*). Other interpretations (Everett, Bohmian mechanics, decoherent histories) treat ψ differently but all use it as the primary mathematical entity. The wavefunction's evolution is reversible and deterministic (between measurements), yet the outcomes of measurements are probabilistic, a feature still debated today.

## connections

- [[schrodinger-equation]] — determines how ψ evolves in time; an eigenstate of the *Hamiltonian* gives a wavefunction with definite energy
- [[quantum-operator]] — operators (like momentum p̂ or position x̂) act on ψ; eigenvalues are possible measurement outcomes
- [[superposition]] — a wavefunction is often a superposition of basis states; coherent superposition is the hallmark of quantum behavior
- [[uncertainty-principle]] — a wavefunction cannot be sharply localized in both position and momentum simultaneously; their uncertainties are related by Planck's constant
- [[wave-particle-duality]] — the wavefunction unifies both aspects: it has wavelike properties (interference, diffraction) and particlelike ones (localization, energy quanta)
- [[quantum-entanglement]] — multi-particle wavefunctions exhibit entanglement when they cannot be factored into separate single-particle wavefunctions
- [[pauli-exclusion-principle]] — multi-fermionic wavefunctions must be antisymmetric under particle exchange

## see also

- [[commutator]] · [[eigenvalue]] · [[hilbert-space]] · [[erwin-schrodinger]]

<!-- footer -->

---

Lists: [[quantum-mechanics-concepts]] · Mark read: `INPUT[toggle:read]`
