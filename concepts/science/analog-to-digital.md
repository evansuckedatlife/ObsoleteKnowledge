---
type: concept
category: science
defines: [analog-to-digital, analog-to-digital converter, ADC, digitization]
related: ["[[amplifier]]", "[[analog-computation]]", "[[central-processing-unit]]", "[[algorithm]]", "[[resistor]]", "[[cold-war]]"]
requires: ["[[resistor]]", "[[central-processing-unit]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# analog-to-digital

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Analog-to-digital** conversion is the electronic process of transforming a continuous-time physical signal, such as an acoustic voltage or temperature reading, into a discrete-time sequence of quantized binary numerical values. Performed by an **analog-to-digital converter** (*ADC*), this translation bridges continuous real-world phenomena and discrete computational architectures. The process relies on sampling at uniform intervals and mapping continuous amplitudes onto a finite set of digital codes, forming the foundation of digital audio, telecommunications, instrumentation, and modern data acquisition.

## you gotta know

- Entails two fundamental mathematical operations: *sampling*, which discretizes the continuous time domain, and *quantization*, which discretizes the continuous amplitude spectrum into a discrete digital code.
- Governed by the *Nyquist-Shannon sampling theorem*, which dictates that a band-limited continuous signal must be sampled at a rate greater than twice its highest frequency component (the *Nyquist rate*) to prevent frequency aliasing.
- Introduces unavoidable *quantization error*, a rounding noise inherent in mapping continuous ranges to discrete binary steps, which sets the theoretical maximum signal-to-quantization-noise ratio (*SQNR*) at roughly six decibels per bit of resolution.
- Relies on precision analog front-end circuits, notably an operational **amplifier** acting as an impedance buffer and low-pass anti-aliasing filter, paired with a sample-and-hold circuit that locks signal voltages during measurement.
- Implemented through diverse hardware architectures, including ultra-fast *flash ADCs* using parallel comparator banks, area-efficient *successive approximation register* (*SAR*) converters using binary search algorithms, and high-resolution *delta-sigma* (*ΔΣ*) modulators that exploit oversampling and noise shaping.
- Enabled the historical transition from real-time continuous computing systems to modern discrete digital signal processors and microcontrollers.
- Quantified by key engineering figures of merit such as effective number of bits (*ENOB*), integral non-linearity (*INL*), differential non-linearity (*DNL*), and conversion latency.

## connections

- [[amplifier]] — conditions, scales, and buffers incoming continuous voltages and acts as a high-speed comparator within converter hardware.
- [[analog-computation]] — historically handled continuous voltage signals directly before being superseded by digital processors fed by converters.
- [[central-processing-unit]] — receives, stores, and executes software instructions on the discrete numerical data streams produced by converters.
- [[algorithm]] — digital routines applied to convert, filter, and extract meaning from digitized numerical data.
- [[resistor]] — deployed in precision networks like *R-2R ladders* to synthesize reference voltages inside converters.
- [[cold-war]] — accelerated development of high-speed radar digitizers and military telemetry conversion hardware.

## see also

- [[amplifier]] · [[analog-computation]] · [[central-processing-unit]]

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
