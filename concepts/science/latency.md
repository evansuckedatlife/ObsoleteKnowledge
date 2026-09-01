---
type: term
category: science
defines: [Latency, memory latency, access latency]
related: ["[[cache-memory]]", "[[memory-hierarchy]]", "[[central-processing-unit]]", "[[ram]]", "[[storage-device]]"]
requires: ["[[memory-hierarchy]]", "[[central-processing-unit]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Latency

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Latency** is the time delay between a request for data and its delivery in a computing system, measured in nanoseconds to milliseconds depending on the storage medium. It is the inverse of the speed at which stored information can be accessed by the [[central-processing-unit]]. Latency is one of the two critical parameters defining computer performance (the other being bandwidth), and managing latency through [[memory-hierarchy|hierarchical memory]] design—fast small caches backed by slower larger storage—is central to modern processor architecture.

## you gotta know

- Measured in *round-trip time* (RTT): the elapsed time from when the CPU initiates a memory request until data returns and is usable by the processor.
- *Cache latency* (L1): ~4 nanoseconds; *RAM latency* (DRAM): ~100 nanoseconds; *SSD latency*: ~10 microseconds; *hard disk latency*: ~5–10 milliseconds.
- The disparity—seven orders of magnitude from cache to disk—motivates the [[memory-hierarchy]] design: L1 cache holds hot data; L2 and L3 caches provide intermediate speed/size tradeoffs; RAM backs cache; SSDs back RAM.
- [[central-processing-unit|CPU]] performance is often latency-bound rather than throughput-bound: a single cache miss can stall the entire processor for hundreds of cycles while waiting for main memory.
- *Cache hit rate* is the fraction of memory accesses satisfied by the [[cache-memory|cache]]; higher hit rates reduce average latency exponentially.
- Latency hiding techniques include prefetching (speculating which data will be needed next), out-of-order execution (working on independent instructions while waiting), and multithreading (switching to other threads during memory waits).
- In networked systems, latency includes transmission time plus propagation delay; even light-speed limits (30 cm/nanosecond) impose fundamental minimums for intercontinental communication.
- Latency is irreducible for random-access operations; sequential access can overlap with computation and approaches zero effective latency through pipelining and buffering.
- Understanding and optimizing latency is critical for real-time systems, databases, and interactive applications where responsiveness directly impacts user experience and application correctness.

## connections

- [[memory-hierarchy]] — the abstraction that masks latency differences across storage tiers.
- [[cache-memory]] — the fastest tier, designed to minimize latency for frequently accessed data.
- [[central-processing-unit]] — the component affected by latency when memory requests block its execution.
- [[ram]] — the main working memory with moderate latency, intermediate between cache and disk.
- [[storage-device]] — the persistent storage tier with the highest latency but largest capacity.

## see also

[[memory-hierarchy]] · [[cache-memory]] · [[central-processing-unit]] · [[ram]]

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
