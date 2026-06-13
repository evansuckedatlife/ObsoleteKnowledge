---
type: term
category: science
defines: [Divide and conquer, D&C]
related: ["[[algorithm]]", "[[recursion]]", "[[sorting-algorithm]]", "[[dynamic-programming]]"]
lists: ["[[programming-terms]]"]
read: false
---

# Divide and conquer

## summary

*Divide and conquer* is an algorithm design paradigm that solves a problem by recursively breaking it into smaller, independent subproblems, solving each subproblem, and combining their solutions into the overall answer. This approach is ideal for problems with recursive structure and yields elegant, efficient algorithms. Classic examples include mergesort (O(n log n) sorting), quicksort, binary search, and matrix multiplication.

## you gotta know

### Three-Phase Structure
- *Divide*: break the problem into k smaller subproblems (usually k=2 or 3).
- *Conquer*: recursively solve subproblems; base case handles trivial inputs.
- *Combine*: merge or aggregate subproblem solutions into the final answer.

### Why It Works
- Reduces problem size exponentially: a problem of size n becomes k problems of size n/k.
- Combined with efficient merging, produces logarithmic or linearithmic time complexity.
- Naturally parallel: independent subproblems can be solved in parallel on multicore systems.

### Canonical Examples
- *Mergesort*: divide array in half, sort halves, merge sorted halves in O(n log n).
- *Quicksort*: partition around pivot, recursively sort left and right; O(n log n) average, O(n²) worst-case.
- *Binary search*: eliminate half the search space per step; O(log n) time.
- *Strassen's matrix multiplication*: 7 multiplications instead of 8, reducing O(n³) to O(n^2.81).

### Complexity Analysis
- Typically analyzed via *recurrence relations*: T(n) = k·T(n/k) + D(n), where D(n) is divide-combine cost.
- *Master theorem*: solves recurrences of the form T(n) = a·T(n/b) + f(n), giving closed-form time bounds.
- Logarithmic depth (roughly log₂ n levels) makes these algorithms very efficient even on large inputs.

### When Divide-and-Conquer Shines
- Problem is naturally recursive: subproblems are independent and smaller versions of the original.
- Work done at each level is polynomial; recursion depth is logarithmic.
- Solutions benefit from parallelization.

## context

Divide and conquer is one of the three fundamental algorithm design paradigms, alongside greedy and dynamic programming. It teaches you to think about problems hierarchically: instead of processing a massive input linearly, break it smartly and process pieces independently. This mindset is invaluable in system design (distributed computing), numerical methods, and compiler optimization. Many of the fastest algorithms in practice—sorting, searching, FFT for signal processing—rely on divide-and-conquer structure.

## connections

- [[algorithm]] — a major algorithm design paradigm.
- [[recursion]] — divide-and-conquer is inherently recursive.
- [[sorting-algorithm]] — mergesort and quicksort are textbook D&C examples.
- [[greedy-algorithm]] — alternative paradigm; different trade-offs.
- [[dynamic-programming]] — memoization of D&C subproblems avoids recomputation.
- [[big-o-notation]] — essential for analyzing recurrence relations.

## see also

- [[recursion]] · [[sorting-algorithm]] · [[big-o-notation]]

<!-- footer -->

---

Lists: [[programming-terms]] · Mark read: `INPUT[toggle:read]`
