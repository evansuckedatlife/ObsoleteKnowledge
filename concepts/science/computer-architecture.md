---
type: concept
category: science
defines: [computer architecture, computer systems architecture]
related: ["[[central-processing-unit]]", "[[computer-memory]]", "[[motherboard]]", "[[algorithm]]", "[[cold-war]]", "[[united-states]]", "[[conduction]]"]
requires: ["[[central-processing-unit]]", "[[motherboard]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Computer architecture

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Computer architecture**, or **computer systems architecture**, is the theoretical and engineering discipline that defines the structure, organization, and behavioral specification of electronic digital computing systems. Encompassing instruction set architectures, microarchitecture, and hardware bus topologies, it dictates how logic units interface with memory and peripheral subsystems. Established formally through foundational models in the mid-twentieth century, the discipline governs modern processor performance, power efficiency, and hardware scaling.

## you gotta know

- The classic *von Neumann architecture* conceptualizes a shared bus and unified memory storage for both operational instructions and program data.
- The contrasting *Harvard architecture* physically isolates instruction storage and signal pathways from data storage, mitigating the von Neumann memory access bottleneck.
- Instruction Set Architecture, or *ISA*, defines the programmer-visible abstract interface, distinguishing *RISC* reduced instruction approaches from *CISC* complex instruction sets.
- Microarchitecture implements the ISA in hardware using techniques such as superscalar execution, out-of-order execution, and branch prediction.
- Instruction pipelining splits computational execution into sequential stages, which can suffer performance stalls caused by structural, data, or control hazards.
- *Amdahl's law* calculates the theoretical latency speedup limit of an overall task when only a portion of the system is parallelized or upgraded.
- *Flynn's taxonomy* classifies processing organizations into *SISD*, *SIMD*, *MISD*, and *MIMD* streams based on concurrent instruction and data flows.

## connections

- [[central-processing-unit]] — the central processing core executing microarchitectural instructions defined by the architecture.
- [[computer-memory]] — primary storage subsystem arranged in hierarchical tiers as specified by the system architecture.
- [[motherboard]] — physical printed circuit board embodying the architectural buses, memory channels, and chipset interconnects.
- [[algorithm]] — software routines optimized to maximize cache locality and instruction-level parallelism provided by the hardware.
- [[conduction]] — fundamental physical heat transfer mechanism that dictates the cooling and power dissipation ceilings of high-density microarchitectures.
- [[cold-war]] — historical period that catalyzed large-scale architectural innovations for ballistic calculations and military supercomputing in the *United States*.

## see also

- [[central-processing-unit]] · [[computer-memory]] · [[motherboard]]

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
