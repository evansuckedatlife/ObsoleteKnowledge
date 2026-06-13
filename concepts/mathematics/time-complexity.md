---
type: term
category: mathematics
defines:
  - "Time complexity"
  - Time complexity
  - "Big O notation"
related:
  - "[[p-complexity-class]]"
  - "[[np-complexity-class]]"
  - "[[space-complexity]]"
  - "[[turing-machine]]"
lists: []
read: false
---

# Time Complexity

## summary

**Time complexity** measures how the running time of an algorithm grows with the size of the input, typically expressed using Big O notation (`O(n)`, `O(n²)`, `O(2^n)`). It is the primary lens through which computer scientists classify algorithms and problems, enabling comparison of efficiency and defining major complexity classes like **P** and **NP**.

## you gotta know

- **Big O notation** `O(f(n))`: an upper bound on the running time; `O(n)` linear, `O(n log n)` linearithmic, `O(n²)` quadratic, `O(2^n)` exponential.
- Measures the worst-case number of elementary operations (comparisons, arithmetic, etc.) as a function of input size `n`.
- **Polynomial time** (`O(n^k)` for fixed `k`) is the practical boundary: algorithms are considered efficient or feasible if they run in polynomial time.
- **Exponential time** (`O(2^n)` or worse) is prohibitive for large inputs; the Halting Problem and NP-complete problems have no known polynomial-time algorithms.
- **Linear time** (`O(n)`), **logarithmic** (`O(log n)`), and **linearithmic** (`O(n log n)`) are very efficient; sorting via merge-sort is `O(n log n)`.
- **P** = problems solvable in polynomial time; **NP** = problems verifiable in polynomial time; the gap between "solvable" and "verifiable" time is the **P vs. NP** question.
- Related: **space complexity** measures memory usage; **amortized** analysis averages cost over many operations.

## connections

- [[p-complexity-class]] — defines the tractable boundary as polynomial time.
- [[np-complexity-class]] — verification time (NP) is polynomial, but solving time is unknown.
- [[space-complexity]] — dual measure of algorithmic efficiency alongside time.
- [[turing-machine]] — time complexity is measured on Turing machines (the standard model).
- [[decision-problem]] — time complexity classifies decision problems by solvability time.

## see also

- [[p-complexity-class]] · [[np-complexity-class]] · [[space-complexity]] · [[turing-machine]]

<!-- footer -->

---

Lists:  · Mark read: `INPUT[toggle:read]`
