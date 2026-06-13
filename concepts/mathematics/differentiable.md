---
type: concept
category: mathematics
defines: [Differentiable, differentiability]
related: ["[[derivative]]", "[[continuity]]"]
lists: []
read: false
---

# Differentiable

## summary

A function is *differentiable* at a point if its derivative exists at that point—the limit defining the derivative converges. Differentiability is a stronger condition than continuity: if f is differentiable at a, then f must be continuous at a, but a continuous function need not be differentiable (e.g., the absolute value function |x| is continuous everywhere but not differentiable at x = 0, where there is a sharp corner). A function is differentiable on an interval if the derivative exists at every point in that interval.

## you gotta know

### The Definition
- f is differentiable at a if lim(h→0) [f(a+h) – f(a)] / h exists (is finite).
- If the derivative exists, it is unique; there is at most one tangent line at a.
- Differentiability implies continuity: if f'(a) exists, then f is continuous at a.

### Failure of Differentiability
- Corners or sharp turns: f(x) = |x| is continuous at 0 but not differentiable there (left and right derivatives differ).
- Vertical tangents: f(x) = ∛x is continuous at 0 but has an undefined (vertical) tangent.
- Discontinuities: if f is not continuous at a, it cannot be differentiable there.
- Cusps and wild oscillations: any abrupt change in direction or undefined slope prevents differentiability.

### Differentiability on Intervals
- A function is *continuously differentiable* (C¹) if both f and f' are continuous.
- Higher smoothness: C² means f'' is continuous; C^∞ means all derivatives are continuous (smooth functions).
- Piecewise-defined functions may be differentiable everywhere by piecing together differentiable pieces, but edges (corners) break differentiability.

## context

Differentiability is the formal guarantee that a function "behaves nicely" around a point—it has a well-defined tangent line, no sharp corners, and can be approximated locally by a line (first-order Taylor expansion). In physics and engineering, modeling with differential equations implicitly assumes differentiability: if you cannot differentiate position to get velocity, you cannot set up F = ma. Quiz-bowl questions test whether you can identify non-differentiable points graphically (corners, cusps), explain why differentiability is stronger than continuity, or apply differentiability to justify a solution technique (e.g., "we can differentiate both sides because f is differentiable").

## connections

- [[derivative]] — a function is differentiable iff its derivative exists.
- [[continuity]] — differentiability implies continuity, but not vice versa.
- [[taylor-series]] — Taylor series require the function to be infinitely differentiable at the center point.

## see also

- [[derivative]] · [[continuity]] · [[taylor-series]]

<!-- footer -->

---

Lists:  · Mark read: `INPUT[toggle:read]`
