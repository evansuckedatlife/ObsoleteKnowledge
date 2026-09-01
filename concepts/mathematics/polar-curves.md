---
type: concept
category: mathematics
defines: ["polar curves", "polar coordinates"]
related: ["[[lemniscate]]", "[[limacon]]", "[[cardioid]]", "[[epicycloid]]", "[[catenary]]"]
requires: ["[[trigonometric-function]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Polar curves

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Polar curves** are curves defined in polar coordinates (r, θ) rather than the familiar Cartesian (x, y) system. In polar form, a point's position is given by its distance from the origin and its angle from a reference direction. This coordinate system reveals hidden symmetries and produces elegant curves—spirals, roses, and loops—that would be cumbersome to express in Cartesian form.

## you gotta know

- A point in polar coordinates is specified by (r, θ): *r* is the radial distance from the origin, and θ is the angle from the positive x-axis, measured counterclockwise.
- The conversion relations are: x = r cos(θ), y = r sin(θ), and conversely r = √(x² + y²), θ = arctan(y/x); these transformations bridge polar and Cartesian worlds.
- Common polar curves include the *spiral of Archimedes* (r = aθ), the *logarithmic spiral* (r = ae^(bθ)), and *rose curves* (r = a cos(nθ)); each exhibits rotational symmetry elegantly.
- The [[lemniscate]] (r² = a² cos(2θ)) is a figure-eight shaped curve; the [[limacon]] (r = a + b cos(θ)) is a looped or dimpled heart shape discovered by Pascal.
- Polar curves excel at capturing rotational symmetry and periodic behaviour; a rose curve with *n* petals has a closed form that emphasizes this structure.
- Integration in polar coordinates uses the element dA = (1/2) r² dθ, differing from Cartesian form; this Jacobian factor is crucial for finding areas and is often overlooked.
- Astronomers and physicists favour polar forms when dealing with orbits, angular momentum, and central-force problems because the symmetry reduces differential equations substantially.
- The [[cardioid]] emerges as a special limiting case of the limacon when a = b; it traces the path of a point on a circle rolling around another circle of equal radius.

## connections

- [[lemniscate]] — a canonical polar curve with figure-eight symmetry, a staple of classical geometry.
- [[limacon]] — another classic polar curve studied by Blaise Pascal, exhibiting a dimple or inner loop.
- [[cardioid]] — a special case of the limacon with a cusp, resembling a heart.
- [[epicycloid]] — a polar curve traced by a point on a circle rolling around another circle.
- [[trigonometric-function]] — polar curves rely on periodic trigonometric expressions.
- [[parametric-equation]] — polar curves are often written in parametric form with θ as the parameter.

## see also

- [[lemniscate]] · [[limacon]] · [[cardioid]] · [[spiral]] · [[trigonometric-function]]

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
