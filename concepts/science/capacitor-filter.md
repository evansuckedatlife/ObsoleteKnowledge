---
type: concept
category: science
defines: [capacitor filter, capacitive filter, smoothing capacitor, reservoir capacitor]
related: ["[[capacitance]]", "[[resistor]]", "[[electron]]", "[[motherboard]]", "[[central-processing-unit]]", "[[algorithm]]"]
requires: ["[[resistor]]", "[[electron]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# capacitor filter

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **capacitor filter**, often designated a **capacitive filter**, **smoothing capacitor**, or **reservoir capacitor**, is an electronic circuit configuration in which a capacitor is placed in parallel across the output terminals of a rectifier circuit to attenuate alternating voltage ripple. By charging rapidly to the peak rectified voltage and discharging slowly through the load [[resistor]] when the input drops, the filter maintains a continuous direct-current potential. This filtering stage is essential in modern electrical engineering and power supply design, converting pulsating rectified waveforms into stable direct-current power suitable for delicate electronic components.

## you gotta know

- Installed in parallel with the load across the output of a half-wave or full-wave rectifier to smooth pulsating direct-current waveforms into steady direct voltages.
- Charges rapidly toward peak voltage during the conduction phase of rectifier diodes, accumulating mobile [[electron]] charge carriers across its plates.
- Discharges stored electric potential energy slowly through the load [[resistor]] between peaks, bridging the troughs of rectified voltage waves.
- Exhibits an *RC* time constant that determines the rate of voltage decay, with larger resistance or [[capacitance]] values yielding smaller ripple voltages.
- Produces a ripple factor inversely proportional to the load resistance, the filtering [[capacitance]], and the operating ripple frequency of the rectifier.
- Experiences substantial surge currents upon initial energization, necessitating series inrush-limiting elements or soft-start circuits to prevent diode failure.
- Serves as the primary filtering stage in linear power supplies and bulk decoupling rails on any modern computer [[motherboard]].

## connections

- [[capacitance]] — quantifies the electric charge storage capability that governs filter performance and output ripple reduction.
- [[resistor]] — represents the external resistive load that establishes the discharge rate and discharge time constant.
- [[electron]] — serves as the mobile charge carrier accumulating on and departing from the conductive plates during cyclic operation.
- [[motherboard]] — houses high-capacitance filtering arrays to supply clean, smoothed direct-current voltage across distribution rails.
- [[central-processing-unit]] — relies on local capacitor filters to suppress transient switching spikes and maintain tight core voltages.
- [[algorithm]] — models the non-linear transient charge and discharge equations in computer-aided circuit simulation suites.

## see also

- [[capacitance]] · [[resistor]] · [[motherboard]]

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
