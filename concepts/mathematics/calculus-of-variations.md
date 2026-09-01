---
type: concept
category: mathematics
defines: [calculus of variations, extremal]
related: ["[[leonhard-euler]]", "[[lagrange]]", "[[euler-lagrange-equations]]", "[[optimization-problem]]", "[[differential-equations]]"]
requires: ["[[calculus]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Calculus of Variations

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **calculus of variations** is the field of mathematics that generalizes calculus to optimize functionals—functions whose inputs are themselves functions rather than numbers. Instead of finding numbers that minimize or maximize a function, variational calculus finds entire functions that optimize a quantity (like path length, energy, or action), yielding the [[euler-lagrange-equations]] as its central result.

## you gotta know

- A *functional* is a map from a space of functions to the real numbers; the **calculus of variations** optimizes these functionals.
- The prototypical problem asks: among all curves connecting two points, which has the shortest length? (The answer: a straight line.)
- An *extremal* is a function that satisfies the conditions for a functional to be minimized or maximized.
- The [[euler-lagrange-equations]] provide the differential equation that any extremal must satisfy, reducing optimization over infinite-dimensional function spaces to solving ordinary or partial differential equations.
- *Variational principles* pervade physics: the principle of least action states that physical systems follow paths that extremize action, recovering Newton's laws, Maxwell's equations, and quantum mechanics.
- The method involves computing the *variation* of a functional—a generalization of the derivative to infinite dimensions.
- Applications span classical mechanics (finding geodesics), beam deflection in engineering, and optimal control theory.
- The brachistochrone problem—finding the fastest path for a particle to slide from one point to another under gravity—was historically the defining challenge that motivated the field's development.
- Constraints are handled via Lagrange multipliers; isoperimetric problems (optimizing area subject to fixed perimeter) exemplify this technique in variational contexts.

## connections

- [[euler-lagrange-equations]] — the fundamental differential equation governing extremals.
- [[lagrange]] — developed the key techniques and equations of variational calculus.
- [[leonhard-euler]] — pioneered the field alongside and in correspondence with [[lagrange]].
- [[optimization-problem]] — variational calculus solves the infinite-dimensional optimization problems.
- [[differential-equations]] — extremals satisfy differential equations derived from variational principles.

## see also

- [[euler-lagrange-equations]] · [[lagrange]] · [[leonhard-euler]] · [[differential-equations]]

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
