---
type: concept
category: mathematics
defines: [Limit, limits]
related: ["[[continuity]]", "[[derivative]]", "[[riemann-sums]]"]
lists: ["[[calculus-ideas]]"]
read: false
---

# Limit

## summary

A *limit* is the value that a function or sequence approaches as the input approaches some value. Limits are the foundational concept underlying calculus—they make rigorous the intuitive idea of "getting arbitrarily close." The formal definition (epsilon-delta) bounds how close the output is to the target for inputs sufficiently close to a point. By defining behavior near a point rather than exactly at it, limits resolve the logical paradoxes of division by zero that historically plagued the study of motion. This framework allows mathematicians to define key concepts like continuity, derivatives, and integrals on solid logical footing.

## you gotta know

### Core Concept
- A limit is written as lim(x→a) f(x) = L, meaning f(x) gets arbitrarily close to L as x approaches a.
- The limit may exist even if f(a) is undefined or different from L (the value at the point doesn't matter).
- Limits can be one-sided: left-limit (x → a⁻) and right-limit (x → a⁺) may differ.

### Key Examples
- lim(x→0) sin(x)/x = 1, a crucial limit in analysis.
- lim(x→∞) 1/x = 0; limits at infinity describe end-behavior of functions.
- Discontinuities: lim(x→a⁻) f(x) ≠ lim(x→a⁺) f(x) signals a jump discontinuity.

### Formal Rigor
- *Epsilon-delta definition*: for any ε > 0, there exists δ > 0 such that |x – a| < δ implies |f(x) – L| < ε.
- Limit laws: sum, product, quotient, and composition rules allow combining limits algebraically.
- Squeeze theorem: if g(x) ≤ f(x) ≤ h(x) near a and lim(x→a) g(x) = lim(x→a) h(x) = L, then lim(x→a) f(x) = L.

## context

Limits are the invisible machinery of calculus. Without them, derivatives and integrals are no more rigorous than hand-waving. The epsilon-delta formalism, while abstract, is what separates calculus from merely-plausible reasoning about rates of change. Quiz-bowl questions often test whether you can compute limits algebraically (factoring, conjugates, L'Hôpital's rule) or recognize limit types (0/0 indeterminate forms, oscillation, infinite). Limits also appear in sequences, series, and the definition of continuity.

## connections

- [[continuity]] — a function is continuous at a point iff the limit equals the function value.
- [[derivative]] — the derivative is defined as a limit of secant-line slopes.
- [[riemann-sums]] — the definite integral is the limit of Riemann sums.
- [[fundamental-theorem-of-calculus]] — links limits of sums (integrals) to limits of differences (derivatives).
- [[taylor-series]] — power series are defined as limits of partial sums of polynomials.
- [[epsilon-delta-definition]] — the formal underpinning of all limit concepts.

## see also

- [[continuity]] · [[derivative]] · [[integral]]

<!-- footer -->

---

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
