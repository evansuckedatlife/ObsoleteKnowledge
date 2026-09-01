---
type: concept
category: mathematics
defines: [linear transformation]
related: ["[[linear-algebra]]", "[[vector-space]]", "[[matrix]]", "[[eigenvalue]]", "[[basis]]", "[[kernel-and-image]]"]
requires: ["[[vector-space]]", "[[linear-algebra]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Linear Transformation

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **linear transformation** is a function T: V → W between two vector spaces that preserves the vector space structure—formally, T(au + bv) = aT(u) + bT(v) for scalars a, b and vectors u, v. Linear transformations are the "natural" maps in algebra, encoding rotations, reflections, scalings, and projections in a unified framework. Every linear transformation between finite-dimensional spaces can be represented by a matrix, connecting abstract algebra to practical computation and unifying linear algebra's heart.

## you gotta know

- A linear transformation satisfies *additivity* (T(u + v) = T(u) + T(v)) and *homogeneity* (T(cu) = cT(u)), preserving the vector space operations.
- Every linear transformation T: ℝⁿ → ℝᵐ corresponds uniquely to an m × n matrix A: T(x) = Ax for column vectors x; this matrix representation depends on the choice of basis.
- The *kernel* (or null space) of T is ker(T) = {v : T(v) = 0}, the set of vectors mapping to zero; the *image* (or range) is im(T) = {T(v) : v ∈ domain}, the set of all output vectors.
- *Rank-nullity theorem*: dim(ker(T)) + dim(im(T)) = dim(domain); this fundamental constraint relates the dimension of the kernel and image, accounting for all dimension in the domain.
- T is *injective* (one-to-one) if ker(T) = {0}, meaning distinct inputs produce distinct outputs; *surjective* (onto) if im(T) = codomain, meaning every target vector is reached; *bijective* (invertible) if both.
- Eigenvalues and eigenvectors describe the transformation's "directions of pure scaling": T(v) = λv for eigenvalue λ and eigenvector v; along these directions, T merely scales.
- The trace and determinant of the matrix representation encode global properties: trace = sum of eigenvalues, determinant = product of eigenvalues.
- Applications permeate science: rotations in computer graphics, diffusion processes in partial differential equations, quantum mechanics operators (observables), and machine learning embeddings.
- Change of basis changes the matrix representation but not the underlying transformation; similarity transformations relate matrices of the same T in different bases.

## connections

- [[linear-algebra]] — the field where linear transformations are central structures.
- [[vector-space]] — the domain and codomain; linear transformations preserve this structure.
- [[matrix]] — the computational representation of linear transformations for finite-dimensional spaces.
- [[eigenvalue]] — characterize linear transformations' behavior; eigenvectors are invariant directions under T.
- [[basis]] — choice of basis determines the matrix representation of T; different bases give different matrices for the same T.
- [[kernel-and-image]] — the fundamental subspaces describing T's surjectivity and injectivity.

## see also

[[linear-algebra]] · [[vector-space]] · [[matrix]] · [[eigenvalue]]

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

Lists: [[mathematics-hubs]] · Mark read: `INPUT[toggle:read]`
