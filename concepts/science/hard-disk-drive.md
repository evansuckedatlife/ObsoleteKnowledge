---
type: term
category: science
defines: [HDD, hard disk drive, hard drive]
related: ["[[solid-state-drive]]", "[[motherboard]]", "[[mechanical-storage]]"]
requires: []
lists: ["[[computer-components]]"]
tour_order: 0
read: false
---

# Hard Disk Drive

## summary

A **hard disk drive** (HDD) is a rotating-platter storage device that uses electromagnetic read/write heads to access data on spinning magnetic disks. Despite being slower than SSDs, HDDs remain cost-effective for bulk storage, offering capacities of 1 to 20 terabytes at low per-gigabyte cost.

## you gotta know

- The HDD stores data on *rotating platters* coated with magnetic material; a *read/write head* hovers above the surface and detects or magnetizes microscopic regions to encode 0s and 1s.
- *Seek time* — the time for the head to move to the correct track on the platter — is the primary bottleneck; mechanical motion makes HDDs 10–100 times slower than SSDs for random access.
- HDDs are measured by *RPM* (revolutions per minute): 5400 RPM drives are energy-efficient and common in external storage, while 7200 RPM is standard for desktop/NAS drives, and 15000 RPM for server environments.
- The data transfer *throughput* of an HDD is typically 100–200 MB/s (much slower than SSDs' 500+ MB/s), but can handle sequential reads of large files reasonably well.
- *Reliability* is measured in *MTBF* (mean time between failures), typically 30,000–50,000 hours; HDDs are mechanically fragile and prone to failure if dropped, jarred, or run at high temperatures.
- An HDD consumes more *power* (5–15 watts) than an SSD, making it unsuitable for battery-powered devices; the spinning motor is the chief culprit.
- Data on an HDD can be *recovered* after mechanical failure more easily than with SSDs, because the read/write process is reversible; professional data recovery services exist specifically for HDDs.
- HDDs remain *non-volatile*—they retain data when powered off, making them the traditional choice for long-term storage, even though their price per gigabyte is higher than RAM.

## connections

- [[solid-state-drive]] — the modern alternative; SSDs are faster but more expensive per gigabyte, so both technologies coexist in hybrid setups.
- [[motherboard]] — connects via *SATA* (Serial ATA) or legacy *IDE* cables; the motherboard's SATA controller manages the connection.
- [[mechanical-storage]] — represents the broader category of moving-part storage; conceptually distinct from electronic flash memory.
- [[power-supply-unit]] — supplies continuous power to the motor and electronics; power loss during a write can corrupt the filesystem.

## see also

- [[solid-state-drive]] · [[motherboard]]

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
