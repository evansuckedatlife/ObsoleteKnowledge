---
type: concept
category: mathematics
defines: ["dimension", "rank", "dimensional analysis"]
related: ["[[vector-space]]", "[[basis]]", "[[linear-algebra]]", "[[linear-transformation]]", "[[matrix]]"]
requires: ["[[vector-space]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Dimension

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Dimension** is a fundamental invariant of a vector space, defined as the cardinality of any basis—the minimum number of linearly independent vectors needed to generate the entire space. For familiar examples: Euclidean 3-space $\mathbb{R}^3$ has dimension 3, while the space of polynomials of degree at most *n* has dimension *n* + 1. Dimension measures the "size" or degrees of freedom of a vector space.

## you gotta know

- The **dimension** of $\mathbb{R}^n$ is *n*; the dimension of a finite-dimensional vector space is the size of any basis.
- All bases of a given vector space have the same cardinality; this is the *dimension theorem*, making dimension well-defined.
- [[vector-space|Vector spaces]] of different dimensions are never isomorphic; dimension is the complete topological invariant for finite-dimensional vector spaces.
- The [[basis|basis]] of a vector space has exactly *dim V* elements; any set of more than *dim V* vectors is linearly dependent.
- The *rank-nullity theorem* states: for a linear map $T : V \to W$, $\dim(\ker T) + \dim(\text{im} T) = \dim V$.
- Dimension extends to infinite-dimensional spaces (like spaces of functions) where bases may be uncountable.
- In practical applications, dimension represents degrees of freedom: a rigid body in 3D space has 6 dimensional freedom (3 translational, 3 rotational).
- The *rank* of a matrix is the dimension of its column space (or equivalently, row space); it determines the dimensionality of solutions to linear systems.
- Hamel and Schauder bases are two types of bases for infinite-dimensional spaces; the concept of dimension generalizes but loses uniqueness of basis size in these settings.

## connections

- [[vector-space]] — dimension is the fundamental invariant characterizing vector spaces.
- [[basis]] — dimension equals the cardinality of any basis.
- [[linear-algebra]] — dimension is central to understanding the structure of linear maps and matrices.
- [[linear-transformation]] — rank-nullity relates the dimensions of kernel and image.
- [[matrix]] — the rank of a matrix equals the dimension of its image.

## see also

- [[vector-space]] · [[basis]] · [[linear-algebra]] · [[linear-transformation]]

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
