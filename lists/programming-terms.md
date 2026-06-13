---
type: list
category: science
read: false
---

# programming terms

The programming terms most worth knowing for quiz bowl.

## nodes

- [[algorithm|Algorithm]] — An algorithm is a step-by-step computational procedure that transforms input data into output, guaranteed to terminate.
- [[compiler|Compiler]] — A compiler is a program that translates source code written in a high-level language into lower-level code (machine code,…
- [[divide-and-conquer|Divide and conquer]] — Divide and conquer is an algorithm design paradigm that solves a problem by recursively breaking it into smaller, independent…
- [[functional-programming|Functional programming]] — Functional programming (FP) is a paradigm that treats computation as the evaluation of mathematical functions, emphasizing…
- [[graph-data-structure|Graph (data structure)]] — A graph is a data structure consisting of nodes (or vertices) and edges (or connections) that link pairs of nodes.
- [[greedy-algorithm|Greedy algorithm]] — A greedy algorithm makes locally optimal choices at each step, hoping (or proving) that these choices lead to a globally…
- [[object-oriented-programming|Object-oriented programming]] — Object-oriented programming (OOP) is a paradigm that organizes code around objects—entities that bundle data (state) and…
- [[programming-language|Programming language]] — A programming language is a formal system of communication with a computer, consisting of syntax (grammatical rules),…
- [[recursion|Recursion]] — Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller,…
- [[type-system|Type system]] — A type system is a set of rules determining which operations are valid on which data, preventing certain kinds of errors.

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
