---
type: concept
category: mathematics
defines:
  - Linear algebra
  - Matrix algebra
related:
  - "[[vector-space]]"
  - "[[matrix]]"
  - "[[eigenvalue]]"
  - "[[eigenvector]]"
  - "[[determinant]]"
  - "[[linear-transformation]]"
  - "[[systems-of-linear-equations]]"
  - "[[inner-product]]"
requires: ["[[vector-space]]"]
lists: []
tour_order: 1
read: false
---

# Linear Algebra


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Linear algebra** is the branch of mathematics dealing with *vectors*, *matrices*, and *linear transformations* between finite-dimensional spaces. It studies systems of linear equations, the structure of solution spaces, and transformations that preserve linearity. With ubiquitous applications in computer graphics, machine learning, quantum mechanics, and data science, linear algebra is fundamental to modern mathematics and engineering.

## you gotta know

- A *vector* is an ordered list of numbers (or scalars); *vector spaces* are collections of vectors closed under addition and scalar multiplication, forming the foundational structure of linear algebra.
- A *matrix* is a rectangular array of numbers; matrices represent linear transformations and systems of equations; matrix operations (addition, multiplication) encode geometric and algebraic relationships.
- *Eigenvalues* and *eigenvectors* are special pairs associated with a matrix: an eigenvector is preserved in direction (only scaled) when the matrix acts on it, with the scaling factor being the eigenvalue; they reveal the "principal directions" of a transformation.
- The *determinant* of a square matrix encodes information about the transformation it represents: a zero determinant indicates the transformation is singular (non-invertible) and collapses dimension; determinants also measure volume scaling.
- *Linear transformations* are functions between vector spaces that preserve linearity (T(au + bv) = aT(u) + bT(v)); every linear transformation can be represented as matrix multiplication.
- *Systems of linear equations* can be written in matrix form (Ax = b) and solved using techniques like Gaussian elimination, matrix inversion, or more advanced methods; linear algebra determines existence and uniqueness of solutions.
- *Inner products* generalize the dot product to abstract vector spaces, enabling definitions of orthogonality, projection, and length; orthogonal matrices and projections are crucial in data analysis and signal processing.

## connections

- [[vector-space]] — the fundamental structure of linear algebra.
- [[matrix]] — rectangular arrays representing linear transformations.
- [[eigenvalue]] — scalars associated with eigenvectors under linear transformation.
- [[eigenvector]] — vectors preserved in direction under linear transformation.
- [[determinant]] — a scalar capturing information about matrix invertibility and volume scaling.
- [[linear-transformation]] — functions preserving linearity; representable as matrices.
- [[systems-of-linear-equations]] — linear algebra solves these systems efficiently.
- [[inner-product]] — generalizes dot products to abstract vector spaces.

## see also

- [[vector-space]] · [[matrix]] · [[eigenvalue]] · [[eigenvector]]

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
