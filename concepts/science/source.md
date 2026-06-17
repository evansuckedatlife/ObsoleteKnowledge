---
type: term
category: science
defines: [Source, "voltage source", "current source"]
related: ["[[resistor]]", "[[circuit-topology]]", "[[thevenin-equivalent]]", "[[power-delivery]]"]
requires: []
lists: ["[[circuit-components]]"]
tour_order: 0
read: false
---

# Source

## summary

A **source** is an active circuit element that supplies electrical energy to a circuit. Two idealized types exist: a *voltage source* maintains a fixed potential difference across its terminals regardless of load (e.g., a battery), and a *current source supplies* a constant current regardless of the load voltage. Real sources exhibit *internal resistance* or *output impedance*.

## you gotta know

- An ideal *voltage source* has zero internal resistance; its terminal voltage equals its EMF (electromotive force) regardless of current drawn.
- An ideal *current source* has infinite internal resistance; it maintains constant current whether connected to 1 Ω or 1 MΩ.
- Real batteries are modeled as an ideal voltage source in series with internal resistance; the terminal voltage drops under load (V = E − I·r).
- *Thevenin equivalent* reduces any linear network to a single voltage source with series resistance, simplifying circuit analysis.
- *Norton equivalent* expresses the same network as a current source with parallel resistance—mathematically equivalent to Thevenin.
- DC sources (batteries, power supplies) maintain constant voltage; AC sources oscillate sinusoidally, triangularly, or with other waveforms.
- Sources can be dependent (controlled) — a voltage-controlled voltage source (VCVS) or current-controlled current source (CCCS) output depends on another circuit variable.
- *Source transformation* converts between voltage and current representations: a voltage source + series resistance is equivalent to a current source + parallel resistance.

## connections

- [[resistor]] — resistive loads consume power from the source; internal resistance limits current in real sources.
- [[circuit-topology]] — all circuits are built from sources and loads; sources are the driving force.
- [[thevenin-equivalent]] — simplifies any source-and-network combination to a single equivalent source.
- [[power-delivery]] — sources transfer energy to loads; maximum power transfer occurs when load impedance matches source impedance.
- [[battery]] — the most common physical realization of a voltage source.

## see also

- [[resistor]] · [[battery]] · [[power-supply]] · [[transformer]]

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
