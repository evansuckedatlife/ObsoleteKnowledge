---
type: concept
category: science
defines: [Kirchhoff's laws, Kirchhoff's first law, Kirchhoff's second law, current law, voltage law]
related: ["[[circuit]]", "[[voltage]]", "[[current]]", "[[resistor]]", "[[circuit-topology]]"]
requires: ["[[circuit]]", "[[current]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Kirchhoff's laws

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Kirchhoff's laws** are two fundamental principles governing [[current]] and [[voltage]] in electrical [[circuit|circuits]], formulated by German physicist *Gustav Kirchhoff* in 1845. The current law (KCL) states that the sum of currents entering a node equals the sum leaving it (conservation of charge), while the voltage law (KVL) states that the sum of voltages around any closed loop is zero (conservation of energy). Together, they provide the mathematical framework for analyzing complex circuits of any topology.

## you gotta know

- *Kirchhoff's Current Law (KCL):* the algebraic sum of currents entering and leaving any node in a circuit equals zero; equivalently, current is conserved at junctions.
- *Kirchhoff's Voltage Law (KVL):* the sum of all [[voltage]] changes around any closed loop in a circuit is zero; no energy is created or destroyed in a circuit path.
- KCL follows from charge conservation: charge cannot accumulate at a node, so whatever current flows in must flow out (or charge steady-state current).
- KVL follows from energy conservation: the total work done by electric fields in moving a charge around a closed path must be zero because the field is conservative.
- Both laws apply to any circuit topology—series, parallel, or mixed—and to both DC (direct current) and AC (alternating current) circuits.
- KCL is the basis for the nodal analysis method: assigning voltages to each node and writing current-conservation equations solves for all node voltages.
- KVL is the basis for mesh analysis (or loop analysis): assigning loop currents and writing voltage-sum equations for each independent loop solves for all currents.
- The laws hold in the ideal circuit limit (thin wires, no radiation losses); real circuits at very high frequencies must account for electromagnetic wave effects beyond the lumped-element approximation.
- Together with Ohm's law, Kirchhoff's laws form the complete foundation for classical circuit theory and practical circuit design.

## connections

- [[circuit]] — the system of components Kirchhoff's laws govern.
- [[voltage]] — one of the two quantities conserved in a circuit (via KVL).
- [[current]] — the other quantity conserved in a circuit (via KCL).
- [[resistor]] — a passive component whose voltage and current obey [[ohms-law]], which combined with Kirchhoff's laws allows complete circuit analysis.
- [[circuit-topology]] — the architecture (connections) to which Kirchhoff's laws apply.

## see also

[[circuit]] · [[voltage]] · [[current]] · [[ohms-law]]

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
