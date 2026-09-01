---
type: concept
category: science
defines: [Current limiting]
related: ["[[resistor]]", "[[ohms-law]]", "[[power-dissipation]]", "[[circuit-protection]]", "[[thermal-design]]"]
requires: ["[[resistor]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Current Limiting

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Current limiting** is the practice of restricting the maximum electrical current flowing through a component or circuit to safe levels, preventing damage from overcurrent. Accomplished primarily through resistance—typically via a *resistor* in series with the load—current limiting protects sensitive components like LEDs and ICs from burnout, manages power dissipation, and prevents thermal runaway. It is an essential principle in electronics design and circuit protection.

## you gotta know

- Current limiting is governed by Ohm's Law: *I* = *V* / *R*; increasing resistance decreases current, and this relationship is the foundation of the technique.
- The most straightforward current-limiting method is placing a resistor in series with the load; for an LED driven by a 5V source requiring 20mA, a resistor of approximately 250 ohms limits current.
- Without current limiting, LEDs would instantly burn out; they have a fixed forward voltage (typically 1.8–3.6V depending on color) but no internal current regulation, so voltage must be dropped externally.
- Power dissipation through a current-limiting *resistor* is given by *P* = *I²* × *R* or *P* = *V* × *I*; high dissipation generates heat, requiring adequate resistor power rating (typically ¼W, ½W, or 1W).
- Fuses and circuit breakers are thermal or magnetic current-limiting devices that protect entire circuits by breaking the connection if current exceeds a threshold.
- Active current limiting using regulators or op-amps provides more sophisticated protection, maintaining constant current even as voltage varies—critical in precision applications.
- Thermal design must account for current-limiting resistor heat; inadequate thermal management can cause resistor failure or damage to nearby components.

## connections

- [[resistor]] — the primary component used for current limiting; chosen based on desired current and power dissipation.
- [[ohms-law]] — the electrical principle governing current-limiting calculations.
- [[led]] — a component requiring current limiting for safe operation.
- [[circuit]] — the broader electrical system being protected.
- [[fuse-circuit-breaker]] — backup protection devices that limit current when main limiting fails.
- [[power-dissipation]] — the energy released as heat by the limiting resistor.

## see also

- [[resistor]] · [[ohms-law]] · [[led]] · [[fuse-circuit-breaker]]

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
