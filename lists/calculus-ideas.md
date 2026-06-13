---
type: list
category: mathematics
read: false
---

# ideas from calculus

The ideas from calculus most worth knowing for quiz bowl.

## nodes

- [[chain-rule|Chain Rule]] — The chain rule is the technique for differentiating composite functions.
- [[derivative|Derivative]] — The derivative of a function measures its instantaneous rate of change at a point—the slope of the tangent line.
- [[fundamental-theorem-of-calculus|Fundamental Theorem of Calculus]] — The Fundamental Theorem of Calculus states that differentiation and integration are inverse operations.
- [[integral|Integral]] — An integral is either the antiderivative of a function (indefinite) or the signed area under a curve (definite).
- [[limit|Limit]] — A limit is the value that a function or sequence approaches as the input approaches some value.
- [[mean-value-theorem|Mean Value Theorem]] — The Mean Value Theorem guarantees a point where the instantaneous rate of change equals the average rate of change.
- [[optimization-problem|Optimization Problem]] — An optimization problem seeks the best solution (maximizing or minimizing an objective function) from a set of candidates.
- [[partial-derivative|Partial Derivative]] — A partial derivative is the derivative of a multivariable function with respect to one variable while holding others constant.
- [[riemann-sums|Riemann Sums]] — Riemann sums are approximations to the area under a curve using partitioned rectangles.
- [[taylor-series|Taylor Series]] — A Taylor series is a power series expansion of a function centered at a point, built from the function's derivatives.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
