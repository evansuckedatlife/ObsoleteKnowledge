---
type: term
category: science
defines: [Ground, Earth, Reference]
related: ["[[circuit-topology]]", "[[potential-difference]]", "[[signal-integrity]]", "[[return-path]]"]
requires: []
lists: ["[[circuit-components]]"]
tour_order: 0
read: false
---

# Ground

## summary

**Ground** is an arbitrary reference point in a circuit assigned zero volts, against which all other voltages are measured. Though sometimes called "earth" (especially in AC mains safety), ground in most electronics is a local reference plane or conductor, not a physical earth connection. All voltage measurements are relative; ground is the chosen zero.

## you gotta know

- Ground is a *reference*, not an absolute; every circuit voltage is measured relative to ground: V_node = V_node − V_ground.
- A single-point ground (one return path) minimizes noise loops; multiple return paths at different frequencies create ground bounce and crosstalk.
- *Star grounding* connects all ground returns to a single point, preventing ground loops that couple noise into sensitive signals.
- In AC power, "earth ground" (true Earth) is a safety requirement; low-impedance return through the utility ground protects against shock and fire.
- Ground planes in PCBs provide a low-impedance return path for current and act as shields for high-frequency noise.
- *Floating ground* (no connection to mains earth) is used in safety-isolated circuits; ground is defined locally within the isolated domain.
- Common-mode voltage is the voltage of ground itself relative to mains earth; circuits must tolerate this offset or reject it via differential sensing.
- In analog circuits, ground noise (ripple on the return path) couples into signal paths and degrades dynamic range; power and signal grounds may be separated near sensitive amplifiers.

## connections

- [[circuit-topology]] — ground is the reference node; all voltages are defined relative to it.
- [[potential-difference]] — voltage is the difference between two nodes; one is chosen as ground.
- [[signal-integrity]] — poor grounding introduces noise and crosstalk in digital and analog signals.
- [[return-path]] — ground serves as the return conductor for all circuit currents.
- [[impedance-matching]] — ground planes and controlled impedance require careful ground design.

## see also

- [[resistor]] · [[capacitor]] · [[source]] · [[op-amp]]

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
