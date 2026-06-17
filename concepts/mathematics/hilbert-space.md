---
type: term
category: mathematics
defines: [Hilbert space, infinite-dimensional vector space, complete inner product space]
related: ["[[vector-space]]", "[[inner-product]]", "[[linear-algebra]]", "[[quantum-mechanics]]", "[[functional-analysis]]", "[[david-hilbert]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Hilbert Space

## summary

A **Hilbert space** is a complete vector space equipped with an inner product—a generalisation of Euclidean space to infinite dimensions. Formally, it is a complete, separable inner product space where "complete" means all Cauchy sequences converge and "inner product" provides a notion of angle and length. Hilbert spaces are the natural mathematical setting for quantum mechanics, signal processing, and functional analysis, enabling rigorous treatment of infinite-dimensional linear systems.

## you gotta know

- **Definition**: a Hilbert space H is a vector space with an inner product ⟨·,·⟩ that is complete (all Cauchy sequences converge).
- **Inner product** generalises the dot product: ⟨u, v⟩ measures the "correlation" between vectors, satisfying linearity, conjugate symmetry, and positive-definiteness.
- **Norm and distance**: the norm ‖v‖ = √⟨v,v⟩ measures length; distance d(u,v) = ‖u − v‖.
- **Orthogonality**: vectors u and v are orthogonal if ⟨u,v⟩ = 0; an orthonormal basis spans the space with orthogonal unit vectors.
- **Completeness** (the defining property): every Cauchy sequence converges to a limit in the space; this ensures limits of approximating sequences remain in the space.
- **Examples**: ℓ²(ℕ) is the space of square-summable infinite sequences; L²([a,b]) is the space of square-integrable functions on [a,b]; these are Hilbert spaces.
- **Fourier series and orthonormal bases**: any element can be written as a convergent sum over an orthonormal basis; generalises Fourier decomposition to any Hilbert space.
- **Operators and spectra**: linear operators on Hilbert spaces may have eigenvalues and eigenvectors; spectral theorem ensures Hermitian operators can be diagonalised.

## context

Hilbert spaces emerged from David Hilbert's work on integral equations (early 20th century) and were formalised by von Neumann and others in the 1920s–1930s. They provided the rigorous mathematical foundation for quantum mechanics: the *state* of a quantum system is a vector in a Hilbert space, *observables* are Hermitian operators, and *measurement outcomes* are eigenvalues. Quantum field theory builds on operator algebras on Hilbert spaces. Beyond physics, Hilbert spaces underpin functional analysis, signal processing (wavelets, Fourier analysis), machine learning (kernel methods), and approximation theory. The concept is so powerful that most of modern mathematical physics and analysis is conducted in the language of Hilbert spaces. For pure mathematicians, Hilbert spaces are a gateway to functional analysis and the study of infinite-dimensional structures.

## connections

- [[vector-space]] — Hilbert spaces are special vector spaces with inner products.
- [[inner-product]] — the inner product is the defining structure of a Hilbert space.
- [[linear-algebra]] — the finite-dimensional analogue of Hilbert space theory.
- [[quantum-mechanics]] — quantum states live in Hilbert spaces; observables are operators.
- [[functional-analysis]] — Hilbert spaces are the foundational objects of functional analysis.
- [[david-hilbert]] — the mathematician who pioneered the theory.
- [[fourier-series]] — orthonormal basis expansions in Hilbert spaces.
- [[eigenvalue]] — spectra of operators on Hilbert spaces.

## see also

- [[vector-space]] · [[linear-algebra]] · [[functional-analysis]]

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

Lists: Mark read: `INPUT[toggle:read]`
