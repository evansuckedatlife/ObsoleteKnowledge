---
type: term
category: science
defines: [Resistor, "ohm resistor"]
related: ["[[capacitor]]", "[[inductor]]", "[[ohm-law]]", "[[resistive-heating]]"]
requires: ["[[capacitor]]", "[[inductor]]"]
lists: ["[[circuit-components]]"]
tour_order: 1
read: false
---

# Resistor


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **resistor** is a two-terminal passive component that opposes the flow of electric current, dissipating electrical energy as heat. Measured in *ohms* (Ω), resistors are fundamental to controlling current magnitude, dividing voltage, and protecting circuits from overcurrent conditions.

## you gotta know

- *Ohms* (Ω) is the SI unit of electrical resistance; defined by *Ohm's Law*: V = IR.
- Resistors are *passive* components—they consume energy and convert it to heat, never generating power.
- Resistance is inversely proportional to wire cross-sectional area and directly proportional to length and *resistivity*.
- Carbon-film resistors (orange/brown/gold color bands) are the most common; axial leads for breadboarding.
- Potentiometers are variable resistors with a sliding contact; used in volume knobs and sensor tuning.
- Thermistors have resistance that changes sharply with temperature; NTC (negative temperature coefficient) types drop resistance when hot.
- Series resistors add directly (R_total = R₁ + R₂); parallel resistors follow the reciprocal rule (1/R_total = 1/R₁ + 1/R₂).
- Power dissipation in a resistor is P = I²R or P = V²/R; exceeded power rating causes failure (smoke/charring).

## connections

- [[capacitor]] — form RC time-constant circuits fundamental to timing and filtering.
- [[inductor]] — resonate in LC oscillators; series/parallel combinations create frequency-selective networks.
- [[voltage-divider]] — two resistors in series split a voltage proportionally.
- [[current-limiting]] — resistors protect LEDs and other components from overcurrent.
- [[ohm-law]] — the foundational relationship governing resistor behavior (V = IR).

## see also

- [[capacitor]] · [[inductor]] · [[diode]] · [[led]]

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
