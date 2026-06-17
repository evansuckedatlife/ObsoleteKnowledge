---
type: term
category: mathematics
defines: ["Halting Problem"]
related: ["[[turing-machine]]", "[[p-complexity-class]]", "[[p-vs-np-problem]]"]
requires: []
lists:
  - "[[computation-types]]"
tour_order: 0
read: false
---

# Halting Problem

## summary

The Halting Problem is a fundamental decision problem in computability theory that asks whether an arbitrary computer program, given a specific input, will eventually finish running (halt) or continue to run forever. In 1936, Alan Turing famously proved that no general algorithm can exist that solves the halting problem for all possible program-input pairs. This landmark result established that the halting problem is undecidable, revealing the first mathematical proof of a fundamental, absolute limitation on the power of computers. It represents a cornerstone of computer science and complexity theory, defining the boundary of what can and cannot be computed.

## you gotta know

### problem statement & definition

- *Definition*: Given a description of an arbitrary computer program (Turing machine $M$) and an input $w$, determine whether $M$ eventually halts when run with input $w$, or runs indefinitely.
- *Decision Problem Status*: It is a decision problem with a binary (yes/no) output, formally defined as the language $H = \{\langle M, w \rangle \mid M \text{ is a Turing machine that halts on input } w\}$.
- *Undecidability*: The problem is undecidable (non-recursive), meaning no Turing machine can solve it for all inputs; however, it is Turing-recognizable (recursively enumerable), as one can simply simulate the program (though this will not terminate if the program loops).

### proof technique & consequences

- *Diagonalization*: Turing's proof utilizes a proof by contradiction using Cantor's diagonalization method; it constructs a machine $D$ that takes a program description $P$ as input, simulates $P$ on its own description, and does the opposite of what a hypothetical halting-decider $H$ predicts.
- *Self-Reference Paradox*: If the decider $H$ says $D(D)$ halts, $D(D)$ loops; if $H$ says $D(D)$ loops, $D(D)$ halts, creating a logical contradiction that proves $H$ cannot exist.
- *Reductions*: The halting problem is the standard starting point for proving other problems undecidable through *reduction*; if a problem $A$ could be decided, we could use that decider to solve the halting problem, which is impossible.

### extensions & practical impact

- *Rice's Theorem*: A generalization of the halting problem which states that any non-trivial semantic property of a Turing machine (e.g., "does this program print the number 5?") is undecidable.
- *Practical Impossibility*: Debuggers, compilers, and static analysis tools cannot perfectly detect infinite loops or verify program correctness for all programs; they must rely on timeouts, heuristics, or restricted languages.
- *Entscheidungsproblem*: Turing's proof of the undecidability of the halting problem resolved David Hilbert's decision problem, showing that there is no universal decision procedure for first-order logic.

## connections

- [[turing-machine]] — the halting problem is defined using Turing machines as the model of computation.
- [[p-complexity-class]] — the complexity class P contains decidable problems; halting is strictly undecidable.
- [[p-vs-np-problem]] — P vs NP deals with the efficiency of decidable problems; halting lies outside all complexity classes.
- [[kurt-godel]] — proved the Incompleteness Theorems, which are closely linked to the undecidability of halting.
- [[traveling-salesman-problem]] — an NP-hard problem that is decidable, unlike the undecidable halting problem.
- [[sorting-algorithms]] — concrete algorithms whose termination is provable, contrasting with the undecidability of halting.

## context

The Halting Problem is the quintessential example of an undecidable problem in computer science. Written by Alan Turing in his historic 1936 paper "On Computable Numbers, with an Application to the Entscheidungsproblem," it introduced the theoretical concept of the Universal Turing Machine alongside the proof of its own limits. In quiz bowl, the halting problem is a staple, frequently clued by the mechanics of its diagonalization proof, its equivalence to the Entscheidungsproblem, its relation to Rice's Theorem, or its status as a recursively enumerable but not recursive language.

## see also

- [[turing-machine]] · [[p-complexity-class]] · [[p-vs-np-problem]] · [[traveling-salesman-problem]]

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

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
