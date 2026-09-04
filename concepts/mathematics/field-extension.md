---
type: concept
category: mathematics
defines: [field extension, algebraic extension, degree of a field extension, splitting field]
related: ["[[polynomial-function]]", "[[vector-space]]", "[[linear-algebra]]", "[[abstract-algebra]]", "[[group-theory]]", "[[fundamental-theorem-of-algebra]]"]
requires: ["[[linear-algebra]]", "[[vector-space]]", "[[polynomial-function]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Field extension

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **field extension** is an algebraic structure consisting of a field containing a smaller base field, denoted as an extension $L/K$. Developed substantially during the nineteenth century through the work of *Évariste Galois*, *Richard Dedekind*, and *Ernst Steinitz*, the concept allows mathematicians to adjoin roots of polynomials to existing number systems. It serves as the primary arena for Galois theory, establishing deep connections between the roots of polynomial equations and finite group symmetries.

## you gotta know

- Formally defined when a field $L$ contains a subfield $K$, written $L/K$ or $L:K$, making $L$ into a [[vector-space]] over $K$.
- The dimension of $L$ as a vector space over $K$ is called the **degree of a field extension**, denoted $[L:K]$, which satisfies the multiplicative tower law $[M:K] = [M:L][L:K]$.
- An **algebraic extension** consists entirely of elements that are roots of non-zero polynomials with coefficients in the base field $K$.
- A **splitting field** is a minimal extension over which a given [[polynomial-function]] factors completely into linear factors.
- Galois theory associates a field extension with its group of field automorphisms that fix the base field, translating intermediate subfield structures into subgroups.
- Resolved ancient geometric problems by proving the impossibility of doubling the cube, trisecting arbitrary angles, and squaring the circle using a straightedge and compass.
- Fundamental examples include extending the rational numbers $\mathbb{Q}$ to the field of Gaussian rationals $\mathbb{Q}(i)$ or obtaining the complex numbers $\mathbb{C}$ over the real numbers $\mathbb{R}$.

## connections

- [[polynomial-function]] — algebraic objects whose roots generate field extensions.
- [[vector-space]] — foundational linear algebraic structure that $L$ forms when viewed over its base field $K$.
- [[linear-algebra]] — mathematical field whose concepts of dimension, basis, and linear independence determine the degree of extensions.
- [[euclidean-algorithm]] — algorithm applied to polynomial rings to establish that irreducible polynomials generate maximal ideals and extension fields.
- [[euler-characteristic]] — topological invariant whose algebraic analogues in étale cohomology study varieties over general fields.
- [[fundamental-theorem-of-algebra]] — classical theorem establishing that the complex numbers form an algebraically closed extension of the real numbers.

## see also

- [[polynomial-function]] · [[vector-space]] · [[linear-algebra]]

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
