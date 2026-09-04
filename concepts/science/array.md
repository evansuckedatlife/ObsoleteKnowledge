---
type: concept
category: science
defines: [Array, Arrays]
related: ["[[algorithms]]", "[[central-processing-unit]]", "[[motherboard]]", "[[resistor]]", "[[quantum-mechanics]]"]
requires: ["[[central-processing-unit]]", "[[algorithm]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Array

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

An **array** is a foundational linear data structure consisting of a contiguous collection of elements of identical data type, directly accessible via integer indices or keys. Originating in the earliest machine coding and high-level programming systems like *FORTRAN*, it maps mathematical matrices and vectors directly into sequential physical memory addresses. Because an **array** guarantees constant-time random access through simple memory offset calculations, it serves as the essential building block for higher-order abstract data structures, internal registers, and cache-efficient routines across computational science.

## you gotta know

- Provides constant *O(1)* time complexity for random element read and write access, calculated via base memory address plus the product of element size and index offset.
- Suffers from linear *O(n)* worst-case time complexity for arbitrary element insertions and deletions due to the necessary contiguous shifting of surrounding elements.
- Implements zero-based indexing in most modern languages such as *C*, *C++*, and *Python*, though older scientific languages like *FORTRAN* and mathematical systems like *MATLAB* standardize on one-based indexing.
- Features outstanding spatial locality of reference, allowing high-speed hardware prefetchers in modern architectures to populate cache lines and minimize memory latency.
- Dynamic variants, such as *std::vector* in *C++* or lists in *Python*, circumvent static memory sizing by automatically resizing the backing store via geometric reallocation and amortized *O(1)* append operations.
- Vulnerable to dangerous *buffer overflow* security exploits when boundary checks are omitted, enabling rogue stack writes that overwrite execution instruction pointers.
- Multi-dimensional representations are physically laid out in linear storage either in *row-major order* or *column-major order*, which profoundly affects cache traversal efficiency.

## connections

- [[algorithms]] — step-by-step computational procedures whose searching, sorting, and partitioning routines operate directly on indexed memory collections.
- [[central-processing-unit]] — hardware processors whose architectural registers and arithmetic units optimize contiguous memory indexing through hardware prefetching.
- [[motherboard]] — physical printed circuit boards routing high-speed memory bus traces between system RAM banks and processor sockets.
- [[resistor]] — foundational circuit elements that regulate voltage levels across semiconductor memory cells holding binary bits.
- [[quantum-mechanics]] — physical theory underlying solid-state semiconductor physics and floating-gate quantum tunneling in flash storage media.

## see also

- [[algorithms]] · [[central-processing-unit]] · [[motherboard]]

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
