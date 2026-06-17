---
type: concept
category: mathematics
defines: ["Shortest Path Problem", "Shortest Path"]
related: ["[[p-vs-np-problem]]", "[[traveling-salesman-problem]]"]
requires: []
lists:
  - "[[computation-types]]"
tour_order: 0
read: false
---

# Shortest Path Problem

## summary

The Shortest Path Problem is the task of finding a path between two vertices in a graph such that the sum of the weights of its constituent edges is minimized. Solvable in polynomial time, it stands in contrast to the NP-complete traveling salesman problem. Shortest path algorithms are critical to modern technology, powering network routing protocols, GPS navigation systems, and artificial intelligence pathfinding.

## you gotta know

- *Dijkstra's algorithm* is the standard method for finding the shortest path from a single source vertex to all other vertices in a graph with non-negative edge weights, achieving a runtime of $O(E + V \log V)$ using a Fibonacci heap.
- The *Bellman-Ford algorithm* handles graphs with negative edge weights and is capable of detecting negative-weight cycles, which would otherwise allow an algorithm to loop infinitely to decrease path cost.
- The *Floyd-Warshall algorithm* is a dynamic programming method that solves the all-pairs shortest path problem (finding shortest paths between all pairs of vertices) in $O(V^3)$ time.
- The $A^*$ search algorithm is a heuristic-guided extension of Dijkstra's algorithm that uses estimates of the remaining distance to prune the search space, commonly used in video games and robotics.
- Because it is solvable in polynomial time, the shortest path problem resides within the complexity class P, distinguishing it from NP-hard routing problems.

## connections

- [[p-vs-np-problem]] — shortest path is a polynomial-time solvable problem in P, contrasting with NP-hard variants.
- [[traveling-salesman-problem]] — TSP requires visiting all vertices (NP-complete), whereas shortest path only requires finding a path between two nodes (in P).
- [[sorting-algorithms]] — Dijkstra's algorithm uses a priority queue, which leverages sorting structures to quickly find the minimum-distance vertex.
- [[matrix-multiplication]] — all-pairs shortest path can be solved algebraically using tropical semiring matrix multiplication.

## see also

- [[p-vs-np-problem]] · [[traveling-salesman-problem]] · [[sorting-algorithms]] · [[matrix-multiplication]]

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
