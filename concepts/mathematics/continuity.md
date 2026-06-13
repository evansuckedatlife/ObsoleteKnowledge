---
type: concept
category: mathematics
defines: [Continuity, continuous, discontinuous]
related: ["[[limit]]", "[[intermediate-value-theorem]]"]
lists: ["[[calculus-ideas]]"]
read: false
---

# Continuity

## summary

A function is *continuous* at a point if the limit of the function as x approaches that point equals the function's value at that point—no jumps, gaps, or breaks. Continuity is essential to calculus: derivatives and integrals are defined only for continuous (or piecewise-continuous) functions, and continuous functions on closed intervals behave nicely (they attain their maximum and minimum).

## you gotta know

### Formal Definition
- f is continuous at a iff lim(x→a) f(x) = f(a); the limit exists, the function is defined, and they agree.
- f is continuous on an interval if it is continuous at every point in that interval.
- Three types of discontinuity: *removable* (hole that could be "fixed"), *jump* (left and right limits differ), and *infinite* (vertical asymptote).

### Examples and Types
- Polynomials and rational functions (away from poles) are continuous everywhere.
- sin(x), cos(x), e^x are continuous everywhere; 1/x is continuous except at x = 0.
- f(x) = {x if x ≠ 1; 5 if x = 1} has a removable discontinuity at x = 1.
- Floor function ⌊x⌋ has jump discontinuities at every integer.

### Theorems Requiring Continuity
- *Intermediate Value Theorem*: if f is continuous on [a, b] and y is between f(a) and f(b), then f(c) = y for some c ∈ [a, b].
- *Extreme Value Theorem*: a continuous function on a closed interval attains its max and min.

## context

Continuity is the mathematician's way of formalizing the intuition that "nearby inputs give nearby outputs." It is essential scaffolding for calculus: you cannot differentiate or integrate at a discontinuity. Quiz-bowl questions test whether you can identify discontinuities graphically, classify them, apply the Intermediate Value Theorem (IVT), or recognize that a continuous function on a closed interval must attain certain values. Continuity also appears in topology and analysis more broadly.

## connections

- [[limit]] — continuity is defined via limits.
- [[derivative]] — a function must be continuous at a point to be differentiable there (though continuity alone doesn't guarantee differentiability).
- [[intermediate-value-theorem]] — IVT is a key application of continuity to existence proofs.
- [[extreme-value-theorem]] — EWT requires continuity on a closed interval.
- [[riemann-sums]] — Riemann integrability requires continuity (or weak variants).

## see also

- [[limit]] · [[derivative]] · [[integral]]

<!-- footer -->

---

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
