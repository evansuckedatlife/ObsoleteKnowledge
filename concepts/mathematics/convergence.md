---
type: concept
category: mathematics
defines: [Convergence, Convergent series, Convergent sequence]
related: ["[[limit]]", "[[calculus]]", "[[derivative]]", "[[power-series]]", "[[fourier-series]]", "[[continuous-functions]]", "[[de-la-vallee-poussin]]"]
requires: ["[[limit]]", "[[calculus]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Convergence

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

In mathematical analysis, **convergence** describes the property of an infinite sequence, series, or improper integral approaching a single well-defined limiting value as its index or domain grows arbitrarily large. Formulated rigorously during the nineteenth-century arithmetization of [[calculus]] by *Augustin-Louis Cauchy* and *Karl Weierstrass*, the concept replaces vague notions of infinitesimals with precise epsilon-delta and epsilon-N criteria. Determining whether an infinite process achieves a finite [[limit]] underpins the theory of function spaces, differential equations, and numerical analysis.

## you gotta know

- A sequence exhibits **convergence** if, for every positive epsilon, there exists an integer threshold beyond which all terms lie strictly within an epsilon neighbourhood of the limit.
- A series of numbers is a **convergent series** if its sequence of partial sums tends to a finite limit, whereas an oscillating or unbounded summation is classified as divergent.
- Common tests for the behaviour of infinite series include the ratio test of *Jean le Rond d'Alembert*, the root test of *Augustin-Louis Cauchy*, and the integral test of *Colin Maclaurin*.
- Distinguishes absolute convergence, where the sum of absolute values remains finite, from conditional convergence, where terms sum to a finite value only due to sign alternations.
- The *Riemann* series theorem demonstrates that any conditionally **convergent series** of real numbers can be rearranged to equal any chosen real number or to diverge.
- For functions, uniform convergence requires a single threshold to suffice across the entire domain, guaranteeing that limits of [[continuous-functions]] remain continuous.
- The radius of a [[power-series]] establishes a boundary disk in the complex plane inside which terms converge absolutely, determined via the *Cauchy*-*Hadamard* theorem.
- Fourier analysis investigates whether trigonometric expansions converge pointwise or in mean square, solved for square-integrable functions by *Lennart Carleson*.

## connections

- [[limit]] — the fundamental quantitative value that a sequence or partial sum must approach to demonstrate convergence.
- [[calculus]] — the foundational branch of mathematics whose rigorous operations rely entirely upon convergent limits.
- [[derivative]] — defined as the convergent value of difference quotients as the interval shrinks to zero.
- [[power-series]] — infinite polynomial representations whose validity is governed by their radius and interval of convergence.
- [[continuous-functions]] — preserve limits under function evaluation and arise as the uniform limits of continuous sequences.
- [[fourier-series]] — infinite sums of sines and cosines whose convergence behaviour prompted modern set theory and real analysis.
- [[de-la-vallee-poussin]] — analyzed the convergence of Fourier sums and formulated summation kernels that guarantee uniform convergence.

## see also

- [[limit]] · [[power-series]] · [[continuous-functions]] · [[fourier-series]]

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
