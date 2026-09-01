---
type: concept
category: mathematics
defines: ["closed interval", "interval closure"]
related: ["[[topology]]", "[[continuous-functions]]", "[[compactness]]", "[[limit]]", "[[real-numbers]]"]
requires: ["[[set-theory]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Closed Interval

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **closed interval** is a set of real numbers of the form $[a, b] = \{x : a \leq x \leq b\}$, including both endpoints *a* and *b*. This simple yet fundamental concept is essential to analysis: closed intervals are compact in the real numbers, making them the setting where continuous functions attain their maximum and minimum values, as guaranteed by the [[extreme-value-theorem]].

## you gotta know

- A **closed interval** $[a, b]$ includes both boundary points, expressed symbolically as $a \leq x \leq b$.
- The complement of a closed interval is an open set; a closed interval is the closure of the open interval $(a, b)$.
- [[compactness]] in the real numbers is characterized by being closed and bounded; all closed intervals are compact.
- On a closed interval, every [[continuous-functions|continuous function]] attains its maximum and minimum values—a foundational result in analysis.
- Closed intervals are *sequentially compact*: every sequence in a closed interval has a convergent subsequence (Bolzano-Weierstrass theorem).
- The Heine-Borel theorem states that a subset of Euclidean space is compact if and only if it is closed and bounded.
- Closed intervals form the basis for [[limit|limits]] and [[continuity]] in single-variable calculus.
- The nested interval property guarantees that the intersection of a decreasing sequence of non-empty closed intervals is non-empty, a key tool in proving existence results.
- Riemann integrability is defined on closed intervals; the fundamental theorem of calculus connects integration and differentiation specifically on closed domains.

## connections

- [[topology]] — closed intervals exemplify closed sets in the standard topology on the reals.
- [[continuous-functions]] — the extreme-value theorem applies specifically to continuous functions on closed intervals.
- [[compactness]] — closed intervals in the reals are the prototypical example of compact sets.
- [[limit]] — the definition of limits relies on intervals to formalize neighborhood concepts.
- [[extreme-value-theorem]] — its conclusion requires the domain to be a closed interval.

## see also

- [[topology]] · [[compactness]] · [[continuous-functions]] · [[extreme-value-theorem]]

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
