---
type: concept
category: mathematics
defines: ["Sorting Algorithms", "Sorting Algorithm", "Sorts"]
related: ["[[p-vs-np-problem]]", "[[turing-machine]]"]
requires: []
lists:
  - "[[computation-types]]"
tour_order: 0
read: false
---

# Sorting Algorithms

## summary

Sorting algorithms are systematic methods used to rearrange a list or array of elements into a specified order, most commonly numerical or alphabetical. They are among the most fundamental and heavily studied topics in computer science, serving as critical components in search algorithms, database engines, and optimization routines. Evaluating sorting methods involves analyzing trade-offs in time complexity, memory usage, and stability.

## you gotta know

- Any comparison-based sorting algorithm has a mathematical lower bound of $O(n \log n)$ operations in the worst and average cases, a fact proven using decision tree models.
- Algorithms that achieve the optimal $O(n \log n)$ worst-case bound include *mergesort* and *heapsort*; *quicksort* achieves $O(n \log n)$ on average but can degrade to $O(n^2)$ in its worst case.
- Non-comparison sorting methods like *counting sort*, *radix sort*, and *bucket sort* can achieve $O(n)$ linear time by exploiting prior knowledge about the range or structure of the inputs.
- A sort is defined as "stable" if it maintains the relative order of duplicate elements; for example, *mergesort* and *insertion sort* are stable, while *heapsort* and standard *quicksort* are unstable.
- Basic comparison sorts like *bubble sort*, *selection sort*, and *insertion sort* run in quadratic $O(n^2)$ time, but *insertion sort* is extremely fast for small arrays or lists that are already mostly sorted.

## connections

- [[p-vs-np-problem]] — sorting is a basic computational problem situated firmly within the class P.
- [[halting-problem]] — sorting algorithms are guaranteed to terminate, and their termination is easily proved.
- [[shortest-path-problem]] — Dijkstra's shortest path algorithm relies on a priority queue, which is maintained using sorting principles (heaps).
- [[knapsack-problem]] — sorting items by value-to-weight ratio is the key step in solving the fractional knapsack problem.

## see also

- [[p-vs-np-problem]] · [[halting-problem]] · [[shortest-path-problem]] · [[knapsack-problem]]

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

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
