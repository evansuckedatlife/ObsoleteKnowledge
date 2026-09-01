---
type: concept
category: mathematics
defines: [composition, function composition]
related: ["[[inverse-function]]", "[[improvisation]]", "[[algebra]]"]
requires: ["[[derivative]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Composition

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

In mathematics, **composition** refers to applying one function to the output of another, creating a new combined function. Written as *(f ∘ g)(x) = f(g(x))*, function composition is fundamental to calculus, algebra, and the abstract study of functions. The concept appears across mathematics in varying forms and underlies many deep structural insights.

## you gotta know

- Composition is associative—(f ∘ (g ∘ h)) = ((f ∘ g) ∘ h)—allowing multiple functions to be chained without ambiguity, though parentheses become unnecessary.
- The order matters: f ∘ g is generally different from g ∘ f; composition is *not* commutative, reflecting how sequential operations can be sensitive to their order.
- The chain rule in calculus is the rule for computing derivatives of composed functions: d/dx[f(g(x))] = f'(g(x)) · g'(x), which lies at the heart of calculus applications.
- In abstract algebra, composition of operations defines group multiplication and other algebraic structures; group theory is fundamentally about composable transformations.
- Inverse functions are defined by their composition: f ∘ f⁻¹ and f⁻¹ ∘ f both equal the identity function, providing the formal definition of what "inverse" means.
- Dynamical systems study repeated composition of a function with itself (iteration), revealing chaos, stability, bifurcations, and fractal structures hidden in apparently simple dynamics.
- Function composition enables abstraction and modularity: complex problems are solved by breaking them into simpler composed functions, a principle central to programming and mathematics alike.
- The study of iterated functions (repeatedly composing a function with itself) reveals surprising phenomena: fixed points, periodic orbits, and chaotic behavior emerge from compositions of simple functions.
- In category theory, composition of morphisms (generalized functions) is the fundamental operation; the structure of categories hinges entirely on how objects and morphisms compose according to strict associativity rules.

## connections

- [[inverse-function]] — the function whose composition with f recovers the identity.
- [[derivative]] — the chain rule is the law for derivatives of compositions.
- [[algebra]] — composition of operations is central to abstract algebraic structures.
- [[calculus]] — composition appears throughout integration and differentiation.
- [[function]] — the fundamental object being composed in mathematics.
- [[improvisation]] — in music, real-time creation parallels the generative power of functional composition.

## see also

- [[inverse-function]] · [[derivative]] · [[algebra]]

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
