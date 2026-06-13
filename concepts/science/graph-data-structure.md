---
type: term
category: science
defines: [Graph, graph data structure]
related: ["[[algorithm]]", "[[tree-data-structure]]", "[[data-structure]]"]
lists: ["[[programming-terms]]"]
read: false
---

# Graph (data structure)

## summary

A *graph* is a data structure consisting of *nodes* (or vertices) and *edges* (or connections) that link pairs of nodes. Graphs model relationships and networks: social networks, road maps, computer networks, dependencies in projects, and knowledge bases. Unlike trees (which have no cycles), graphs can be cyclic and disconnected. They are classified as *directed* (edges have direction) or *undirected* (bidirectional), and *weighted* (edges carry numeric values) or unweighted.

## you gotta know

### Fundamental Concepts
- A *node* or *vertex* represents an entity; an *edge* or *link* represents a relationship between two nodes.
- *Directed graph*: edges have direction (e.g., Twitter follows); *undirected*: edges are bidirectional (e.g., roads).
- *Weighted graph*: edges carry numeric labels (e.g., distance, cost); used in optimization problems.
- *Degree*: the number of edges connected to a node; *in-degree* and *out-degree* for directed graphs.

### Common Graph Types
- *Acyclic graph* (DAG): no cycles; used for dependency graphs, scheduling.
- *Connected graph*: a path exists between any two nodes.
- *Complete graph*: every pair of nodes has an edge.
- *Bipartite graph*: nodes split into two groups; edges only connect across groups (matching problems).

### Representation Methods
- *Adjacency matrix*: 2D array where matrix[i][j] indicates an edge from i to j; dense graphs, O(n²) space.
- *Adjacency list*: array of lists; each node stores its neighbors; sparse graphs, O(n+m) space (m = edges).
- *Incidence list*: lists edges instead of adjacencies; useful for weighted graphs.

### Key Algorithms
- *BFS* (breadth-first search): explore level-by-level; find shortest paths in unweighted graphs.
- *DFS* (depth-first search): explore as far as possible; detect cycles, topological sort.
- *Dijkstra's algorithm*: shortest path in weighted graphs (non-negative edges).
- *Kruskal's/Prim's algorithms*: minimum spanning tree; connect all nodes with minimum total weight.

## context

Graphs are one of the most versatile data structures in computer science. Almost every real-world network—the internet, transportation systems, biological pathways, recommendation engines—is modeled as a graph. Understanding graph algorithms is essential for backend engineers, data scientists, and anyone working on optimization, routing, or relationship modeling. The problem of finding an efficient path through a graph (or determining feasibility) underlies countless practical applications, from GPS navigation to compiler optimization to social network analysis.

## connections

- [[algorithm]] — graph algorithms are a major algorithm family.
- [[tree-data-structure]] — a tree is a special (acyclic) type of graph.
- [[data-structure]] — graphs are a fundamental data structure alongside arrays, linked lists.
- [[divide-and-conquer]] — some graph algorithms use divide-and-conquer strategy.
- [[dynamic-programming]] — shortest-path problems solved via dynamic programming.
- [[big-o-notation]] — critical for analyzing graph algorithm complexity.

## see also

- [[tree-data-structure]] · [[algorithm]] · [[big-o-notation]]

<!-- footer -->

---

Lists: [[programming-terms]] · Mark read: `INPUT[toggle:read]`
