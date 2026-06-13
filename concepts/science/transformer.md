---
type: term
category: science
defines: [Transformer]
related: ["[[inductor]]", "[[magnetic-coupling]]", "[[voltage-transformation]]", "[[step-up-down]]"]
lists: ["[[circuit-components]]"]
read: false
---

# Transformer

## summary

A **transformer** is a passive component consisting of two or more inductively coupled coils wound on a shared magnetic core, used to transfer electrical energy between circuits while changing voltage and current levels. Transformers operate only on AC, as they rely on changing magnetic flux to induce voltage in the secondary coil.

## you gotta know

- The *turns ratio* (N₁:N₂) determines voltage and current scaling: V₂/V₁ = N₂/N₁ and I₁/I₂ = N₂/N₁ (for an ideal transformer).
- *Step-up* transformers (N₂ > N₁) increase voltage and decrease current; *step-down* transformers do the reverse—used in power supplies.
- Transformers provide *galvanic isolation*—the primary and secondary coils are electrically separate, floating with respect to each other; critical for safety in high-voltage circuits.
- Core material (iron laminations, ferrite, toroidal) concentrates magnetic flux and minimizes losses; laminated cores reduce eddy-current heating.
- *Impedance matching* via transformers allows maximum power transfer between circuits of different impedances (e.g., antenna to receiver).
- Real transformers have *copper losses* (resistive heating in windings) and *core losses* (hysteresis and eddy currents); efficiency is typically 95–99%.
- AC frequency affects transformer performance; used at 50–60 Hz in power distribution, kHz–MHz in switching supplies, and GHz in RF circuits.
- No frequency = no transfer: transformers are useless for DC (no changing flux); DC blocking transformers carry DC on top of AC but decouple the DC component.

## connections

- [[inductor]] — transformers are pairs of inductors with mutual magnetic coupling.
- [[magnetic-coupling]] — the physical mechanism by which transformer coils share energy.
- [[voltage-transformation]] — the primary function enabling power distribution and impedance matching.
- [[power-supply]] — step-down transformers reduce mains voltage to usable levels for electronics.
- [[galvanic-isolation]] — transformers float the secondary from ground, critical for safety.

## see also

- [[inductor]] · [[capacitor]] · [[rectifier]] · [[power-supply]]

<!-- footer -->

---

Lists: [[circuit-components]] · Mark read: `INPUT[toggle:read]`
