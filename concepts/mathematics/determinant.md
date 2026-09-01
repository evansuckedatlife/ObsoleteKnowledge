---
type: concept
category: mathematics
defines: [determinant]
related: ["[[linear-algebra]]", "[[eigenvalue]]", "[[matrix]]"]
requires: ["[[linear-algebra]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Determinant

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **determinant** is a scalar value computed from a square matrix that encodes crucial geometric and algebraic information about the matrix. It measures whether a matrix is invertible, captures volume scaling in linear transformations, and appears in solutions to systems of equations. Determinants connect linear algebra to geometry, physics, and even topology.

## you gotta know

- For a 2×2 matrix [[a, b], [c, d]], the determinant is ad − bc, the simplest non-trivial formula; higher-order determinants follow more complex recursive patterns.
- A matrix is invertible if and only if its determinant is nonzero; det(A) = 0 signals degeneracy or information loss, meaning the transformation collapses space into lower dimensions.
- In geometric terms, |det(A)| gives the factor by which a linear transformation scales volumes; a negative determinant indicates orientation reversal (left-handed becomes right-handed).
- Determinants satisfy key algebraic properties: det(AB) = det(A)det(B), det(A^T) = det(A), and multiplying a row by k multiplies the determinant by k; these enable efficient computation.
- Cramer's rule uses determinants to solve systems of linear equations Ax = b in closed form, though it's impractical for large systems due to computational expense.
- Eigenvalues of a matrix A are roots of the characteristic polynomial det(A − λI), connecting eigenvalue theory to determinant computation and revealing hidden structure.
- The permanent (a determinant variant without sign changes) appears in combinatorics and quantum physics, showing how related functions encode different mathematical truths.
- Computing determinants efficiently is non-trivial; Gaussian elimination runs in O(n³) time, and no substantially faster classical algorithm exists, but quantum computers might eventually solve this via quantum factorization.
- In probability and statistics, the Jacobian determinant (the determinant of the matrix of partial derivatives) is essential for changing variables in multidimensional integrals and probability distributions.

## connections

- [[linear-algebra]] — determinants are a central tool in the study of matrices and linear transformations.
- [[eigenvalue]] — eigenvalues are found by solving det(A − λI) = 0.
- [[matrix]] — determinants are only defined for square matrices.
- [[calculus]] — the Jacobian determinant measures volume scaling in multivariable integration.
- [[algebra]] — determinants appear in the theory of algebraic equations.
- [[polynomial-function]] — the characteristic polynomial whose roots are eigenvalues.

## see also

- [[linear-algebra]] · [[eigenvalue]] · [[matrix]]

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
