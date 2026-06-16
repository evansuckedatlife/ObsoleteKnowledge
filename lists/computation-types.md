---
type: list
category: mathematics
read: false
---

# types of computation problems

The types of computation problems most worth knowing for quiz bowl.

## nodes

- [[graph-coloring|Graph Coloring]] — Graph coloring is an assignment of labels, called colors, to the elements of a graph subject to certain constraints.
- [[halting-problem|Halting Problem]] — The Halting Problem is a fundamental decision problem in computability theory that asks whether an arbitrary computer program,…
- [[integer-factorization|Integer Factorization]] — Integer factorization is the process of decomposing a composite integer into a product of smaller integers, typically prime…
- [[knapsack-problem|Knapsack Problem]] — The Knapsack Problem is a classic combinatorial optimization problem.
- [[matrix-multiplication|Matrix Multiplication]] — Matrix multiplication is a fundamental algebraic operation that combines two matrices to produce a third matrix, representing…
- [[p-vs-np-problem|P vs NP Problem]] — The P vs NP problem is a major unsolved question in theoretical computer science and mathematics that asks whether every…
- [[primality-testing|Primality Testing]] — Primality testing is the computational process of determining whether a given input integer is prime.
- [[shortest-path-problem|Shortest Path Problem]] — The Shortest Path Problem is the task of finding a path between two vertices in a graph such that the sum of the weights of…
- [[sorting-algorithms|Sorting Algorithms]] — Sorting algorithms are systematic methods used to rearrange a list or array of elements into a specified order, most commonly…
- [[traveling-salesman-problem|Traveling Salesman Problem]] — The Traveling Salesman Problem (TSP) is a classic optimization problem in graph theory and theoretical computer science.

## progress

Live read-status for this list (requires the **Bases** core plugin). Flip a node's `read` from its footer toggle and it moves here.

```base
filters:
  and:
    - file.hasLink(this.file)
views:
  - type: table
    name: Progress
    order:
      - file.name
      - read
      - type
    sort:
      - property: read
        direction: ASC
      - property: file.name
        direction: ASC
```
