---
type: concept
category: mathematics
defines: ["Graph Coloring", "Vertex Coloring", "Chromatic Number"]
related: ["[[p-vs-np-problem]]", "[[traveling-salesman-problem]]"]
requires: []
lists:
  - "[[computation-types]]"
tour_order: 0
read: false
---

# Graph Coloring

## summary

Graph coloring is an assignment of labels, called colors, to the elements of a graph subject to certain constraints. In vertex coloring, the most common form, the constraint is that no two adjacent vertices share the same color. The minimum number of colors required to color a graph is its chromatic number, and finding this number is a fundamental NP-complete problem with wide applications in scheduling and compiler optimization.

## you gotta know

- The minimum number of colors needed to color a graph $G$ is called the chromatic number of $G$, denoted by $\chi(G)$.
- Determining if a general graph can be colored with $k$ colors (the $k$-coloring problem) is NP-complete for $k \ge 3$, while the 2-coloring problem is solvable in linear time because it is equivalent to checking if the graph is bipartite.
- The *Four Color Theorem* states that any planar graph (a graph that can be drawn on a flat plane without crossing edges) can be colored using at most four colors; it was famously proved in 1976 using a computer to verify thousands of cases.
- Greedy coloring algorithms can color graphs quickly by choosing colors sequentially, and heuristics like the Welsh-Powell algorithm improve this by processing vertices in descending order of their degree.
- In compiler optimization, graph coloring is the standard method for *register allocation*, where variables are mapped to a limited number of physical CPU registers.

## connections

- [[p-vs-np-problem]] — graph coloring is a classic NP-complete decision problem used to study complexity.
- [[traveling-salesman-problem]] — another NP-complete graph theory problem focused on cycles rather than vertex labeling.
- [[shortest-path-problem]] — contrasts a global vertex labeling constraint (NP-complete) with a local traversal path (polynomial-time solvable).
- [[sorting-algorithms]] — degree-sorting heuristics use sorting algorithms to order vertices before coloring.

## see also

- [[p-vs-np-problem]] · [[traveling-salesman-problem]] · [[shortest-path-problem]] · [[sorting-algorithms]]

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
