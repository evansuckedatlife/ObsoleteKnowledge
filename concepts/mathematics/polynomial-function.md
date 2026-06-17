---
type: term
category: mathematics
defines: [Polynomial Function, Polynomial]
related: ["[[monomial-function]]", "[[rational-function]]", "[[continuous-functions]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Polynomial Function

## summary

A **polynomial function** is an algebraic function whose definition is a sum of terms, each a constant coefficient times a variable raised to a non-negative integer power. Polynomials are the most fundamental class of functions in mathematics: continuous and differentiable everywhere, with explicit formulas for roots (up to degree 4), and appearing ubiquitously in physics, engineering, and economics as models of real phenomena. Their structure—degree, roots, end behaviour—is central to calculus and forms the foundation for understanding more complex functions.

## you gotta know

### Definition and Basic Properties
- Expressed in standard form: `f(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀`, where the exponents are non-negative integers, the coefficients *a*ᵢ are real or complex, and *aₙ* ≠ 0 (the leading coefficient).
- The *degree* is the highest power of *x* that appears; it determines fundamental behavior (number of roots, turning points, end behaviour).
- *Terminology by degree*: degree 0 (constant), degree 1 (linear), degree 2 (quadratic), degree 3 (cubic), degree 4 (quartic), degree 5+ (quintic, sextic, septic, etc.).
- *Coefficients* may be real (for real-valued polynomials) or complex; coefficients determine the polynomial's specific shape and roots.

### Continuity, Differentiability, and Calculus
- *Continuous and differentiable everywhere* on the real line (in fact, infinitely differentiable); a polynomial function is one of the smoothest function classes.
- *Derivative*: if `f(x) = aₙxⁿ + ... + a₀`, then `f'(x) = naₙxⁿ⁻¹ + ... + a₁`, a polynomial of degree *n*−1 (degree decreases by 1).
- *Antiderivative*: integrating a polynomial yields another polynomial (plus a constant); ∫`f(x)dx = (aₙ/(n+1))xⁿ⁺¹ + ...`.
- *Taylor series*: every polynomial is its own Taylor series (finite expansion); approximation beyond a polynomial requires higher-order terms.

### Roots and Factorization
- *Fundamental Theorem of Algebra*: a degree-*n* polynomial has exactly *n* roots in the complex numbers (counting multiplicity); may have fewer real roots.
- *Rational Root Theorem*: if a polynomial has integer coefficients and a rational root *p/q* (in lowest terms), then *p* divides the constant term and *q* divides the leading coefficient.
- *Factorization*: a degree-*n* polynomial factors uniquely into *n* linear factors (in ℂ): `f(x) = aₙ(x − r₁)(x − r₂)...(x − rₙ)`, where *rᵢ* are the roots.
- *Multiplicity*: a root may appear more than once (e.g., `(x − 2)²` has a double root at *x* = 2); the multiplicity affects the shape of the graph.

### End Behaviour and Turning Points
- *End behaviour* is determined by the *leading term* `aₙxⁿ`: if *n* is even and *aₙ* > 0, then `f(x) → +∞` as `x → ±∞`; if *n* is odd and *aₙ* > 0, then `f(x) → −∞` as `x → −∞` and `f(x) → +∞` as `x → +∞`.
- *Turning points (local extrema)*: a degree-*n* polynomial has at most *n*−1 turning points (local maxima/minima), found where `f'(x) = 0`.
- *Inflection points*: where the concavity changes (where `f''(x) = 0`); a degree-*n* polynomial has at most *n*−2 inflection points.

## context

Polynomials are the gateway to both theoretical and applied mathematics. Theoretically, they motivated the Fundamental Theorem of Algebra, the theory of fields and rings, and the Galois theory of equations. Practically, they model countless real-world phenomena: projectile motion (quadratic), population growth, economic cost functions, signal processing, and numerical methods (interpolation via Lagrange polynomials). The study of polynomial roots has a long history—Cardano solved the cubic, Ferrari solved the quartic, and Galois proved that degree-5 and higher have no closed-form radical solutions. In modern mathematics, polynomials appear in every domain: differential equations (linear operators are polynomials in the derivative), algebra (polynomial rings), and computer science (polynomial-time algorithms). In quiz bowl, polynomials appear in algebra, calculus, and in contexts of the Fundamental Theorem, Galois theory, and applications.

## connections

- [[rational-function]] — quotient of two polynomials; generalizes the polynomial idea to allow poles.
- [[monomial-function]] — a single term `axⁿ`; the building block of a polynomial.
- [[quadratic-function]] — polynomials of degree 2; special properties (parabola, vertex form, discriminant).
- [[exponential-function]] — not polynomial; but polynomial approximation via Taylor series.
- [[continuous-functions]] — polynomials are the canonical examples of continuous, smooth functions.
- [[fundamental-theorem-of-algebra]] — guarantees that polynomials have roots in ℂ.
- [[taylor-series]] — polynomials are special cases (finite Taylor expansions).
- [[lagrange-interpolation]] — uses polynomials to fit data points uniquely.

## see also

- [[monomial-function]] · [[rational-function]] · [[quadratic-function]] · [[exponential-function]]

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
