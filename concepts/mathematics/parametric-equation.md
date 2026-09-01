---
type: concept
category: mathematics
defines: [Parametric equation, Parametrization]
related: ["[[polar-curves]]", "[[epicycloid]]", "[[calculus]]"]
requires: ["[[function]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Parametric Equation

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **parametric equation** describes a curve by expressing both coordinates as functions of a single parameter, usually *t* or θ. Instead of *y* = *f*(*x*), parametric form uses *x* = *f*(*t*) and *y* = *g*(*t*). This approach elegantly handles curves that fail the vertical-line test and naturally represents motion along paths, revealing geometric structure that Cartesian equations often obscure.

## you gotta know

- *Parametric form*: a plane curve is given by (*x*(*t*), *y*(*t*)) for *t* in some interval [*a*, *b*]; the parameter *t* traces out the curve as it varies (often *t* represents time).
- Avoids the constraint of functions: *a single parameter can represent multi-valued relations* (circles, ellipses) and curves failing the vertical-line test; one curve, many Cartesian equations.
- *Eliminating the parameter*: solve for *t* from one equation, substitute into the other to recover a Cartesian relation *F*(*x*, *y*) = 0; may lose direction and multiplicity information.
- *Derivative in parametric form*: d*y*/d*x* = (d*y*/d*t*) / (d*x*/d*t*), provided d*x*/d*t* ≠ 0; enables tangent lines and calculus without explicitly solving for *y*(*x*).
- *Arc length* from *t* = *a* to *b*: *s* = ∫_a^b √((d*x*/d*t*)² + (d*y*/d*t*)²) d*t*; elegant formula, avoids messy square roots inherent in Cartesian arc length.
- *Cycloid* (*x* = *r*(θ − sin θ), *y* = *r*(1 − cos θ)), *epicycloid*, *hypocycloid* (rolling circle curves) are far cleaner parametrically; Cartesian forms are polynomials of high degree.
- *Polar curves* *r* = *f*(θ) are a special parametrization; convert to parametric (*x* = *r* cos θ, *y* = *r* sin θ), enabling unified treatment of curves in polar and Cartesian coordinates.
- *Curvature* and *torsion* (for 3D curves) have elegant parametric formulas; parametrization is essential for studying the intrinsic geometry of curves without reference to coordinate systems.
- *Kinematics and dynamics* use parametric equations where *t* is time; velocity *v* = (d*x*/d*t*, d*y*/d*t*) and acceleration *a* = (d²*x*/d*t*², d²*y*/d*t*²) emerge naturally from parametric representations.

## connections

- [[polar-curves]] — another parametrization scheme; shares the property of encoding geometric structure efficiently.
- [[epicycloid]] — naturally defined by parametric equations from the rolling motion of circles.
- [[cycloid]] — a classical curve best understood parametrically.
- [[calculus]] — calculus on parametric curves extends differentiation and integration to this form.
- [[vector-calculus]] — parametrization is fundamental to line integrals and curve theory.

## see also

[[polar-curves]] · [[epicycloid]] · [[cycloid]] · [[calculus]]

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
