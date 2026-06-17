---
type: term
category: mathematics
defines: [Periodic Function]
related: ["[[trigonometric-function]]", "[[sine-function]]", "[[cosine-function]]", "[[fourier-series]]"]
requires: []
lists: ["[[classifications-of-functions]]"]
tour_order: 0
read: false
---

# Periodic Function

## summary

A *periodic function* repeats its values at regular intervals; it satisfies `f(x + p) = f(x)` for all *x*, where *p* is the *period*. Periodic functions model cyclical phenomena—seasons, tides, heartbeats, light waves—and are the language of oscillatory systems throughout physics and engineering.

## you gotta know

- Definition: a function *f* is periodic with period *p* > 0 if `f(x + p) = f(x)` for all *x* in the domain.
- The *fundamental period* is the smallest positive *p* for which periodicity holds.
- Sine and cosine have period 2π; tangent has period π; more generally, `sin(kx)` has period 2π/*k*.
- A periodic function is bounded if its range is a closed interval; for instance, `sin(x)` and `cos(x)` are bounded on [−1, 1].
- Periodic functions need not be continuous or even bounded; examples include the sawtooth wave, square wave, and Dirac comb.
- *Fourier series* decompose periodic functions into sums of sines and cosines, a tool central to signal processing and physics.

## connections

- [[trigonometric-function]] — sine and cosine are the canonical periodic functions.
- [[fourier-series]] — decompose periodic functions into harmonic components.
- [[wave-equation]] — periodic functions model oscillatory solutions.

## see also

- [[trigonometric-function]] · [[sine-function]] · [[cosine-function]] · [[fourier-series]]

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

Lists: [[classifications-of-functions]] · Mark read: `INPUT[toggle:read]`
