---
type: concept
category: mathematics
defines: ["Monotonic Function", Monotonicity, "monotonic functions", "increasing function", "decreasing function"]
related: ["[[derivative]]", "[[injective]]", "[[continuous-functions]]"]
requires: ["[[calculus]]"]
lists: ["[[classifications-of-functions]]"]
tour_order: 1
read: false
---

# Monotonic Function


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A *monotonic function* is a function between ordered sets that preserves or reverses the given order. For real-valued functions, this means the function is either entirely non-increasing or entirely non-decreasing. Monotonicity simplifies the analysis of function behavior, guarantees the existence of limits, and is closely tied to injectivity and differentiability.

## you gotta know

- A function is *monotonically increasing* (or non-decreasing) if $x \le y$ implies $f(x) \le f(y)$.
- A function is *monotonically decreasing* (or non-increasing) if $x \le y$ implies $f(x) \ge f(y)$.
- If the inequalities are strict ($x < y$ implies $f(x) < f(y)$ or $f(x) > f(y)$), the function is *strictly monotonic*.
- For differentiable functions, monotonicity on an interval can be verified using the derivative: $f'(x) \ge 0$ implies the function is increasing, while $f'(x) \le 0$ implies it is decreasing.
- Any strictly monotonic function is injective (one-to-one), which guarantees it has a well-defined inverse on its range.
- The *Monotone Convergence Theorem* states that any bounded monotonic sequence of real numbers converges to a limit.

## connections

- [[derivative]] — the sign of the derivative determines local monotonicity.
- [[injective]] — strict monotonicity is a sufficient condition for a function to be injective.
- [[continuous-functions]] — continuous monotonic functions have continuous inverses.

## see also

- [[bijective]] · [[injective]] · [[surjective]] · [[continuous-functions]] · [[differentiable-functions]]

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
