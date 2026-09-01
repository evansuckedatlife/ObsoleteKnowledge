---
type: concept
category: mathematics
defines: []
related: ["[[continuous-functions]]", "[[henri-poincare]]", "[[limit]]", "[[compactness]]", "[[connectedness]]"]
requires: ["[[continuous-functions]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Topology

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

This is the branch of mathematics studying spaces and continuity, focusing on properties that remain invariant under continuous deformation. Unlike geometry, which cares about distances and angles, topology asks only: which properties survive stretching, twisting, and bending without tearing or gluing? Born from Henri Poincaré's foundational work, topology bridges algebra, geometry, and analysis.

## you gotta know

- A *topological space* is a set X with a collection of *open sets* satisfying three axioms: the empty set and X are open, finite intersections of open sets are open, and arbitrary unions are open.
- *Continuous functions* generalise from metric spaces to abstract topological spaces: f is continuous if the preimage of every open set is open.
- *Homeomorphism* is the topological equivalence: two spaces are homeomorphic if there exists a continuous bijection with continuous inverse; a coffee cup is homeomorphic to a torus (one handle).
- Henri Poincaré founded algebraic topology, studying *homology* and *homotopy* groups—invariants that distinguish topological spaces and remain unchanged under homeomorphism.
- A space is connected if it cannot be partitioned into two disjoint, nonempty, open sets; connectedness is a topological property preserved under continuous images.
- *Compactness* (Heine-Borel): a metric space is compact iff it is closed and bounded; compactness is a topological property preserved under continuous images with profound implications.
- Knot theory (a subfield) studies knots and links up to ambient isotopy—a purely topological classification that ignores how tightly or loosely a knot is tied.
- The *fundamental group* measures "holes" in a space; spaces with different fundamental groups cannot be homeomorphic, providing a practical tool for distinguishing topological spaces.
- Hausdorff spaces axiomatize separation: any two distinct points can be separated by disjoint open neighborhoods; many important spaces satisfy this condition.

## connections

- [[continuous-functions]] — continuity is the central concept of topology; topology formalises which functions are continuous in abstract settings.
- [[henri-poincare]] — founded algebraic topology and established foundational invariants.
- [[limit]] — fundamental to defining continuity and convergence in topological spaces.
- [[compactness]] — a central topological property with profound implications (e.g., continuous functions on compact spaces are uniformly continuous).
- [[connectedness]] — a key topological property distinguishing spaces that are "in one piece."
- [[set-theory]] — provides the foundational language (sets, functions) upon which topology is built.

## see also

- [[continuous-functions]] · [[henri-poincare]] · [[limit]]

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
