---
type: concept
category: mathematics
defines: [Wave equation, d'Alembert's equation]
related: ["[[calculus]]", "[[derivative]]", "[[periodic-function]]", "[[trigonometric-function]]", "[[linear-algebra]]", "[[optics]]", "[[isaac-newton]]"]
requires: ["[[calculus]]", "[[derivative]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Wave Equation

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **wave equation**, sometimes called **d'Alembert's equation**, is a second-order linear partial differential equation that describes the propagation of waves through a medium, encompassing acoustic vibrations, mechanical stresses, and electromagnetic radiation. First formulated during the *[[enlightenment]]* in *[[france]]* by *Jean le Rond d'Alembert* to analyze the dynamics of a vibrating musical string, the equation is celebrated as the archetype of hyperbolic differential equations. Because its solutions preserve wave profiles and propagate disturbances at a finite characteristic speed, the equation serves as a foundational cornerstone of mathematical physics, providing the mathematical framework for classical field theory, acoustics, seismology, and physical [[optics]].

## you gotta know

- Formulates wave propagation by equating the second time [[derivative]] of a field to the spatial Laplacian scaled by the square of the propagation speed, written in one spatial dimension as the relation $\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$.
- Admits an exact closed-form solution in one dimension through *d'Alembert's formula*, which expresses any disturbance as the superposition of two arbitrary traveling wave profiles, $f(x - ct)$ moving rightward and $g(x + ct)$ moving leftward, governed entirely by initial displacement and velocity.
- Provided the pivotal breakthrough for *James Clerk Maxwell*, whose unification of electricity and magnetism proved that electromagnetic potentials in a vacuum satisfy the three-dimensional wave equation traveling at the speed of light, directly incorporating the field of [[optics]] into electromagnetic theory.
- Solved across bounded geometric intervals through separation of variables, decomposing complex standing waveforms into infinite Fourier series consisting of orthogonal [[trigonometric-function]] and [[periodic-function]] modes with harmonic integer frequencies.
- Classifies fundamentally as the prototype of a second-order hyperbolic partial differential equation, distinguished by having real characteristic curves along which physical signals, wave fronts, and discontinuities travel at strictly finite velocities.
- Exhibits the geometric dependence of *Huygens' principle*, holding true in odd spatial dimensions greater than one where disturbances propagate with sharp, clean trailing edges, whereas waves in even dimensions leave behind lingering reverberations and trailing wakes.
- Preserves total mechanical and field energy across conservative systems, demonstrating that the spatial integral of kinetic energy and strain gradient energy remains invariant throughout the entire time evolution of the wave.

## connections

- [[calculus]] — supplies the differential calculus and multivariable integration required to construct spatial Laplacians and analyze boundary value problems.
- [[derivative]] — provides the mathematical definition of the second-order temporal and spatial rates of change that govern the equation.
- [[periodic-function]] — models the recurring oscillatory patterns, fundamental frequencies, and harmonic overtones characteristic of stationary wave modes.
- [[trigonometric-function]] — furnishes the sinusoidal basis functions used in Fourier analysis to synthesize arbitrary wave solutions.
- [[linear-algebra]] — governs the superposition principle and structures solution spaces as vector spaces decomposed into orthogonal eigenspaces.
- [[optics]] — builds upon wave equation solutions to describe the physical behavior of light, including diffraction, refraction, and interference.
- [[isaac-newton]] — established classical mechanics and the fundamental laws of motion from which continuous wave mechanics was subsequently derived.

## see also

- [[calculus]] · [[derivative]] · [[periodic-function]] · [[trigonometric-function]] · [[linear-algebra]] · [[isaac-newton]]

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
