---
type: concept
category: mathematics
defines: [Injective, injection, "injective function", "one-to-one function"]
related: ["[[bijective]]", "[[surjective]]", "[[inverse-function]]"]
requires: []
lists: ["[[classifications-of-functions]]"]
tour_order: 0
read: false
---

# Injective

## summary

A function is *injective* (or one-to-one) if it maps distinct elements of its domain to distinct elements of its codomain. In other words, no two different inputs produce the same output, meaning that each element in the range is mapped to by exactly one element in the domain. Injective functions are essential for establishing unique relations, and they form one of the two halves required for a function to be bijective.

## you gotta know

- A function *f* from set *A* to set *B* is injective if for all *x* and *y* in *A*, `f(x) = f(y)` implies `x = y`.
- On a coordinate graph, a real-valued function is injective if and only if it passes the *Horizontal Line Test*: no horizontal line intersects the graph more than once.
- Strictly monotonic functions (always strictly increasing or strictly decreasing) on an interval are guaranteed to be injective on that interval.
- If an injection exists from set *A* to set *B*, the cardinality of *A* is less than or equal to the cardinality of *B* ($|A| \le |B|$).
- The composition of two injective functions is always injective.
- Unlike bijections, an injective function does not need to cover the entire codomain; elements in the codomain may have no inputs mapping to them.

## connections

- [[bijective]] — a bijection is a function that is both injective and surjective.
- [[surjective]] — the counterpart to injectivity; covers the codomain.
- [[inverse-function]] — an injective function has a well-defined left inverse.
- [[monotonic-functions]] — strict monotonicity guarantees injectivity.

## see also

- [[bijective]] · [[surjective]] · [[monotonic-functions]] · [[even-odd-functions]]

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

Lists: [[classifications-of-functions]] · Mark read: `INPUT[toggle:read]`
