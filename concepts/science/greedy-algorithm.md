---
type: term
category: science
defines: [Greedy algorithm, greedy]
related: ["[[algorithm]]", "[[divide-and-conquer]]", "[[dynamic-programming]]", "[[graph-data-structure]]"]
requires: ["[[algorithm]]"]
lists: ["[[programming-terms]]"]
tour_order: 6
read: false
---

# Greedy algorithm


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A *greedy algorithm* makes locally optimal choices at each step, hoping (or proving) that these choices lead to a globally optimal solution. Unlike divide-and-conquer or dynamic programming, greedy algorithms commit to decisions immediately without reconsidering them. They are often fast and simple but not always correct; the challenge is proving or identifying when a greedy approach guarantees optimality.

## you gotta know

### Core Idea
- At each step, select the option that seems best *right now*, without looking ahead.
- Once a choice is made, it is never undone or reconsidered (no backtracking).
- Greedy algorithms are naturally iterative and typically run in O(n log n) or O(n) time.

### When Greedy Works
- *Matroid structures*: certain optimization problems have the *greedy choice property*—a locally optimal choice is part of a globally optimal solution.
- *Optimal substructure*: the optimal solution contains optimal solutions to subproblems.
- If both properties hold, greedy is provably correct; otherwise, it may fail.

### Classic Examples
- *Activity selection*: schedule non-overlapping tasks; greedily pick earliest-ending activity.
- *Huffman coding*: build optimal prefix-free code by repeatedly merging lowest-frequency nodes.
- *Dijkstra's shortest path*: greedily explore nearest unvisited node; optimal for non-negative weights.
- *Fractional knapsack*: stuff items by highest value-to-weight ratio; optimal for fractions.
- *Kruskal's minimum spanning tree*: add lowest-weight edge that doesn't create a cycle.

### Where Greedy Fails
- *0-1 knapsack*: can't break items; greedy by value-to-weight ratio fails (need dynamic programming).
- *Traveling salesman*: greedy nearest-neighbor is fast but suboptimal.
- Many graph coloring and scheduling variants have no greedy solution.

### Analysis Strategy
- Prove correctness via exchange argument: show that any non-greedy solution can be transformed into a greedy solution without worsening optimality.
- Provide counterexamples when greedy fails; verify with dynamic programming or branch-and-bound.

## context

Greedy algorithms are a programmer's workhorse: simple to code, fast to execute, and excellent for approximation when optimality is intractable. They dominate practical applications in networking (load balancing), resource allocation, and scheduling. However, the trap is assuming greedy works without proof. A hallmark of algorithmic maturity is recognizing the class of problems where greedy is valid and having the discipline to reach for dynamic programming or approximation techniques when it isn't. Many interview problems test exactly this discernment.

## connections

- [[algorithm]] — a major algorithm design paradigm.
- [[divide-and-conquer]] — an alternative approach; divide-and-conquer is slower but more general.
- [[dynamic-programming]] — when greedy fails, DP often succeeds via exhaustive cached search.
- [[graph-data-structure]] — many greedy algorithms operate on graphs (Dijkstra, Kruskal).
- [[big-o-notation]] — greedy algorithms typically have favorable complexity bounds.

## see also

- [[divide-and-conquer]] · [[dynamic-programming]] · [[graph-data-structure]]

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

Lists: [[programming-terms]] · Mark read: `INPUT[toggle:read]`
