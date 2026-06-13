---
type: term
category: science
defines: [PCIe, PCI Express, PCI]
related: ["[[motherboard]]", "[[graphics-card]]", "[[solid-state-drive]]"]
lists: ["[[computer-components]]"]
read: false
---

# PCI Express

## summary

**PCI Express** (PCIe) is a high-speed serial bus standard that connects expansion cards and peripherals to the motherboard. It has largely replaced the older parallel PCI bus, offering dramatically higher bandwidth and lower latency, and is the standard for graphics cards, NVMe SSDs, and advanced I/O adapters.

## you gotta know

- PCIe is a *serial* bus (data flows in one direction at a time, encoded serially) rather than a *parallel* bus like legacy PCI; serial design allows higher clock rates and longer cable distances with lower latency.
- *Lane count* (1x, 4x, 8x, 16x) determines bandwidth; a 16-lane connection (x16) at PCIe 4.0 speed offers 32 GB/s, sufficient for graphics cards and fast storage; lower lane counts (x1, x4) serve slower devices.
- PCIe *generations* (3.0, 4.0, 5.0, 6.0) increase speed: Gen 3 at 16 GB/s per 16-lane slot, Gen 4 at 32 GB/s, Gen 5 at 64 GB/s; newer generations are backward-compatible with older cards at slower speeds.
- *Topology* on a motherboard is hierarchical: a *root complex* (integrated into the chipset) manages a tree of PCIe switches and devices; each slot is assigned a unique address, allowing the OS to discover and communicate with each device.
- *Hot-swapping* is supported in theory (you can remove and insert cards without reboot), but driver support varies; server and enterprise setups rely on this; consumer boards are less tested.
- *Power delivery* over PCIe is limited to 75 watts per slot (for x16 slots); high-power devices (GPUs) use auxiliary power connectors; low-power devices (SSDs, network cards) draw only from the slot.
- The PCIe *controller* on the motherboard's chipset implements the protocol layer and translates CPU requests into PCIe transactions; its quality and driver support affect device stability.
- *Bifurcation* (the ability to split one x16 slot into multiple x4 slots) is a motherboard feature allowing installation of multiple M.2 SSDs or other x4 devices in a single slot; not all boards support it.

## connections

- [[motherboard]] — the PCIe bus is built into the chipset; the motherboard layout determines which devices can share lanes and how lanes are assigned.
- [[graphics-card]] — uses x16 slot; a PCIe bottleneck (Gen 3 x4 instead of x16) can reduce GPU performance, though modern cards rarely saturate even Gen 3 x16.
- [[solid-state-drive]] — NVMe SSDs connect via M.2 slots backed by PCIe lanes; PCIe Gen 4 and 5 are needed to fully utilize modern NVMe speeds.

## see also

- [[motherboard]] · [[graphics-card]] · [[solid-state-drive]]

<!-- footer -->

---

Lists: [[computer-components]] · Mark read: `INPUT[toggle:read]`
