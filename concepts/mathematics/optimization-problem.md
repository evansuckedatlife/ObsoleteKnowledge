---
type: term
category: mathematics
defines:
  - Optimization problem
  - Optimization problem
related:
  - "[[decision-problem]]"
  - "[[np-hard]]"
  - "[[np-complete]]"
lists:
  - "[[calculus-ideas]]"
read: true
---

# Optimization Problem

## summary

An **optimization problem** seeks the best solution from a set of candidates according to some criterion—maximizing profit, minimizing cost, finding the shortest path, etc. Unlike decision problems (yes/no), optimization problems ask "what is the *best* value?" and are fundamental to practical computing and algorithm design.

## you gotta know

- Formally: given a set of feasible solutions and an objective function, find the solution that maximizes (or minimizes) the objective.
- Examples: Travelling Salesman (find the shortest tour), Knapsack (maximize value subject to weight), Graph Coloring (minimize colors), Longest Path (find the longest simple path), Integer Linear Programming.
- **Harder than the decision variant**: the decision version asks "is there a solution with value ≥ k?" (yes/no), while the optimization version asks "what is the best value?" The decision version reduces to the optimization one.
- **NP-hard optimization problems** have no known polynomial-time algorithm; approximation algorithms and heuristics (greedy, dynamic programming, branch-and-bound) are practical approaches.
- Widely studied in operations research, machine learning, and cryptanalysis—nearly all real-world computational problems are optimization, not pure decision.
- Closely paired with its decision variant for complexity analysis: if the decision version is NP-complete, the optimization version is NP-hard.

## connections

- [[decision-problem]] — optimization problems have corresponding decision variants used in complexity proofs.
- [[np-hard]] — most natural optimization problems are NP-hard.
- [[np-complete]] — decision versions of NP-hard optimization problems are often NP-complete.
- [[time-complexity]] — optimization algorithms are classified by their runtime.

## see also

- [[decision-problem]] · [[np-hard]] · [[np-complete]]

<!-- footer -->

---

Lists: [[calculus-ideas]] · Mark read: `INPUT[toggle:read]`
