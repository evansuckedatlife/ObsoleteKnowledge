---
type: term
category: mathematics
defines: [Inverse function, functional inverse, one-to-one correspondence]
related: ["[[function]]", "[[bijective]]", "[[composition]]", "[[logarithm]]", "[[trigonometric-function]]", "[[inverse-trigonometric-function]]"]
lists: []
read: false
---

# Inverse Function

## summary

An **inverse function** is a function that "undoes" the action of another function. If f maps an element x to f(x), then the inverse function f^(-1) maps f(x) back to x. Inverse functions exist only for bijections (one-to-one and onto functions). They are essential across mathematics: logarithms are inverses of exponentials; inverse trigonometric functions (arcsin, arccos, arctan) are inverses of sine, cosine, tangent; and matrix inverses solve systems of linear equations.

## you gotta know

- **Definition**: f^(-1) is the inverse of f if f(f^(-1)(x)) = x and f^(-1)(f(x)) = x for all x in the respective domains.
- **Existence condition**: f has an inverse if and only if f is bijective (one-to-one/injective and onto/surjective).
- **One-to-one (injective)**: f(a) = f(b) implies a = b; each output corresponds to exactly one input.
- **Onto (surjective)**: every element in the codomain is mapped to by some input; no outputs are "missed."
- **Graphical interpretation**: the graph of f^(-1) is the reflection of the graph of f across the line y = x.
- **Composition property**: (f ∘ f^(-1))(x) = x and (f^(-1) ∘ f)(x) = x; composition with the inverse yields the identity function.
- **Derivative of inverse function**: if f is differentiable and invertible, then (f^(-1))'(y) = 1/f'(f^(-1)(y))—relating the slopes of f and f^(-1).
- **Examples**: f(x) = 2x has inverse f^(-1)(x) = x/2; f(x) = e^x has inverse f^(-1)(x) = ln(x); sin and arcsin are inverses (on restricted domains).

## context

Inverse functions are a cornerstone of algebra and calculus. In algebra, solving equations is fundamentally about finding inverse functions—to solve f(x) = y, you apply f^(-1) to both sides. In calculus, inverse function theorems ensure smooth invertibility under regularity conditions and enable differentiation of implicitly defined functions. The concept scales to linear algebra (matrix inverses solve Ax = b) and functional analysis (inverse operators on Banach/Hilbert spaces). Logarithms were computationally indispensable in pre-calculator eras, inverting the exponential function to turn multiplication into addition. Inverse trigonometric functions enable solving equations like sin(x) = a, crucial in physics and engineering. Modern applications span: cryptography (finding inverses of complicated functions is hard, hence security); numerical methods (Newton's method approximates f^(-1) iteratively); and deep learning (invertible neural networks encode symmetries).

## connections

- [[function]] — inverse functions are functions with special properties.
- [[bijective]] — a function has an inverse if and only if it is bijective (injective and surjective).
- [[composition]] — composition with the inverse yields the identity function.
- [[logarithm]] — the inverse of exponential functions.
- [[inverse-trigonometric-function]] — arcsin, arccos, arctan are inverses of trig functions.
- [[one-to-one]] — injectivity is necessary for an inverse to exist.
- [[domain-and-range]] — restricting domain is often needed to ensure injectivity.
- [[implicit-function-theorem]] — enables inversion in multivariable calculus.

## see also

- [[function]] · [[bijective]] · [[logarithm]]

<!-- footer -->

---

Lists: Mark read: `INPUT[toggle:read]`
