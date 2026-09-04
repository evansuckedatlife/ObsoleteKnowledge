---
type: concept
category: mathematics
defines: [Heat equation, Diffusion equation]
related: ["[[fourier-series]]", "[[calculus]]", "[[derivative]]", "[[trigonometric-function]]", "[[periodic-function]]", "[[eigenvalue]]", "[[exponential-function]]"]
requires: ["[[calculus]]", "[[derivative]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Heat equation

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **heat equation**, often called the **diffusion equation**, is a fundamental second-order parabolic partial differential equation that describes the conduction of thermal energy and the microscopic diffusion of particles over time. Formulated by the French mathematician and physicist *Joseph Fourier* in his 1822 landmark treatise *Théorie analytique de la chaleur*, it established the foundational framework for continuum thermodynamics and modern transport phenomena. It holds an indispensable place in mathematical history because developing its analytic solutions directly motivated the invention of [[fourier-series]] and classical harmonic analysis.

## you gotta know

- Formulated as the time [[derivative]] of temperature being proportional to its spatial Laplacian, conventionally written in one dimension as $\partial u/\partial t = \alpha \partial^2 u/\partial x^2$, where $\alpha$ represents thermal diffusivity.
- Prototypical example of a parabolic partial differential equation, contrasting fundamentally with hyperbolic wave equations and elliptic potential equations in classical classification.
- Solved analytically on bounded intervals through the method of separation of variables, decomposing arbitrary initial spatial temperature profiles into infinite linear combinations of [[trigonometric-function]] modes with [[exponential-function]] temporal decays.
- Solved on an unbounded domain via convolution with the fundamental solution known as the heat kernel, which takes the form of a normalized Gaussian distribution whose variance grows linearly with time.
- Exhibits an instantaneous smoothing effect, meaning that any bounded, measurable initial condition immediately becomes infinitely differentiable for all strictly positive times.
- Possesses the unphysical physical trait of infinite propagation speed, where a point heat disturbance at the origin immediately exerts a non-zero influence at arbitrarily distant spatial locations.
- Obeys the strong maximum principle, stating that non-constant solutions on a compact space-time domain must attain their global extreme values exclusively on the initial time slice or the spatial boundaries.
- Models the macroscopic density evolution of Brownian motion particles, establishing a direct probabilistic bridge between diffusive continuum physics and stochastic calculus via the *Feynman-Kac* theorem.

## connections

- [[fourier-series]] — developed by *Joseph Fourier* precisely to solve this equation under Dirichlet and Neumann boundary conditions on a rod.
- [[calculus]] — provides the core differential framework governing temporal rates of change and multi-dimensional spatial flux.
- [[derivative]] — represents both the single first-order temporal evolution and the second-order spatial curvature driving diffusion.
- [[trigonometric-function]] — supply the orthogonal spatial eigenfunctions that emerge when separating variables on bounded domains.
- [[periodic-function]] — describe the spatial profiles expanded into Fourier series when solving this equation on circular rings.
- [[eigenvalue]] — characterizes the discrete spatial spectrum of the Laplacian operator that dictates mode-by-mode decay rates.
- [[exponential-function]] — determines the rapid, strictly dissipative temporal decay factor attached to each spatial frequency mode.
- [[france]] — the historical home where *Joseph Fourier* developed and presented his thermal theory to the *Académie des Sciences*.

## see also

- [[fourier-series]] · [[calculus]] · [[derivative]]

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
