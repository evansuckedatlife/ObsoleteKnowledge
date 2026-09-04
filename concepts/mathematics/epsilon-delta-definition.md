---
type: concept
category: mathematics
defines: [epsilon-delta-definition, (ε, δ)-definition of limit, Cauchy limit definition]
related: ["[[limit]]", "[[calculus]]", "[[continuous-functions]]", "[[discontinuity]]", "[[derivative]]", "[[isaac-newton]]"]
requires: ["[[limit]]", "[[calculus]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# epsilon-delta-definition

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **epsilon-delta-definition** is the rigorous formulation that formalizes the intuitive notion of a mathematical [[limit]] without relying on vague appeals to infinitesimal quantities. Formulated by *Augustin-Louis Cauchy* and perfected by *Karl Weierstrass* in nineteenth-century *Germany* and *France*, it placed analysis on an unassailable algebraic footing. It serves as the foundational cornerstone of modern [[calculus]], governing the formal proofs of continuity, differentiability, and convergence.

## you gotta know

- States formally that $\lim_{x \to c} f(x) = L$ if and only if for every real $\varepsilon > 0$, there exists a corresponding real $\delta > 0$ such that whenever $0 < |x - c| < \delta$, the inequality $|f(x) - L| < \varepsilon$ must hold.
- The parameter $\varepsilon$ controls the error tolerance or vertical margin around the target value $L$, while $\delta$ prescribes the required input proximity or horizontal radius around $c$.
- Solved the foundational crisis of early modern [[calculus]], banishing dubious "vanishing quantities" championed during the era of [[isaac-newton]] and *Gottfried Wilhelm Leibniz*.
- A function is certified continuous at a point $c$ when the limit $L$ equals $f(c)$, eliminating the strict punctured neighborhood condition $0 < |x - c|$ so that $|x - c| < \delta$ implies $|f(x) - f(c)| < \varepsilon$.
- Serves as the direct instrument used to identify a [[discontinuity]], proven by demonstrating the existence of an $\varepsilon_0 > 0$ for which no suitable $\delta$ can keep outputs confined.
- Generalizes seamlessly to metric spaces and topological spaces, where open balls of radius $\varepsilon$ and $\delta$ define neighborhoods in multivariable analysis and general topology.
- Uniform continuity strengthens this condition across an entire set by requiring a single choice of $\delta$ that works universally for every point in the domain given any fixed $\varepsilon$.

## connections

- [[limit]] — the core analytic concept that this formulation rigorously defines.
- [[calculus]] — the foundational mathematical discipline whose theorems depend upon this precise mechanism.
- [[continuous-functions]] — functions defined globally or locally by satisfying this condition at every input point.
- [[discontinuity]] — points where the quantified condition fails to hold due to jumps, asymptotes, or erratic oscillations.
- [[derivative]] — defined as a differential quotient whose existence hinges strictly on this bounding framework.
- [[isaac-newton]] — early pioneer whose intuitive fluxions were eventually replaced by Weierstrassian precision.

## see also

- [[limit]] · [[continuous-functions]] · [[discontinuity]] · [[derivative]]

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
