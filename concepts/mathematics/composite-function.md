---
type: concept
category: mathematics
defines: [composite function]
related: ["[[derivative]]", "[[calculus]]", "[[continuous-functions]]", "[[polynomial-function]]", "[[cardinality]]", "[[periodic-function]]"]
requires: ["[[derivative]]", "[[calculus]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Composite Function

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **composite function** is a mathematical mapping created by chaining two or more functions together, applying one operation to the direct output of another. Formally written as $(f \circ g)(x) = f(g(x))$, the concept arose with the systematic development of analysis in seventeenth-century Europe under scholars like *Gottfried Wilhelm Leibniz* and *Isaac Newton*. The operation forms the basis of algebraic substitution, structural transformation, and the fundamental rules of modern differential calculus.

## you gotta know

- Evaluated from the inside out, meaning the inner function acts first on the initial input before the outer function processes that result.
- Composition is strictly associative, satisfying $(f \circ g) \circ h = f \circ (g \circ h)$, but it is generally non-commutative since swapping order alters the overall rule.
- The derivative of a composite mapping is calculated using the *chain rule*, which multiplies the derivative of the outer function evaluated at the inner value by the derivative of the inner function.
- Combining two continuous mappings preserves unbroken continuity across their shared domains and codomains.
- When two bijective functions are chained together, the resulting mapping remains bijective, and its two-sided inverse unwinds in reversed sequence as $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$.
- Higher-order derivatives of chained functions can be calculated systematically through *Faà di Bruno's formula*, which employs *Bell polynomials*.
- In abstract algebra and transformation geometry, the composition of self-maps on a given set generates transformation monoids and permutation groups.

## connections

- [[derivative]] — rates of instantaneous change calculated across nested mappings via the fundamental chain rule.
- [[calculus]] — broad branch of analysis reliant on decomposing complex equations into nested elementary operations.
- [[cardinality]] — set sizes whose equivalence is established through chaining invertible bijective mappings.
- [[continuous-functions]] — foundational topological mappings that remain continuous under consecutive functional evaluation.
- [[polynomial-function]] — algebraic expressions whose nested evaluation produces higher-degree polynomial systems.
- [[periodic-function]] — oscillating curves whose frequencies and amplitudes shift when composed with linear scaling functions.
- [[isaac-newton]] — pioneering natural philosopher who formulated early fluxions and analytical rules for dynamic motion.

## see also

- [[cardinality]] · [[derivative]] · [[continuous-functions]]

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

Lists: [[mathematics-hubs]] · Mark read: `INPUT[toggle:read]`
