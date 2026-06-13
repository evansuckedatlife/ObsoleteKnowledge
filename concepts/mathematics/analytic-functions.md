---
type: concept
category: mathematics
defines: ["Analytic Function", analyticity, "analytic functions"]
related: ["[[differentiable-functions]]", "[[continuous-functions]]", "[[taylor-series]]", "[[complex-analysis]]"]
lists: ["[[classifications-of-functions]]"]
read: false
---

# Analytic Function

## summary

An *analytic function* is a function that can be locally represented by a convergent power series (specifically, a Taylor series). While real analytic functions are infinitely differentiable ($C^\infty$), complex analytic functions (also called holomorphic functions) have the remarkable property that a single complex derivative guarantees infinite differentiability and analyticity. Analytic functions are central to complex analysis, number theory, and mathematical physics due to their rigidity and smooth behavior.

## you gotta know

- A function *f* is analytic at a point *x*₀ if it can be expressed as a power series $f(x) = \sum_{n=0}^\infty a_n (x - x_0)^n$ that converges to $f(x)$ for all *x* in some neighborhood of *x*₀.
- The class of all real analytic functions on a domain is denoted $C^\omega$, which is a strict subset of $C^\infty$ (infinitely differentiable functions); for example, $f(x) = e^{-1/x^2}$ for $x \neq 0$ and $f(0) = 0$ is $C^\infty$ but not analytic at $x = 0$.
- In complex analysis, analyticity is equivalent to being *holomorphic* (complex-differentiable on an open set).
- *Cauchy-Riemann equations*: A complex function $f(z) = u(x, y) + i v(x, y)$ is analytic if and only if its real and imaginary parts satisfy $\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$.
- *Identity Theorem*: If two analytic functions on a connected domain agree on a subset with an accumulation point, they must agree everywhere on the domain.
- *Liouville's Theorem*: Any bounded, entire (analytic everywhere in the complex plane) function must be constant.

## connections

- [[differentiable-functions]] — complex differentiability guarantees analyticity, but real differentiability does not.
- [[continuous-functions]] — analytic functions are always continuous.
- [[taylor-series]] — the power series representation of an analytic function is its Taylor series.
- [[complex-analysis]] — the branch of mathematics focusing on complex analytic functions.

## see also

- [[differentiable-functions]] · [[continuous-functions]] · [[transcendental-functions]] · [[periodic-function]]

<!-- footer -->

---

Lists: [[classifications-of-functions]] · Mark read: `INPUT[toggle:read]`
