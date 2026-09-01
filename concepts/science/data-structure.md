---
type: concept
category: science
defines: ["Data structure"]
related: ["[[algorithm]]", "[[array]]", "[[linked-list]]", "[[tree-data-structure]]", "[[graph-data-structure]]"]
requires: ["[[algorithm]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Data Structure

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Data structures** are organized formats for storing and accessing data in memory, designed to enable efficient operations like searching, insertion, and deletion. From simple arrays to complex graphs, they form the foundation of computer science and are central to designing fast [[algorithms]]. The choice of data structure directly determines how quickly a program can solve a problem.

## you gotta know

- Arrays store elements in contiguous memory; fast random access (O(1)) but expensive insertion/deletion.
- [[Linked lists]] use pointers to connect nodes; flexible insertion/deletion (O(1) if position is known) but slow search (O(n)).
- Stacks and queues are abstract structures imposing LIFO or FIFO ordering on data, often implemented atop arrays or lists.
- [[Trees]] organize data hierarchically; binary search trees enable O(log n) search if balanced.
- [[Graphs]] generalize trees by allowing arbitrary connections between nodes; essential for modeling networks and relationships.
- Hash tables map keys to values with nearly O(1) average-case lookup via hash functions that distribute keys across buckets.

## connections

- [[algorithm]] — algorithms operate on data structures, and structure choice affects algorithm performance.
- [[tree-data-structure]] — a hierarchical data structure common in databases and search.
- [[graph-data-structure]] — a general structure for representing relationships.
- [[array]] — the simplest and most fundamental data structure.
- [[linked-list]] — an alternative to arrays with different performance tradeoffs.
- [[hash-table]] — enables fast key-value lookups.

## see also

[[algorithm]] · [[tree-data-structure]] · [[graph-data-structure]] · [[array]]

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
