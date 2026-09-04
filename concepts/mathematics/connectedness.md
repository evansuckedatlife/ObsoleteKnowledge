---
type: concept
category: mathematics
defines: [Connectedness, Connected Space]
related: ["[[continuous-functions]]", "[[limit]]", "[[calculus]]", "[[polynomial-function]]", "[[continuum-hypothesis]]"]
requires: ["[[continuous-functions]]", "[[limit]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Connectedness

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Connectedness** is a core topological property that formalizes the geometric intuition of a mathematical space being in a single piece. Originating in nineteenth-century real analysis through investigations into the intermediate value theorem, the concept was generalized to abstract topological spaces by mathematicians including *Felix Hausdorff* and *Maurice Fréchet*. It serves as a foundational topological invariant that is preserved under continuous mappings and plays an indispensable role in analysis, differential geometry, and algebraic topology.

## you gotta know

- Defined formally for a topological space as the impossibility of partitioning the space into two non-empty, disjoint open sets.
- The real line satisfies this property as a consequence of the completeness of its order, which directly underpins the continuum studied in the [[continuum-hypothesis]].
- The intermediate value theorem of elementary [[calculus]] is a direct consequence, stating that the continuous image of an interval must itself remain connected.
- Preserved under [[continuous-functions]], meaning that if a space is connected, any continuous image of that space into another topological space must also be connected.
- Path-connectedness is a stronger variant requiring any two points to be joined by a continuous curve; while path-connectedness implies connectedness, the converse is false.
- The topologist's sine curve provides the classic counterexample of a space that is connected but fails to be path-connected due to infinite oscillation near the origin.
- Every topological space decomposes uniquely into maximal connected subsets termed connected components, which are always closed subsets of the overall space.
- In algebraic topology, the zeroth homology group and the zeroth homotopy set directly count the number of path-connected components of a space.

## connections

- [[continuous-functions]] — fundamental mappings that preserve topological connectedness and map connected domains onto connected image sets.
- [[limit]] — analytic convergence tool used to construct continuous paths, open neighborhoods, and boundary points within topological spaces.
- [[calculus]] — foundational subject whose core analytical results, notably the intermediate value theorem, rely fundamentally on the connected property of intervals.
- [[polynomial-function]] — smooth continuous maps on the real line whose unbroken graphs illustrate path-connected subsets of the Euclidean plane.
- [[continuum-hypothesis]] — the foundational conjecture regarding the cardinality of the real continuum, whose topological structure forms the archetype of connected spaces.

## see also

- [[continuous-functions]] · [[limit]] · [[calculus]] · [[continuum-hypothesis]]

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
