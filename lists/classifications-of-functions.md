---
type: list
category: mathematics
read: false
---

# classifications of mathematical functions

The classifications of mathematical functions most worth knowing for quiz bowl.

## nodes

- [[continuous-functions|Continuous Function]] — A continuous function has no jumps, breaks, or holes in its graph; intuitively, you can draw it without lifting your pencil.
- [[differentiable-functions|Differentiable Function]] — A differentiable function is one that has a well-defined derivative at every point in its domain—a measure of how the…
- [[exponential-function|Exponential Function]] — An exponential function has the form `f(x) = aˣ` (or more generally `f(x) = abˣ`), where the variable appears as an exponent…
- [[logarithmic-function|Logarithmic Function]] — A logarithmic function is the inverse of an exponential function, written as `f(x) = logₐ(x)`, and answers "what exponent do I…
- [[monomial-function|Monomial]] — A monomial is a single term consisting of a constant coefficient multiplied by a variable raised to a non-negative integer power.
- [[periodic-function|Periodic Function]] — A periodic function repeats its values at regular intervals; it satisfies `f(x + p) = f(x)` for all x, where p is the period.
- [[polynomial-function|Polynomial Function]] — A polynomial function is an algebraic function composed of a sum of terms, each a constant coefficient times a variable raised…
- [[quadratic-function|Quadratic Function]] — A quadratic function is a polynomial of degree 2, written as `f(x) = ax² + bx + c` with a ≠ 0.
- [[rational-function|Rational Function]] — A rational function is a quotient of two polynomials, written as `f(x) = P(x) / Q(x)`, where both numerator and denominator…
- [[trigonometric-function|Trigonometric Function]] — Trigonometric functions—sine, cosine, tangent, and their reciprocals—relate angles in a right triangle to ratios of its sides.

## progress

Live read-status for this list (requires the **Bases** core plugin). Flip a node's `read` from its footer toggle and it moves here.

```base
filters:
  and:
    - file.hasLink(this.file)
views:
  - type: table
    name: Progress
    order:
      - file.name
      - read
      - type
    sort:
      - property: read
        direction: ASC
      - property: file.name
        direction: ASC
```
