---
type: term
category: science
defines: [PSU, power supply unit, power supply]
related: ["[[motherboard]]", "[[graphics-card]]", "[[central-processing-unit]]", "[[cooling]]"]
requires: ["[[power-supply]]"]
lists: ["[[computer-components]]"]
tour_order: 1
read: false
---

# Power Supply Unit


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **power supply unit** (PSU) is an electrical component that converts alternating current (AC) from a wall outlet into the stable direct current (DC) voltages required by all computer components. Sized in watts, a PSU's capacity must exceed the sum of all component power draws; undersizing causes crashes, while proper sizing ensures reliability and efficiency.

## you gotta know

- The PSU transforms *AC mains voltage* (110–240V depending on country) into regulated *DC outputs* at fixed voltages: typically +3.3V, +5V, +12V, and ground; component designs expect these voltages to remain stable within 5% tolerance.
- PSU capacity is measured in *watts*; a typical desktop system draws 300–750 watts under full load, and a PSU is usually oversized by 20–30% for efficiency and headroom (e.g., a 550W PSU for a 450W system).
- *Power delivery* (how well the PSU maintains stable voltage under load changes) is critical; poor PSUs exhibit *ripple* (voltage fluctuations) that can corrupt data or trigger hardware shutdowns.
- The PSU contains a *rectifier* (converting AC to pulsating DC) and a *switching regulator* (using high-frequency transistor switching to achieve efficient voltage conversion); these circuits generate heat.
- Cooling occurs via a *fan* (usually 80–140 mm); the fan speed is variable and adapts to load; high-end PSUs use larger, quieter fans with higher efficiency (80 Plus Gold/Platinum ratings).
- *Cable types* include the 24-pin *ATX* connector (delivering power to the motherboard), 8-pin *auxiliary* for the CPU, 6-pin or 8-pin connectors for GPUs, and 4-pin or SATA connectors for other drives.
- *Efficiency rating* (80 Plus Bronze, Silver, Gold, Platinum, Titanium) indicates what fraction of AC power is delivered to the system versus lost as heat; higher ratings mean lower power consumption from the wall and lower energy bills.
- Failure of a PSU can cascade: a failed capacitor or regulator can output incorrect voltage, damaging motherboards and CPUs; protection circuits (*overcurrent, overvoltage, thermal shutdown*) exist to prevent catastrophic failure, but prevention through proper sizing is better.

## connections

- [[motherboard]] — receives power via 24-pin ATX and 8-pin auxiliary connectors; power quality directly affects stability and data integrity.
- [[graphics-card]] — high-end GPUs draw 150–450 watts, requiring dedicated 6-pin, 8-pin, or dual 8-pin power connectors; a PSU must have sufficient 12V rail capacity.
- [[central-processing-unit]] — draws 65–250 watts depending on generation; the 8-pin auxiliary connector delivers clean, regulated power.
- [[cooling]] — PSU cooling fans must operate continuously under load; design and fan quality determine operating temperature and noise.
- [[hard-disk-drive]] and [[solid-state-drive]] — consume far less power (5–20 watts), but the PSU must deliver the correct voltage on the SATA power connector.

## see also

- [[motherboard]] · [[graphics-card]] · [[central-processing-unit]] · [[cooling]]

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

Lists: [[computer-components]] · Mark read: `INPUT[toggle:read]`
