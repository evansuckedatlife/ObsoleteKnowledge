---
type: concept
category: mathematics
defines: [Inverse trigonometric functions, inverse trigonometric function, arcsin, arccos, arctan, arcsine, arccosine, arctangent]
related: ["[[trigonometric-function]]", "[[inverse-function]]", "[[domain-restriction]]", "[[principal-value]]", "[[calculus]]", "[[integration]]"]
requires: ["[[trigonometric-function]]", "[[inverse-function]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Inverse Trigonometric Function

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Inverse trigonometric functions** recover angles from trigonometric ratios. If sin(θ) = x, then θ = arcsin(x) (denoted sin⁻¹(x)); similarly for arccosine and arctangent. Since trigonometric functions are periodic, they are not one-to-one on their natural domains; we restrict to principal ranges (e.g., [-π/2, π/2] for arcsin) to define legitimate inverses with single-valued outputs. These functions appear ubiquitously in navigation, physics, engineering, and computer graphics whenever we need to find an angle from a known trigonometric ratio.

## you gotta know

- *arcsin(x)* is defined for x ∈ [-1, 1], with range [-π/2, π/2]; arcsin(sin(θ)) = θ only if θ is in this principal range, otherwise the angle must be reduced to this interval.
- *arccos(x)* is defined for x ∈ [-1, 1], with range [0, π]; note the different principal range reflecting cosine's decreasing monotonicity and symmetry properties.
- *arctan(x)* is defined for all real x, with range (-π/2, π/2); it approaches ±π/2 asymptotically as x → ±∞, never quite reaching the limits.
- The derivative of arcsin(x) is 1/√(1 − x²); of arccos(x) is −1/√(1 − x²); of arctan(x) is 1/(1 + x²); these reveal the function's sensitivity to input changes.
- These derivatives are critical to integration: ∫ dx/√(1 − x²) = arcsin(x) + C, ∫ dx/(1 + x²) = arctan(x) + C; these antiderivatives arise in countless applications.
- Commonly denoted sin⁻¹, cos⁻¹, tan⁻¹, though this notation can confuse since 1/sin(x) is the reciprocal (cosecant), not the inverse function; the ISO 80000-2 standard uses arcsin, arccos, arctan to avoid ambiguity.
- Used in physics for angle recovery in projectile motion (finding launch angle from range), optics (Snell's law), and oscillatory systems (phase angle determination).
- In computer graphics and robotics, inverse trig functions compute rotation angles from coordinate transformations, enabling 3D rendering and inverse kinematics calculations.
- Multivalued inverses exist (all possible angles with a given sine/cosine/tangent value), but principal values enable function notation and calculus.

## connections

- [[trigonometric-function]] — the parent functions being inverted; sine, cosine, tangent.
- [[inverse-function]] — the general concept; inverse trig functions exemplify the need for domain restriction.
- [[domain-restriction]] — sine/cosine/tangent must be restricted to principal ranges to become invertible.
- [[principal-value]] — the central angle in the restricted range, uniquely determined by the inverse function.
- [[calculus]] — inverse trig functions appear constantly in derivative and integral rules.
- [[integration]] — integrals of 1/√(1 − x²) and 1/(1 + x²) reduce to inverse trig functions.

## see also

[[trigonometric-function]] · [[inverse-function]] · [[calculus]] · [[integration]]

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
