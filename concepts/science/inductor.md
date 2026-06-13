---
type: term
category: science
defines: [Inductor, "inductive coil"]
related: ["[[capacitor]]", "[[magnetic-field]]", "[[inductance]]", "[[transformer]]"]
lists: ["[[circuit-components]]"]
read: false
---

# Inductor

## summary

An **inductor** is a two-terminal passive component that stores electrical energy in a magnetic field created by current flowing through a coil of wire. Inductance is measured in *henries* (H), and inductors oppose changes in current—a core principle in AC circuits, filters, and energy storage.

## you gotta know

- *Inductance* (L) is the property that relates a changing current to the induced voltage across the coil: V = L(dI/dt), measured in *henries*.
- An inductor resists changes in current; DC steady-state current flows freely (zero impedance), but a sudden change produces a large opposing voltage (back-EMF).
- *Inductive reactance* (X_L = 2πfL) increases with frequency; at DC, reactance is zero; at high AC frequencies, an inductor blocks current.
- Inductors are wound on a core (air, iron, ferrite); core material amplifies inductance by concentrating the magnetic field.
- *Mutual inductance* occurs when two coils are coupled magnetically—the basis for transformers and isolation in switching power supplies.
- Inductor's energy is proportional to current: E = ½LI²; when current is suddenly interrupted, stored energy causes voltage spikes (risk of arcing).
- LC oscillators (resonant circuits) combine inductors and capacitors to generate or select specific frequencies.
- Ferrite chokes suppress electromagnetic interference (EMI) by blocking high-frequency noise while passing DC and low-frequency signals.

## connections

- [[capacitor]] — form LC resonant circuits; combined impedance varies with frequency to filter or oscillate.
- [[transformer]] — two inductively coupled coils enable voltage stepping and galvanic isolation.
- [[magnetic-field]] — inductors store energy by creating a magnetic field around the coil.
- [[filter-circuit]] — inductive elements suppress switching noise and harmonics in power supplies.
- [[back-emf]] — the voltage spike when an inductor's current is forced to change rapidly.

## see also

- [[capacitor]] · [[transformer]] · [[resistor]] · [[filter-circuit]]

<!-- footer -->

---

Lists: [[circuit-components]] · Mark read: `INPUT[toggle:read]`
