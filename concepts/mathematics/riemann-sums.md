---
type: concept
category: mathematics
defines: ["Riemann Sums", Riemann]
related: ["[[integral]]", "[[limit]]", "[[fundamental-theorem-of-calculus]]"]
lists: ["[[calculus-ideas]]"]
read: false
---

# Riemann Sums

## summary

*Riemann sums* are approximations to the area under a curve, formed by partitioning the interval [a, b] into subintervals, constructing rectangles over each subinterval (using left endpoint, right endpoint, or midpoint), and summing their areas. As the partition width shrinks (the number of rectangles increases), the Riemann sum converges to the *Riemann integral* ∫[a,b] f(x) dx, making Riemann sums the formal definition of what we mean by "the signed area under a curve."

## you gotta know

### The Setup
- Partition [a, b] into n subintervals of width Δx = (b – a) / n.
- Over each subinterval [x_(i–1), x_i], choose a sample point c_i.
- Riemann sum: Σ(i=1 to n) f(c_i) · Δx.

### Types of Riemann Sums
- *Left sum*: use c_i = x_(i–1) (left endpoint of each subinterval).
- *Right sum*: use c_i = x_i (right endpoint).
- *Midpoint sum*: use c_i = (x_(i–1) + x_i) / 2.
- *Trapezoidal rule*: average left and right; approximates the curve with trapezoids instead of rectangles.

### Convergence to the Integral
- As n → ∞ (Δx → 0), the Riemann sum converges to ∫[a,b] f(x) dx for continuous (or Riemann-integrable) functions.
- This limit defines the *definite integral*—no antiderivatives needed, just the area computation.
- Different choices of sample points (left, right, midpoint) all converge to the same integral for continuous f.

## context

Riemann sums are the computational foundation of integration. Conceptually, they bridge intuition (stacking rectangles to approximate area) with formality (the limit defines the integral precisely). In practice, Riemann sums and their cousins (trapezoidal rule, Simpson's rule) are how numerical integration is implemented: computers cannot compute antiderivatives symbolically, so they approximate via Riemann sums. The Fundamental Theorem of Calculus tells us that computing the limit of Riemann sums is equivalent to evaluating F(b) – F(a)—a profound insight that connects area, antiderivatives, and accumulation. Quiz-bowl questions test understanding of how Riemann sums approximate integrals, recognizing overestimates and underestimates, and computing them explicitly for simple functions.

## connections

- [[integral]] — Riemann sums define the definite integral.
- [[limit]] — the integral is the limit of Riemann sums as partition width → 0.
- [[fundamental-theorem-of-calculus]] — the FTC shows Riemann sums equal F(b) – F(a).
- [[continuity]] — continuous functions on closed intervals are Riemann-integrable.

## see also

- [[integral]] · [[limit]] · [[fundamental-theorem-of-calculus]]

<!-- footer -->

---

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
