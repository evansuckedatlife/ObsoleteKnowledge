---
type: term
category: science
defines: [Cache Memory, CPU cache]
related: ["[[central-processing-unit]]", "[[ram]]", "[[motherboard]]", "[[memory-hierarchy]]", "[[latency]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Cache Memory

## summary

**Cache memory** is a small, extremely fast data storage system positioned between the CPU and main RAM that holds frequently accessed data and instructions, reducing the latency cost of fetching from slower main memory. Modern CPUs contain multiple cache levels (L1, L2, L3) in a hierarchical arrangement where smaller caches are faster but hold less data; cache design—through algorithms determining which data to keep and when to evict it—is central to CPU performance and is one of computer architecture's most critical optimization challenges.

## you gotta know

- Cache memory operates on the principle of *spatial* and *temporal locality*: programs tend to re-access recently used data (temporal) and data near recently accessed data (spatial); cache exploits both by storing nearby blocks.
- *L1 cache* (primary cache) is tiny (~32 KB per core) and integrated directly on the CPU die; it operates at CPU speed with nearly zero latency; L2 cache is larger (~256 KB) and slightly slower; L3 (last-level cache) is shared among cores (~8–20 MB) and slower still.
- The *cache miss rate* is critical: accessing L1 costs ~4 cycles, L2 costs ~10 cycles, L3 costs ~40 cycles, and RAM access costs ~200+ cycles; reducing miss rates by even a few percent significantly improves performance.
- *Cache coherence* is complex in multi-core systems: if one core modifies data in its cache, other cores must be notified so they don't use stale copies; coherence protocols use messages between caches to maintain consistency.
- *Cache eviction policies* (replacement algorithms) determine which data to remove when cache is full; common strategies include LRU (least-recently-used), LFU (least-frequently-used), and random replacement, with different trade-offs.
- *Cache line* is the basic unit: data is loaded/stored in fixed-size blocks (typically 64 bytes); loading a single byte may pull 64 bytes into cache, which is beneficial if nearby bytes are used (spatial locality) but wasteful if they are not.
- *Instruction cache* and *data cache* are often separated at L1 for faster parallel access (Harvard architecture), but unified caches at higher levels reduce complexity and improve flexibility.

## connections

- [[central-processing-unit]] — cache is an integral part of modern CPUs; cache design directly impacts CPU performance.
- [[ram]] — cache bridges the enormous speed gap between CPU and main RAM.
- [[motherboard]] — some cache (L3) resides on the motherboard; memory controllers coordinate cache-RAM interaction.
- [[memory-hierarchy]] — cache is a level in the memory hierarchy from fast/small (cache) to slow/large (disk).
- [[latency]] — cache exists to minimize memory-access latency, the time cost of retrieving data.

## see also

- [[central-processing-unit]] · [[ram]] · [[motherboard]] · [[memory-hierarchy]]

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

Lists:  · Mark read: `INPUT[toggle:read]`
