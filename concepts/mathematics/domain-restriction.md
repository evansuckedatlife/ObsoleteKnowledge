---
type: concept
category: mathematics
defines: [domain restriction, restricted domain]
related: ["[[trigonometric-function]]", "[[continuous-functions]]", "[[calculus]]", "[[discontinuity]]", "[[polynomial-function]]", "[[periodic-function]]"]
requires: ["[[continuous-functions]]", "[[calculus]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# domain-restriction

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **domain restriction** is the mathematical practice of truncating the allowable input set of a relation or function to a smaller designated subset. Developed systematically within modern set-theoretic analysis, it allows non-injective or non-invertible maps to achieve injectivity and possess single-valued inverses. It is an indispensable tool across [[calculus]] and analysis for isolating branches of multivalued operations and removing singular points.

## you gotta know

- Restricting a mapping $f: X \to Y$ to a subset $A \subset X$ produces a new function, denoted $f|_A: A \to Y$, which evaluates identically on all inputs within $A$.
- A primary application is constructing inverse functions for non-injective mappings by enforcing injectivity, ensuring that every output within the restricted range maps back to a unique input.
- Standard inverse trigonometric relations require strict conventions: the sine function is restricted to $[-\pi/2, \pi/2]$ to yield $\arcsin$, cosine to $[0, \pi]$ for $\arccos$, and tangent to $(-\pi/2, \pi/2)$ for $\arctan$.
- Algebraic functions such as the simple quadratic squaring map $f(x) = x^2$ require pruning negative numbers to the half-line $[0, \infty)$ so that the principal square root function remains single-valued.
- Eliminates points of [[discontinuity]], such as vertical asymptotes or unremovable singular points in rational functions, to yield well-behaved, continuous domains for integration and differentiation.
- Vital in multivariable [[calculus]] and differential geometry when defining coordinate charts and local parameterizations of manifolds.
- Essential in boundary value problems and partial differential equations, where differential operators are restricted to Sobolev spaces satisfying specified Dirichlet or Neumann boundary data.

## connections

- [[trigonometric-function]] — periodic functions that require conventional restrictions to define single-valued inverse branches.
- [[periodic-function]] — classes of functions whose infinite repetition necessitates bounded intervals for invertible isolation.
- [[continuous-functions]] — properties preserved or isolated on closed intervals through strategic domain reduction.
- [[discontinuity]] — singular points and asymptotic breaks excised from broader domains to establish well-behaved maps.
- [[calculus]] — mathematical field where isolating intervals enables definite integration and inverse differentiation.
- [[polynomial-function]] — even-degree polynomial curves whose natural lack of injectivity requires bounded branches for inversion.

## see also

- [[trigonometric-function]] · [[periodic-function]] · [[continuous-functions]] · [[discontinuity]]

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
