---
type: term
category: science
defines: [Fuse, Circuit breaker, Overcurrent protection]
related: ["[[resistor]]", "[[current-limiting]]", "[[safety-device]]", "[[thermal-design]]"]
lists: ["[[circuit-components]]"]
read: false
---

# Fuse and Circuit Breaker

## summary

**Fuses** and **circuit breakers** are safety devices that interrupt current flow when it exceeds a rated threshold, protecting circuit components and wiring from overcurrent damage, overheating, and fire. Fuses are single-use; circuit breakers are reusable mechanical switches that automatically trip and reset.

## you gotta know

- A *fuse* is a resistive element (typically a metal alloy) that melts and opens the circuit when current exceeds its rating for a specified time (e.g., a 1 A, slow-blow fuse).
- *Slow-blow* fuses tolerate inrush current and nuisance trips; *fast-blow* fuses respond instantly to overcurrent (e.g., protecting expensive ICs from shorts).
- *Circuit breakers* use either a bimetallic strip (heats and bends open) or an electromagnetic coil (large currents trip instantly); they reset by flipping a lever.
- The *I²t* rating (ampere-squared × time) defines fuse energy; higher values tolerate longer overloads before opening, important in circuits with startup surges.
- A *thermal trip* current is typically 1.5–2× the continuous rating; a *magnetic trip* triggers at 10–20× rating or higher (millisecond response).
- Ground-fault circuit interrupters (GFCIs) detect imbalance between supply and return current (leakage to ground) and trip in ~25 ms—critical for safety in wet environments.
- Fuse and breaker rating must match wire gauge; undersizing risks nuisance trips; oversizing allows wires to overheat and fail, creating fire hazard.
- Coordination: multiple protection devices (fuses or breakers) in series are designed so the upstream device clears faults before downstream devices fail.

## connections

- [[resistor]] — fuses contain resistive elements that dissipate I²R heat until melting.
- [[current-limiting]] — fuses and breakers limit the maximum current in a circuit.
- [[safety-device]] — the primary function is to prevent fire and equipment damage.
- [[power-supply]] — fuses protect power distribution circuits and downstream components.
- [[thermal-design]] — breaker heating determines trip time; poor heat dissipation accelerates tripping.

## see also

- [[resistor]] · [[source]] · [[transformer]] · [[power-supply]]

<!-- footer -->

---

Lists: [[circuit-components]] · Mark read: `INPUT[toggle:read]`
