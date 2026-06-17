---
type: term
category: science
defines: ["Power Supply", "PSU", "power-supply unit"]
related: ["[[electricity]]", "[[voltage]]", "[[current-electricity]]", "[[transformer]]", "[[rectifier]]", "[[motherboard]]", "[[cooling]]"]
lists: []
read: false
---

# Power Supply

## summary

A **power supply** (or PSU—power supply unit) converts incoming alternating current (AC) from the wall outlet into regulated direct current (DC) at multiple voltage levels required by a computer's components. It distributes power safely to the CPU, RAM, storage devices, and peripheral components while protecting them from voltage spikes and brownouts. Power supply capacity, measured in watts, must exceed the system's peak demand to ensure stable operation.

## you gotta know

- **AC to DC conversion:** the supply contains a transformer (steps down voltage) and a rectifier (converts AC to DC), followed by filtering and regulation stages.
- **Multiple voltage rails:** a modern PSU outputs ±3.3V, ±5V, ±12V, and ±24V to different components; the 12V rail typically supplies the CPU and GPU.
- **Efficiency rating:** standard 80 Plus certifications (Bronze, Silver, Gold, Platinum, Titanium) indicate what fraction of input power is delivered to components vs. lost as heat; Gold+ supplies are ~90% efficient.
- **Wattage specification:** a 500W supply means continuous rated output at full load; peak surge capacity is higher. Undersized supplies throttle performance; oversized supplies operate below peak efficiency.
- **Modular cabling:** modern supplies have disconnectable cables so users route only what they need, improving airflow and cable management.
- **Protection circuits:** overvoltage, overcurrent, and thermal shutdown safeguards prevent damage to expensive components from electrical faults.
- **Standby power:** supplies maintain a small 5V rail even when the computer is off, powering standby features (wake-on-LAN, USB charging).

## connections

- [[electricity]] — power supply is the interface between grid AC and digital DC logic.
- [[voltage]] — regulates and distributes multiple voltage levels to different subsystems.
- [[transformer]] — the core step-down component for AC-to-DC conversion.
- [[cooling]] — power supplies generate heat; adequate airflow prevents thermal failure and improves efficiency.
- [[motherboard]] — receives and distributes power to all mounted components.
- [[cpu]] — consumes the most power in a system; the 8-pin/24-pin connectors deliver peak current.
- [[gpu]] — competing with CPU for power budget; high-end GPUs demand dedicated 6-pin or 8-pin rails.

## see also

- [[voltage]] · [[electricity]] · [[cooling]] · [[cpu]]

<!-- footer -->

---

Lists: Mark read: `INPUT[toggle:read]`
