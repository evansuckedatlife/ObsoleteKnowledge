---
type: concept
category: science
defines: [Storage Device, Secondary Storage, Mass Storage]
related: ["[[cache-memory]]", "[[memory-hierarchy]]", "[[central-processing-unit]]", "[[ram]]", "[[motherboard]]", "[[latency]]", "[[algorithm]]"]
requires: ["[[central-processing-unit]]", "[[motherboard]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Storage Device

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **storage device**, commonly designated as **secondary storage** or **mass storage**, is a hardware component engineered to retain digital information permanently without requiring a continuous supply of electrical power. Operating at the foundational base of the standard [[memory-hierarchy]], persistent media provide vast data capacity and low cost per gigabyte, accepting the trade-off of considerably greater operational [[latency]] than volatile tiers such as [[ram]]. Coordinated with the [[central-processing-unit]] via dedicated high-speed buses and controller chipsets on the [[motherboard]], these mechanisms hold system operating software, persistent user data, and dormant libraries across machine reboots and power outages. Modern systems rely on secondary media not only for archival durability, but also as an indispensable extension of primary memory through virtual memory paging mechanisms.

## you gotta know

- Distinguishes itself from volatile primary memory by providing non-volatile retention, preserving structured data intact through complete power interruption and operating at the bottom of the system [[memory-hierarchy]].
- Emerged in commercial computing with the 1956 *IBM 350* disk storage system of the *RAMAC 305*, which pioneered magnetic disk recording using fifty spinning metal platters and movable read-write heads.
- Relies traditionally on hard disk drives containing spinning ferromagnetic platters divided into concentric tracks and sectors, where magnetic orientation determines stored binary states through electromagnetic induction.
- Evolved rapidly toward solid-state drives that employ non-volatile *NAND* flash memory, replacing mechanical spinning platters to eliminate rotational delay and seek times while substantially improving random access speeds.
- Exhibits access latencies orders of magnitude slower than volatile system memory, with mechanical hard drives requiring milliseconds to reposition physical actuator arms while solid-state flash drives complete reads within microseconds.
- Interfaces with the host architecture through established protocols and interconnects like *SATA*, *SAS*, and *NVMe*, routing data through host controllers on the [[motherboard]] directly to the [[central-processing-unit]].
- Integrates tightly with operating system kernels by acting as block devices that support hierarchical file systems, partition tables, and disk paging for virtual memory when physical [[ram]] becomes constrained.
- Utilizes specialized embedded microcontroller firmware to execute sophisticated background algorithms, including wear leveling, bad-block retirement, garbage collection, and hardware-level error correction to prolong media longevity.

## connections

- [[central-processing-unit]] — the primary computational processor that issues read and write instructions to fetch instructions and datasets from persistent disk.
- [[motherboard]] — the main circuit platform hosting chipset controllers, expansion slots, and high-speed data buses that link drives to the system.
- [[ram]] — fast, volatile primary workspace that holds active programs and pages transferred temporarily from persistent storage during system execution.
- [[cache-memory]] — tiny, ultra-fast semiconductor memory on the processor core representing the opposite extreme of the hierarchy from bulk storage.
- [[latency]] — the critical performance delay governed by physics that separates nanosecond chip operations from microsecond or millisecond drive transfers.
- [[algorithm]] — programmed mathematical rules executing inside storage drive controllers for flash wear leveling, sector mapping, and transparent data compression.
- [[electron]] — quantum charge carrier manipulated and trapped inside isolated floating gates or charge-trap transistors to encode persistent binary state.

## see also

- [[cache-memory]] · [[ram]] · [[central-processing-unit]] · [[motherboard]] · [[latency]]

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

Lists: [[science-hubs]] · Mark read: `INPUT[toggle:read]`
