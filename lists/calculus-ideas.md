---
type: list
category: mathematics
read: false
---

# ideas from calculus

The ideas from calculus most worth knowing for quiz bowl.

## nodes

- [[chain-rule|Chain Rule]] — The chain rule is the fundamental technique for differentiating composite functions: if y = f(g(x)), then dy/dx = f'(g(x)) ·…
- [[continuity|Continuity]] — A function is continuous at a point if the limit of the function as x approaches that point equals the function's value at…
- [[derivative|Derivative]] — The derivative of a function measures its instantaneous rate of change at a point—the slope of the tangent line to the curve.
- [[differentiable|Differentiable]] — A function is differentiable at a point if its derivative exists at that point—the limit defining the derivative converges.
- [[differential-equations|Differential Equations]] — A differential equation is an equation involving a function and its derivatives.
- [[fundamental-theorem-of-calculus|Fundamental Theorem of Calculus]] — The Fundamental Theorem of Calculus states that differentiation and integration are inverse operations.
- [[integral|Integral]] — An integral is either the antiderivative of a function (indefinite integral) or the signed area under a curve (definite integral).
- [[limit|Limit]] — A limit is the value that a function or sequence approaches as the input approaches some value.
- [[product-rule|Product Rule]] — The product rule states that the derivative of a product of two functions is (f·g)' = f'·g + f·g'—the derivative of the first…
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
      - property: file.name
        direction: ASC
```
