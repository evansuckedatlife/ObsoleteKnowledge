---
type: concept
category: mathematics
defines: [Function, Mapping]
related: ["[[composition]]", "[[inverse-function]]", "[[limit]]"]
requires: ["[[set-theory]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Function

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **function** is a fundamental mathematical object that assigns to each element of one set (the domain) exactly one element of another set (the codomain). Functions formalize the idea of a rule or correspondence; they are the building blocks of analysis, algebra, and all modern mathematics. Every equation *y* = *f*(*x*) encodes a function.

## you gotta know

- Formally, a **function** *f*: *A* → *B* assigns to each element *x* ∈ *A* (domain) exactly one element *f*(*x*) ∈ *B* (codomain); defined as a set of ordered pairs with no repeated first coordinates.
- The *domain* is the set of valid inputs *A*; the *codomain* is the target set *B* (possibly larger than the actual outputs); the *range* or *image* is {*f*(*x*) : *x* ∈ *A*}.
- *Injective* (one-to-one): *f*(*x*₁) = *f*(*x*₂) ⟹ *x*₁ = *x*₂; *surjective* (onto): every *y* ∈ *B* is *f*(*x*) for some *x*; *bijective*: both (one-to-one correspondence, exists inverse).
- *Composition* *f* ∘ *g*: if *g*: *A* → *B* and *f*: *B* → *C*, then (*f* ∘ *g*)(*x*) = *f*(*g*(*x*)); composition is associative but generally not commutative.
- *Inverse function* *f*⁻¹: *B* → *A* satisfies *f*⁻¹(*f*(*x*)) = *x* and *f*(*f*⁻¹(*y*)) = *y*; exists if and only if *f* is bijective.
- *Continuity* at *x₀*: lim_{x→x₀} *f*(*x*) = *f*(*x₀*); continuous functions on compact spaces attain their maximum and minimum values (extreme value theorem).
- Functions formalize the idea of dependence and are central to calculus, linear algebra, analysis, and all mathematics; higher-dimensional functions underlie vector calculus and multivariable analysis.
- *Partial functions* may be undefined on parts of their domain; in computability theory, partial recursive functions distinguish computable functions that may not terminate.
- *Higher-order functions* (functions taking or returning other functions) appear in functional programming, lambda calculus, and abstract mathematics; currying converts *n*-ary **functions** into nested unary **functions**.

## connections

- [[composition]] — functions naturally compose, creating hierarchies and complex transformations.
- [[inverse-function]] — the inverse formalizes the idea of "undoing" a function.
- [[limit]] — continuity of a function is defined using limits.
- [[continuous-functions]] — the subset of functions preserving topological or metric structure.
- [[polynomial-function]] — a classical and important class of functions.

## see also

[[composition]] · [[inverse-function]] · [[continuous-functions]] · [[limit]]

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
