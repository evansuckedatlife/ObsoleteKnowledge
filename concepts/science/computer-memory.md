---
type: concept
category: science
defines: [computer memory, primary storage, main memory]
related: ["[[central-processing-unit]]", "[[motherboard]]", "[[computer-architecture]]", "[[algorithm]]", "[[cold-war]]", "[[united-states]]", "[[resistor]]"]
requires: ["[[central-processing-unit]]", "[[motherboard]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Computer memory

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Computer memory**, encompassing **primary storage** and **main memory**, consists of semiconductor components and storage technologies that retain digital data and execution instructions for rapid access by an electronic processor. Evolving from early acoustic delay lines and magnetic cores during the mid-twentieth century, modern memory forms the operational workspace of digital systems. Organized hierarchically by latency, capacity, and cost, memory bridges high-speed computational logic with persistent secondary storage.

## you gotta know

- Divided fundamentally into *volatile memory*, which loses stored state upon power interruption, and *non-volatile memory*, which preserves binary contents indefinitely.
- Dynamic Random-Access Memory, or *DRAM*, stores individual bits in integrated circuit cells consisting of a single transistor and capacitor that requires periodic electrical refreshing.
- Static Random-Access Memory, or *SRAM*, uses multi-transistor bistable latch circuits to provide ultra-fast access times, commonly serving as on-die cache memory.
- Read-Only Memory, or *ROM*, retains immutable firmware such as the *BIOS* or *UEFI* required to initialize computer hardware during the bootstrap sequence.
- Organized in the memory hierarchy where fast, expensive registers and caches feed larger, slower main memory and storage drives to minimize the processor memory wall.
- Managed by an operating system through *virtual memory*, which maps abstract virtual address spaces onto physical pages using page tables and translation lookaside buffers.
- Early digital computers during the *Cold War* utilized magnetic-core memory planes hand-woven with ferrite rings, leading to the lasting terminology of core dumps.

## connections

- [[central-processing-unit]] — computational engine that fetches instructions and reads or writes data directly from main memory.
- [[motherboard]] — primary circuit board providing memory slots and high-speed traces connecting memory channels to the processor.
- [[computer-architecture]] — systemic framework defining memory addressing schemes, bus topologies, and memory hierarchy design.
- [[algorithm]] — procedural program logic whose performance, locality of reference, and complexity depend directly on memory access patterns.
- [[cold-war]] — geopolitical era during which defense computing and aerospace programs funded pioneering magnetic memory developments in the *United States*.
- [[resistor]] — fundamental electronic circuit element utilized in termination networks and memory cell biasing.

## see also

- [[computer-architecture]] · [[central-processing-unit]] · [[motherboard]]

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
