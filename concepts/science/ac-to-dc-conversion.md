---
type: practice
category: science
defines: [AC-to-DC conversion, rectification, AC/DC conversion]
related: ["[[diode]]", "[[transformer]]", "[[power-supply]]", "[[resistor]]", "[[acid]]", "[[absolute-zero]]", "[[industrial-revolution]]"]
requires: ["[[electron]]", "[[resistor]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# AC-to-DC Conversion

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**AC-to-DC conversion**, commonly known as electrical **rectification** or **AC/DC conversion**, is the foundational process of converting alternating current—whose periodic oscillations reverse direction—into unidirectional direct current. Developed during the late nineteenth and early twentieth centuries to bridge incompatible power systems, rectification enabled the modern electrical grid to combine efficient high-voltage AC transmission with stable DC electronics. It remains indispensable for operating digital computational hardware, telecommunications networks, electric vehicle drivetrains, and electrochemical storage systems worldwide.

## you gotta know

- Rectification fundamentally relies on nonlinear circuit elements, primarily semiconductor p-n junction diodes, which conduct freely in forward bias while blocking electrical current in reverse bias.
- Half-wave rectifiers allow current to pass during only one half of the input AC sinusoidal cycle, producing a pulsed output with high ripple voltage and poor transformer utilization.
- Full-wave bridge rectifiers, standardized by German physicist *Leo Graetz* as the *Graetz* circuit, employ four arranged diodes to route both alternating polarities into an identical unidirectional output.
- Smoothing stages immediately following rectification incorporate reservoir capacitors and choke inductors as low-pass filters to suppress voltage ripple and produce a steady DC supply.
- Switched-mode power supplies (SMPS) have largely superseded bulky linear transformers by chopping rectified DC at high frequencies using MOSFETs and pulse-width modulation, attaining energy efficiencies exceeding ninety percent.
- Historic early conversion technologies included rotating motor-generator sets, mechanical commutators, toxic mercury-arc rectifiers developed by *Peter Cooper Hewitt*, and solid-state selenium stacks.
- Rectified direct current supplies the continuous unidirectional charging current necessary to replenish electrochemical storage banks, including industrial lead-[[acid]] batteries.
- Cryogenic power electronics operating near [[absolute-zero]] implement superconducting rectifiers and Josephson junctions that eliminate Ohmic resistive losses, facilitating ultra-efficient current processing for quantum computers.

## connections

- [[electron]] — serves as the physical subatomic charge carrier whose directional drift velocity is constrained to unidirectional flow.
- [[resistor]] — introduces Ohmic dissipation and establishes load resistance, voltage dropping, and thermal management within rectifier networks.
- [[central-processing-unit]] — relies exclusively on low-voltage, ripple-free direct current delivered by onboard voltage regulator modules for logic switching.
- [[motherboard]] — houses multi-phase buck converters and rectifier topologies that distribute conditioned DC power to microprocessors and memory buses.
- [[industrial-revolution]] — established the electrified manufacturing plants and utility grids that fought the "War of the Currents" between Edison and Westinghouse.
- [[acid]] — provides the liquid chemical electrolyte within secondary storage cells that absorb and deliver stabilized direct current.
- [[absolute-zero]] — provides the cryogenic operating environment where superconducting rectification circuits achieve zero electrical resistance.
- [[united-states]] — served as the primary industrial arena where pioneering electrical innovators developed early dynamos, transformers, and distribution networks.

## see also

- [[resistor]] · [[motherboard]] · [[central-processing-unit]] · [[absolute-zero]]

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
