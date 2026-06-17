---
type: term
category: science
defines: [SSD, solid state drive, flash storage, NVMe]
related: ["[[hard-disk-drive]]", "[[pci-express]]", "[[motherboard]]"]
requires: []
lists: ["[[computer-components]]"]
tour_order: 0
read: false
---

# Solid State Drive

## summary

A **solid state drive** (SSD) is a storage device that uses no moving parts, instead relying on flash memory (transistors arranged in a grid) to store and retrieve data electronically. SSDs are dramatically faster than hard drives, consume less power, and have become the standard boot drive for modern computers.

## you gotta know

- SSDs use *flash memory*—a type of non-volatile semiconductor memory in which transistors hold charge representing data; no moving parts means no seek time.
- *Random access time* for an SSD is measured in microseconds (millionths of a second), versus milliseconds for an HDD; this gap makes SSDs feel instantaneous to users.
- *Throughput* of a typical SATA SSD is 500+ MB/s; *NVMe* SSDs (connected via PCI Express rather than SATA) achieve 3,000–7,000 MB/s, effectively eliminating I/O as a bottleneck for most workloads.
- SSDs have a *finite lifespan* measured in *write cycles*; after approximately 1000–10000 rewrites per cell, the transistor degrades and can no longer hold charge reliably.
- *Wear leveling* — a firmware technique that distributes writes evenly across all cells — extends SSD lifespan to 5–10 years of normal use; modern consumer SSDs are unlikely to wear out through ordinary operation.
- SSDs consume 1–5 watts, compared to 5–15 watts for HDDs, making them essential for laptop battery life and low-power systems.
- Unlike HDDs, data recovery from SSDs is far more difficult because SSDs employ *TRIM* operations that physically erase unused blocks, and failed SSDs can produce no mechanical recovery clues.
- *Capacity* of SSDs ranges from 250 GB to 8 TB; the largest capacities are expensive and mostly used in servers and workstations, while 500 GB–2 TB is typical for consumer machines.

## connections

- [[hard-disk-drive]] — the mechanical predecessor; most modern systems use an SSD for the OS and frequently-accessed programs, plus HDDs for backup and archival.
- [[pci-express]] — NVMe SSDs connect directly to PCIe slots via M.2 form factor, bypassing the older SATA bus and achieving higher speeds.
- [[motherboard]] — modern motherboards include M.2 slots for NVMe SSDs; the chipset controls the connection and TRIM/power management.
- [[power-supply-unit]] — consumes relatively little power, so stable low-voltage delivery is less critical than for mechanical drives.

## see also

- [[hard-disk-drive]] · [[pci-express]] · [[motherboard]]

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
