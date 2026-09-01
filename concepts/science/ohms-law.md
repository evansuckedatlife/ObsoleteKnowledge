---
type: concept
category: science
defines: [Ohm's law]
related: ["[[circuit]]", "[[voltage]]", "[[current]]", "[[resistor]]", "[[resistance]]"]
requires: ["[[circuit]]", "[[current]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Ohm's law

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Ohm's law** is the fundamental relationship between [[voltage]], [[current]], and resistance in an electrical [[circuit]]: `V = IR`, where *V* is voltage in volts, *I* is current in amperes, and *R* is resistance in ohms. First formulated by German physicist *Georg Ohm* in 1827, it describes how a conductor's resistance opposes the flow of electric current for a given applied voltage. While the term "law" suggests universality, Ohm's law is more accurately an empirical description of *ohmic* materials (metals, most resistors) that maintain constant resistance across practical voltage ranges; many materials exhibit non-ohmic behavior under extreme conditions.

## you gotta know

- The simplest statement: `V = IR` or equivalently `I = V/R` or `R = V/I`, relating the three fundamental circuit quantities.
- Ohmic resistance is *linear* and *time-independent*: doubling the voltage doubles the current (at constant temperature); the ratio V/I remains constant.
- *Power dissipation* in a resistor is `P = VI = I²R = V²/R`, showing that power scales with the square of current (or voltage), making current-limiting critical in power-delivery design.
- Resistance arises from microscopic collisions of electrons with atomic lattices; in conductors like copper, it increases slightly with temperature (positive temperature coefficient).
- At the component level, resistors are ubiquitous in [[circuit|circuits]] to set currents, divide voltages, and dissipate power; practical resistors span picoohms (superconductors) to teraohms (insulators).
- *Conductivity* (σ) and *resistivity* (ρ) describe materials: `R = ρL/A`, where resistivity is an intrinsic material property and the resistance of a wire depends on its length *L* and cross-sectional area *A*.
- Non-ohmic materials (diodes, [[transistor|transistors]], lightbulbs) violate `V = IR`: their resistance changes with voltage or current, enabling complex circuit behaviors (rectification, amplification, logic).
- Superconductors (below critical temperature) exhibit zero resistance, enabling lossless current flow; this extreme ohmic behavior at *R = 0* is fundamentally different from normal conductors.

## connections

- [[circuit]] — the system of interconnected components where Ohm's law applies.
- [[voltage]] — the electric potential difference driving current (numerator in **V = IR**).
- [[current]] — the flow of charge driven by voltage against resistance (denominator in **V = IR**).
- [[resistor]] — the component whose resistance is most directly described by Ohm's law.
- [[kirchhoffs-laws]] — Ohm's law combines with Kirchhoff's current and voltage laws to solve complex circuits.

## see also

[[circuit]] · [[voltage]] · [[current]] · [[resistor]]

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
