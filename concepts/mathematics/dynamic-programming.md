---
type: term
category: mathematics
defines: [Dynamic Programming, DP, memoization, tabulation]
related: ["[[recursion]]", "[[algorithm]]", "[[divide-and-conquer]]", "[[optimization-problem]]", "[[big-o-notation]]", "[[polynomial-function]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Dynamic Programming

## summary

*Dynamic programming* is an algorithmic technique that solves complex problems by breaking them into overlapping subproblems, storing the results of solved subproblems to avoid redundant recomputation, and building solutions upward from base cases. It transforms inefficient recursive approaches—often exponential in complexity—into polynomial-time algorithms by trading space for speed. Dynamic programming excels at optimization problems where decisions must be made sequentially and subproblems recur throughout the solution.

## you gotta know

### Core Principles
- *Optimal substructure*: the optimal solution to a problem contains optimal solutions to its subproblems.
- *Overlapping subproblems*: the same subproblems are computed many times in a naive recursive approach; DP computes each once and caches the result.
- Two implementation styles: *memoization* (top-down recursion with caching) and *tabulation* (bottom-up iterative table-filling).

### Classic Examples
- *Fibonacci*: naive recursion is O(2ⁿ); DP memoization or tabulation reduces it to O(n).
- *Longest increasing subsequence (LIS)*: find the longest ordered subsequence in an array; DP is O(n²) or O(n log n) with binary search.
- *0/1 knapsack problem*: select items with maximum value subject to a weight constraint; DP solves it in O(n·W) where W is the weight limit.
- *Edit distance (Levenshtein distance)*: minimum number of insertions, deletions, substitutions to transform one string into another; DP is O(m·n).
- *Coin change*: minimum number of coins to make a target value; DP is O(n·amount).

### Implementation Strategies
- *Memoization*: recursively solve subproblems, store results in a hash table; recurse only if result not cached.
- *Tabulation*: build a table bottom-up, filling cells in dependency order; no recursion stack, explicit control flow.
- *Space optimization*: for problems like LIS or coin change, the full table is unnecessary; rolling arrays or single-dimension arrays can reduce space from O(n²) to O(n) or O(1).

### Problem Recognition
- Presence of overlapping subproblems (exponential naive recursion) and optimal substructure signals a DP opportunity.
- Common DP problem patterns: counting paths, finding optima (min/max), detecting subsequences, tiling/partition problems.

## context

Dynamic programming emerged from control theory and operations research but has become central to computer science practice. It exemplifies a fundamental principle: *invest space upfront to save time later*. Without DP, many practical problems—sequence alignment in computational biology, speech recognition, resource scheduling—would be computationally infeasible. Modern applications range from compiler optimization (shortest path problems) to game-playing AI (minimax with memoization) to machine learning (certain matrix factorization techniques). The discipline teaches not just a technique but a mindset: recognize structure, eliminate redundancy, and build solutions incrementally. Many engineers first encounter DP in coding interviews, where it separates those who understand algorithmic thinking from those who merely implement; it is often the difference between a O(2ⁿ) solution that times out and a O(n²) solution that passes.

## connections

- [[recursion]] — DP is recursion with memoization; the base technique and the optimization are inseparable.
- [[algorithm]] — DP is one of the fundamental algorithmic paradigms.
- [[divide-and-conquer]] — both decompose problems, but DP solves overlapping subproblems; divide-and-conquer solves disjoint ones.
- [[optimization-problem]] — DP is the primary tool for knapsack, scheduling, and resource allocation problems.
- [[big-o-notation]] — DP dramatically reduces Big O: Fibonacci from O(2ⁿ) to O(n).
- [[polynomial-function]] — DP solutions often run in polynomial time O(n²), O(n³), or O(n·m).
- [[shortest-path-problem]] — Bellman-Ford uses DP principles to find optimal paths in weighted graphs.
- [[traveling-salesman-problem]] — can be solved optimally via DP in O(n²·2ⁿ), and approximated via greedy or branch-and-bound.
- [[knapsack-problem]] — the canonical DP problem: select items to maximize value within a weight constraint.

## see also

- [[recursion]] · [[algorithm]] · [[optimization-problem]] · [[knapsack-problem]]

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

Lists: · Mark read: `INPUT[toggle:read]`
