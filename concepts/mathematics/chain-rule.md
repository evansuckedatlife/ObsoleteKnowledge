---
type: concept
category: mathematics
defines: ["Chain Rule", chain-rule]
related: ["[[derivative]]", "[[composite-function]]"]
requires: ["[[calculus]]"]
lists: ["[[calculus-ideas]]"]
tour_order: 1
read: false
---

# Chain Rule


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The *chain rule* is the fundamental technique for differentiating composite functions: if y = f(g(x)), then dy/dx = f'(g(x)) · g'(x)—the derivative of the outer function (evaluated at the inner function) times the derivative of the inner function. The chain rule is one of the most-applied rules in calculus and is essential for handling complex expressions like sin(x²), e^(3x), or (2x + 1)^5.

## you gotta know

### The Rule Itself
- Chain rule: d/dx f(g(x)) = f'(g(x)) · g'(x).
- Notation: if y = f(u) and u = g(x), then dy/dx = (dy/du) · (du/dx)—a useful mnemonic.
- The "derivative of the outside times the derivative of the inside."

### Common Examples
- d/dx sin(x²) = cos(x²) · 2x (outer: sin; inner: x²).
- d/dx e^(3x) = e^(3x) · 3 (outer: e^u; inner: 3x).
- d/dx (2x + 1)^5 = 5(2x + 1)^4 · 2 = 10(2x + 1)^4 (outer: (·)^5; inner: 2x + 1).

### Iteration and Generalization
- The chain rule applies to any depth: d/dx sin(cos(x)) = cos(cos(x)) · (–sin(x)).
- With the power rule, chain rule gives d/dx (f(x))^n = n(f(x))^(n–1) · f'(x).
- Implicit differentiation relies on the chain rule: differentiating both sides of an implicit equation introduces chain-rule terms.

## context

The chain rule is the third leg of differentiation, alongside the power rule and product rule. It is indispensable because most real-world functions are composite: you do not often differentiate sin(x) or x² in isolation, but rather sin(x²) or (x² + 1)^3. Mastering the chain rule is what separates "can do calculus" from "understands calculus." It also appears in higher dimensions as the multivariable chain rule (Jacobian matrices in vector calculus). Quiz-bowl questions often test chain rule combined with other rules: differentiate (x² + 1)^3 · sin(x) requires product rule, chain rule, and power rule in concert.

## connections

- [[derivative]] — the chain rule is a core differentiation technique.
- [[composite-function]] — the chain rule applies to composites f ∘ g.
- [[product-rule]] — often combined with the chain rule in complex derivatives.
- [[quotient-rule]] — another differentiation rule often paired with the chain rule.

## see also

- [[derivative]] · [[product-rule]] · [[quotient-rule]]

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
