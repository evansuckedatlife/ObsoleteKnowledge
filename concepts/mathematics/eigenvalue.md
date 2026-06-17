---
type: term
category: mathematics
defines: [Eigenvalue, eigenvector, eigenspace, characteristic polynomial]
related: ["[[linear-algebra]]", "[[matrix-multiplication]]", "[[vector-space]]", "[[differential-equations]]", "[[principal-component-analysis]]", "[[quantum-mechanics]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Eigenvalue

## summary

An **eigenvalue** is a scalar that emerges from the action of a square matrix on a vector. When a matrix A multiplies a nonzero vector v and the result is a scalar multiple of v (i.e., Av = λv), the scalar λ is an eigenvalue and v is the corresponding **eigenvector**. Eigenvalues and eigenvectors reveal the "principal directions" of linear transformations and are fundamental to solving differential equations, understanding vibrations, and modern data science applications like principal component analysis.

## you gotta know

- **Definition**: λ is an eigenvalue of matrix A if there exists a nonzero vector v such that Av = λv; v is the corresponding eigenvector.
- **Geometric interpretation**: an eigenvector is a direction that the matrix does not rotate, only stretches (or compresses) by the factor λ.
- The **characteristic polynomial** of A is det(A − λI), where I is the identity matrix; eigenvalues are roots of this polynomial.
- For an n×n matrix, there are at most n eigenvalues (counting multiplicity); real matrices may have complex eigenvalues (which appear in conjugate pairs).
- **Diagonalisation**: if A has n linearly independent eigenvectors, it can be written as A = PDP^(-1), where D is diagonal (eigenvalues on the diagonal) and P contains eigenvectors as columns.
- **Trace and determinant**: the sum of eigenvalues equals the trace (sum of diagonal entries); the product equals the determinant.
- **Applications**: differential equations (e^(λt) governs exponential growth/decay), vibrations (eigenvalues = squared natural frequencies), stability analysis (sign of eigenvalues determines stability), and data analysis (PCA finds directions of maximum variance).

## context

Eigenvalues emerged in the 18th century from Euler's work on rotating bodies and inertia; the deep theory developed through the 19th century with Cauchy and Jacobi. They are indispensable in physics and engineering: the natural frequencies of a vibrating bridge are eigenvalues; the stability of spacecraft attitude control depends on eigenvalues; quantum mechanics is built on eigenvalues (observables are Hermitian operators, and measured values are eigenvalues). In modern machine learning, eigendecomposition underlies principal component analysis (PCA), a cornerstone technique for dimension reduction. The eigenvalue problem—finding them computationally—is one of numerical analysis' central challenges; algorithms like QR iteration and Lanczos iteration are essential tools in scientific computing.

## connections

- [[linear-algebra]] — eigenvalues are core objects in linear algebra.
- [[matrix-multiplication]] — eigenvalues relate the input and output under matrix multiplication.
- [[vector-space]] — eigenvectors are special vectors preserved under linear transformations.
- [[differential-equations]] — solutions often involve e^(λt), where λ are eigenvalues of the system's matrix.
- [[principal-component-analysis]] — finds directions (eigenvectors) of maximum variance in data.
- [[quantum-mechanics]] — observables are operators; measured values are eigenvalues.
- [[determinant]] — the product of eigenvalues.
- [[trace]] — the sum of eigenvalues equals the matrix trace.

## see also

- [[linear-algebra]] · [[matrix-multiplication]] · [[vector-space]]

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
