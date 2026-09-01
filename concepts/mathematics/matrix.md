---
type: concept
category: mathematics
defines: [Matrix, Matrices]
related: ["[[linear-algebra]]", "[[determinant]]", "[[eigenvalue]]"]
requires: ["[[linear-algebra]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Matrix

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **matrix** is a rectangular array of numbers, symbols, or expressions arranged in rows and columns. Matrices are fundamental tools in mathematics for representing linear transformations, systems of equations, and data in a compact form. They enable efficient computation and reveal deep structure in linear algebra and applied sciences.

## you gotta know

- Denoted as an *m × n* array with *m* rows and *n* columns; each entry is called an element or component.
- *Matrix multiplication*: (AB)*ij* = Σ*k* *A*ik *B*kj*; associative but *not* commutative (*AB* ≠ *BA* generally), and not every matrix has a multiplicative inverse.
- The *identity matrix* *I* (1s on diagonal, 0s elsewhere) satisfies *AI* = *IA* = *A*; acts like 1 in multiplication.
- *Determinant* of a square matrix measures invertibility and volume scaling of the transformation; det(*A*) ≠ 0 if and only if *A* has an inverse.
- *Eigenvalues* λ and *eigenvectors* *v* satisfy *Av* = λ*v*; they reveal intrinsic directions along which the matrix stretches or contracts by scalar factors.
- *Row operations* (swapping, scaling, adding multiples) preserve linear system solution sets; used in Gaussian elimination to solve *Ax* = *b* and to compute inverses.
- *Matrix rank* is the dimension of its row or column space; rank(*A*) ≤ min(*m*, *n*); determines whether *Ax* = *b* has solutions and their uniqueness.
- Over a field, an *m × n* **matrix** can be viewed as a linear transformation from an *n*-dimensional space to an *m*-dimensional space; this perspective unifies matrix algebra with geometric transformations.
- *Trace* (sum of diagonal entries) equals the sum of eigenvalues and is invariant under similarity transformations, capturing a fundamental scalar property of the matrix.
- In applications, **matrices** encode adjacency information in graph theory, transition probabilities in Markov chains, and covariance structure in statistics and machine learning.

## connections

- [[linear-algebra]] — matrices are the central computational objects of linear algebra.
- [[determinant]] — a scalar quantity that encodes crucial invertibility information for square matrices.
- [[eigenvalue]] — values that reveal the geometric action of a matrix.
- [[vector-space]] — matrices act on vector spaces and can represent linear transformations between them.
- [[kernel-and-image]] — the kernel and image of a matrix describe its null space and range.

## see also

[[determinant]] · [[eigenvalue]] · [[linear-transformation]] · [[vector-space]]

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
