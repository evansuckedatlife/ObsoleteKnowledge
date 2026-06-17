---
type: term
category: mathematics
defines: [Big O Notation, O(n), Landau notation, asymptotic complexity]
related: ["[[algorithm]]", "[[time-complexity]]", "[[space-complexity]]", "[[sorting-algorithms]]", "[[recursion]]", "[[polynomial-function]]", "[[exponential-function]]"]
lists: []
read: false
---

# Big O Notation

## summary

*Big O notation* is a mathematical framework for describing the asymptotic behavior of a function—how its value grows relative to the size of its input. In computer science, it quantifies algorithm efficiency by expressing the worst-case time or space resources required as input size approaches infinity. Big O strips away constant factors and lower-order terms, revealing the dominant growth pattern: linear O(n), quadratic O(n²), logarithmic O(log n), or exponential O(2ⁿ). It is the lingua franca of algorithm analysis and performance prediction.

## you gotta know

### Definition and Intuition
- *Big O* formalizes "grows no faster than": f(n) = O(g(n)) if there exist constants c and n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀.
- Ignores constant factors and lower-order terms; O(2n + 5) simplifies to O(n), and O(n² + n + 7) simplifies to O(n²).
- Measures worst-case behavior—the most resource-intensive input of a given size.

### Common Complexity Classes
- *Constant* O(1): lookup in a hash table; array access by index.
- *Logarithmic* O(log n): binary search; balanced tree insertion/lookup.
- *Linear* O(n): simple scan through an array; linear search.
- *Linearithmic* O(n log n): optimal comparison-based sorting (merge sort, quicksort average case).
- *Quadratic* O(n²): naive nested-loop algorithms; bubble sort, insertion sort.
- *Cubic* O(n³): naive matrix multiplication; some dynamic programming solutions.
- *Exponential* O(2ⁿ): brute-force subset enumeration; backtracking without pruning; NP-complete problems.
- *Factorial* O(n!): generating all permutations.

### Big O in Practice
- Allows rigorous comparison of algorithms independent of hardware or implementation language.
- Predicts scalability: O(n) scales to large n; O(2ⁿ) hits a wall quickly (n=40 → 10¹² operations).
- Space complexity uses the same notation: an algorithm might be O(n) time and O(1) space, or O(n) time and O(n) space.

### Related Notations
- *Ω (big omega)*: lower bound—f(n) = Ω(g(n)) means f grows no slower than g.
- *Θ (big theta)*: tight bound—f(n) = Θ(g(n)) means f and g have the same asymptotic growth.
- *o (little o)*: f(n) = o(g(n)) means f grows strictly slower than g.

## context

Big O notation is foundational to computer science because it abstracts away the physical details of computation—CPU speed, memory latency, cache behavior—and focuses on the intrinsic algorithmic cost. When your input size doubles, knowing whether an algorithm's running time doubles (linear), quadruples (quadratic), or stays almost the same (logarithmic) is the difference between a responsive system and one that grinds to a halt. Big O analysis has become a standard in job interviews, algorithm courses, and engineering decisions: when choosing between a Θ(n log n) sort and a Θ(n²) sort, Big O makes the trade-off transparent. For problems in the NP-complete complexity class, Big O helps formalize why no known polynomial-time algorithm exists, driving the search for approximations and heuristics instead.

## connections

- [[algorithm]] — Big O is the primary tool for analyzing algorithm efficiency.
- [[time-complexity]] — formalizes the runtime growth of a computation.
- [[space-complexity]] — measures memory usage in the same asymptotic framework.
- [[sorting-algorithms]] — a classic domain for Big O analysis (merge sort O(n log n), bubble sort O(n²)).
- [[recursion]] — recursive depth and work per call determine the overall Big O (e.g., fibonacci is O(2ⁿ) naive, O(n) with memoization).
- [[polynomial-function]] — Big O polynomial classes (O(n), O(n²), O(n³)) arise from polynomial time algorithms.
- [[exponential-function]] — exponential Big O (O(2ⁿ)) marks the boundary of practical solvability.
- [[np-complete]] — problems with no known polynomial-time algorithms; Big O shows why brute force is O(2ⁿ).
- [[dynamic-programming]] — reduces exponential Big O to polynomial via memoization.
- [[binary-search]] — logarithmic Big O exemplifies the power of divide-and-conquer.

## see also

- [[time-complexity]] · [[space-complexity]] · [[sorting-algorithms]] · [[np-complete]]

<!-- footer -->

---

Lists: · Mark read: `INPUT[toggle:read]`
