---
type: term
category: mathematics
defines:
  - NP-complete
related:
  - "[[np-complexity-class]]"
  - "[[np-hard]]"
  - "[[p-complexity-class]]"
  - "[[decision-problem]]"
lists:
  - "[[computation-types]]"
read: false
---

# NP-Complete

## summary

**NP-complete** problems are the hardest problems in **NP**: they are both in **NP** (verifiable in polynomial time) and **NP-hard** (at least as hard as every other problem in **NP**). The existence of a polynomial-time algorithm for any NP-complete problem would prove **P = NP** and revolutionize mathematics and cryptography.

## you gotta know

- A problem is **NP-complete** if it is in **NP** and **NP-hard**—every other **NP** problem can be *reduced* to it in polynomial time.
- The first NP-complete problem was **Boolean Satisfiability (SAT)**, proved by Stephen Cook in 1971; thousands are now known.
- Famous examples: Travelling Salesman Problem, Clique Problem, Vertex Cover, Hamiltonian Cycle, 3-SAT, Integer Knapsack.
- All known NP-complete problems have exponential-time algorithms; none are known to be in **P**, but none are proven to be outside it.
- If **P ≠ NP** (conjectured), then NP-complete problems are strictly harder than polynomial-time solvable ones and have no fast general solution.
- Practical importance: NP-complete problems underpin the hardness assumptions for modern cryptography (e.g., integer factorization).
- Reduction technique: to prove a new problem is NP-complete, show it is in **NP** and that **SAT** (or another known NP-complete problem) reduces to it.

## connections

- [[np-complexity-class]] — NP-complete problems are a subset of **NP**.
- [[np-hard]] — NP-complete = NP-hard ∩ NP; NP-hard problems need not be in NP.
- [[p-complexity-class]] — if any NP-complete problem is in **P**, then **P = NP**.
- [[decision-problem]] — NP-complete problems are decision problems.
- [[boolean-satisfiability]] — the archetypal NP-complete problem (dangling link).

## see also

- [[np-complexity-class]] · [[np-hard]] · [[p-complexity-class]] · [[decision-problem]]

<!-- footer -->

---

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
