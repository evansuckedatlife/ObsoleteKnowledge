---
type: term
category: science
defines: ["RAM", "Random-Access Memory", "random-access-memory"]
related: ["[[computer-memory]]", "[[cpu]]", "[[cache-memory]]", "[[virtual-memory]]", "[[volatile-memory]]"]
lists: []
read: false
---

# RAM

## summary

**RAM** (Random-Access Memory) is a type of volatile computer memory that allows fast read and write access to data in any order, regardless of location. It serves as the primary working memory for a computer's processor during active computation. Unlike permanent storage (hard drives, SSDs), RAM loses all data when power is cut, making it unsuitable for long-term storage but essential for real-time performance.

## you gotta know

- **Volatile memory:** RAM requires continuous power to retain data; switching off the computer erases all contents instantly.
- **Random access:** any memory location can be accessed in constant time, unlike sequential storage media (tape), making it orders of magnitude faster.
- **Working memory:** the processor loads programs and data into RAM during execution, reading and writing at nanosecond speeds.
- **Capacity hierarchy:** modern systems have gigabytes of RAM (GB), vastly more than CPU caches (megabytes) but less than permanent storage (terabytes).
- **DRAM vs. SRAM:** dynamic RAM requires periodic refresh to maintain charge; static RAM holds data without refresh but is more expensive and power-hungry, used only for caches.
- **Memory address space:** an N-bit address bus can reference 2^N bytes; 32-bit systems address 4 GB, 64-bit systems address exabytes.
- **Latency vs. bandwidth:** RAM latency (time to first access) is ~100 nanoseconds; bandwidth (data throughput) is tens of gigabytes per second, a trade-off with frequency.

## connections

- [[cpu]] — relies on RAM for all instruction and data storage during execution.
- [[cache-memory]] — sits between CPU and RAM, holding frequently-accessed data to reduce latency.
- [[virtual-memory]] — extends effective memory by swapping RAM contents to disk when capacity is exceeded.
- [[motherboard]] — physically hosts RAM chips; bus bandwidth limits RAM speed.
- [[volatile-memory]] — RAM is the canonical example of volatile vs. non-volatile storage trade-off.
- [[memory-hierarchy]] — RAM occupies the middle tier: slower than cache, faster than storage.

## see also

- [[cache-memory]] · [[cpu]] · [[volatile-memory]] · [[virtual-memory]]

<!-- footer -->

---

Lists: Mark read: `INPUT[toggle:read]`
