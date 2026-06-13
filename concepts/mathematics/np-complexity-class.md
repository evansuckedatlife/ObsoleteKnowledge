---
type: term
category: mathematics
defines:
  - NP
  - "NP (complexity class)"
  - "Nondeterministic polynomial time"
related:
  - "[[p-complexity-class]]"
  - "[[np-complete]]"
  - "[[np-hard]]"
  - "[[decision-problem]]"
  - "[[time-complexity]]"
lists:
  - "[[computation-types]]"
read: false
---

# NP (Complexity Class)

## summary

**NP** is the complexity class of decision problems whose solutions can be *verified* in polynomial time, even if finding them may be hard. Formally, it is the set of languages decidable by a nondeterministic Turing machine in polynomial time, and it is the central class in the **P vs. NP** problem.

## you gotta know

- **NP** stands for "nondeterministic polynomial time"; a problem is in **NP** if a proposed solution can be checked in `O(n^k)` steps.
- A problem can be in **NP** without being in **P**—knowing a solution is right does not mean finding one is quick.
- Includes the Travelling Salesman Problem, Boolean Satisfiability (**SAT**), the Clique Problem, and integer factorization.
- **P ⊆ NP** (proven): every polynomial-time solvable problem is polynomial-time verifiable, since solving also verifies.
- **NP ⊆ PSPACE** (proven): NP problems are solvable with polynomial space, though possibly requiring exponential time.
- The unknown question: **does P = NP?** If yes, then every verifiable problem is solvable in polynomial time; the answer would overturn cryptography as we know it.
- Contains the **NP-complete** problems, the hardest problems in NP, as a subclass.

## connections

- [[p-complexity-class]] — the subset of **NP** of polynomial-time *solvable* problems; equality is open.
- [[np-complete]] — the hardest problems in **NP**; if any is in **P**, then **P = NP**.
- [[np-hard]] — problems at least as hard as the hardest **NP** problems; need not be in **NP** themselves.
- [[decision-problem]] — **NP** is defined for decision problems (yes/no answers).
- [[turing-machine]] — **NP** is formally defined using nondeterministic Turing machines.

## see also

- [[p-complexity-class]] · [[np-complete]] · [[np-hard]] · [[decision-problem]]

<!-- footer -->

---

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
