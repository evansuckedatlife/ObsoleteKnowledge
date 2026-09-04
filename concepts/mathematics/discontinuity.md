---
type: concept
category: mathematics
defines: [discontinuity, points of discontinuity]
related: ["[[continuous-functions]]", "[[limit]]", "[[calculus]]", "[[epsilon-delta-definition]]", "[[domain-restriction]]", "[[polynomial-function]]"]
requires: ["[[continuous-functions]]", "[[limit]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# discontinuity

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **discontinuity** occurs at a point in the domain or boundary of a real function where the function fails to be continuous, meaning the limit does not exist or does not equal the function's value. Classified systematically in nineteenth-century analysis, these points reveal essential structural breakdowns in mathematical modeling and curves. Recognizing and categorizing discontinuities is vital across [[calculus]] and mathematical physics for understanding boundary conditions, shock waves, and integrability.

## you gotta know

- A point $x = c$ is a **discontinuity** if the two-sided [[limit]] $\lim_{x \to c} f(x)$ does not exist, or if it exists but does not equal the defined value $f(c)$.
- Removable discontinuities occur where the two-sided limit exists and is finite, but the function is either undefined at that coordinate or evaluated to a different point, creating an isolated hole that can be filled by redefining a single output.
- Jump discontinuities happen when both the left-hand and right-hand one-sided limits exist as finite numbers but are unequal, a classic hallmark of the Heaviside step function and piecewise models.
- Essential or infinite discontinuities arise when at least one of the one-sided limits fails to exist or diverges to infinity, as seen in the vertical asymptotes of rational functions like $f(x) = 1/x$ or rapid oscillations in $f(x) = \sin(1/x)$.
- A function can possess infinitely many or everywhere-dense points of failure, famously demonstrated by the Dirichlet function, which assigns 1 to rational numbers and 0 to irrational numbers.
- Under Darboux's theorem, any function that arises as the [[derivative]] of another function satisfies the intermediate value property, meaning its points of failure cannot include simple jump discontinuities.
- Functions possessing only jump discontinuities or isolated removable points remain Riemann integrable on compact intervals, whereas pathologies with dense disruptions generally require Lebesgue integration.

## connections

- [[continuous-functions]] — the baseline property that breaks down wherever a point of failure occurs.
- [[limit]] — the fundamental limiting behavior whose absence or mismatch defines every non-continuous point.
- [[epsilon-delta-definition]] — provides the formal algebraic criteria through which the negation of continuity is proven.
- [[domain-restriction]] — utilized to excise asymptotes or holes to yield well-behaved continuous sub-domains.
- [[calculus]] — the mathematical branch where classifying non-continuous boundaries governs integration and differentiability.
- [[polynomial-function]] — continuous everywhere on the real line, serving as the canonical smooth contrast to discontinuous rational maps.

## see also

- [[continuous-functions]] · [[limit]] · [[epsilon-delta-definition]] · [[domain-restriction]]

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
