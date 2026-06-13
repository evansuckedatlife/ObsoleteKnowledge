---
type: term
category: science
defines: [Algorithm, algo]
related: ["[[recursion]]", "[[divide-and-conquer]]", "[[greedy-algorithm]]", "[[big-o-notation]]"]
lists: ["[[programming-terms]]"]
read: false
---

# Algorithm

## summary

An *algorithm* is a step-by-step computational procedure that transforms input data into output, guaranteed to terminate. It forms the backbone of computer science: every program is ultimately an algorithm, and every algorithm can be analyzed for correctness, efficiency, and scalability. Algorithms exist independent of programming language—the same algorithm can be implemented in Python, C++, or Rust with identical logic.

## you gotta know

### Definition & Properties
- An algorithm must be *finite* (terminate in bounded steps), *deterministic* (same input → same output), and *well-defined* (each step unambiguous).
- Correctness means the algorithm solves the stated problem; *efficiency* means it does so with minimal time and space.

### Classic Categories
- *Search algorithms* locate items (linear search, binary search).
- *Sorting algorithms* order sequences (quicksort, mergesort, heapsort).
- *Graph algorithms* traverse or optimize networks (BFS, DFS, Dijkstra).
- *String matching* finds substrings (KMP, Rabin-Karp).

### Analysis & Complexity
- *Big O notation* formalizes runtime growth: O(1), O(n), O(n²), O(2^n).
- *Best, worst, average case* distinguish performance under different input distributions.
- Trade-offs: some algorithms are fast but use memory; others save space at the cost of time.

### Fundamental Techniques
- *Brute force*: try all possibilities (exhaustive, often slow).
- *Divide and conquer*: break into subproblems, solve independently, merge.
- *Dynamic programming*: cache subproblem results to avoid redundant computation.
- *Greedy*: make locally optimal choices hoping for a global optimum.

## context

Algorithms are the vocabulary of computer science. Every practical problem—routing data through a network, compressing video, predicting weather, sorting millions of records—boils down to choosing the right algorithm. The shift from an O(n²) to O(n log n) sorting algorithm can mean the difference between a program that runs in seconds versus hours. Understanding algorithms deeply teaches you how to think about problems abstractly before committing to code; this skill transfers across all programming domains.

## connections

- [[recursion]] — many elegant algorithms exploit recursive structure.
- [[divide-and-conquer]] — a systematic algorithm design paradigm.
- [[greedy-algorithm]] — one class of algorithmic strategy with known trade-offs.
- [[graph-data-structure]] — algorithms on graphs solve routing, scheduling, matching problems.
- [[big-o-notation]] — the formal language for algorithm analysis.
- [[sorting-algorithm]] — canonical examples that illustrate algorithm design and analysis.
- [[dynamic-programming]] — technique for optimizing recursive algorithms via memoization.

## see also

- [[binary-search]] · [[sorting-algorithm]] · [[big-o-notation]]

<!-- footer -->

---

Lists: [[programming-terms]] · Mark read: `INPUT[toggle:read]`
