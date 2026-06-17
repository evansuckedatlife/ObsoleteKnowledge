---
type: term
category: mathematics
defines: [Tree data structure, rooted tree, binary tree, leaf node, internal node]
related: ["[[recursion]]", "[[graph-coloring]]", "[[algorithm]]", "[[binary-search]]", "[[shortest-path-problem]]", "[[polynomial-function]]", "[[divide-and-conquer]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Tree Data Structure

## summary

A *tree* is a connected acyclic graph—a hierarchical data structure with one distinguished *root* node, from which all other nodes are reachable via a unique path. Each non-root node has exactly one *parent* node; a node may have zero or more *children*. Nodes with no children are *leaf nodes*; nodes with at least one child are *internal nodes*. Trees are pervasive in computer science: file systems organize directories in trees, compilers parse code into abstract syntax trees, databases use B-trees and AVL trees for fast lookup, and recursion naturally mirrors tree structure.

## you gotta know

### Fundamental Concepts
- A tree with n nodes has exactly n-1 edges and is connected and acyclic; adding any edge creates a cycle; removing any edge disconnects it.
- The *height* of a tree is the longest path from root to leaf; a tree with one node has height 0.
- The *depth* of a node is its distance from the root; the root has depth 0.
- A *subtree* rooted at node v consists of v and all its descendants; it is itself a tree.

### Binary Trees
- Each node has at most two children (left and right); a *full binary tree* has each node with 0 or 2 children; a *complete binary tree* fills levels left-to-right.
- A *balanced* binary tree has height O(log n), allowing operations like search and insertion in O(log n) time.
- Binary search trees (BSTs) maintain left < parent < right, enabling efficient sorted traversal and lookup.

### Tree Traversals
- *Inorder* (left, node, right): useful for extracting sorted values from a BST.
- *Preorder* (node, left, right): natural for copying or serializing trees.
- *Postorder* (left, right, node): natural for deletion or computing tree properties bottom-up.
- *Breadth-first (level-order)*: visit nodes by depth, useful for many algorithms.

### Special Trees
- *Balanced search trees* (AVL, red-black): maintain height O(log n) after insertion/deletion, guaranteeing O(log n) operations.
- *Heaps* (binary heaps): partially ordered trees supporting O(log n) insertion and O(1) min/max extraction.
- *Tries*: trees for storing strings, where each node is a character and paths spell words; used in autocomplete and spell-checking.
- *Segment trees* and *Fenwick trees*: specialized structures for range queries and updates in O(log n).

### Recursive Nature
- Tree algorithms are naturally recursive: compute a result for a node by combining results from its children.
- Example: tree height = 1 + max(left_height, right_height); tree size = 1 + left_size + right_size.

## context

Trees are among the most fundamental data structures in all of computer science. The tree abstraction appears whenever you need hierarchy: organizational charts, taxonomies, parse trees in compilers, game decision trees in AI, and file systems. Balanced binary search trees like AVL and red-black trees are the backbone of many databases and operating systems, guaranteeing logarithmic search and insertion even after arbitrary edit sequences. Heaps power priority queues and Dijkstra's algorithm, which in turn enables GPS routing and network optimization. The recursive structure of trees makes them natural subjects for analysis: understanding tree height, path length, and traversal cost translates directly to analyzing algorithm performance. Many advanced algorithms—Huffman coding, closest-pair-in-divide-and-conquer, dynamic programming on tree DP—exploit tree structure to achieve efficiency. Learning to work with trees teaches structural thinking and recursive decomposition, skills that transfer to parsing, compiler design, and complex problem-solving.

## connections

- [[recursion]] — tree operations are intrinsically recursive; each node delegates to its children.
- [[algorithm]] — tree algorithms (search, traversal, balancing) are foundational.
- [[binary-search]] — binary search trees maintain the property that enables O(log n) search.
- [[divide-and-conquer]] — tree problems naturally decompose: solve left subtree, right subtree, combine.
- [[graph-coloring]] — coloring problems can be solved on tree subgraphs via dynamic programming.
- [[shortest-path-problem]] — trees are acyclic paths; shortest path in a tree is unique; generalizations use graphs.
- [[dynamic-programming]] — tree DP (e.g., rerooting technique, tree knapsack) solves optimization problems on trees in O(n).
- [[big-o-notation]] — balanced trees achieve O(log n) operations; analysis uses Big O to prove it.
- [[polynomial-function]] — tree traversal is O(n), sorting O(n log n); polynomial bounds arise from tree operations.

## see also

- [[recursion]] · [[algorithm]] · [[binary-search]] · [[divide-and-conquer]]

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

Lists: · Mark read: `INPUT[toggle:read]`
