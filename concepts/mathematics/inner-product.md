---
type: concept
category: mathematics
defines: ["Inner product", "Dot product", "Scalar product"]
related: ["[[vector-space]]", "[[linear-algebra]]", "[[hilbert-space]]", "[[orthogonality]]", "[[norm]]"]
requires: ["[[vector-space]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Inner Product

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

An **inner product** is a generalisation of the familiar dot product from Euclidean space to abstract vector spaces, assigning to each pair of vectors a scalar that measures their geometric relationship. Inner products introduce notions of *length* (norm), *angle*, and *orthogonality* to abstract spaces, forming the foundation of *Hilbert spaces* and enabling rigorous analysis in infinite dimensions. They are essential in quantum mechanics, signal processing, and functional analysis, where they provide the geometric structure underlying linear operators and spectral theory.

## you gotta know

- *Definition:* an inner product ⟨·, ·⟩ on a vector space assigns to each pair of vectors u, v a scalar satisfying linearity in the second argument, conjugate symmetry ⟨u, v⟩ = ⟨v, u⟩*, and positive-definiteness ⟨v, v⟩ > 0 for v ≠ 0.
- **Dot product** as example: in ℝⁿ, the standard inner product is ⟨u, v⟩ = u·v = u₁v₁ + u₂v₂ + ... + uₙvₙ, the canonical prototype.
- *Norm induction:* an inner product induces a norm ||v|| = √⟨v, v⟩, measuring vector length; this norm defines a metric and enables convergence and continuity arguments.
- *Orthogonality:* vectors u and v are orthogonal if ⟨u, v⟩ = 0; orthogonal families are the analogue of perpendicular directions in Euclidean space.
- *Cauchy–Schwarz inequality:* |⟨u, v⟩| ≤ ||u|| · ||v||, a fundamental inequality bounding the inner product and ensuring geometric reasonableness.
- *Gram–Schmidt process:* given any finite set of linearly independent vectors, the Gram–Schmidt orthogonalisation produces an orthonormal basis (vectors of unit length and mutually orthogonal), crucial for numerical stability in computations.
- *Function spaces:* inner products extend to spaces of functions; on L²[a, b] (square-integrable functions), the inner product is ⟨f, g⟩ = ∫ₐᵇ f(x)g(x) dx, making calculus and Fourier analysis rigorous.
- *Hilbert spaces:* an inner product space that is complete (every Cauchy sequence converges) is a Hilbert space, the setting for functional analysis, quantum mechanics, and spectral theory of operators.

## connections

- [[vector-space]] — inner products structure vector spaces geometrically.
- [[linear-algebra]] — inner products define orthogonality and enable diagonalisation via spectral theorem.
- [[hilbert-space]] — a complete inner product space; the primary setting for functional analysis.
- [[orthogonality]] — vectors are orthogonal when their inner product vanishes.
- [[norm]] — inner products induce norms, measuring vector length and distance.
- [[eigenvector]] — eigenvectors of symmetric matrices are orthogonal with respect to the standard inner product.

## see also

- [[vector-space]] · [[linear-algebra]] · [[hilbert-space]] · [[orthogonality]]

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
