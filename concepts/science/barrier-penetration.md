---
type: concept
category: science
defines: [Barrier penetration, barrier tunneling]
related: ["[[quantum-mechanics]]", "[[wavefunction]]", "[[electron]]", "[[atom]]", "[[nucleus]]", "[[central-processing-unit]]", "[[back-emf]]"]
requires: ["[[quantum-mechanics]]", "[[wavefunction]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Barrier Penetration

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Barrier penetration**, synonymous with **quantum tunneling** or **barrier tunneling**, is the non-classical phenomenon whereby a subatomic particle crosses a potential energy barrier whose height exceeds the particle's own kinetic energy. First formulated theoretically in 1927 by *Friedrich Hund* and applied to nuclear physics by *George Gamow*, *Ronald Gurney*, and *Edward Condon*, it is a direct consequence of the continuous spatial nature of the quantum [[wavefunction]]. The mechanism quantifies tunneling probability vs. energy and width, dictating the decay rates of heavy nuclei, the thermonuclear fusion rates inside stars, and the physical scaling limits of modern solid-state electronics.

## you gotta know

- Occurs because matter exhibits wave-particle duality governed by the *Schrödinger equation*, where the spatial [[wavefunction]] does not terminate abruptly at a barrier boundary but decays as an evanescent exponential wave before emerging with reduced amplitude on the opposite side.
- Quantifies tunneling probability vs. energy and width via the transmission coefficient $T$, which scales exponentially according to the *Wentzel–Kramers–Brillouin* (*WKB*) approximation as $T \approx \exp(-2 \int \kappa(x) dx)$, where $\kappa$ represents the imaginary wave vector within the barrier.
- Solved the physical puzzle of the *Geiger–Nuttall law* in radioactive alpha decay, wherein *George Gamow* demonstrated that minute differences in alpha particle kinetic energy yield multi-order-of-magnitude differences in half-lives across isotopes of the atomic [[nucleus]].
- Sustains nuclear fusion in the core of the Sun and other main-sequence stars, enabling low-energy protons to overcome their mutual electrostatic repulsion at temperatures hundreds of times lower than the classical *Coulomb barrier* threshold.
- Formulates the operating mechanism of the scanning tunneling microscope (*STM*), invented by *Gerd Binnig* and *Heinrich Rohrer*, which measures tiny variations in electron tunneling current across an atomic gap to map surface topography with sub-angstrom resolution.
- Produces gate dielectric leakage current in sub-nanometer field-effect transistors inside each [[central-processing-unit]], generating parasitic heat and presenting a major obstacle to the continuation of *Moore's law*.
- Underpins solid-state devices such as the *Esaki diode*, which exhibits negative differential resistance, as well as superconducting *Josephson junctions*, which are used in ultrasensitive magnetometers and superconducting quantum bits.

## connections

- [[quantum-mechanics]] — the overarching physical theory that replaced classical determinism with probabilistic wave mechanics and permitted barrier traversal.
- [[wavefunction]] — the mathematical amplitude whose exponential attenuation inside a classically forbidden region determines the barrier transmission coefficient.
- [[electron]] — the low-mass charged lepton that readily undergoes quantum tunneling through vacuum gaps and dielectric gates.
- [[nucleus]] — the compact positive core that expels alpha particles via barrier penetration through the confining nuclear potential well.
- [[atom]] — defines the atomic-scale potential wells and electron orbitals mapped experimentally by scanning tunneling microscopy.
- [[central-processing-unit]] — suffers from unwanted quantum leakage currents when insulating oxide barriers become only a few atoms thick.
- [[back-emf]] — transient counter-voltage spikes can drastically raise local electric fields across thin insulators, driving field emission and tunneling breakdown.

## see also

- [[wavefunction]] · [[quantum-mechanics]] · [[electron]] · [[central-processing-unit]] · [[back-emf]]

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

Lists: [[science-hubs]] · Mark read: `INPUT[toggle:read]`
