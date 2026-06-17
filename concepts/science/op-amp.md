---
type: term
category: science
defines: [Op-amp, "operational amplifier"]
related: ["[[amplifier]]", "[[feedback-control]]", "[[filter-circuit]]", "[[analog-computation]]"]
requires: []
lists: ["[[circuit-components]]"]
tour_order: 0
read: false
---

# Op-Amp

## summary

An **op-amp** (operational amplifier) is an integrated circuit containing a high-gain differential amplifier with very high input impedance and low output impedance, designed to be applied with external feedback networks to implement almost any linear or non-linear analog function. Modern op-amps are among the most versatile and cost-effective building blocks in electronics.

## you gotta know

- The op-amp has three terminals: non-inverting input (+), inverting input (−), and output; two power supplies (typically ±15 V or ±5 V); gain without feedback is 100,000–1,000,000 (80–120 dB).
- With *negative feedback* (output routed back to inverting input), the op-amp forces both inputs to the same voltage; this *virtual short* enables predictable, linear circuit behavior.
- The *gain-bandwidth product* (GBW, measured in MHz) is constant; reducing closed-loop gain increases bandwidth: f_c = GBW / A_v; a 100× amplifier with GBW = 1 MHz has 10 kHz bandwidth.
- An *inverting amplifier* applies input to the inverting pin (non-inverting grounded); output inverts the signal and scales by A_v = −R_feedback / R_input.
- A *non-inverting amplifier* applies input to the non-inverting pin; output is in-phase: A_v = 1 + (R_feedback / R_input).
- *Summing amplifier* (inverting adder) routes multiple inputs through resistors to the inverting pin; weighted sum is inverted and amplified.
- *Integrator* (RC feedback) converts input voltage ramps to output frequency (integrates dV/dt); used in function generators and analog computers.
- *Comparator* (no feedback) amplifies the difference between inputs to saturation; used as a high-speed voltage threshold detector and ADC front-end.

## connections

- [[amplifier]] — op-amps are the workhorse linear amplifier; frequency response, gain, and linearity set by feedback.
- [[feedback-control]] — negative feedback defines gain and stability; bandwidth-gain tradeoff is fundamental.
- [[filter-circuit]] — active filters (Sallen-Key, inverting) use op-amps for precise frequency response without large inductors.
- [[resistor-capacitor]] — feedback resistors and capacitors set gain, bandwidth, and function (inverting, summing, integrating).
- [[analog-to-digital]] — op-amps buffer and condition signals for ADCs; comparators serve as threshold detectors.

## see also

- [[resistor]] · [[capacitor]] · [[amplifier]] · [[filter-circuit]]

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
