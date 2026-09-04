---
type: concept
category: science
defines: [amplifier, electronic amplifier]
related: ["[[analog-computation]]", "[[analog-to-digital]]", "[[resistor]]", "[[electron]]", "[[cold-war]]", "[[central-processing-unit]]"]
requires: ["[[resistor]]", "[[electron]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# amplifier

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

An **amplifier** is an active electronic device or circuit that increases the power, voltage, or current of a time-varying signal by modulating energy drawn from an external power supply. Developed alongside the thermionic triode vacuum tube in the early twentieth century and revolutionized by the solid-state transistor, it serves as the primary building block of modern communication, audio engineering, and signal conditioning. In instrumentation and computing, specialized configurations such as the **operational amplifier** provide high-gain linear amplification governed precisely by external negative feedback networks.

## you gotta know

- Increases the amplitude of an input electrical signal without significantly altering its waveform, quantified by the ratio of output to input known as *gain*.
- Relies critically on negative feedback, a stabilizing principle formalized by *Harold Stephen Black* at *Bell Telephone Laboratories* to trade high open-loop gain for linearity, broader bandwidth, and reduced distortion.
- Categorized into standard operational classes based on conduction angle: *Class A* conducts over the full 360-degree input cycle for minimum distortion, *Class B* conducts for 180 degrees using push-pull pairs, *Class AB* introduces a slight bias to eliminate crossover distortion, and switching modes like *Class D* achieve high energy efficiency through pulse-width modulation.
- The **operational amplifier**, or op-amp, features a differential input with extremely high open-loop voltage gain, high input impedance, and low output impedance, functioning as the quintessential linear gain block.
- Characterized by performance metrics including the *gain-bandwidth product*, input offset voltage, slew rate, and common-mode rejection ratio (*CMRR*).
- Formed the fundamental active component of mid-century electrical analog computers, using feedback configurations around vacuum-tube or solid-state op-amps to execute real-time mathematical operations.
- Serves as an indispensable buffer, preamplifier, and anti-aliasing filter stage before signal sampling in modern conversion systems.

## connections

- [[analog-computation]] — provides the high-gain active element configured with passive components to model differential equations.
- [[analog-to-digital]] — conditions, scales, and buffers weak input voltages prior to quantization.
- [[resistor]] — establishes negative feedback ratios and sets closed-loop gain in operational circuits.
- [[electron]] — the fundamental charge carrier whose flow is modulated across semiconductor junctions or vacuum gaps.
- [[central-processing-unit]] — relies on digital logic gates built from switching amplifier stages fabricated at microscopic scale.
- [[cold-war]] — spurred intense development of robust operational amplifiers for missile guidance and radar systems.

## see also

- [[analog-computation]] · [[analog-to-digital]] · [[resistor]]

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
