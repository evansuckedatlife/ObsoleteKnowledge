---
type: term
category: mathematics
defines:
  - P
  - "P (complexity class)"
  - Polynomial time
related:
  - "[[np-complexity-class]]"
  - "[[np-complete]]"
  - "[[decision-problem]]"
  - "[[time-complexity]]"
lists:
  - "[[computation-types]]"
read: false
---

# P (Complexity Class)

## summary

**P** is the complexity class of decision problems solvable in polynomial time—that is, by a deterministic algorithm in a number of steps bounded by a polynomial function of the input size. It represents the realm of computationally *feasible* problems and forms the basis for asking whether **P = NP**, one of computer science's deepest open questions.

## you gotta know

- **P** stands for "polynomial time"; a problem is in **P** if a deterministic Turing machine can solve it in `O(n^k)` steps for some fixed constant `k`.
- Includes common algorithmic problems: sorting, searching, graph reachability, primality testing (via AKS), and integer multiplication.
- The practical boundary: problems in **P** are considered computationally tractable; problems outside it are generally infeasible for large inputs.
- Defined formally as the set of languages decidable by a deterministic Turing machine in polynomial time.
- **P ⊆ NP** (a proven fact): every polynomial-time solvable problem is also polynomial-time verifiable.
- **P vs. NP** is the Millennium Prize Problem—if **P = NP**, then every NP problem would be solvable in polynomial time, upending cryptography and optimization.
- All NP-complete problems would be solvable in polynomial time *if* **P = NP**, but none are known to be.

## connections

- [[np-complexity-class]] — the larger class that includes **P**; whether they are equal is open.
- [[np-complete]] — problems that are NP-hard and in NP; if any is in P, then P = NP.
- [[decision-problem]] — **P** is defined for decision problems (yes/no answers).
- [[time-complexity]] — **P** is a classification by time complexity polynomial in input size.
- [[turing-machine]] — **P** is formally defined using deterministic Turing machines.

## see also

- [[np-complexity-class]] · [[np-complete]] · [[np-hard]] · [[decision-problem]]

<!-- footer -->

---

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
