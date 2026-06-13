---
type: concept
category: mathematics
defines: ["Product Rule", product-rule]
related: ["[[derivative]]", "[[quotient-rule]]"]
lists: ["[[calculus-ideas]]"]
read: false
---

# Product Rule

## summary

The *product rule* states that the derivative of a product of two functions is (f·g)' = f'·g + f·g'—the derivative of the first times the second, plus the first times the derivative of the second. It is one of the three essential differentiation rules (alongside power and chain) and is necessary whenever you differentiate expressions where two functions are multiplied together, such as x·sin(x) or e^x·(x²+1).

## you gotta know

### The Rule
- Product rule: d/dx [f(x) · g(x)] = f'(x) · g(x) + f(x) · g'(x).
- Mnemonic: "first times derivative of second, plus second times derivative of first."
- Not the product of derivatives: d/dx [f · g] ≠ (f'(x)) · (g'(x)).

### Examples
- d/dx [x · sin(x)] = 1 · sin(x) + x · cos(x) = sin(x) + x·cos(x).
- d/dx [e^x · (x² + 1)] = e^x · (x² + 1) + e^x · 2x = e^x(x² + 2x + 1).
- d/dx [x · ln(x)] = 1 · ln(x) + x · (1/x) = ln(x) + 1.

### Related Techniques
- Quotient rule is the analogous rule for division: (f/g)' = (f'·g – f·g') / g².
- The product rule generalizes: d/dx [f · g · h] = f' · g · h + f · g' · h + f · g · h'.
- Combined with the chain rule for composite products: d/dx [sin(x) · e^(2x)] uses product rule plus chain rule on the second term.

## context

The product rule is one of the foundational techniques in calculus because so many natural expressions involve products. It often appears combined with the chain rule and other rules in complex differentiation problems. Understanding why the product rule is *not* just "multiply the derivatives" is key to understanding how differentiation works at a deeper level. Quiz-bowl questions test direct application (compute the derivative of x · cos(x)) and recognition (when do you need the product rule versus just expanding and differentiating term-by-term?).

## connections

- [[derivative]] — the product rule is a core differentiation technique.
- [[quotient-rule]] — the analogous rule for quotients.
- [[chain-rule]] — often combined with the product rule in complex expressions.

## see also

- [[derivative]] · [[quotient-rule]] · [[chain-rule]]

<!-- footer -->

---

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
