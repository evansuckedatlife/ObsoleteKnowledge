---
type: term
category: mathematics
defines: [Rational Function]
related: ["[[polynomial-function]]", "[[quadratic-function]]", "[[discontinuity]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Rational Function

## summary

A *rational function* is a quotient of two polynomials, written as `f(x) = P(x) / Q(x)`, where both numerator and denominator are polynomials. Rational functions generalize simpler polynomial behaviour by introducing asymptotes and discontinuities, making them essential in modeling rates, proportions, and complex engineering systems.

## you gotta know

- General form: `f(x) = P(x) / Q(x)`, where *P* and *Q* are polynomials and *Q* is not the zero polynomial.
- *Vertical asymptotes* occur where the denominator is zero and the numerator is nonzero; the function approaches infinity near these points.
- *Horizontal asymptotes* are determined by the degrees of *P* and *Q*: if deg(*P*) < deg(*Q*), the horizontal asymptote is *y* = 0; if equal, it is *y* = (leading coefficient of *P*) / (leading coefficient of *Q*); if deg(*P*) > deg(*Q*), no horizontal asymptote.
- *Oblique* (or *slant*) *asymptotes* appear when deg(*P*) = deg(*Q*) + 1; found by polynomial long division.
- Rational functions are continuous except at the zeros of *Q*; they are differentiable wherever they are continuous.
- Common examples include `1/x` (reciprocal), `1/(x²)`, and `(x+1)/(x−2)`.

## connections

- [[polynomial-function]] — numerator and denominator are polynomials.
- [[asymptote]] — the key feature of rational function behaviour.
- [[discontinuity]] — rational functions exhibit jump and infinite discontinuities.

## see also

- [[polynomial-function]] · [[quadratic-function]] · [[exponential-function]] · [[logarithmic-function]]

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

Lists:  · Mark read: `INPUT[toggle:read]`
