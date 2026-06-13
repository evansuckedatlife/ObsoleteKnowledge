---
type: list
category: mathematics
read: false
---

# types of computation problems

The types of computation problems most worth knowing for quiz bowl.

## nodes

- [[p-vs-np-problem|P vs NP Problem]] — The fundamental question of whether verifying a solution's correctness is as easy as finding it.
- [[halting-problem|Halting Problem]] — The undecidable problem of determining whether an arbitrary computer program will eventually finish running or loop forever.
- [[traveling-salesman-problem|Traveling Salesman Problem]] — An NP-hard optimization problem seeking the shortest cycle that visits each vertex of a weighted graph exactly once.
- [[knapsack-problem|Knapsack Problem]] — An NP-complete optimization problem seeking the most valuable subset of items that fits within a weight limit.
- [[sorting-algorithms|Sorting Algorithms]] — Systematic procedures for rearranging a sequence of elements into numerical or alphabetical order.
- [[matrix-multiplication|Matrix Multiplication]] — A core algebraic operation whose optimal asymptotic time complexity remains a major open question.
- [[graph-coloring|Graph Coloring]] — An NP-complete problem that assigns colors to vertices such that no adjacent vertices share a color.
- [[shortest-path-problem|Shortest Path Problem]] — The polynomial-time problem of finding the route of minimum total weight between vertices in a graph.
- [[primality-testing|Primality Testing]] — The polynomial-time decision problem of determining whether a given integer is a prime number.
- [[integer-factorization|Integer Factorization]] — The computationally difficult problem of decomposing a composite integer into its prime factors.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
