---
type: concept
category: mathematics
defines: [Derivative, derivatives, differentiation]
related: ["[[limit]]", "[[chain-rule]]", "[[product-rule]]", "[[differential-equations]]"]
lists: ["[[calculus-ideas]]"]
read: false
---

# Derivative

## summary

The *derivative* of a function measures its instantaneous rate of change at a point—the slope of the tangent line to the curve. Defined as the limit of the secant-line slope, f'(x) = lim(h→0) [f(x+h) – f(x)] / h, the derivative is the workhorse of calculus, with applications spanning physics (velocity, acceleration), optimization (maxima and minima), and approximation. Computing derivatives by applying rules (power, product, chain, quotient) is a core calculus skill.

## you gotta know

### Core Definition and Notation
- f'(x), df/dx, and Df(x) are all notations for the derivative of f at x.
- The derivative is the *limit* of the difference quotient (secant line slope) as the interval shrinks.
- Geometric interpretation: f'(a) is the slope of the tangent line to the curve y = f(x) at x = a.

### Derivative Rules
- *Power rule*: d/dx (x^n) = nx^(n–1).
- *Product rule*: (fg)' = f'g + fg'.
- *Quotient rule*: (f/g)' = (f'g – fg') / g².
- *Chain rule*: (f ∘ g)'(x) = f'(g(x)) · g'(x).

### Applications and Consequences
- First derivative test: f'(x) > 0 means f is increasing; f'(x) < 0 means f is decreasing.
- Critical points (where f'(x) = 0 or f'(x) is undefined) are candidates for local extrema.
- Second derivative: f''(x) measures concavity (f'' > 0 is concave up; f'' < 0 is concave down).
- L'Hôpital's rule: to evaluate lim(x→a) f(x)/g(x) when it is 0/0 or ∞/∞, compute lim(x→a) f'(x)/g'(x).

## context

The derivative is the bridge between algebra and calculus—it translates the static problem "what is the value at this point?" into the dynamic one "how fast is it changing?" This shift is profound: it unlocks optimization (finding maxima/minima), curve-sketching, and modeling rates of change in nature. Physics is built on derivatives: velocity is the derivative of position; acceleration is the derivative of velocity. Quiz-bowl questions range from basic rule application (compute the derivative of x³ sin(x)) to interpreting derivatives (what does f'(x) < 0 tell you about the graph?) to applying them to real-world models. The derivative is also the gateway to differential equations.

## connections

- [[limit]] — the derivative is defined as a limit.
- [[chain-rule]] — one of the most-tested derivative rules.
- [[product-rule]] — another essential differentiation technique.
- [[quotient-rule]] — for differentiating fractions.
- [[taylor-series]] — derivatives of all orders appear in the Taylor expansion.
- [[differential-equations]] — differential equations are equations involving derivatives.

## see also

- [[chain-rule]] · [[product-rule]] · [[integral]]

<!-- footer -->

---

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
