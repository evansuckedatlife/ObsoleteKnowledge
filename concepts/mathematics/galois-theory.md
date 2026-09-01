---
type: concept
category: mathematics
defines: [Galois theory]
related: ["[[polynomial-function]]", "[[fundamental-theorem-of-algebra]]", "[[field-extension]]", "[[abstract-algebra]]", "[[group-theory]]", "[[solvable-group]]"]
requires: ["[[polynomial-function]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Galois Theory

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Galois theory** connects the structure of polynomial equations to the symmetries of their solutions through group theory. *Évariste Galois* proved that a polynomial equation is solvable by radicals (nth roots) if and only if its *Galois group* is *solvable*. This theory answers the ancient question: "Why does the quintic (degree-5 polynomial) have no general closed-form solution?" Galois theory stands as one of mathematics' most elegant unifications, revealing why algebra and symmetry are inseparable.

## you gotta know

- The *Galois group* of a polynomial is the group of permutations of its roots that preserve rational operations (automorphisms of the splitting field fixing the base field).
- For a quadratic ax² + bx + c, the *Galois group* is either trivial (one repeated root) or the 2-element cyclic group Z₂ (two distinct roots that swap).
- For a cubic, the *Galois group* is either the 3-element cyclic group C₃ or the full 6-element symmetric group S₃, determined by the discriminant.
- *Fundamental Theorem of Galois Theory*: there is a one-to-one correspondence between subgroups of the *Galois group* and intermediate field extensions between the base field and the splitting field; larger subgroups correspond to smaller fields.
- A polynomial is *solvable by radicals* if and only if its *Galois group* is *solvable* (a group with a normal series where each quotient is abelian, or equivalently, derived series reaches trivial).
- The symmetric group S_n is *solvable* only for n ≤ 4, which rigorously explains why the quintic (degree-5) polynomial and higher have no general closed-form radical solutions.
- Galois' original 1832 manuscript on permutation groups and field extensions was largely unread for years; the theory only gained recognition after *Liouville* published it in 1846, more than a decade after Galois' death in a duel at age 20.
- The *Galois group* acts on the roots, encoding all the algebraic relationships; studying this symmetry group reveals whether and how solutions can be expressed using radicals.
- Modern Galois theory extends to infinite extensions, p-adic fields, and Galois cohomology, with deep applications to algebraic number theory and arithmetic geometry.

## connections

- [[polynomial-function]] — the objects whose solvability Galois theory characterizes.
- [[fundamental-theorem-of-algebra]] — relates to the existence of roots; Galois theory explains their form.
- [[field-extension]] — the algebraic objects whose symmetries define the Galois group.
- [[group-theory]] — the symmetry framework underlying Galois' method.
- [[abstract-algebra]] — Galois theory exemplifies abstract thinking's power in classical algebra.
- [[solvable-group]] — the group-theoretic criterion for when radicals can solve a polynomial.

## see also

[[polynomial-function]] · [[group-theory]] · [[abstract-algebra]] · [[field-extension]]

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
