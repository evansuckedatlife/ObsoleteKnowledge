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

The **motherboard** is the central circuit board that physically and electrically integrates all components of a computer. It provides sockets and slots for the CPU, memory, storage, and expansion cards, carries the buses that route data and control signals, and distributes power. The motherboard is the computer's nervous system and skeleton combined: it is both the platform on which all computation occurs and the interface between specialized subsystems (GPU, storage, network, audio).

## you gotta know

### Architecture and Core Functions
- The motherboard is fundamentally a *routing and power-distribution layer*: every major component plugs into it (CPU socket, RAM slots, expansion slots) or connects via cable; it is the physical backbone of the machine.
- *Chipset*: a collection of integrated circuits (northbridge, southbridge, or a unified chipset in modern designs) that orchestrates data flow between the CPU, RAM, storage devices, and I/O controllers; the chipset is often the primary determinant of a motherboard's generation, performance class, and features.
- *Multiple buses* route data: the *front-side bus* (FSB, now largely obsolete) connected CPU to RAM and graphics; the *PCI Express bus* connects expansion cards; the *DMI* (Direct Media Interface) or *HyperTransport* connects chipset components.

### Power and Voltage Regulation
- *Power delivery network (PDN)*: voltage regulators on the motherboard convert the PSU's raw outputs (12V, 5V, 3.3V) into the specific, stable voltages required by each component—the CPU may need 1.2V, RAM 1.35V, I/O circuits 3.3V, etc.
- *Capacitors and inductors* filter the power supply, smoothing transients and maintaining voltage stability under variable load.
- *Connectors* (24-pin ATX main, 8-pin auxiliary CPU power, SATA power) deliver power to the motherboard, which then distributes it to all subsystems.

### Sockets, Slots, and Compatibility
- *CPU socket* (e.g., Intel LGA1700, AMD AM5): determines which processor generation can be installed; socket compatibility is a critical hardware constraint and defines a motherboard's lifespan.
- *RAM slots* (DIMM sockets for modern systems): accommodate memory modules; the motherboard provides timing, voltage control, and ECC support (if implemented).
- *Expansion slots* (PCI Express x16, x8, x4, x1; legacy PCI): allow installation of graphics cards, network adapters, sound cards, and other peripherals; PCIe lane allocation and slot configuration vary by motherboard model.
- *Storage connectors* (SATA, NVMe M.2): connect SSDs and hard drives; modern motherboards typically support 2–6 SATA ports and 2–4 NVMe slots.

### Firmware and Control
- *BIOS/UEFI firmware*: stored in a non-volatile chip (ROM or flash) on the motherboard; it initializes hardware during boot (power-on self-test, POST), loads the operating system kernel, and provides configuration and diagnostic interfaces.
- *Battery-backed real-time clock (RTC) and CMOS RAM*: maintains system time and BIOS settings when powered off; powered by a coin-cell battery.
- *Overclocking controls*: modern BIOS allows modification of CPU frequency, voltage, and timing parameters (with stability and thermal risks).

### Form Factors
- *ATX* (standard): the most common desktop form factor; approximately 305 × 244 mm; supports 6–8 DIMM slots, 6–8 SATA, multiple PCIe slots.
- *Micro-ATX* (smaller): ~244 × 244 mm; fewer expansion slots (typically 4 DIMM, 4 SATA, 2–3 PCIe).
- *Mini-ITX* (compact): ~170 × 170 mm; minimal slots and ports; used in small-form-factor PCs.
- *E-ATX* (extended): larger than standard ATX; supports 8+ DIMM slots; used in high-end workstations and servers.

## context

The motherboard is the integrating platform that defines what a computer is: it enforces compatibility standards (socket, chipset, bus protocols), distributes power fairly and stably, and sequences the intricate handshake between specialized chips. From an engineering perspective, the motherboard faces constant trade-offs: cost vs. features, power delivery capacity vs. size, number of expansion slots vs. form factor. Historically, motherboard evolution has tracked Moore's Law and the rise of integrated chipsets; the shift from discrete northbridge/southbridge to unified chipsets reflects the trend toward integration on the CPU die. Understanding motherboards is essential for system assembly, troubleshooting (power delivery failures, bent pins, slot incompatibility), and building specialized systems (gaming rigs with high-power delivery, workstations with multiple GPUs, servers with IPMI management). In quiz bowl, motherboards appear in contexts of PC architecture, computer components, and technical specifications.

## connections

- [[central-processing-unit]] — plugs into the motherboard's socket; depends entirely on power delivery and signal routing.
- [[ram]] — inserts into DIMM slots on the motherboard; the motherboard provides voltage regulation and access control.
- [[pci-express]] — the standard expansion slot technology; implemented as lanes on the chipset and routed to expansion slots.
- [[bios]] — firmware stored in a chip on the motherboard; controls hardware initialization and low-level operation.
- [[power-supply-unit]] — delivers power via multi-pin connectors to the motherboard's voltage regulators.
- [[chipset]] — the integrated-circuit complex that routes data between CPU, RAM, storage, and I/O.
- [[nvidia-geforce]] — a discrete GPU that plugs into a PCIe slot on the motherboard.
- [[computer-architecture]] — the motherboard is the physical embodiment of the system bus and memory hierarchy.

## see also

- [[central-processing-unit]] · [[ram]] · [[pci-express]] · [[bios]]

<!-- footer -->

---

Lists: [[computer-components]] · Mark read: `INPUT[toggle:read]`
