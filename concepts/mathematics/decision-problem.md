---
type: term
category: mathematics
defines:
  - "Decision problem"
  - Decision problem
related:
  - "[[p-complexity-class]]"
  - "[[np-complexity-class]]"
  - "[[optimization-problem]]"
  - "[[turing-machine]]"
lists:
  - "[[computation-types]]"
read: false
---

# Decision Problem

## summary

A **decision problem** is a computational problem with a yes-or-no (binary) answer: given an input, determine whether it satisfies a specified property. Decision problems form the foundation of complexity theory, since all major complexity classes (**P**, **NP**, etc.) are formally defined for decision problems.

## you gotta know

- The simplest formal model: input → yes/no. Variants like counting or optimization are distinct but often reducible to decision variants.
- Examples: "Is this number prime?" (yes/no), "Does this graph contain a Hamiltonian cycle?" (yes/no), "Is this Boolean formula satisfiable?" (yes/no).
- Formally represented as a language: the set of input strings for which the answer is yes; an algorithm *solves* the problem by recognizing this language.
- **P** and **NP** are defined for decision problems: a problem is in **P** if it can be solved in polynomial time, in **NP** if a yes-answer can be *verified* in polynomial time.
- Most NP-complete and NP-hard problems are phrased as decision problems for theoretical purposes; the corresponding optimization problems ("find the best solution") are typically harder.
- Contrast with optimization problems: "Find the shortest path" (optimization) vs. "Is there a path of length ≤ k?" (decision).

## connections

- [[p-complexity-class]] — **P** is the class of polynomial-time solvable decision problems.
- [[np-complexity-class]] — **NP** is the class of polynomial-time verifiable decision problems.
- [[np-complete]] — NP-complete problems are decision problems in **NP** that are NP-hard.
- [[optimization-problem]] — often paired with decision variants for complexity analysis.
- [[turing-machine]] — decision problems are naturally solved by Turing machines.

## see also

- [[p-complexity-class]] · [[np-complexity-class]] · [[optimization-problem]] · [[turing-machine]]

<!-- footer -->

---

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
