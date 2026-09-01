---
type: concept
category: mathematics
defines: [Euler-Lagrange equation, Variational calculus]
related: ["[[lagrange]]", "[[leonhard-euler]]", "[[calculus-of-variations]]"]
requires: ["[[calculus]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Euler-Lagrange Equations

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Euler-Lagrange equations** are the fundamental differential equations that govern stationary points of variational problems. They arise when minimizing or maximizing a functional (a function of functions). These equations unify mechanics, optics, and field theory, expressing the principle that nature follows paths of stationary action.

## you gotta know

- Arises from the *calculus of variations*: for a functional *S* = ∫ *L*(*y*, *y'*, *t*) *dt*, paths making *S* stationary satisfy ∂*L*/∂*y* − d/d*t*(∂*L*/∂*y'*) = 0 (the Euler-Lagrange equation).
- In classical mechanics, the *Lagrangian* *L* = *T* − *V* (kinetic minus potential energy); stationary action principle yields Newton's equations of motion from pure variational principle.
- The *Hamiltonian* formulation *H* = *T* + *V* (total energy) is symplectically equivalent but often more convenient, especially in quantum mechanics and integrable systems.
- *Principle of least action* (Hamilton's principle): physical systems follow paths that render the action stationary (usually a minimum), not arbitrary paths; encodes the whole dynamical law.
- *Generalized coordinates*: for constrained systems, Lagrange formulation automatically handles constraints; one Euler-Lagrange equation per degree of freedom, no constraint forces needed.
- Central to deriving conservation laws: *Noether's theorem* states each continuous symmetry of the Lagrangian yields a conservation law (translation → momentum, rotation → angular momentum, time-invariance → energy).
- Applies universally: rigid body dynamics, fluid mechanics, electromagnetism (Maxwell's equations from an action), field theory, and quantum mechanics (path integral formulation).
- *Lagrange multipliers* solve constrained optimization problems: for optimizing *f*(x) subject to *g*(x) = 0, the Lagrangian is ℒ = *f* − λ*g*, leading to ∇*f* = λ∇*g*.
- The **Euler-Lagrange equations** are second-order differential equations; their general solution involves integration constants determined by initial or boundary conditions (Dirichlet or Neumann).
- In field theory, the Euler-Lagrange equations apply to fields φ(*x*, *t*) rather than particles; yields partial differential equations governing wave equations, Klein-Gordon, and quantum field equations.

## connections

- [[lagrange]] — developed this formulation in the late 18th century, generalizing Euler's work.
- [[leonhard-euler]] — foundational work in variational calculus; Euler-Lagrange equations bear both names.
- [[calculus-of-variations]] — the broader field studying extrema of functionals.
- [[isaac-newton]] — Newton's laws are the starting point; Lagrange recast them more elegantly.
- [[william-rowan-hamilton]] — developed the Hamiltonian formalism, an equivalent but often more powerful approach.

## see also

[[lagrange]] · [[leonhard-euler]] · [[calculus-of-variations]] · [[william-rowan-hamilton]]

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
