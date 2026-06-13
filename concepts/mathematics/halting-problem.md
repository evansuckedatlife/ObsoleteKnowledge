---
type: term
category: mathematics
defines:
  - "Halting problem"
  - Halting problem
related:
  - "[[turing-machine]]"
  - "[[undecidable-problem]]"
lists:
  - "[[computation-types]]"
read: false
---

# Halting Problem

## summary

The **Halting Problem** asks: given an arbitrary algorithm and an input, will the algorithm terminate or loop forever? Turing proved in 1936 that no algorithm can solve this problem for all cases—it is *undecidable*, establishing a fundamental limit of computation.

## you gotta know

- **The problem**: determine whether a given Turing machine with a given input will halt (terminate) or run forever.
- **Turing's proof** uses *reductio ad absurdum*: assume a halting-decider exists, then construct a self-referential machine that contradicts itself—hence no halting-decider can exist.
- The Halting Problem is *undecidable*: no algorithm can solve it for all inputs; some Turing machines will loop detecting halting behavior.
- **Unsolvability does not mean unprovability**: for specific machines we can often prove halting (by induction or measure arguments); undecidability means there is no universal procedure.
- Practical consequence: debuggers, static analysis, and verification tools cannot fully solve halting either—they must use heuristics, timeouts, or restrict the class of programs.
- Closely related: Rice's Theorem states that no nontrivial property of Turing machines is decidable (undecidability generalizes beyond halting).
- Establishes that computation has intrinsic limits—not all mathematical questions can be answered algorithmically.

## connections

- [[turing-machine]] — the Halting Problem is defined for Turing machines; its undecidability bounds their power.
- [[p-complexity-class]] — **P** contains decidable problems; the Halting Problem is outside all complexity classes because it is undecidable.
- [[np-complexity-class]] — **NP** contains decidable problems; undecidable problems are strictly beyond **NP**.

## see also

- [[turing-machine]] · [[p-complexity-class]] · [[np-complexity-class]]

<!-- footer -->

---

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
