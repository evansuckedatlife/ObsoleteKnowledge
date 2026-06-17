---
type: list
category: mathematics
read: false
---

# ideas from calculus

The ideas from calculus most worth knowing for quiz bowl.

## nodes

- [[chain-rule|Chain Rule]] — The chain rule is the fundamental technique for differentiating composite functions: if y = f(g(x)), then dy/dx = f'(g(x)) ·…
- [[derivative|Derivative]] — The derivative of a function measures its instantaneous rate of change at a point—the slope of the tangent line to the curve.
- [[fundamental-theorem-of-calculus|Fundamental Theorem of Calculus]] — The Fundamental Theorem of Calculus states that differentiation and integration are inverse operations.
- [[integral|Integral]] — An integral is either the antiderivative of a function (indefinite integral) or the signed area under a curve (definite integral).
- [[limit|Limit]] — A limit is the value that a function or sequence approaches as the input approaches some value.
- [[mean-value-theorem|Mean Value Theorem]] — The Mean Value Theorem (MVT) states that for a function continuous on a closed interval [a, b] and differentiable on the open…
- [[optimization-problem|Optimization Problem]] — An optimization problem seeks the best solution from a set of candidates according to some criterion—maximizing profit,…
- [[partial-derivative|Partial Derivative]] — A partial derivative of a multivariable function is its derivative with respect to one variable while holding all other…
- [[riemann-sums|Riemann Sums]] — Riemann sums are approximations to the area under a curve, formed by partitioning the interval [a, b] into subintervals,…
- [[taylor-series|Taylor Series]] — A Taylor series is a power series expansion of a function centered at a point, built from the function's derivatives: f(x) =…

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
      - property: tour_order
        direction: ASC
      - property: file.name
        direction: ASC
```
