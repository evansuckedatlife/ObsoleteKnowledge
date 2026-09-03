---
type: concept
category: mathematics
defines: [Boolean satisfiability, SAT, propositional satisfiability]
related: ["[[p-vs-np-problem]]", "[[np-complexity-class]]", "[[p-complexity-class]]", "[[decision-problem]]", "[[turing-machine]]", "[[big-o-notation]]"]
requires: ["[[decision-problem]]", "[[np-complexity-class]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Boolean satisfiability

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Boolean satisfiability**, commonly designated as **SAT** or **propositional satisfiability**, is the fundamental computational [[decision-problem]] of determining whether there exists an assignment of truth values to propositional variables that renders a given Boolean formula true. Formulated in the mathematical framework of classical logic, it achieved historic prominence in theoretical computer science when the *Cook-Levin theorem* proved it to be the first rigorously demonstrated NP-complete problem in the early 1970s. The question of whether an efficient algorithm exists to solve it remains the central unsolved mystery of computational complexity theory, as resolving it is mathematically equivalent to settling the legendary [[p-vs-np-problem]].

## you gotta know

- Formally proved to be the archetypal NP-complete problem via the *Cook-Levin theorem*, established independently by *Stephen Cook* in the [[united-states]] in 1971 and *Leonid Levin* in the [[soviet-union]] in 1973.
- Asks whether the atomic variables in a propositional logic formula can be consistently assigned truth values of *true* or *false* in such a way that the entire compound expression evaluates to true.
- Served as the universal starting problem for *Richard Karp*'s seminal 1972 paper, which employed polynomial-time reductions from it to prove that twenty-one diverse combinatorial and graph-theoretic problems are likewise NP-complete.
- Customarily analyzed in conjunctive normal form (CNF) as a conjunction of clauses, where structural constraints establish a sharp complexity divide: *2-SAT* is solvable in linear time within the [[p-complexity-class]], whereas *3-SAT* is NP-complete.
- Demonstrates a stark contrast between worst-case theoretical intractability and empirical performance, as modern *SAT solvers* utilizing the *DPLL algorithm* (*Davis-Putnam-Logemann-Loveland*) and conflict-driven clause learning efficiently resolve industrial instances with millions of variables.
- Forms the foundation of the *exponential time hypothesis*, a major conjecture in fine-grained complexity positing that *3-SAT* cannot be solved by any algorithm running in subexponential time relative to the number of variables.
- Extends naturally to the *quantified Boolean formula problem* (QBF), which incorporates both universal and existential quantifiers over propositional variables, elevating the computational complexity from the [[np-complexity-class]] to become the canonical complete problem for PSPACE.
- Exhibits a mathematically intriguing phase transition phenomenon, where random *3-SAT* formulas display a sharp threshold in satisfiability probability at a clause-to-variable ratio of approximately 4.267, where empirical difficulty peaks.

## connections

- [[p-vs-np-problem]] — resolving whether a deterministic polynomial-time algorithm exists for SAT would definitively settle the premier open question in computer science.
- [[np-complexity-class]] — serves as the foundational, defining representative of NP-completeness to which all other non-deterministic polynomial-time problems can be reduced.
- [[p-complexity-class]] — delineates the frontier of tractability, as restricted variants such as *2-SAT* and *Horn-satisfiability* admit deterministic polynomial-time solutions.
- [[decision-problem]] — represents the classical yes-or-no computational query upon which modern formal complexity hierarchies and automata theory are constructed.
- [[turing-machine]] — foundational proofs encode the instantaneous configurations and transitions of a non-deterministic machine directly into the clauses of a Boolean formula.
- [[big-o-notation]] — provides the standard asymptotic mathematical language used to characterize the time complexity of exhaustive truth-table searches versus sophisticated heuristic solvers.
- [[united-states]] — location where *Stephen Cook* published his landmark 1971 paper *The Complexity of Theorem-Proving Procedures* at the *STOC* conference.
- [[soviet-union]] — nation where *Leonid Levin* independently formulated universal search problems and established the equivalence of propositional satisfiability during the early 1970s.

## see also

- [[p-vs-np-problem]] · [[np-complexity-class]] · [[p-complexity-class]] · [[decision-problem]] · [[turing-machine]]

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
