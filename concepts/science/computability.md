---
type: concept
category: science
defines: [computability, computability theory, recursion theory]
related: ["[[church-turing-thesis]]", "[[turing-machine]]", "[[functional-programming]]", "[[recursion]]", "[[formal-logic]]", "[[algorithm]]", "[[central-processing-unit]]"]
requires: ["[[algorithm]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Computability

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Computability**, studied systematically as **computability theory** or historically as **recursion theory**, is a core branch of mathematical logic and theoretical computer science concerned with identifying which problems can be resolved using an effective [[algorithm]]. Originating in the 1930s through the work of *Kurt Gödel*, *Alonzo Church*, *Alan Turing*, and *Emil Post*, the field categorizes mathematical functions into those that are mechanically decidable and those that are intrinsically undecidable. Understanding these fundamental limits prevents computer scientists from pursuing impossible procedures and clarifies what physical hardware can achieve.

## you gotta know

- Originated during the 1930s crisis in the foundations of mathematics, spurred by *Kurt Gödel's* incompleteness theorems and the formalization of recursive functions.
- Centered on the boundary between decidable languages, where an [[algorithm]] halts with an answer for every input, and undecidable problems, where no universal halting algorithm can exist.
- Illustrated most famously by the *Halting Problem*, wherein *Alan Turing* proved via a diagonal argument that no general algorithm can decide whether an arbitrary program will eventually terminate.
- Classifies non-computable sets using *Turing degrees*, a hierarchy that measures relative algorithmic unsolvability and degrees of algorithmic information.
- Defined by *Rice's Theorem*, which states that every non-trivial semantic property of a partial computable function is undecidable.
- Uses *Arithmetical Hierarchy* classifications to sort logical assertions into levels of alternating existential and universal quantifiers based on their relative difficulty.
- Employs *Post's problem*, which questioned whether intermediate degrees of unsolvability exist between computable sets and the halting problem, resolved affirmatively by *Albert Muchnik* and *Richard Friedberg*.
- Connects directly to hardware engineering by establishing that no physical [[central-processing-unit]], regardless of architecture or clock rate, can circumvent theoretical undecidability.

## connections

- [[church-turing-thesis]] — establishes the foundational equivalence between distinct models defining computable functions.
- [[turing-machine]] — serves as the standard theoretical automaton used to formalize decision procedures and undecidability.
- [[algorithm]] — denotes the mechanical recipe whose inherent limitations are mapped by the theory.
- [[recursion]] — provides the primary mathematical mechanism for defining primitive and general recursive functions.
- [[formal-logic]] — supplies the formal axiomatic systems whose limitations are exposed by undecidability proofs.
- [[functional-programming]] — relies on computational models proven equivalent to general recursion for evaluating expressions.
- [[central-processing-unit]] — implements the finite physical approximations of universal computation bounded by computability limits.

## see also

- [[church-turing-thesis]] · [[turing-machine]] · [[algorithm]] · [[recursion]]

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

Lists: [[science-hubs]] · Mark read: `INPUT[toggle:read]`
