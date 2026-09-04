---
type: concept
category: mathematics
defines: [Computational Complexity, Complexity Theory, Computational Complexity Theory]
related: ["[[turing-machine]]", "[[decision-problem]]", "[[p-vs-np-problem]]", "[[p-complexity-class]]", "[[np-complexity-class]]", "[[big-o-notation]]", "[[congruence]]"]
requires: ["[[turing-machine]]", "[[decision-problem]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Computational Complexity

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Computational complexity** is the subfield of theoretical computer science and mathematics that classifies computational problems according to the inherent resources required to solve them. Formalized during the mid-twentieth century through the work of *Alan Turing*, *Juris Hartmanis*, and *Richard Stearns*, the field models computation using abstract automata to measure execution time, memory footprint, and circuit depth. Its central pursuit is establishing formal boundaries between tractable and intractable problems, most famously epitomized by the unresolved status of the *P versus NP* question.

## you gotta know

- The central open problem in the discipline is the [[p-vs-np-problem]], which asks whether every problem whose solution can be verified in polynomial time can also be solved in polynomial time.
- Time and space consumption are mathematically characterized as asymptotic functions of input length using [[big-o-notation]], abstracting away specific hardware architectures.
- The foundation of formal classification rests upon the abstract [[turing-machine]], introduced in 1936, which provides standard metrics such as deterministic time, non-deterministic time, and logarithmic space.
- Problems are grouped into fundamental complexity classes such as the [[p-complexity-class]] for efficient deterministic algorithms and the [[np-complexity-class]] for non-deterministic verifiability.
- *Stephen Cook* and *Leonid Levin* independently proved that the boolean satisfiability problem is *NP-complete*, establishing polynomial-time reductions as the primary technique for proving intractability.
- *Richard Karp* expanded this foundation in 1972 by demonstrating twenty-one diverse combinatorial problems to be *NP-complete*, including clique, Hamiltonian cycle, and vertex cover.
- Modern cryptographic protocols rely directly on computational asymmetry, where algorithms built on [[congruence]] and modular arithmetic assume that factoring large integers cannot be achieved in polynomial time.
- The time and space hierarchy theorems establish that granting strictly larger asymptotic resource bounds guarantees the existence of strictly harder decidable problems.

## connections

- [[p-vs-np-problem]] — the foundational unsolved problem concerning the equivalence of efficient search and efficient verification.
- [[turing-machine]] — the universal mathematical abstraction of computation that serves as the reference architecture for resource bounds.
- [[decision-problem]] — the standard formalization of computational tasks framed as formal language membership queries.
- [[p-complexity-class]] — the complexity class capturing problems solvable deterministically in polynomial time.
- [[np-complexity-class]] — the class of languages verifiable in polynomial time by a deterministic automaton.
- [[big-o-notation]] — the essential analytical calculus used to describe limiting algorithmic behavior and machine bounds.
- [[congruence]] — number-theoretic relation underpinning asymmetric cryptography, whose security presupposes the computational hardness of discrete logarithms and integer factorization.

## see also

- [[p-vs-np-problem]] · [[p-complexity-class]] · [[np-complexity-class]] · [[turing-machine]] · [[decision-problem]]

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

Lists: [[mathematics-hubs]] · Mark read: `INPUT[toggle:read]`
