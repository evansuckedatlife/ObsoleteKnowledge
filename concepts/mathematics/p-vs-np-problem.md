---
type: concept
category: mathematics
defines: ["P vs NP Problem", "P vs NP", "P versus NP"]
related:
  - "[[turing-machine]]"
  - "[[halting-problem]]"
  - "[[traveling-salesman-problem]]"
  - "[[knapsack-problem]]"
lists:
  - "[[computation-types]]"
read: false
---

# P vs NP Problem

## summary

The P vs NP problem is a major unsolved question in theoretical computer science and mathematics that asks whether every computational problem whose solution can be quickly verified (in polynomial time) can also be solved quickly (in polynomial time). Formulated independently by Stephen Cook and Leonid Levin in 1971, it is widely considered the most important open question in computer science. The resolution of this question would define the fundamental limits of efficient computation and has massive implications for cryptography, optimization, and mathematics. Because of its profound significance, it was selected as one of the seven Millennium Prize Problems by the Clay Mathematics Institute.

## you gotta know

### complexity classes P and NP

- *Class P*: The class of decision problems that can be solved by a deterministic Turing machine in polynomial time (meaning the running time is bounded by $O(n^k)$ for some constant $k$ relative to input size $n$).
- *Class NP*: The class of decision problems whose positive instances ("yes" answers) can be verified by a deterministic Turing machine in polynomial time, given an appropriate proof or "certificate."
- *The Inclusion*: It is trivially true that $P \subseteq NP$ (if we can solve a problem quickly, we can verify it by just running the solver). The core question is whether $NP \subseteq P$ holds, meaning that verification and solution are computationally equivalent.

### NP-completeness & Cook-Levin Theorem

- *Cook-Levin Theorem*: This foundational theorem proved that the Boolean Satisfiability Problem (SAT) is NP-complete, meaning every other problem in NP can be reduced to it in polynomial time.
- *NP-Completeness*: A problem is NP-complete if it is in NP and is NP-hard (at least as hard as any problem in NP). If any single NP-complete problem is shown to have a polynomial-time algorithm, then $P = NP$.
- *Classic Examples*: Major NP-complete problems include the traveling salesman problem (decision version), the knapsack problem, and graph coloring.

### implications of resolution

- *Consequences of P = NP*: If the classes are equal, cryptography (including RSA and elliptic curve) would collapse because finding secret keys would be as easy as verifying them. Conversely, optimization, automated theorem proving, and machine learning would become vastly more powerful.
- *Consequences of P != NP*: If the classes are unequal, it confirms that finding solutions is inherently harder than verifying them, securing modern cryptography and validating the search for heuristic and approximation algorithms for NP-complete problems.
- *Millennium Prize*: The Clay Mathematics Institute offers a \$1 million reward for the first formal proof showing either $P = NP$ or $P \neq NP$.

## connections

- [[turing-machine]] — the computational model used to formally define the classes P and NP.
- [[halting-problem]] — represents the limit of what is decidable, while P vs NP represents the limit of what is efficiently decidable.
- [[traveling-salesman-problem]] — a classic NP-complete problem that would be solvable in polynomial time if $P = NP$.
- [[knapsack-problem]] — an NP-complete resource allocation problem that illustrates the difficulty of finding exact solutions.
- [[integer-factorization]] — a problem in NP that is not known to be in P or to be NP-complete, which forms the basis for RSA encryption.
- [[primality-testing]] — a decision problem that was long known to be in NP and was proven to be in P in 2002 via the AKS algorithm.
- [[sorting-algorithms]] — fundamental algorithms that solve problems lying comfortably within the class P.

## context

The P vs NP problem is the ultimate question of computational complexity. While early intimations of the problem appeared in letters from Kurt Gödel to John von Neumann in the 1950s, it was Cook and Levin who formalized it using polynomial-time reductions. Most computer scientists believe that $P \neq NP$ because centuries of mathematical effort have not yielded easy algorithms for hard tasks, but a formal proof is blocked by our inability to prove lower bounds on the complexity of general algorithms. In quiz bowl, the topic is frequently clued via the Cook-Levin theorem, the definition of NP-completeness, polynomial-time reductions, and the Millennium Prize.

## see also

- [[turing-machine]] · [[halting-problem]] · [[traveling-salesman-problem]] · [[knapsack-problem]] · [[integer-factorization]]

<!-- footer -->

---

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
