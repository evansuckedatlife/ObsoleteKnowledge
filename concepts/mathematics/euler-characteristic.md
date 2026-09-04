---
type: concept
category: mathematics
defines: [Euler characteristic, Euler-Poincaré characteristic, polyhedral formula]
related: ["[[graph-theory]]", "[[calculus]]", "[[continuous-functions]]", "[[enlightenment]]", "[[euler-totient]]"]
requires: ["[[continuous-functions]]", "[[calculus]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Euler characteristic

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Euler characteristic** is a topological invariant, denoted by the Greek letter $\chi$ (chi), that describes the topological space's shape or structure regardless of bending or stretching. Originating in *Leonhard Euler*'s 1758 polyhedron formula relating vertices, edges, and faces, it was generalized by *Henri Poincaré* into algebraic topology. It provides a computable bridge between geometry, combinatorics, differential topology, and algebraic surfaces.

## you gotta know

- Originally discovered as the polyhedral formula $V - E + F = 2$ for convex polyhedra, where $V$ represents vertices, $E$ represents edges, and $F$ represents faces.
- Defined for finite CW complexes and triangulated spaces as the alternating sum $\chi = k_0 - k_1 + k_2 - k_3 + \dots$, where $k_n$ denotes the count of $n$-dimensional cells.
- Shown by *Henri Poincaré* to equal the alternating sum of the ranks of the homology groups: $\chi(X) = \sum_{i} (-1)^i \operatorname{rank}(H_i(X))$, proving its invariance under homotopy equivalence.
- Distinguishes compact closed orientable surfaces by genus $g$ via the relationship $\chi = 2 - 2g$, giving $\chi = 2$ for the sphere and $\chi = 0$ for the torus.
- Connects intrinsic geometry to topology through the *Gauss-Bonnet theorem*, which equates the total integral of Gaussian curvature over a surface to $2\pi\chi(M)$.
- Powers the *Poincaré-Hopf theorem*, which dictates that the sum of the indices of isolated zeroes of a smooth vector field on a manifold equals its Euler characteristic.
- Applied in planar [[graph-theory]] to establish that every planar graph contains a vertex of degree at most five, forming a critical step in coloring theorem proofs.

## connections

- [[continuous-functions]] — morphisms preserving topological structure under which the Euler characteristic remains invariant.
- [[calculus]] — differential machinery integrated over surfaces to yield the Euler characteristic in the Gauss-Bonnet theorem.
- [[enlightenment]] — historic intellectual era during which *Leonhard Euler* first proposed the polyhedral formula.
- [[euler-totient]] — arithmetic function named after the same Swiss mathematician who formulated the polyhedral characteristic.
- [[field-extension]] — algebraic structures whose geometric counterparts, algebraic varieties, utilize the étale Euler characteristic.

## see also

- [[continuous-functions]] · [[calculus]] · [[euler-totient]]

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
