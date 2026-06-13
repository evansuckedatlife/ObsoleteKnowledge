---
type: term
category: mathematics
defines: [Continuous Function, Continuity]
related: ["[[limit]]", "[[differentiable-functions]]", "[[intermediate-value-theorem]]", "[[polynomial-function]]", "[[weierstrass-function]]", "[[topology]]"]
lists: ["[[classifications-of-functions]]"]
read: false
---

# Continuous Function

## summary

A *continuous function* is a mathematical function that displays no sudden changes in value, meaning there are no jumps, breaks, or holes in its graph. Formally, a function is continuous at a point if the limit of the function as the input approaches that point exists and is equal to the function's value at that point. Continuity is a core concept in calculus and analysis, guaranteeing that local behaviors approximate global ones. On closed intervals, continuous functions possess remarkable properties, such as the guarantee of attaining both maximum and minimum values, and mapping to every intermediate value.

## you gotta know

### Definition and Limit Criteria

- A function *f* is continuous at *x* = *a* if the limit as *x* approaches *a* of *f*(*x*) exists, *f*(*a*) is defined, and `lim (x → a) f(x) = f(a)`.
- For functions between metric spaces, continuity is defined via the epsilon-delta definition: for every $\epsilon > 0$ there exists a $\delta > 0$ such that $|x - c| < \delta$ implies $|f(x) - f(c)| < \epsilon$.
- In topology, a function is continuous if and only if the preimage of every open set in the codomain is an open set in the domain.

### Types of Discontinuity

- *Removable discontinuity*: A point where the limit exists but does not equal the function's value (producing a "hole" in the graph).
- *Jump discontinuity*: A point where the left-hand and right-hand limits exist but are not equal (common in piecewise functions like the step function).
- *Infinite discontinuity*: A point where the function approaches positive or negative infinity (typically at vertical asymptotes, such as $f(x) = 1/x$ at $x = 0$).

### Key Theorems

- *Intermediate Value Theorem*: If *f* is continuous on a closed interval [*a*, *b*], then for any value *u* between *f*(*a*) and *f*(*b*), there is at least one *c* in (*a*, *b*) such that *f*(*c*) = *u*.
- *Extreme Value Theorem*: A continuous function on a closed, bounded interval [*a*, *b*] must attain a maximum and a minimum value at least once.
- *Uniform continuity*: A stronger form of continuity where the choice of $\delta$ depends only on $\epsilon$, not on the point *c* in the domain.

### Pathological Examples

- The *Weierstrass function* is a famous example of a function that is continuous everywhere but differentiable nowhere, defying early geometric intuition about continuity.
- The *Dirichlet function* (which outputs 1 for rationals and 0 for irrationals) is discontinuous everywhere, while its modification, the *Thomae function*, is continuous at all irrationals and discontinuous at all rationals.

## context

Continuity formalizes the intuitive physical notion of smooth, unbroken motion, representing processes that do not jump instantaneously from one state to another. In mathematical analysis, it serves as the baseline requirement for most operations: you cannot define derivatives or Riemann integrals without assuming continuity (or at least piecewise continuity). Quiz-bowl questions often test the distinction between continuity and differentiability, the applications of the Intermediate Value Theorem to root-finding, the classification of different kinds of discontinuities, and the topological definition using preimages of open sets.

## connections

- [[limit]] — the fundamental limit process is used to define continuity.
- [[differentiable-functions]] — differentiability is a strictly stronger condition than continuity.
- [[intermediate-value-theorem]] — a key existence theorem that requires continuity.
- [[extreme-value-theorem]] — guarantees extreme values for continuous functions on closed intervals.
- [[weierstrass-function]] — a counterexample showing continuity does not imply differentiability.
- [[topology]] — generalizes continuity to abstract topological spaces via open sets.

## see also

- [[limit]] · [[differentiable-functions]] · [[bijective]] · [[monotonic-functions]] · [[analytic-functions]]

<!-- footer -->

---

Lists: [[classifications-of-functions]] · Mark read: `INPUT[toggle:read]`
