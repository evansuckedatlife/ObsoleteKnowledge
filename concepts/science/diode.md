---
type: term
category: science
defines: [Diode, "PN junction"]
related: ["[[rectifier]]", "[[led]]", "[[junction-voltage]]", "[[forward-bias]]", "[[reverse-bias]]"]
requires: []
lists: ["[[circuit-components]]"]
tour_order: 0
read: false
---

# Diode

## summary

A **diode** is a two-terminal semiconductor device constructed from a *PN junction* (p-type and n-type silicon fused together) that conducts current primarily in one direction. Diodes are the foundation for rectification, protection, and non-linear circuit functions, allowing current to flow when forward-biased and blocking it when reverse-biased.

## you gotta know

- *Forward bias* (positive voltage applied to p-side) enables current flow across the junction; *reverse bias* (negative on p-side) blocks current (except for a small leakage current).
- The *forward voltage drop* (V_f) across a silicon diode is ~0.7 V; for germanium, ~0.3 V; this constant drop defines rectified and clamping circuits.
- A diode conducts when forward voltage exceeds the threshold (0.7 V for Si); below threshold, the junction capacitance stores charge but negligible current flows.
- *Reverse breakdown* occurs at the reverse voltage rating (e.g., 1000 V for a 1N4007); exceeding this causes avalanche multiplication and device failure (destructive unless current-limited).
- *Schottky diodes* (metal-semiconductor junction) have lower forward drop (~0.3–0.4 V Si, even lower for specialty materials) and faster switching, critical in switching supplies.
- *PIN diode* (p-intrinsic-n) has an intrinsic (undoped) layer providing high-impedance reverse bias; acts as a voltage-dependent resistor and is used in RF switches.
- *Zener diode* operates in reverse breakdown with a stable knee voltage; used as a voltage regulator (shunt regulation) and protection device.
- *Varactor diode* (junction capacitance) varies capacitance with reverse voltage; used in frequency tuning and phase modulators.

## connections

- [[rectifier]] — diodes convert AC to DC; the bridge rectifier uses four diodes.
- [[led]] — a forward-biased diode junction emits light; brightness depends on forward current.
- [[junction-voltage]] — the 0.7 V drop is a defining characteristic of silicon diode behavior.
- [[transistor]] — BJTs and FETs contain parasitic diodes (base-collector and drain-substrate junctions).
- [[protection-circuit]] — diodes clamp voltage transients and prevent reverse current.

## see also

- [[led]] · [[rectifier]] · [[transistor]] · [[capacitor]]

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

Lists: [[circuit-components]] · Mark read: `INPUT[toggle:read]`
