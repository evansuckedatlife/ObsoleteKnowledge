---
type: concept
category: mathematics
defines: ["sine function", "sine"]
related: ["[[periodic-function]]", "[[trigonometric-function]]", "[[cosine-function]]", "[[sine-curve]]", "[[fourier-series]]"]
requires: ["[[trigonometric-function]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Sine function

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **sine function** is one of the primary trigonometric functions, fundamental to oscillatory phenomena and periodic behaviour. Defined as the ratio of the opposite side to the hypotenuse in a right triangle, it generalises to all real numbers and lies at the heart of Fourier analysis, physics, and engineering. The sine function captures the essence of periodicity and smooth cyclical motion.

## you gotta know

- In a right triangle, sin(θ) = opposite / hypotenuse; the angle θ is measured from the horizontal baseline.
- The sine function is defined on all real numbers; it maps ℝ → [−1, 1] with period 2π, so sin(x + 2π) = sin(x).
- sin(0) = 0, sin(π/2) = 1, sin(π) = 0, sin(3π/2) = −1; these key values anchor sine's behaviour across the full cycle.
- The sine function is *odd*: sin(−x) = −sin(x), meaning its graph has rotational symmetry about the origin (a 180° rotation leaves it unchanged).
- The derivative d/dx sin(x) = cos(x); integrating yields ∫ sin(x) dx = −cos(x) + C, making sine and cosine mutually related through calculus.
- Fourier's theorem states that any periodic function can be expressed as an infinite sum of sine (and cosine) functions of various frequencies; this foundation underlies signal processing.
- The complex exponential form links sine to the exponential: sin(x) = (e^(ix) − e^(−ix)) / (2i), unifying trigonometry with complex analysis via Euler's formula.
- The sine function arises naturally in harmonic motion, wave propagation, and oscillations; any smooth periodic phenomenon can be approximated by sums of sines and cosines.
- The Taylor series expansion sin(x) = x − x³/3! + x⁵/5! − x⁷/7! + ... converges for all x and reveals sine's smooth, infinitely differentiable nature.
- The inverse sine function (arcsin) has domain [−1, 1] and range [−π/2, π/2], allowing recovery of angles from sine values.

## connections

- [[periodic-function]] — the sine function is the canonical example of periodicity.
- [[trigonometric-function]] — sine is one of the core trigonometric functions alongside cosine and tangent.
- [[cosine-function]] — closely related; cosine is a phase-shifted sine (cos(x) = sin(x + π/2)).
- [[sine-curve]] — the graph of y = sin(x) is called a sine curve or sinusoid.
- [[fourier-series]] — expresses functions as infinite sums of sines (and cosines).
- [[complex-numbers]] — sine links real and imaginary parts via Euler's formula.

## see also

- [[trigonometric-function]] · [[periodic-function]] · [[fourier-series]] · [[cosine-function]]

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
