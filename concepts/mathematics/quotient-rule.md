---
type: term
category: mathematics
defines: [Quotient rule, quotient rule of differentiation]
related: ["[[derivative]]", "[[product-rule]]", "[[chain-rule]]", "[[calculus]]", "[[rational-function]]"]
requires: ["[[derivative]]", "[[calculus]]"]
lists: []
tour_order: 2
read: false
---

# Quotient Rule


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **quotient rule** is a differentiation formula that computes the derivative of a ratio of two functions. If h(x) = f(x)/g(x), then h'(x) = (f'(x)·g(x) − f(x)·g'(x)) / [g(x)]². It is one of the fundamental rules of differential calculus, alongside the power rule, product rule, and chain rule. Though it can be derived from the product and chain rules, the quotient rule is so common (rational functions are ubiquitous) that it is typically memorised and applied directly.

## you gotta know

- **Formula**: if h(x) = f(x)/g(x) where g(x) ≠ 0, then h'(x) = [f'(x)·g(x) − f(x)·g'(x)] / [g(x)]².
- **Memory aid**: "low d-high minus high d-low, over low-low" — the denominator is squared; the numerator is the *derivative* of the numerator times the denominator minus the numerator times the *derivative* of the denominator.
- **Derivation**: quotient rule follows from the product rule applied to f(x) · [1/g(x)], combined with the chain rule for the reciprocal.
- **Rational functions**: polynomials divided by polynomials—quotient rule applies directly (derivative is another rational function).
- **Domain**: the derivative is undefined where g(x) = 0 (discontinuities/vertical asymptotes of the original function).
- **Example**: d/dx [x² / (x + 1)] = [(2x)(x+1) − x²(1)] / (x+1)² = (2x² + 2x − x²) / (x+1)² = (x² + 2x) / (x+1)².
- **Trigonometric and logarithmic**: quotient rule is used for derivatives of tan(x) = sin(x)/cos(x) and log_a(x) = ln(x)/ln(a).
- **Reciprocal rule** (special case): if h(x) = 1/g(x), then h'(x) = −g'(x) / [g(x)]²—a simplified quotient rule with f(x) = 1.

## context

The quotient rule is one of a trinity of basic differentiation techniques—alongside the product rule and chain rule—that enables differentiation of all elementary functions. While not as universally applicable as the chain rule, it is indispensable for rational functions, which appear everywhere: in control theory (transfer functions), signal processing (filters), and physics (potentials, forces). Students sometimes derive it from the product rule to avoid memorisation; however, direct application is faster for complicated expressions. The quotient rule highlights a principle: differentiation rules are compositional—complex derivatives are built from simpler rules applied layer by layer. In numerical differentiation, finite-difference approximations to quotient-rule formulas are used to estimate derivatives computationally.

## connections

- [[derivative]] — the quotient rule is a fundamental differentiation formula.
- [[product-rule]] — analogous rule for products; quotient rule can be derived from it.
- [[chain-rule]] — another fundamental differentiation rule; used in deriving quotient rule.
- [[calculus]] — part of the toolkit of differential calculus.
- [[rational-function]] — quotient rule applies to ratios of polynomials.
- [[power-rule]] — the simplest differentiation rule; quotient and product rules generalise it.
- [[trigonometric-function]] — quotient rule used for tan(x) = sin(x)/cos(x).

## see also

- [[derivative]] · [[product-rule]] · [[chain-rule]]

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

Lists: Mark read: `INPUT[toggle:read]`
