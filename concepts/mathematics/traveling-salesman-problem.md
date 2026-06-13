---
type: concept
category: mathematics
defines: ["Traveling Salesman Problem", "TSP", "Travelling Salesman Problem"]
related:
  - "[[p-vs-np-problem]]"
  - "[[shortest-path-problem]]"
lists:
  - "[[computation-types]]"
read: false
---

# Traveling Salesman Problem

## summary

The Traveling Salesman Problem (TSP) is a classic optimization problem in graph theory and theoretical computer science. Given a set of cities and the distance between each pair, the goal is to find the shortest possible route that visits every city exactly once and returns to the starting city. The decision version of the problem is NP-complete, making it a central benchmark for studying optimization and algorithmic complexity.

## you gotta know

- Formally, the problem asks for the minimum-weight Hamiltonian cycle in a complete weighted graph.
- The decision version of TSP ("Is there a tour of length at most $k$?") is NP-complete, which means that no polynomial-time algorithm is known to solve it exactly for all inputs.
- The Held-Karp algorithm, which uses dynamic programming, is one of the classic exact methods for solving the TSP, operating in $O(2^n n^2)$ time, which is much faster than brute-force search ($O(n!)$) but still exponential.
- For metric TSP (where distances satisfy the triangle inequality), Christofides' algorithm is a famous approximation algorithm that guarantees a tour no longer than 1.5 times the optimal tour length.
- The problem is heavily studied in operations research and has practical applications in logistics, microchip manufacturing, and DNA sequencing.

## connections

- [[p-vs-np-problem]] — TSP is a classic NP-complete/NP-hard problem used to illustrate the difficulty of finding efficient algorithms.
- [[shortest-path-problem]] — contrasts with finding the shortest path between two specific vertices, which is solvable in polynomial time.
- [[knapsack-problem]] — another iconic NP-complete combinatorial optimization problem.
- [[graph-coloring]] — shares complexity properties and is often studied alongside TSP in graph optimization.

## see also

- [[p-vs-np-problem]] · [[shortest-path-problem]] · [[knapsack-problem]] · [[graph-coloring]]

<!-- footer -->

---

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
