---
type: term
category: science
defines: [LED, "light-emitting diode"]
related: ["[[diode]]", "[[electroluminescence]]", "[[photon-emission]]", "[[current-limiting]]"]
requires: []
lists: ["[[circuit-components]]"]
tour_order: 0
read: false
---

# LED

## summary

An **LED** (light-emitting diode) is a semiconductor diode that emits light when forward-biased, converting electrical current directly into photons through electroluminescence. LEDs are among the most efficient light sources available, with lifetimes exceeding 50,000 hours, and are ubiquitous in indicators, displays, and general illumination.

## you gotta know

- LEDs emit light via *electroluminescence*—when a forward-biased diode carries current, electrons recombine with holes in the bandgap, releasing energy as a photon.
- The *bandgap energy* of the semiconductor material determines photon wavelength (color): wider gap → shorter wavelength (blue); narrower gap → longer wavelength (red).
- Forward voltage drop varies with LED color: red/amber ~1.8–2.0 V, green/yellow ~2.0–2.2 V, blue/white ~3.0–3.5 V; exceeding V_f by even 0.1–0.2 V significantly increases current and shortens life.
- *Luminous intensity* is measured in *candelas* (cd) and depends on forward current; typical low-power LEDs at 20 mA draw 1–100 mcd (millicandelas).
- A *series current-limiting resistor* is essential to protect the LED: R = (V_supply − V_f) / I_desired (e.g., 5 V supply, 2 V drop, 20 mA desired → 150 Ω resistor).
- High-power LEDs (1–100 W) require active current limiting (constant-current driver), thermal sinking, and careful management to avoid catastrophic failure.
- *RGB LEDs* contain red, green, and blue dies in one package; mixing brightness levels creates any visible color.
- Lifespan degrades with temperature and current stress; operating at 50% rated current extends life significantly versus maximum current.

## connections

- [[diode]] — LEDs are diodes; forward-biased PN junction emits light instead of wasting energy as heat.
- [[electroluminescence]] — the physics mechanism; energy released as photons, not thermal radiation.
- [[resistor]] — a series resistor is mandatory to limit LED current and prevent burnout.
- [[current-limiting]] — proper biasing protects the LED and maximizes brightness and lifespan.
- [[indicator-circuit]] — LEDs confirm power-on, status, and mode switching in nearly all electronic devices.

## see also

- [[diode]] · [[resistor]] · [[source]] · [[photodiode]]

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
