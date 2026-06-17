---
type: concept
category: mathematics
defines: ["Taylor Series", "Taylor expansion", Maclaurin]
related: ["[[derivative]]", "[[power-series]]", "[[convergence]]"]
requires: ["[[calculus]]"]
lists: ["[[calculus-ideas]]"]
tour_order: 1
read: false
---

# Taylor Series


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A *Taylor series* is a power series expansion of a function centered at a point, built from the function's derivatives: f(x) = f(a) + f'(a)(x–a) + f''(a)(x–a)²/2! + f'''(a)(x–a)³/3! + ···. A *Maclaurin series* is a Taylor series centered at x = 0. Taylor series are the bridge between polynomial approximation and transcendental functions, allowing you to approximate sin(x), e^x, or ln(x) locally with polynomials.

## you gotta know

### The Formula
- Taylor series of f at x = a: f(x) = Σ(n=0 to ∞) [f^(n)(a) / n!] · (x – a)^n.
- The n-th derivative of f at a, divided by n!, gives the coefficient of (x – a)^n.
- Maclaurin series: centered at a = 0, so f(x) = Σ(n=0 to ∞) [f^(n)(0) / n!] · x^n.

### Canonical Examples
- e^x = 1 + x + x²/2! + x³/3! + ··· (Maclaurin; converges for all x).
- sin(x) = x – x³/3! + x⁵/5! – x⁷/7! + ··· (Maclaurin; all x).
- cos(x) = 1 – x²/2! + x⁴/4! – x⁶/6! + ··· (Maclaurin; all x).
- ln(1 + x) = x – x²/2 + x³/3 – x⁴/4 + ··· (Maclaurin; converges for |x| ≤ 1, x ≠ –1).

### Convergence and Error
- A Taylor series converges within a *radius of convergence*—the interval where the series equals the original function.
- Remainder term: error in truncating after n terms is bounded by *Lagrange remainder* or *integral remainder*.
- Some series (e^x, sin, cos) converge everywhere; others (ln(1+x)) converge only on a restricted domain.

## context

Taylor series are the hidden backbone of scientific computing and approximation. When a calculator computes sin(0.5) or e^2, it is likely using a truncated Taylor series (or a related rational approximation). In theoretical mathematics, Taylor series allow you to study a function through its derivatives—smoothness, singularities, and local behavior all show up in the coefficients. They are also the foundation of perturbation theory in physics: approximating a hard problem by starting with a simpler one and adding corrections term by term. Quiz-bowl questions test the ability to write out the first few terms of a Maclaurin series, recognize which functions match which series, and apply series to compute limits or approximations.

## connections

- [[derivative]] — every term depends on evaluating a derivative at the center point.
- [[power-series]] — a Taylor series is a specific type of power series.
- [[convergence]] — determining where a Taylor series equals the original function.
- [[limit]] — used to evaluate functions via their series (e.g., lim(x→0) sin(x)/x = 1 via series).
- [[polynomial-approximation]] — Taylor series are local polynomial approximations to a function.

## see also

- [[power-series]] · [[convergence]] · [[derivative]]

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

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
