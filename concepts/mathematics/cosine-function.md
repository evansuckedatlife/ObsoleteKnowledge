---
type: concept
category: mathematics
defines: [cosine function, cosine, cos]
related: ["[[trigonometric-function]]", "[[periodic-function]]", "[[sine]]"]
requires: ["[[trigonometric-function]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Cosine Function

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **cosine function** is one of the fundamental trigonometric functions, mapping angles to the ratio of the adjacent side to the hypotenuse in a right triangle. Defined for all real numbers and taking values between −1 and 1, the cosine function is periodic with period 2π and appears ubiquitously in physics, engineering, and harmonic analysis.

## you gotta know

- The cosine of an angle θ in a right triangle is the length of the adjacent side divided by the length of the hypotenuse; this geometric definition extends to all angles via the unit circle.
- As a periodic function, cos(θ + 2π) = cos(θ); its graph oscillates smoothly between −1 and 1 with a wavelike pattern, making it ideal for modeling cyclic phenomena.
- The cosine function is even: cos(−θ) = cos(θ), reflecting symmetry about the vertical axis; this symmetry simplifies many calculations and appears throughout mathematics.
- Via Euler's formula, cosine is the real part of the complex exponential: cos(θ) = Re(e^(iθ)) = (e^(iθ) + e^(−iθ))/2, bridging trigonometry and complex analysis.
- Fourier analysis decomposes periodic signals into sums of cosines (and sines), fundamental to signal processing, audio compression, image processing, and quantum mechanics.
- The derivative of cosine is negative sine: d/dx[cos(x)] = −sin(x), making cosine and sine deeply intertwined through calculus; repeatedly differentiating cycles between them.
- Cosine appears in the law of cosines (relating side lengths in triangles), dot products of vectors, and countless physics applications from wave mechanics to orbital mechanics.
- The cosine approximation cos(x) ≈ 1 − x²/2 for small x enables linear stability analysis and perturbation theory across science and engineering, illustrating why the function's structure matters for applications.

## connections

- [[trigonometric-function]] — cosine is one of the six classical trigonometric functions.
- [[periodic-function]] — cosine is a canonical example of a periodic function with period 2π.
- [[sine]] — the sine and cosine are complementary, related by a 90° phase shift.
- [[calculus]] — the derivative relationship between cosine and sine illustrates foundational calculus principles.
- [[fourier-series]] — decompose complex waves into sums of sines and cosines.
- [[complex-numbers]] — cosine appears in Euler's formula connecting real trigonometry to complex exponentials.

## see also

- [[trigonometric-function]] · [[periodic-function]] · [[sine]]

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
