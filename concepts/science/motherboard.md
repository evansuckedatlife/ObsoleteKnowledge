---
type: term
category: science
defines: [motherboard, mainboard]
related: ["[[central-processing-unit]]", "[[ram]]", "[[pci-express]]", "[[bios]]"]
lists: ["[[computer-components]]"]
read: false
---

# Motherboard

## summary

The **motherboard** is the central circuit board that physically and electrically connects all components of a computer. It provides sockets and slots for the CPU, memory, storage devices, and expansion cards, along with the buses and control logic that orchestrate communication between them.

## you gotta know

- The motherboard is fundamentally a *routing and power-distribution* layer; every component either plugs into it or connects via a cable, making it the physical backbone of the machine.
- It houses the *chipset* — a collection of integrated circuits that manages data flow between the CPU, RAM, storage, and I/O devices; the chipset is often what defines a motherboard's generation and capabilities.
- The CPU sits in a *socket* (e.g., LGA1700 on Intel, AM5 on AMD); the motherboard design determines which processors can be installed, making socket compatibility a critical constraint.
- *Power delivery* — a network of voltage regulators on the motherboard — converts the PSU's raw 12V/5V/3.3V outputs to the specific, stable voltages required by each component.
- The motherboard contains the *BIOS/UEFI* firmware, stored in non-volatile memory, which initializes hardware at boot and provides low-level control and diagnostics.
- *Expansion slots* (PCI Express, legacy PCI) allow installation of graphics cards, network adapters, sound cards, and other peripherals; the motherboard determines which slots and how many lanes are available.
- The *northbridge and southbridge* (or unified chipset in modern designs) route data between the CPU, RAM, and slower I/O devices; this architecture has historically been the boundary between high-speed and low-speed buses.
- Form factors such as *ATX*, *micro-ATX*, and *mini-ITX* define the physical size and slot layout, constraining which cases and cooling solutions will fit.

## connections

- [[central-processing-unit]] — the CPU plugs into the motherboard's socket and depends entirely on its power delivery and signal integrity.
- [[ram]] — RAM modules insert into DIMM slots on the motherboard; the motherboard provides the voltage and control signals.
- [[pci-express]] — the standard expansion slot technology, defined by a PCI Express specification implemented on the motherboard.
- [[bios]] — lives in a firmware chip on the motherboard and controls the initialization and low-level operation of the entire system.
- [[power-supply-unit]] — connected via multi-pin connectors (24-pin ATX, 8-pin auxiliary) that deliver power to the motherboard's voltage regulators.
- [[cooling]] — the motherboard's design and layout determine airflow patterns and heat sink compatibility.

## see also

- [[central-processing-unit]] · [[ram]] · [[pci-express]] · [[bios]]

<!-- footer -->

---

Lists: [[computer-components]] · Mark read: `INPUT[toggle:read]`
