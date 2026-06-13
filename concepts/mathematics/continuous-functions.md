---
type: term
category: mathematics
defines: [Continuous Function, Continuity]
related: ["[[limit]]", "[[differentiable-functions]]", "[[intermediate-value-theorem]]", "[[polynomial-function]]"]
lists: ["[[classifications-of-functions]]"]
read: false
---

# Continuous Function

## summary

A *continuous function* has no jumps, breaks, or holes in its graph; intuitively, you can draw it without lifting your pencil. Formally, a function *f* is continuous at a point if the limit as you approach that point equals the function's value there. Continuity is foundational to calculus and guarantees nice properties like the Intermediate Value Theorem.

## you gotta know

- A function *f* is continuous at *x* = *a* if `lim (x → a) f(x) = f(a)` (the limit exists and equals the value).
- Discontinuities come in three types: *removable* (a hole; limit exists but function value differs or is undefined), *jump* (left and right limits differ), *infinite* (limit is ±∞, e.g., at vertical asymptotes).
- All polynomial, exponential, and trigonometric functions are continuous wherever they are defined.
- The *Intermediate Value Theorem* states: if *f* is continuous on [*a*, *b*] and *y* is between *f*(*a*) and *f*(*b*), then *f*(*c*) = *y* for some *c* in (*a*, *b*).
- Sums, products, and compositions of continuous functions are continuous (where defined).
- Continuity is weaker than differentiability; a function can be continuous but not smooth (e.g., *f*(*x*) = |*x*| at the origin).

## connections

- [[limit]] — the foundation of continuity; a function is continuous if its limit matches its value.
- [[differentiable-functions]] — differentiability implies continuity, but not the converse.
- [[intermediate-value-theorem]] — a key consequence of continuity.
- [[polynomial-function]] — polynomials are continuous everywhere.

## see also

- [[limit]] · [[differentiable-functions]] · [[polynomial-function]] · [[trigonometric-function]]

<!-- footer -->

---

Lists: [[classifications-of-functions]] · Mark read: `INPUT[toggle:read]`
