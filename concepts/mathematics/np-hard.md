---
type: term
category: mathematics
defines:
  - NP-hard
  - NP-hard problem
related:
  - "[[np-complete]]"
  - "[[np-complexity-class]]"
  - "[[decision-problem]]"
  - "[[optimization-problem]]"
lists: []
read: true
---

# NP-Hard

## summary

**NP-hard** problems are at least as computationally hard as the hardest problems in **NP**, defined by the property that every problem in **NP** can be *reduced* to them in polynomial time. Unlike **NP-complete**, an NP-hard problem need not be in **NP** itself or even be a decision problem—it represents the upper bound of difficulty for NP-reducible problems.

## you gotta know

- A problem is **NP-hard** if every **NP** problem can be reduced to it in polynomial time; intuitively, it is at least as hard as any **NP** problem.
- **NP-complete = NP-hard ∩ NP**: NP-hard problems that are also verifiable in polynomial time are exactly the NP-complete problems.
- **NP-hard** problems may be *outside* **NP**: they could be undecidable (like the Halting Problem), or they could be decision problems outside **NP**—either way, solving them in polynomial time would solve all NP problems.
- Examples of NP-hard problems: Travelling Salesman Problem (decision and optimization versions), Longest Path, Steiner Tree, Bin Packing, Graph Coloring (general k).
- If a polynomial-time algorithm is found for an NP-hard problem, then **P = NP** (because NP-complete problems would be in **P**).
- Common technique: to prove a problem is NP-hard, reduce a known NP-complete problem to it in polynomial time.

## connections

- [[np-complete]] — NP-complete problems are the intersection of NP-hard and NP.
- [[np-complexity-class]] — defines the scope of NP problems that reduce to NP-hard ones.
- [[p-complexity-class]] — if any NP-hard problem is in **P**, then **P = NP**.
- [[optimization-problem]] — many NP-hard problems are optimization (not decision) problems.
- [[decision-problem]] — some NP-hard problems are decision problems.

## see also

- [[np-complete]] · [[np-complexity-class]] · [[p-complexity-class]] · [[optimization-problem]]

<!-- footer -->

---

Lists:  · Mark read: `INPUT[toggle:read]`
