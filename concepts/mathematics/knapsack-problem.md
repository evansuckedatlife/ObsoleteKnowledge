---
type: concept
category: mathematics
defines: ["Knapsack Problem"]
related:
  - "[[p-vs-np-problem]]"
  - "[[traveling-salesman-problem]]"
lists:
  - "[[computation-types]]"
read: false
---

# Knapsack Problem

## summary

The Knapsack Problem is a classic combinatorial optimization problem. Given a set of items, each with a weight and a value, the objective is to select a subset of items to include in a knapsack such that the total weight does not exceed a given capacity, and the total value is maximized. The decision version of this problem is NP-complete, making it a fundamental model for resource allocation and budgeting under constraints.

## you gotta know

- In the most common version, the 0-1 Knapsack Problem, items cannot be divided; each item must be either fully accepted or rejected.
- Although NP-complete, it can be solved in pseudo-polynomial time $O(n W)$ using dynamic programming, where $n$ is the number of items and $W$ is the weight capacity.
- The fractional version of the problem, where items can be broken down (like liquids or powders), can be solved optimally in polynomial time using a greedy algorithm.
- It was the basis for the Merkle-Hellman knapsack cryptosystem, one of the first public-key encryption schemes, which was eventually broken because the underlying subset sum problems were solvable in polynomial time for the chosen keys.
- It admits a fully polynomial-time approximation scheme (FPTAS), meaning one can find a solution within $1 - \epsilon$ of the optimal value in time polynomial in $n$ and $1/\epsilon$.

## connections

- [[p-vs-np-problem]] — serves as a representative NP-complete decision problem.
- [[traveling-salesman-problem]] — another classic NP-complete optimization problem frequently paired in complexity theory.
- [[sorting-algorithms]] — sorting items by their value-to-weight ratio is the primary step in the greedy algorithm for the fractional version.
- [[matrix-multiplication]] — dynamic programming algorithms for knapsack share similarities with the matrix chain ordering problem.

## see also

- [[p-vs-np-problem]] · [[traveling-salesman-problem]] · [[sorting-algorithms]]

<!-- footer -->

---

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
