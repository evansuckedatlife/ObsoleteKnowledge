---
type: term
category: science
defines: [Rectifier, "bridge rectifier", "full-wave rectifier", "half-wave rectifier"]
related: ["[[diode]]", "[[transformer]]", "[[power-supply]]", "[[ac-to-dc-conversion]]"]
lists: ["[[circuit-components]]"]
read: false
---

# Rectifier

## summary

A **rectifier** is a circuit that converts alternating current (AC) into direct current (DC) using one or more diodes to allow current flow in only one direction. Rectifiers form the front end of nearly all DC power supplies, converting utility AC (50–60 Hz) or transformer-secondary AC into a rough but usable DC voltage.

## you gotta know

- A *half-wave rectifier* uses a single diode to block the negative half-cycle; only half the AC input appears at the output, resulting in 50% efficiency and high ripple.
- A *full-wave rectifier* uses two diodes and a center-tapped transformer to reverse the negative half-cycle, delivering twice the power of half-wave and lower ripple.
- A *bridge rectifier* (Graetz bridge) uses four diodes arranged so that regardless of AC polarity, current flows in the same direction—most common topology; no center tap required.
- The output of any rectifier is pulsating DC; *ripple voltage* (the AC component) decays as 1/(fC), where f is frequency and C is the filter capacitor; larger C reduces ripple.
- *Peak inverse voltage* (PIV) is the maximum reverse voltage across a diode during the non-conducting half-cycle; diode rating must exceed PIV to prevent breakdown (safety margin ~2×).
- A *rectifier diode* (e.g., 1N4007) has fast switching speed and high voltage/current ratings; slower, cheaper options suffice if frequency is low.
- The *DC average* of a full-wave rectified sine is V_DC ≈ 0.636 × V_peak = 0.45 × V_rms; this is the nominal output before filtering.
- *Synchronous rectification* (using MOSFETs instead of diodes) reduces forward-drop losses in high-current supplies, critical in battery chargers and DC-DC converters.

## connections

- [[diode]] — rectifiers are built from diodes; the forward drop (0.7 V per diode) reduces output voltage.
- [[transformer]] — steps down mains voltage before rectification; bridges DC isolation and provides the AC waveform to rectify.
- [[power-supply]] — rectifiers are the front stage, converting AC input to rough DC; followed by filtering and regulation.
- [[capacitor-filter]] — a large capacitor across the rectifier output smooths ripple; RC time constant determines ripple amplitude.
- [[ac-to-dc-conversion]] — the fundamental function enabling all battery-powered electronics.

## see also

- [[diode]] · [[transformer]] · [[power-supply]] · [[capacitor]]

<!-- footer -->

---

Lists: [[circuit-components]] · Mark read: `INPUT[toggle:read]`
