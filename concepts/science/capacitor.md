---
type: term
category: science
defines: [Capacitor]
related: ["[[resistor]]", "[[dielectric]]", "[[capacitance]]", "[[energy-storage]]"]
lists: ["[[circuit-components]]"]
read: false
---

# Capacitor

## summary

A **capacitor** is a two-terminal passive component that stores electrical energy in an electric field between two conducting plates separated by an insulating material called a *dielectric*. Capacitance is measured in *farads* (F), though practical values are typically in microfarads (μF) or nanofarads (nF).

## you gotta know

- *Capacitance* (C) is defined as the ratio of charge stored (Q) to applied voltage (V): C = Q/V, measured in *farads*.
- The dielectric material (ceramic, film, electrolytic) determines breakdown voltage and capacitance density; higher permittivity allows smaller physical size.
- Electrolytic capacitors are polarized (marked with + and −); exceeding reverse voltage destroys the dielectric, causing catastrophic failure.
- In DC steady-state, a capacitor acts as an open circuit; in AC or during charging/discharging, it passes current.
- The *RC time constant* (τ = R × C in seconds) governs charge and discharge rates; at t = τ, capacitor voltage reaches ~63% of applied voltage.
- Series capacitors follow the reciprocal rule: 1/C_total = 1/C₁ + 1/C₂; parallel capacitors add directly.
- Capacitors block DC (used in AC coupling) but pass AC through, making them essential for filtering high-frequency noise.
- Coupling capacitors decouple AC signals between stages; bypass capacitors shunt high-frequency noise to ground near supply pins.

## connections

- [[resistor]] — RC networks filter signals and establish timing constants in analog circuits.
- [[dielectric]] — the insulating material whose properties define capacitor behavior and voltage rating.
- [[inductor]] — resonate in LC circuits to select specific frequencies for oscillation or filtering.
- [[energy-storage]] — capacitors store energy electrostatically and release it quickly for power delivery.
- [[filter-circuit]] — capacitors are the active element in low-pass, high-pass, and band-pass filters.

## see also

- [[resistor]] · [[inductor]] · [[diode]] · [[transformer]]

<!-- footer -->

---

Lists: [[circuit-components]] · Mark read: `INPUT[toggle:read]`
