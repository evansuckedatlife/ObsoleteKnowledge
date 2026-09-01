---
type: concept
category: mathematics
defines: [Elliptic curve, Elliptic curves]
related: ["[[fermat-last-theorem]]", "[[andrew-wiles]]", "[[number-theory]]"]
requires: ["[[polynomial-function]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Elliptic Curves

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

An **elliptic curve** is a smooth algebraic curve defined by a cubic equation in two variables, typically written as *y² = x³ + ax + b*. Despite their classical roots in the geometry of ellipses, elliptic curves have become powerful tools in modern number theory, cryptography, and the study of Diophantine equations. Their group law structure and deep connections to modular forms revolutionized 20th-century mathematics.

## you gotta know

- A non-singular cubic curve *y² = x³ + ax + b* over a field *k* is an elliptic curve; the discriminant Δ = -16(4a³ + 27b²) ≠ 0 ensures smoothness.
- Elliptic curves carry an *abelian group* structure: the chord-and-tangent method defines a natural addition operation on points.
- The *point at infinity* serves as the identity element of the group; three collinear points on the curve sum to the identity.
- Elliptic curves over ℚ (the rationals) are finitely generated abelian groups by Mordell-Weil theorem; the rank measures how many independent points of infinite order exist.
- *Fermat's Last Theorem*: solutions to *xⁿ + yⁿ = zⁿ* correspond to elliptic curves via Frey's construction; proving no such curves exist proved Fermat's claim.
- *Taniyama-Shimura conjecture* linked elliptic curves to modular forms; Wiles' proof of this conjecture completed the proof of FLT.
- Elliptic curves over finite fields are used in *elliptic curve cryptography* for secure key exchange and digital signatures.
- *L-functions* attached to elliptic curves encode deep arithmetic information; conjectures about their zeros (like the Birch and Swinnerton-Dyer conjecture) are central to modern number theory.
- Elliptic curves appear in *descent theory*, used to compute rational points; the structure of torsion subgroups (finite-order points) and free rank can be computed via explicit algorithms.

## connections

- [[fermat-last-theorem]] — elliptic curves encode the structure of potential solutions to Fermat's equation.
- [[andrew-wiles]] — proved the Taniyama-Shimura conjecture connecting elliptic curves and modular forms, completing FLT.
- [[number-theory]] — elliptic curves are central to modern Diophantine analysis.
- [[modular-forms]] — the bridge between elliptic curves and modular forms was the key to Wiles' proof.
- [[algebraic-geometry]] — elliptic curves are fundamental objects in algebraic geometry with rich geometric and arithmetic structure.

## see also

[[fermat-last-theorem]] · [[andrew-wiles]] · [[modular-forms]] · [[number-theory]]

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
