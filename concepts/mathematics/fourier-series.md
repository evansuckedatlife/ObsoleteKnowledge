---
type: concept
category: mathematics
defines: [Fourier series]
related: ["[[periodic-function]]", "[[trigonometric-function]]", "[[hilbert-space]]", "[[complex-analysis]]", "[[signal-processing]]", "[[heat-equation]]"]
requires: ["[[trigonometric-function]]", "[[periodic-function]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Fourier Series

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **Fourier series** is an infinite sum of sines and cosines that represents a periodic function on a finite interval. *Jean-Baptiste Joseph Fourier* discovered that any periodic function—even jagged or discontinuous ones—can be decomposed into a superposition of harmonic oscillations. This insight revolutionized mathematics and physics, enabling solutions to heat diffusion, wave equations, and signal analysis. Fourier series bridge algebra (decomposing functions) and geometry (harmonic resonances).

## you gotta know

- Any periodic function f(x) with period 2π can be written as f(x) = a₀/2 + Σ(aₙ cos(nx) + bₙ sin(nx)), where aₙ and bₙ are Fourier coefficients determined uniquely by f.
- Fourier coefficients are computed via orthogonality of sines and cosines: aₙ = (1/π) ∫ f(x) cos(nx) dx, bₙ = (1/π) ∫ f(x) sin(nx) dx; this orthogonality is the key to their isolation.
- The series converges pointwise at continuity points; at discontinuities, it converges to the average of left and right limits (*Dirichlet convergence*), a subtle but essential result for rough functions.
- *Completeness*: the set of sines and cosines forms an *orthonormal basis* for the space of periodic functions (in the sense of Hilbert spaces), meaning every periodic function can be approximated arbitrarily well.
- Fourier used this technique to solve the heat diffusion equation (the parabolic PDE), revolutionizing applied mathematics and giving rise to the entire field of partial differential equations.
- Generalizes to non-periodic functions via the Fourier *transform* (integral transform), which replaces discrete frequencies with continuous spectrum; this is core to signal processing and quantum mechanics.
- The *Discrete Fourier Transform* (DFT) and Fast Fourier Transform (FFT) algorithm make Fourier analysis computationally tractable, enabling digital signal processing at gigahertz speeds.
- Used in audio compression (MP3), image processing (JPEG, PNG), medical imaging (MRI, CT scans), and scientific instrumentation worldwide.
- Generalizations include wavelets and time-frequency analysis, which overcome Fourier series' limitation of time-localization information.

## connections

- [[periodic-function]] — the class of functions Fourier series represent.
- [[trigonometric-function]] — sines and cosines are the building blocks of Fourier decomposition.
- [[hilbert-space]] — Fourier series exemplify orthonormal basis expansions in abstract function spaces.
- [[complex-analysis]] — exponential representations of Fourier series link real and imaginary parts elegantly.
- [[signal-processing]] — Fourier analysis underpins the entire field of digital signal processing.
- [[heat-equation]] — the PDE Fourier solved to motivate his series theory.

## see also

[[periodic-function]] · [[trigonometric-function]] · [[hilbert-space]] · [[complex-analysis]]

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
