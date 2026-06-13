---
type: list
category: mathematics
read: false
---

# types of computation problems

The types of computation problems most worth knowing for quiz bowl.

## nodes

- [[decision-problem|Decision Problem]] — A decision problem is a computational problem with a yes-or-no (binary) answer: given an input, determine whether it satisfies…
- [[halting-problem|Halting Problem]] — The Halting Problem asks: given an arbitrary algorithm and an input, will the algorithm terminate or loop forever?
- [[np-complexity-class|NP (Complexity Class)]] — NP is the complexity class of decision problems whose solutions can be verified in polynomial time, even if finding them may…
- [[np-complete|NP-Complete]] — NP-complete problems are the hardest problems in NP: they are both in NP (verifiable in polynomial time) and NP-hard (at least…
- [[np-hard|NP-Hard]] — NP-hard problems are at least as computationally hard as the hardest problems in NP, defined by the property that every…
- [[optimization-problem|Optimization Problem]] — An optimization problem seeks the best solution from a set of candidates according to some criterion—maximizing profit,…
- [[p-complexity-class|P (Complexity Class)]] — P is the complexity class of decision problems solvable in polynomial time—that is, by a deterministic algorithm in a number…
- [[space-complexity|Space Complexity]] — Space complexity measures the amount of memory (auxiliary storage) an algorithm uses as a function of input size, expressed in…
- [[time-complexity|Time Complexity]] — Time complexity measures how the running time of an algorithm grows with the size of the input, typically expressed using Big…
- [[turing-machine|Turing Machine]] — A Turing machine is an abstract mathematical model of computation introduced by Alan Turing in 1936 that consists of an…

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
