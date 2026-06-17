---
type: term
category: science
defines: ["Filter Circuit", "electrical filter", "active filter", "passive filter"]
related: ["[[capacitor]]", "[[inductor]]", "[[resistor]]", "[[frequency]]", "[[signal-processing]]", "[[rectifier]]", "[[power-supply]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Filter Circuit

## summary

A **filter circuit** is an electronic circuit that selectively passes signals of certain frequencies while attenuating (weakening) others. Filters are fundamental in power supplies (smoothing ripple), audio systems (removing hum), and signal processing (isolating desired information from noise). They exploit the frequency-dependent behavior of capacitors and inductors to achieve frequency selectivity without active amplification.

## you gotta know

- **Four main types:** low-pass (blocks high frequencies, passes low), high-pass (blocks low, passes high), band-pass (passes a range), and band-stop/notch (rejects a range).
- **Passive vs. active:** passive filters use only R, L, C components and are simple but have limited control; active filters use op-amps to amplify and shape response more precisely.
- **Cutoff frequency:** the frequency at which a filter's response drops to 70.7% (−3 dB) of its pass-band level; defines the boundary between pass and reject regions.
- **Ripple and rolloff:** pass-band ripple is unwanted signal variation; stop-band rolloff (attenuation slope) quantifies how quickly rejection increases beyond cutoff, measured in dB/octave.
- **Common applications in power supplies:** a capacitor-inductor low-pass filter smooths the rectified AC (ripple) into clean DC; essential because raw rectified voltage contains high-frequency harmonics.
- **Order and complexity:** a first-order filter has one reactive element (C or L); higher orders (second, third, etc.) provide steeper rolloff but greater complexity.
- **Resonance:** LC circuits can resonate at a specific frequency, creating a sharp peak (band-pass) or dip (band-stop), useful for tuning radio receivers or rejecting 50/60 Hz mains noise.

## connections

- [[capacitor]] — stores charge and blocks DC; its impedance decreases with frequency, making it ideal for low-pass filtering.
- [[inductor]] — impedes AC current and passes DC; used in power-supply filters to smooth ripple and in LC oscillators.
- [[resistor]] — provides damping and frequency-independent attenuation; combined with C or L creates first-order filters.
- [[power-supply]] — employs LC filters to convert rectified AC into smooth DC rails.
- [[signal-processing]] — filters isolate desired signals from noise across audio, RF, and data communications.
- [[rectifier]] — produces ripple-laden output that a filter circuit must smooth.
- [[frequency]] — filters exploit frequency-dependent impedance to differentiate signals.

## see also

- [[capacitor]] · [[inductor]] · [[power-supply]] · [[signal-processing]]

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

Lists: Mark read: `INPUT[toggle:read]`
