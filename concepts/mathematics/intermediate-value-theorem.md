---
type: concept
category: mathematics
defines: [Intermediate Value Theorem, IVT]
related: ["[[continuous-functions]]", "[[continuity]]", "[[limit]]", "[[extreme-value-theorem]]", "[[topology]]", "[[fixed-point-theorem]]"]
requires: ["[[continuous-functions]]", "[[continuity]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Intermediate Value Theorem

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Intermediate Value Theorem** (IVT) asserts that if a continuous function f takes values f(a) and f(b) at two endpoints, then it must take *every* intermediate value between f(a) and f(b) somewhere in [a, b]. This intuitive but profound result formalizes the idea that a continuous function cannot "jump" over intermediate values. IVT is a foundational existence theorem in calculus, enabling us to prove roots exist without finding them explicitly, and underpinning both theoretical and practical mathematics.

## you gotta know

- *Statement*: If f is continuous on [a, b] and k is any value between f(a) and f(b), then there exists c ∈ [a, b] with f(c) = k; the function *must* hit every intermediate value.
- Requires both *continuity* (no jumps or discontinuities) and that f(a) ≠ f(b) (or more generally: the intermediate value lies strictly between f(a) and f(b)).
- The simplest application: if f(a) < 0 and f(b) > 0, then f must cross zero at some point c ∈ [a, b]—guaranteeing a root exists without explicitly finding it.
- IVT does not tell you *where* the root is, only that it *exists*; numerical methods (bisection, Newton's method, Secant method) then locate it iteratively to any desired precision.
- Fails for discontinuous functions: the step function f(x) = 0 for x ≤ 0 and f(x) = 1 for x > 0 jumps from 0 to 1 without ever taking intermediate values like 0.5.
- Equivalent to the topological statement that *connected* spaces have continuous images that are also *connected*; in ℝ, connected sets are exactly intervals, making IVT a manifestation of connectedness.
- The proof uses the completeness axiom of the real numbers, essentially the supremum property: if a non-empty bounded set has no least upper bound, a contradiction arises.
- Used throughout calculus and analysis for existence proofs; indispensable for establishing fixed-point theorems, optimization results, and the intermediate value property of derivatives.
- Extensions: the generalized intermediate value theorem holds in connected topological spaces, and analogues exist for multivalued and vector-valued functions in higher dimensions.
- Real-world applications include finding break-even points in economics, zero crossings in signal processing, and equilibrium points in dynamical systems.

## connections

- [[continuous-functions]] — continuity is the essential hypothesis; IVT fails without it.
- [[continuity]] — the foundational property enabling the theorem's conclusion.
- [[limit]] — limits formalize the continuity assumption underlying IVT.
- [[extreme-value-theorem]] — another fundamental existence theorem grounded in continuity.
- [[fixed-point-theorem]] — often proved using IVT; if f is continuous on [a, b] and a ≤ f(x) ≤ b for all x ∈ [a, b], then f has a fixed point.
- [[topology]] — IVT reflects connectedness; continuous images of connected spaces are connected.

## see also

[[continuous-functions]] · [[extreme-value-theorem]] · [[fixed-point-theorem]] · [[topology]]

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
