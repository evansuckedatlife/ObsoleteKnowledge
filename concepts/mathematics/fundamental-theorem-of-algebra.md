---
type: concept
category: mathematics
defines: ["Fundamental Theorem of Algebra"]
related: ["[[polynomial-function]]", "[[complex-numbers]]", "[[carl-friedrich-gauss]]", "[[roots]]", "[[algebra]]"]
requires: ["[[polynomial-function]]", "[[complex-numbers]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Fundamental Theorem of Algebra

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Fundamental Theorem of Algebra** states that every non-constant polynomial of degree n with complex coefficients has exactly n roots in the complex numbers (counting multiplicity). This theorem completes the number system by guaranteeing that polynomial equations always have solutions within the complex field, no matter their degree. *Carl Friedrich Gauss* gave the first rigorous proof in 1799, and the result is foundational to all of algebra, analysis, and applied mathematics.

## you gotta know

- *Statement:* if p(x) is a polynomial of degree n ≥ 1 with complex coefficients, then there exist exactly n complex numbers r₁, r₂, ..., rₙ (not necessarily distinct) such that p(x) = aₙ(x − r₁)(x − r₂)···(x − rₙ), where aₙ is the leading coefficient.
- *Counting multiplicity:* repeated roots are counted according to their multiplicity; a root that appears k times in the factorization is said to have multiplicity k.
- *Real polynomials:* a polynomial with real coefficients may have complex roots, but they occur in conjugate pairs; if a + bi is a root, so is a − bi, ensuring real factorization structure.
- *Existence vs constructibility:* the theorem guarantees existence of roots but does not provide a method to find them; for degree ≥ 5, no closed-form radical solution exists (by Galois theory).
- *Historical significance:* earlier centuries saw solutions for low-degree polynomials (Cardano for cubics, Ferrari for quartics), but the general case eluded proof until Gauss's rigorous argument in 1799.
- *No real analogue:* the set of real numbers is not algebraically closed; the polynomial x² + 1 has no real roots, which is why complex numbers were necessary.
- *Consequences:* every polynomial can be uniquely factored into linear factors in the complex numbers; this factorisation is the starting point for partial fractions, residue calculus, and signal processing.
- *Proofs:* Gauss's original proof was geometric; later proofs use complex analysis (the argument principle), topology (winding number arguments), or algebra (reduction to the case of real polynomials via conjugation).

## connections

- [[polynomial-function]] — the objects to which the theorem applies; establishes roots exist.
- [[complex-numbers]] — the field in which roots are guaranteed to lie.
- [[carl-friedrich-gauss]] — gave the first rigorous proof in 1799.
- [[algebra]] — the theorem is central to the structure of algebraic systems.
- [[galois-theory]] — explains why degree-5 polynomials have no closed-form solutions.

## see also

- [[polynomial-function]] · [[complex-numbers]] · [[carl-friedrich-gauss]] · [[galois-theory]]

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
