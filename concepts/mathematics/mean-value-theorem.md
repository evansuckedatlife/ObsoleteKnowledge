---
type: concept
category: mathematics
defines: ["Mean Value Theorem", MVT]
related: ["[[derivative]]", "[[continuity]]", "[[rolle-theorem]]"]
lists: ["[[calculus-ideas]]"]
read: false
---

# Mean Value Theorem

## summary

The *Mean Value Theorem* (MVT) states that for a function continuous on a closed interval [a, b] and differentiable on the open interval (a, b), there exists at least one point c in (a, b) where the instantaneous rate of change (derivative) equals the average rate of change over the interval. In geometric terms, it guarantees that the slope of the tangent line at some point c is parallel to the secant line passing through the endpoints (a, f(a)) and (b, f(b)). It is one of the most important theoretical results in calculus, serving as the foundation for proving many other key theorems.

## you gotta know

- Formally, if f is continuous on [a, b] and differentiable on (a, b), then there is some c in (a, b) such that f'(c) = [f(b) – f(a)] / (b – a).
- *Rolle's theorem* is a special case of the Mean Value Theorem where f(a) = f(b), guaranteeing the existence of a point c where the derivative f'(c) = 0.
- The theorem requires both continuity on the closed interval and differentiability on the open interval; failing either condition at even a single point invalidates the guarantee.
- The Mean Value Theorem is used to prove that if f'(x) = 0 everywhere on an interval, then f(x) is constant, which in turn justifies the "+ C" constant of integration.
- The *Cauchy Mean Value Theorem* (or generalized MVT) extends this to two functions, stating that [f(b) - f(a)] / [g(b) - g(a)] = f'(c) / g'(c) under similar conditions.

## connections

- [[derivative]] — MVT relates the derivative at a point to the average rate of change.
- [[continuity]] — the theorem strictly requires the function to be continuous on the closed interval.
- [[rolle-theorem]] — Rolle's theorem is the special case that serves as the basis for proving the MVT.

## see also

- [[derivative]] · [[fundamental-theorem-of-calculus]] · [[integral]]

<!-- footer -->

---

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
