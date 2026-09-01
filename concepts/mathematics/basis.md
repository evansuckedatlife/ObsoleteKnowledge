---
type: concept
category: mathematics
defines: [Basis, Bases]
related: ["[[linear-algebra]]", "[[vector-space]]", "[[linear-transformation]]"]
requires: ["[[vector-space]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Basis

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **basis** of a vector space is a minimal set of linearly independent vectors that span the entire space. Every vector in the space can be uniquely expressed as a linear combination of basis vectors. The concept is central to understanding the geometry and algebra of vector spaces.

## you gotta know

- A basis for a vector space *V* is a set of vectors that are *linearly independent* (no nontrivial linear combination equals zero) and *span* *V* (every vector is a linear combination of basis vectors).
- *Dimension* of *V* is the cardinality of any basis; fundamental invariant—all bases of the same space have equal size (dimension is well-defined).
- The *standard basis* for ℝⁿ is *e₁*, ..., *eₙ* (unit vectors along coordinate axes); any vector has a unique representation as a linear combination of standard basis vectors.
- *Change of basis*: via transition matrix *P*, coordinates transform as [*v*]_B' = *P*⁻¹ [*v*]_B; useful when a non-standard basis simplifies a problem (e.g., eigenvector basis diagonalizes a matrix).
- *Orthonormal bases* (mutually perpendicular unit vectors, like the standard basis) enable simple computations: dot products and projections become scalar multiplications; Gram-Schmidt constructs them.
- A linear transformation *T*: *V* → *W* is represented by a matrix whose columns are the images of basis vectors of *V*; different basis choices yield different matrices for the same transformation.
- The *rank* of a matrix (or transformation) is the dimension of its image; rank(*A*) + nullity(*A*) = # columns (rank-nullity theorem); full rank means injective (one-to-one).
- *Hamel bases* exist for any vector space (by the axiom of choice); however, infinite-dimensional spaces require uncountably many basis vectors, making Hamel bases impractical for analysis.
- *Schauder bases* and *frame theory* provide practical alternatives for infinite-dimensional spaces (Hilbert spaces, Banach spaces); enable convergent expansions even if not every vector is a finite combination.

## connections

- [[linear-algebra]] — basis is a foundational concept organizing vector spaces.
- [[vector-space]] — every vector space (except {0}) has a basis.
- [[linear-transformation]] — bases allow representation of transformations as matrices.
- [[dimension]] — defined as the cardinality of any basis.
- [[matrix]] — matrix entries depend on the choice of basis for the domain and codomain.

## see also

[[vector-space]] · [[linear-transformation]] · [[dimension]] · [[matrix]]

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
