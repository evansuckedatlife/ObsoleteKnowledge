---
type: concept
category: mathematics
defines:
  - Vector space
  - Linear space
related:
  - "[[linear-algebra]]"
  - "[[vector]]"
  - "[[basis]]"
  - "[[dimension]]"
  - "[[subspace]]"
  - "[[linear-transformation]]"
  - "[[inner-product]]"
  - "[[eigenvector]]"
requires: []
lists: []
tour_order: 0
read: false
---

# Vector Space

## summary

A **vector space** is an algebraic structure consisting of a set of objects (vectors) equipped with operations of *vector addition* and *scalar multiplication*, subject to specific axioms (associativity, distributivity, identity, and inverse elements). Vector spaces generalize geometric vectors to abstract settings, forming the foundation of linear algebra and enabling the systematic study of linearity, dimension, and transformations.

## you gotta know

- A vector space over a field (usually the real or complex numbers) is closed under addition and scalar multiplication: adding two vectors yields another vector, and multiplying a vector by a scalar yields another vector.
- The *zero vector* (identity for addition) and *additive inverses* must exist; scalar multiplication by 0 produces the zero vector, and by 1 leaves vectors unchanged.
- *Basis* is a set of vectors that spans the space (every vector is a linear combination of basis vectors) and are linearly independent (no non-trivial linear combination equals zero); every vector space (possibly infinite-dimensional) has a basis.
- *Dimension* is the number of basis vectors; finite-dimensional spaces like ℝⁿ (n-dimensional Euclidean space) have dimension n; infinite-dimensional spaces (function spaces, sequence spaces) require infinite basis elements.
- A *subspace* is a subset of a vector space that is itself a vector space under the same operations; subspaces are preserved under linear combinations—a key structural property.
- *Linear transformations* (or linear maps) are functions T: V → W between vector spaces preserving linearity (T(au + bv) = aT(u) + bT(v)); they are the morphisms of vector spaces.
- *Eigenvectors* are special vectors preserved in direction under a linear transformation (scaling but not rotating); finding eigenvectors reveals the "principal directions" of how a transformation acts, central to understanding linear transformations.

## connections

- [[linear-algebra]] — vector spaces are the foundational structure of linear algebra.
- [[vector]] — elements of a vector space.
- [[basis]] — linearly independent spanning sets of a vector space.
- [[dimension]] — the cardinality of a basis; characterizes the "size" of a vector space.
- [[subspace]] — vector spaces contained within larger vector spaces.
- [[linear-transformation]] — structure-preserving maps between vector spaces.
- [[inner-product]] — generalizes the dot product, introducing notions of length and orthogonality.
- [[eigenvector]] — vectors preserved in direction under linear transformations.

## see also

- [[linear-algebra]] · [[basis]] · [[dimension]] · [[linear-transformation]]

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

Lists:  · Mark read: `INPUT[toggle:read]`
