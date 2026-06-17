---
type: concept
category: mathematics
defines: ["Even and odd functions", "Even function", "Odd function", "Even/odd functions"]
related: ["[[periodic-function]]", "[[trigonometric-function]]", "[[polynomial-function]]"]
requires: ["[[calculus]]"]
lists: ["[[classifications-of-functions]]"]
tour_order: 1
read: false
---

# Even and odd functions


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

*Even and odd functions* are classes of functions characterized by specific symmetry properties under additive inversion of their inputs. An even function is symmetric with respect to the y-axis, satisfying $f(-x) = f(x)$, while an odd function is symmetric with respect to the origin, satisfying $f(-x) = -f(x)$. These classifications simplify algebraic calculations, integration, and the analysis of Fourier series, where functions are decomposed into symmetric components.

## you gotta know

- Even function definition: $f(-x) = f(x)$ for all $x$ in the domain. Graphically, it is symmetric under reflection across the y-axis.
- Odd function definition: $f(-x) = -f(x)$ for all $x$ in the domain. Graphically, it is symmetric under $180^\circ$ rotation about the origin.
- Canonical examples of even functions include $x^2$, $x^4$, and $\cos(x)$.
- Canonical examples of odd functions include $x$, $x^3$, and $\sin(x)$.
- Any function can be uniquely decomposed into the sum of an even function and an odd function: $f(x) = E(x) + O(x)$, where $E(x) = \frac{f(x) + f(-x)}{2}$ and $O(x) = \frac{f(x) - f(-x)}{2}$.
- Integration property: the integral of an odd function over a symmetric interval $[-a, a]$ is always $0$, whereas the integral of an even function over $[-a, a]$ is $2 \int_0^a f(x) dx$.
- The product of two even functions or two odd functions is even; the product of an even function and an odd function is odd.

## connections

- [[trigonometric-function]] — cosine is even; sine and tangent are odd.
- [[polynomial-function]] — a polynomial is even if all its terms have even powers, and odd if all have odd powers.
- [[periodic-function]] — Fourier series expand periodic functions in terms of even (cosines) and odd (sines) harmonics.

## see also

- [[periodic-function]] · [[continuous-functions]] · [[monotonic-functions]] · [[analytic-functions]]

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

Lists: [[classifications-of-functions]] · Mark read: `INPUT[toggle:read]`
