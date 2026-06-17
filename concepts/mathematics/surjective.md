---
type: concept
category: mathematics
defines: [Surjective, surjection, "surjective function", "onto function"]
related: ["[[bijective]]", "[[injective]]", "[[inverse-function]]"]
requires: []
lists: ["[[classifications-of-functions]]"]
tour_order: 0
read: false
---

# Surjective

## summary

A function is *surjective* (or onto) if its range is equal to its codomain, meaning every element in the target set is mapped to by at least one element in the domain. No elements in the codomain are left "unpaired," although multiple elements in the domain are allowed to map to the same output. Surjectivity is a fundamental classification that, alongside injectivity, is required for a function to be bijective.

## you gotta know

- A function *f* from set *A* to set *B* is surjective if for every *b* in *B*, there exists at least one *a* in *A* such that `f(a) = b`.
- Surjectivity depends entirely on the choice of codomain; for example, $f(x) = x^2$ is surjective if the codomain is $[0, \infty)$ but not if the codomain is all real numbers $\mathbb{R}$.
- If a surjection exists from set *A* to set *B*, then the cardinality of *A* is greater than or equal to the cardinality of *B* ($|A| \ge |B|$).
- The composition of two surjective functions is always surjective.
- Under the Axiom of Choice, a function is surjective if and only if it has a right inverse function *g* such that $f(g(y)) = y$ for all $y$ in the codomain.

## connections

- [[bijective]] — a bijection is both surjective and injective.
- [[injective]] — the counterpart to surjectivity; requires distinct inputs to map to distinct outputs.
- [[inverse-function]] — a surjective function has a right inverse.

## see also

- [[bijective]] · [[injective]] · [[monotonic-functions]] · [[periodic-function]]

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
