---
type: term
category: mathematics
defines: [Differentiable Function, Differentiability]
related: ["[[derivative]]", "[[continuous-functions]]", "[[mean-value-theorem]]", "[[polynomial-function]]"]
requires: ["[[calculus]]", "[[continuity]]"]
lists: ["[[classifications-of-functions]]"]
tour_order: 1
read: false
---

# Differentiable Function


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A *differentiable function* is one that has a well-defined derivative at every point in its domain—a measure of how the function's output changes with its input. Differentiability is stronger than continuity; it requires smoothness with no sharp corners or cusps, making it central to optimization, modeling motion, and the entire edifice of calculus.

## you gotta know

- A function *f* is differentiable at *x* = *a* if the derivative `f'(a) = lim (h → 0) [f(a+h) − f(a)] / h` exists (the slope of the tangent line).
- Differentiability implies continuity, but not vice versa; a continuous function like *f*(*x*) = |*x*| is not differentiable at *x* = 0 (corner).
- All polynomial, exponential, and trigonometric functions are differentiable on their natural domains.
- The derivative tells the rate of change; positive derivative means increasing, negative means decreasing, zero means a critical point (local extremum).
- The *Mean Value Theorem* (a cornerstone result) states: if *f* is differentiable on [*a*, *b*], there exists *c* in (*a*, *b*) where `f'(c) = [f(b) − f(a)] / (b − a)`.
- Higher derivatives measure concavity: `f''(x)` > 0 means concave up (bowl-shaped); `f''(x)` < 0 means concave down (arch-shaped).

## connections

- [[derivative]] — the central concept; *f* is differentiable if *f'* exists.
- [[continuous-functions]] — differentiability implies continuity.
- [[mean-value-theorem]] — a fundamental result for differentiable functions.
- [[polynomial-function]] — all polynomials are differentiable everywhere.

## see also

- [[derivative]] · [[continuous-functions]] · [[mean-value-theorem]] · [[polynomial-function]]

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
