---
type: concept
category: mathematics
defines: ["Fundamental Theorem of Calculus", FTC]
related: ["[[integral]]", "[[derivative]]", "[[riemann-sums]]"]
lists: ["[[calculus-ideas]]"]
read: false
---

# Fundamental Theorem of Calculus

## summary

The *Fundamental Theorem of Calculus* states that differentiation and integration are inverse operations. In two parts: the first part says that if F is continuous and f is its derivative, then ∫[a,b] f(x) dx = F(b) – F(a); the second part says that differentiation undoes integration—d/dx ∫[a,x] f(t) dt = f(x). This theorem is the bridge connecting discrete sums to continuous accumulation and is arguably the most powerful result in calculus. By linking the rate of change of a function with its cumulative area, this theorem resolves the dual nature of calculus as originally conceived. It provides a practical, algebraic method for evaluating integrals without resorting to tedious limits of sums, serving as the ultimate justification for using differentiation and integration as complementary tools.

## you gotta know

### Part 1 (Integration-Differentiation)
- If f is continuous on [a, b] and F is any antiderivative of f (i.e., F'(x) = f(x)), then ∫[a,b] f(x) dx = F(b) – F(a).
- This reduces the problem of computing a definite integral to finding an antiderivative—often much easier than computing the limit of Riemann sums directly.

### Part 2 (Differentiation-Integration)
- If f is continuous, then d/dx ∫[a,x] f(t) dt = f(x)—differentiating an integral recovers the integrand.
- This says that integration and differentiation are inverse processes (at least for continuous functions).
- If the upper limit of the integral is a function g(x) rather than x, the chain rule must be applied, yielding d/dx ∫[a,g(x)] f(t) dt = f(g(x)) · g'(x).

### Consequences and Significance
- The theorem transforms calculus from a computational tool into a unified framework—answers to "how much accumulated?" can be found via antiderivatives.
- It enables applications across physics: total distance = ∫ velocity; total work = ∫ force; total charge = ∫ current.
- It explains why antiderivatives and indefinite integrals are related—they are, through this theorem.

## context

The Fundamental Theorem of Calculus is the pinnacle of elementary mathematics. It is what makes calculus work: without it, integrals would be computed only through limit-of-sums approximations (slow and hard), and the connection between rate-of-change (derivative) and total-accumulation (integral) would be mysterious. Historically, Newton and Leibniz independently discovered this theorem, and it was the key insight that unified their respective calculi. In quiz bowl, questions test whether you can state the theorem, apply it to evaluate definite integrals, or recognize scenarios where it applies (e.g., relating area under a curve to antiderivative values).

## connections

- [[integral]] — Part 1 shows how to compute definite integrals via antiderivatives.
- [[derivative]] — Part 2 shows differentiation undoes integration.
- [[riemann-sums]] — the FTC shows that the limit of Riemann sums equals F(b) – F(a).
- [[continuity]] — the theorem requires f to be continuous (or Riemann-integrable).
- [[isaac-newton]] — independently discovered and formulated the theorem.
- [[gottfried-leibniz]] — independently formulated the theorem and created the standard notation.

## see also

- [[integral]] · [[derivative]] · [[riemann-sums]]

<!-- footer -->

---

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
