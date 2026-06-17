---
type: term
category: science
defines: [RAM, random access memory, DRAM, SDRAM]
related: ["[[central-processing-unit]]", "[[motherboard]]", "[[cache-memory]]"]
requires: []
lists: ["[[computer-components]]"]
tour_order: 0
read: false
---

# RAM

## summary

**RAM** (random access memory) is the main working memory of a computer, providing fast, temporary storage for program instructions and data while the CPU executes. It is volatile—losing its contents when power is cut—and measured in gigabytes; today's computers typically have 8 to 64 GB depending on workload.

## you gotta know

- RAM is *volatile*—it loses all data when the computer shuts down, making it unsuitable for permanent storage; it is purely a high-speed staging area for the CPU.
- The CPU accesses RAM far more slowly than it accesses its own *cache*, so memory bandwidth (how much data per cycle) is a constant bottleneck in modern systems.
- *DRAM* (dynamic RAM) is the standard RAM technology; it stores charge in tiny capacitors that must be *refreshed* (recharged) thousands of times per second to retain data.
- RAM is installed in *DIMM* (dual in-line memory module) sticks that plug vertically into slots on the motherboard; the number of slots determines the maximum RAM capacity.
- *Memory speed* is measured in *megatransfers per second* (MT/s); common RAM today runs at 3200 MT/s or higher; faster RAM can marginally improve CPU performance.
- *Memory latency* — the time it takes for a requested byte to be delivered — is often more important than raw speed for real-world performance; lower latency (measured in nanoseconds) is better.
- *Dual-channel* or *quad-channel* memory architectures (common in consumer and server boards) allow multiple RAM sticks to be accessed in parallel, significantly boosting throughput.
- RAM capacity directly constrains how many programs can run simultaneously and how large datasets an application can handle; insufficient RAM forces the OS to use slow disk *swap space*.

## connections

- [[central-processing-unit]] — reads and writes data to RAM continuously; the CPU's performance is limited by memory latency and bandwidth.
- [[motherboard]] — RAM installs on the motherboard's DIMM slots; the motherboard's chipset controls all memory access.
- [[cache-memory]] — sits between the CPU and RAM, holding frequently-accessed data; cache misses force slower accesses to main RAM.
- [[solid-state-drive]] — when RAM is full, the OS spills data to disk via *swap*; SSD speed makes this less painful than with HDDs.

## see also

- [[central-processing-unit]] · [[motherboard]] · [[cache-memory]]

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
