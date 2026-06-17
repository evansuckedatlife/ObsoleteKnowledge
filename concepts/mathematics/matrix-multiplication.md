---
type: concept
category: mathematics
defines: ["Matrix Multiplication"]
related: ["[[p-vs-np-problem]]", "[[sorting-algorithms]]"]
requires: []
lists:
  - "[[computation-types]]"
tour_order: 0
read: false
---

# Matrix Multiplication

## summary

Matrix multiplication is a fundamental algebraic operation that combines two matrices to produce a third matrix, representing the composition of linear transformations. The computational efficiency of multiplying matrices is a major area of study in computer science, as it is a core bottleneck in graphics, physics simulations, and machine learning. Breakthroughs in matrix multiplication algorithms have repeatedly redefined our understanding of theoretical complexity limits.

## you gotta know

- The standard, naive algorithm for multiplying two $n \times n$ matrices requires $O(n^3)$ arithmetic operations, directly performing the dot products of rows and columns.
- *Strassen's algorithm*, introduced in 1969, was the first to show that matrix multiplication can be done faster than $O(n^3)$ by using a divide-and-conquer strategy that reduces the number of sub-multiplications from 8 to 7, yielding a runtime of $O(n^{\log_2 7}) \approx O(n^{2.81})$.
- The asymptotic complexity limit of matrix multiplication is denoted by $\omega$ (omega), representing the lower bound of exponents such that two $n \times n$ matrices can be multiplied in $O(n^\omega)$ operations.
- The *Coppersmith-Winograd algorithm* established a theoretical bound of $O(n^{2.376})$ in 1987, and modern refinements have lowered this bound to approximately $O(n^{2.371})$.
- Despite their theoretical speed, algorithms with exponents below Strassen's are rarely used in practice because they have extremely large hidden constant factors (referred to as "galactic algorithms").

## connections

- [[p-vs-np-problem]] — matrix multiplication is a polynomial-time operation located securely in the class P.
- [[sorting-algorithms]] — comparison-based sorting has a known lower bound of $O(n \log n)$, whereas the exact lower bound for matrix multiplication ($\omega \ge 2$) remains an open question.
- [[shortest-path-problem]] — the all-pairs shortest path problem can be solved by translating it into "min-plus" matrix multiplication over a tropical semiring.
- [[knapsack-problem]] — the matrix chain multiplication problem, which finds the most efficient order to multiply a sequence of matrices, is solved using dynamic programming similar to the knapsack problem.

## see also

- [[p-vs-np-problem]] · [[sorting-algorithms]] · [[shortest-path-problem]] · [[knapsack-problem]]

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
