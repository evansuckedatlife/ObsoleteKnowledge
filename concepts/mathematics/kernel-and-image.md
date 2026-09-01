---
type: concept
category: mathematics
defines: ["kernel", "image", "null space", "range"]
related: ["[[linear-transformation]]", "[[matrix]]", "[[vector-space]]", "[[linear-algebra]]", "[[dimension]]"]
requires: ["[[linear-algebra]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Kernel and Image

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

For a linear transformation $T : V \to W$ between vector spaces, the **kernel** (or null space) is the set of all inputs that map to zero: $\ker(T) = \{v \in V : T(v) = 0\}$, while the **image** (or range) is the set of all possible outputs: $\text{im}(T) = \{T(v) : v \in V\}$. These two fundamental subspaces completely characterize the behavior of *T*, encapsulating its injectivity and surjectivity through their dimensions.

## you gotta know

- The **kernel** measures where *T* "loses" information; $T$ is injective if and only if $\ker(T) = \{0\}$.
- The **image** is the set of all reachable outputs; $T$ is surjective if and only if $\text{im}(T) = W$.
- Both kernel and image are subspaces: closed under addition and scalar multiplication.
- The *rank-nullity theorem* is central: $\dim(\ker T) + \dim(\text{im} T) = \dim V$.
- For a matrix, the kernel is the null space (solutions to $Ax = 0$) and the image is the column space (span of columns).
- The kernel and image partition the geometric action of *T*: directions sent to zero and directions that contribute to the output.
- Understanding kernel and image is essential for solving systems of linear equations and analyzing matrix rank.
- The *first isomorphism theorem* states that $V / \ker(T) \cong \text{im}(T)$, connecting quotient spaces to the structure of linear maps.
- Left and right inverses exist only when the kernel is trivial and image is the full codomain, respectively; understanding these conditions requires kernel-image analysis.

## connections

- [[linear-transformation]] — kernel and image characterize the structure of linear maps.
- [[matrix]] — for matrices, kernel is the null space and image is the column space.
- [[vector-space]] — kernel and image are subspaces of their respective domain and codomain.
- [[linear-algebra]] — rank-nullity and the kernel-image decomposition are foundational theorems.
- [[dimension]] — ranks are defined as dimensions: $\text{rank}(T) = \dim(\text{im} T)$.

## see also

- [[linear-transformation]] · [[matrix]] · [[vector-space]] · [[linear-algebra]]

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
