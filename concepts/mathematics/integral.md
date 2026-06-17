---
type: concept
category: mathematics
defines: [Integral, integrals, integration, antiderivative]
related: ["[[riemann-sums]]", "[[fundamental-theorem-of-calculus]]", "[[differential-equations]]"]
requires: ["[[calculus]]"]
lists: ["[[calculus-ideas]]"]
tour_order: 1
read: false
---

# Integral


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

An *integral* is either the antiderivative of a function (indefinite integral) or the signed area under a curve (definite integral). The indefinite integral ∫ f(x) dx = F(x) + C is a function whose derivative is f; the definite integral ∫[a,b] f(x) dx is a number representing the net area between the curve and the x-axis. Integrals are the inverse of derivatives and are essential to computing areas, volumes, and accumulating quantities. By formalizing the process of continuous summation, integration resolves the ancient geometric problem of finding the area of shapes with curved boundaries. This operation is crucial in physics for determining total work, electromagnetic flux, and probability distributions in quantum mechanics.

## you gotta know

### Core Concepts
- *Indefinite integral* (antiderivative): ∫ f(x) dx = F(x) + C, where F'(x) = f(x) and C is an arbitrary constant.
- *Definite integral*: ∫[a,b] f(x) dx represents the signed area under the curve from x = a to x = b.
- The *Riemann integral* is defined as the limit of Riemann sums: partition [a,b], form rectangles, and take the limit as partition width → 0.

### Integration Techniques
- *Power rule*: ∫ x^n dx = x^(n+1) / (n+1) + C (for n ≠ –1).
- *Substitution* (u-substitution): reverse the chain rule; ∫ f(g(x)) g'(x) dx = ∫ f(u) du.
- *Integration by parts*: ∫ u dv = uv – ∫ v du; the reverse of the product rule.
- *Partial fractions*: decompose rational functions before integrating.

### The Fundamental Theorem
- If F is an antiderivative of f, then ∫[a,b] f(x) dx = F(b) – F(a)—the definite integral reduces to evaluating the antiderivative at the bounds.

## context

Integration is the twin pillar of calculus, complementing differentiation. While the derivative asks "how fast?", the integral asks "how much total?" This shift enables powerful applications: computing areas and volumes, solving accumulation problems (distance from velocity), and evaluating work and probability. The Fundamental Theorem of Calculus is the crown jewel of calculus because it unites the two concepts: differentiating and integrating are inverse operations. Quiz-bowl questions test integration techniques (u-substitution, by parts), the interpretation of definite integrals as areas, and applications to modeling and physics.

## connections

- [[riemann-sums]] — the formal definition of the definite integral.
- [[fundamental-theorem-of-calculus]] — links integration and differentiation.
- [[derivative]] — the derivative and integral are inverse operations.
- [[differential-equations]] — differential equations are often solved via integration.
- [[taylor-series]] — term-by-term integration of power series.
- [[gottfried-leibniz]] — co-creator of calculus who introduced the integration symbol (∫).

## see also

- [[riemann-sums]] · [[fundamental-theorem-of-calculus]] · [[derivative]]

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

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
