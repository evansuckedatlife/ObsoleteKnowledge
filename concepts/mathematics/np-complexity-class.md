---
type: term
category: mathematics
defines:
  - NP
  - NP (complexity class)
  - Nondeterministic polynomial time
related:
  - "[[p-complexity-class]]"
  - "[[np-complete]]"
  - "[[np-hard]]"
  - "[[decision-problem]]"
  - "[[time-complexity]]"
lists: []
read: true
---

# NP (Complexity Class)

## summary

**NP** (nondeterministic polynomial time) is the complexity class of decision problems whose proposed solutions can be *verified* in polynomial time, even if finding those solutions may be computationally hard. Formally, it is the set of languages decidable by a nondeterministic Turing machine in polynomial time. **NP** contains **P** and is the core of the **P vs. NP** problem—the distinction between "verifiable in polynomial time" and "solvable in polynomial time" remains one of mathematics' greatest unsolved mysteries and has profound implications for cryptography, optimization, and computational theory.

## you gotta know

### Definition and Characterization
- **NP** stands for "nondeterministic polynomial time"; a problem is in **NP** if a proposed solution (a certificate or witness) can be *verified* in polynomial time `O(n^k)`.
- *Verification-based definition*: a problem *L* is in **NP** if there exists a polynomial-time verifier *V* and a polynomial *p* such that for each input *x*: *x* ∈ *L* ⟺ there exists a certificate *c* of length ≤ *p*(|*x*|) where *V*(*x*, *c*) = "yes".
- *Nondeterministic Turing machine definition*: a problem is in **NP** if a nondeterministic Turing machine can decide it in polynomial time (i.e., guess a certificate and verify it).
- *Asymmetry*: **NP** is about verification, not solution-finding; a problem can be in **NP** even if no known polynomial-time algorithm finds the solution.

### Examples of **NP** Problems
- *Travelling Salesman Problem (TSP)*: given cities and distances, is there a tour visiting all cities with total distance ≤ *k*? Verifying a proposed tour takes O(*n*) time.
- *Boolean Satisfiability (SAT)*: given a logical formula, is there an assignment of variables making it true? Verifying a proposed assignment takes O(*n*) time.
- *Clique Problem*: does a graph contain a clique (complete subgraph) of size ≥ *k*? Verifying a proposed clique takes O(*k*²) time.
- *Subset Sum*: given integers, is there a subset summing to a target value? Verifying a proposed subset takes O(*n*) time.
- *Integer Factorization*: given *n*, is there a factor in a range [*a*, *b*]? Verifying a proposed factor takes O(log *n*) time.
- *Graph Coloring*: can a graph be colored with ≤ *k* colors such that no adjacent vertices share a color? Verifying a coloring takes O(*m*) time (where *m* is the number of edges).

### Relationship to Other Complexity Classes
- **P ⊆ NP** (proven): every problem solvable in polynomial time can also be verified in polynomial time; simply ignore the certificate and solve it deterministically.
- **NP ⊆ PSPACE** (proven): NP problems are solvable in polynomial space (though potentially exponential time).
- **NP vs. P** is open: it is unknown whether **P = NP**; intuitively, finding a solution seems harder than verifying it, but this remains unproven.
- **NP vs. PSPACE**: it is unknown whether **NP = PSPACE**, though this is generally believed to be false.

### **NP**-Complete and Hardness
- **NP-complete** problems are the hardest in **NP**: every problem in **NP** reduces to them in polynomial time.
- *Examples*: SAT, TSP, Clique, Subset Sum, 3-Coloring, Hamiltonian Cycle, Knapsack.
- *Significance*: if any **NP**-complete problem is in **P**, then **P = NP** (all **NP** problems are solvable in polynomial time). Conversely, if any is not in **P**, then **P ≠ NP**.
- *Current state*: thousands of real-world problems are **NP**-complete; no polynomial-time algorithm for any is known, and they are widely believed to be intractable.

## context

**NP** captures a fundamental aspect of computational difficulty: the ease of verifying a claimed solution versus the hardness of finding it. This asymmetry underlies cryptography (hashing, digital signatures, proof-of-work): one-way functions are believed to exist because verifying a solution is easy but finding it is hard. Practically, **NP** encompasses many real-world optimization problems (scheduling, planning, combinatorial design), which are attacked via heuristics (greedy algorithms, genetic algorithms, simulated annealing) because exact solutions are believed to be intractable. The **P vs. NP** problem is the Millennium Prize Problem, one of seven offered by the Clay Mathematics Institute; solving it would resolve fundamental questions about the nature of computation and have immediate applications to cryptography and optimization. In quiz bowl, **NP** appears in contexts of complexity theory, **NP**-completeness, the **P vs. NP** problem, and specific hard problems.

## connections

- [[p-complexity-class]] — the subset of **NP** of polynomial-time *solvable* problems; whether they are equal is open.
- [[np-complete]] — the hardest problems in **NP**; if any is in **P**, then **P = NP**.
- [[np-hard]] — problems at least as hard as **NP**-complete; need not be in **NP** themselves.
- [[decision-problem]] — **NP** is defined for decision problems (yes/no answers).
- [[turing-machine]] — **NP** is formally defined using nondeterministic Turing machines and polynomial-time verification.
- [[cryptography]] — depends on the assumption that certain problems are in **NP** but not in **P** (e.g., factorization).
- [[pspace-complexity-class]] — contains **NP**; encompasses problems solvable in polynomial space.
- [[cook-karp-theorem]] — established NP-completeness and the existence of NP-complete problems.

## see also

- [[p-complexity-class]] · [[np-complete]] · [[np-hard]] · [[decision-problem]]

<!-- footer -->

---

Lists:  · Mark read: `INPUT[toggle:read]`
