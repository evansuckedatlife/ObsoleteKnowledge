---
type: concept
category: science
defines: [Transistor]
related: ["[[diode]]", "[[switch]]", "[[integrated-circuit]]", "[[semiconductor]]", "[[capacitor]]"]
requires: ["[[diode]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Transistor

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Transistors** are semiconductor devices that amplify or switch electrical signals, forming the foundation of modern electronics. By controlling the flow of current through a small input signal, transistors enable everything from simple switching logic to complex signal amplification. The invention of the transistor in 1947 revolutionized technology by replacing bulky, power-hungry vacuum tubes, enabling the microelectronic era and the digital revolution.

## you gotta know

- Transistors come in two main types: bipolar junction transistors (BJTs), which use current to control current, and field-effect transistors (FETs), which use voltage to control current.
- A transistor has three terminals: in BJTs these are the base (input), collector, and emitter; in FETs they are the gate (input), drain, and source.
- BJTs work by allowing a small base current to control a much larger collector-emitter current, providing current amplification; they are used in analog amplifiers and early digital circuits.
- FETs (including MOSFETs, the dominant type in modern chips) use a voltage applied to the gate to create an electric field that controls current flow; they are more power-efficient than BJTs.
- When biased as a switch, a transistor can be driven between two states: fully off (cutoff) or fully on (saturation), enabling binary logic gates that form the basis of digital computers.
- Millions of transistors are integrated onto microchips; modern processors contain billions, with feature sizes now in the nanometer range.
- The transistor's ability to amplify and switch small signals enabled telecommunications, radio, television, computers, and all modern electronics.
- Gain (amplification factor) in BJTs is hFE or beta (β), the ratio of collector current to base current; typical values range from 20 to 300, allowing small signals to control large currents.
- Transistor aging and degradation occur over time through mechanisms like hot-carrier injection, electromigration, and bias temperature instability, affecting performance in long-running devices.

## connections

- [[diode]] — the simpler semiconductor component; BJTs and FETs contain parasitic diodes.
- [[switch]] — transistors function as electronic switches in digital circuits.
- [[semiconductor]] — the material (silicon or germanium) upon which transistors are built.
- [[integrated-circuit]] — collections of transistors and other components on a single chip.
- [[resistor]] — often paired with transistors in amplifier and switching circuits.
- [[capacitor]] — used with transistors in filters and timing circuits.
- [[central-processing-unit]] — the chip containing billions of transistors performing computation.

## see also

- [[diode]] · [[semiconductor]] · [[integrated-circuit]] · [[central-processing-unit]]

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
