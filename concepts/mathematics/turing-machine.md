---
type: term
category: mathematics
defines:
  - "Turing machine"
  - "Turing machine"
  - "Deterministic Turing machine"
  - "Nondeterministic Turing machine"
related:
  - "[[p-complexity-class]]"
  - "[[np-complexity-class]]"
  - "[[halting-problem]]"
  - "[[time-complexity]]"
lists: []
read: false
---

# Turing Machine

## summary

A **Turing machine** is an abstract mathematical model of computation introduced by Alan Turing in 1936 that consists of an infinite tape, a read-write head, and a finite set of states. It is the foundational model for analyzing what problems are computable, and all major complexity classes (**P**, **NP**) are defined in terms of Turing machines.

## you gotta know

- **Deterministic Turing machine**: a single tape, a read-write head, and a state transition table that uniquely determines the next action from the current state and symbol.
- **Nondeterministic Turing machine**: at each step, the machine may follow one of several possible transitions; it accepts an input if *any* path leads to acceptance.
- Turing proved that no algorithm can decide whether an arbitrary Turing machine halts on a given input—the **Halting Problem** is undecidable.
- **Church-Turing thesis** (1936): every effectively computable function can be computed by a Turing machine; it is the standard model of computational universality.
- Despite simplicity, Turing machines are computationally universal: any algorithm on any real computer can be simulated by a Turing machine (within a polynomial factor for deterministic machines).
- **P** = problems decidable by a deterministic Turing machine in polynomial time; **NP** = problems decidable by a nondeterministic Turing machine in polynomial time.
- The tape is infinite (unlimited memory), but most real complexity analysis bounds both time and space.

## connections

- [[p-complexity-class]] — **P** is formally defined as deterministic Turing machine polynomial-time decidable.
- [[np-complexity-class]] — **NP** is formally defined as nondeterministic Turing machine polynomial-time decidable.
- [[halting-problem]] — proved undecidable (no Turing machine solves it), showing computation has limits.
- [[time-complexity]] — Turing machines are the standard reference for measuring time and space.
- [[decision-problem]] — Turing machines decide languages (decision problems).

## see also

- [[p-complexity-class]] · [[np-complexity-class]] · [[halting-problem]] · [[time-complexity]]

<!-- footer -->

---

Lists:  · Mark read: `INPUT[toggle:read]`
