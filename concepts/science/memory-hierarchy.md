---
type: concept
category: science
defines: [Memory hierarchy]
related: ["[[cache-memory]]", "[[ram]]", "[[central-processing-unit]]", "[[motherboard]]", "[[latency]]", "[[storage-device]]"]
requires: ["[[central-processing-unit]]", "[[ram]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Memory Hierarchy

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **memory hierarchy** is the tiered organization of computer memory from fast/small (CPU registers) to slow/large (disk storage), a fundamental principle of computer architecture. Each tier serves a distinct role: fast memories hold active data for immediate computation, while slower layers provide bulk storage at lower cost. This hierarchy bridges the vast performance gap between modern processors and disk drives, enabling practical computing at scale.

## you gotta know

- The memory hierarchy typically consists of: CPU registers (fastest, smallest), L1/L2/L3 cache (progressively slower and larger), RAM (main memory), and disk storage (slowest, largest).
- Access latency increases dramatically across tiers: register access is ~1 nanosecond, L1 cache is ~4 ns, main memory is ~100 ns, and disk access is ~10 milliseconds.
- Capacity increases inversely with speed: registers hold kilobytes, caches hold megabytes to tens of megabytes, RAM holds gigabytes to hundreds of gigabytes, and disks hold terabytes.
- Cache operates on the principle of *locality*: programs repeatedly access nearby memory locations (spatial locality) and recently used data (temporal locality).
- Cache misses (when requested data is not in fast memory) force slower access times, creating a performance penalty that grows with each level accessed.
- Virtual memory uses disk storage to extend apparent RAM capacity, swapping data between disk and main memory as needed, trading performance for greater address space.
- The design of memory hierarchies shapes algorithms and programming practices: cache-efficient sorting and matrix multiplication exploit data locality to minimize stalls.
- L3 cache is shared among multiple CPU cores, while L1 and L2 caches are typically private to each core, enabling fine-grained control of data coherence.
- Write policies (write-through vs. write-back) in cache layers determine how changes propagate down the hierarchy, affecting both performance and data consistency.
- Modern processors optimize for sequential access patterns by prefetching data into cache before it is requested, anticipating program behavior to reduce latency.

## connections

- [[cache-memory]] — the fast intermediate storage between CPU and main memory.
- [[ram]] — random-access memory occupying the middle tier of the hierarchy.
- [[central-processing-unit]] — the processor whose performance depends critically on memory latency.
- [[motherboard]] — the physical substrate integrating multiple hierarchy tiers.
- [[latency]] — the delay in accessing data, varying by orders of magnitude across tiers.
- [[storage-device]] — the persistent disk storage at the base of the hierarchy.

## see also

[[cache-memory]] · [[ram]] · [[central-processing-unit]] · [[latency]] · [[storage-device]]

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
