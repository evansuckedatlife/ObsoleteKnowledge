---
type: concept
category: mathematics
defines: [Compactness, Compact space, Compact]
related: ["[[topology]]", "[[continuous-functions]]", "[[closed-interval]]"]
requires: ["[[topology]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Compactness

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Compactness** is a topological property that generalizes the familiar finiteness of closed intervals to arbitrary spaces. A space is compact if every open cover has a finite subcover. This seemingly abstract condition has profound consequences: continuous functions on compact spaces achieve their maximum and minimum values, and compact spaces are well-behaved in surprising ways.

## you gotta know

- A topological space *X* is **compact** if every open cover (collection of open sets whose union is *X*) admits a finite subcover; no infinite collection of open sets is *necessary* to cover *X*.
- Closed intervals *[a, b]* in ℝ are compact; open intervals *(a, b)* are not (endpoints escape); finite unions of compact sets are compact.
- *Heine-Borel theorem*: in Euclidean space ℝⁿ, a set is compact if and only if it is closed and bounded; this classical result fails in infinite-dimensional spaces.
- *Continuous images of compact spaces are compact*: if *f*: *X* → *Y* is continuous and *X* is compact, then *f*(*X*) is compact; compactness is topologically preserved.
- *Extreme value theorem*: a continuous function on a compact space attains its maximum and minimum values (unlike on open intervals, where suprema may be unattained).
- *Hausdorff spaces* (including ℝⁿ) separate distinct points with disjoint open sets; compact Hausdorff spaces are normal (can separate disjoint closed sets with disjoint open neighborhoods).
- Compactness ensures convergence: in compact metric spaces, every sequence has a convergent subsequence (Bolzano-Weierstrass); compact sets behave like "generalized finite sets" with finiteness-like properties.
- *Tychonoff's theorem*: an arbitrary product of compact spaces is compact (in the product topology); surprising because infinite products of non-compact spaces can be non-compact.
- *Sequential compactness* (every sequence has a convergent subsequence) is equivalent to compactness in metric spaces but weaker in general topological spaces; countable compactness is an intermediate notion.

## connections

- [[topology]] — compactness is a central topological property defined via open covers.
- [[continuous-functions]] — compactness is preserved by continuous maps and ensures well-behaved behavior of continuous functions.
- [[closed-interval]] — the prototypical compact space in the real numbers.
- [[extreme-value-theorem]] — relies fundamentally on compactness to guarantee maxima and minima exist.
- [[limit]] — compactness is closely related to convergence and accumulation of limits.

## see also

[[topology]] · [[continuous-functions]] · [[extreme-value-theorem]] · [[limit]]

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
