---
type: term
category: science
defines: [Switch, Contact]
related: ["[[resistor]]", "[[relay]]", "[[logic-gate]]", "[[control-circuit]]"]
lists: ["[[circuit-components]]"]
read: false
---

# Switch

## summary

A **switch** is a mechanical or electronic component that opens or closes a circuit path, controlling whether current can flow. Switches range from simple single-pole single-throw (SPST) hand levers to complex electromechanical relays and solid-state field-effect transistors, all serving to route or block current under user or circuit control.

## you gotta know

- An ideal switch has zero resistance when closed (ON) and infinite resistance when open (OFF); real switches exhibit contact resistance and leakage.
- *Contact bounce* (chatter) occurs when mechanical contacts vibrate during closure, producing multiple brief open/close transients; digital systems require *debouncing* (RC filter or firmware delays).
- Switch nomenclature: SPST (single pole, single throw) is a simple on/off; SPDT (single pole, double throw) has two outputs; DPDT (double pole, double throw) controls two circuits simultaneously.
- A *relay* is an electromagnetically actuated switch—a coil energizes an electromagnet that mechanically opens/closes contacts, providing isolation and high-power switching from a weak control signal.
- *Solid-state switches* (transistors, MOSFETs, IGBTs) have no moving parts, no contact bounce, and switch at nanosecond speeds; they dissipate heat in the ON state (not zero resistance).
- *Analog switches* (transmission gates) pass AC or DC signals with minimal distortion; used for audio/video routing and multiplexing.
- Thermal cycling and arcing degrade mechanical contacts over time; *contact wear* reduces lifecycle.
- *Switch matrix* in keyboards and robotics routes many inputs through a small number of pins; debouncing and scanning prevent false reads.

## connections

- [[resistor]] — contact resistance adds to load impedance; heavy loads require low-resistance contacts.
- [[relay]] — electromechanical switches for high-power or isolated switching.
- [[logic-gate]] — digital switches (transistors) implement Boolean logic.
- [[control-circuit]] — switches are the user interface—buttons, toggles, selector knobs.
- [[transient]] — switch closure creates voltage spikes and inductive kickback (spark) if applied to inductive loads.

## see also

- [[relay]] · [[diode]] · [[transistor]] · [[resistor]]

<!-- footer -->

---

Lists: [[circuit-components]] · Mark read: `INPUT[toggle:read]`
