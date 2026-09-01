---
type: concept
category: mathematics
defines:
  - Binary search
  - Binary search algorithm
related:
  - "[[algorithm]]"
  - "[[divide-and-conquer]]"
  - "[[time-complexity]]"
  - "[[logarithm]]"
  - "[[big-o-notation]]"
  - "[[sorting-algorithms]]"
  - "[[data-structures]]"
  - "[[logarithmic-time]]"
requires: ["[[algorithm]]"]
lists: []
tour_order: 6
read: false
---

# Binary Search


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Binary search** is a fundamental computer science algorithm for finding a target value within a *sorted* list or array by repeatedly dividing the search space in half. With a time complexity of O(log n), binary search exemplifies the power of *divide-and-conquer*: by eliminating half the remaining candidates with each comparison, it achieves exponential speedup over naive linear search, especially on large datasets.

## you gotta know

- Binary search works only on sorted data; at each step, it compares the target to the middle element and discards either the upper or lower half of the remaining search space, rapidly converging on the target or confirming its absence.
- The algorithm's time complexity is O(log n), meaning searching a million-element array requires at most ~20 comparisons; this logarithmic scaling makes it vastly faster than linear search (O(n), requiring up to a million comparisons).
- Binary search is a canonical example of *divide-and-conquer*: the problem is recursively split into smaller subproblems (left or right half), each solved in the same way, demonstrating how strategic problem decomposition yields exponential efficiency gains.
- The algorithm requires that the underlying data structure (usually an array or list) support random access (O(1) lookup by index); linked lists are unsuitable for binary search because accessing the middle element requires O(n) traversal.
- Binary search trees (BSTs) generalize binary search into a data structure where every node's left subtree contains smaller values and the right subtree larger values, enabling efficient search, insertion, and deletion (O(log n) average case).
- Variants exist for partially sorted data, finding boundaries (smallest element ≥ target), and approximate searching; *lower_bound* and *upper_bound* functions in programming libraries implement these variants.
- Binary search is ubiquitous in practice: database indexing, version control systems (finding the commit that introduced a bug via *git bisect*), and hardware design all leverage logarithmic search efficiency.

## connections

- [[algorithm]] — binary search is a canonical computer science algorithm.
- [[divide-and-conquer]] — the algorithmic strategy binary search exemplifies.
- [[time-complexity]] — the study of O(log n) complexity that characterizes binary search.
- [[big-o-notation]] — the mathematical framework for analyzing algorithm efficiency.
- [[sorting-algorithms]] — binary search requires sorted input; sorting algorithms prepare data for it.
- [[logarithm]] — the mathematical function that characterizes binary search's time complexity.
- [[data-structures]] — arrays and binary search trees are the data structures enabling binary search.
- [[recursion]] — binary search is often implemented recursively, dividing the problem recursively.

## see also

- [[algorithm]] · [[divide-and-conquer]] · [[time-complexity]] · [[big-o-notation]]

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

Lists:  · Mark read: `INPUT[toggle:read]`
