---
type: concept
category: science
defines: [Church-Turing thesis, Church's thesis]
related: ["[[computability]]", "[[turing-machine]]", "[[functional-programming]]", "[[recursion]]", "[[formal-logic]]", "[[fixed-point-combinator]]", "[[central-processing-unit]]"]
requires: ["[[algorithm]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Church-Turing Thesis

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Church-Turing thesis**, also historically referenced as **Church's thesis**, is a foundational hypothesis in theoretical computer science and mathematical logic regarding the nature of an effective [[algorithm]]. Formulated independently in 1936 by the American logician *Alonzo Church* and the British mathematician *Alan Turing*, it posits that any function intuitively calculable by an effective mechanical procedure can be computed by a [[turing-machine]] or lambda calculus. This conjecture establishes the theoretical boundary of classical calculation, equating disparate formal models of [[computability]] and asserting that no idealized mechanical apparatus possesses greater computational capability than a universal machine.

## you gotta know

- Formulated independently in 1936 by *Alonzo Church* using untyped lambda calculus and by *Alan Turing* using abstract computing machines.
- States that the informal, intuitive notion of effective calculability coincides mathematically with functions computable by a universal [[turing-machine]].
- Proved that *Church's* untyped lambda calculus and *Turing's* formulation are formally equivalent in expressive power, demonstrating that fundamentally distinct mathematical paradigms yield the exact same class of solvable problems.
- Emerged directly from efforts to resolve *David Hilbert's* *Entscheidungsproblem*, establishing that first-order [[formal-logic]] is undecidable because no general decision procedure exists.
- Remains a thesis or philosophical conjecture rather than a provable mathematical theorem, because it bridges an informal human intuition of mechanical calculation with rigorous formal models.
- Influenced the foundational design of practical programming paradigms, where the lambda calculus inspired [[functional-programming]] and the [[turing-machine]] model governed the imperative architecture of the modern [[central-processing-unit]].
- Extended to the *Physical Church-Turing thesis*, which asserts that any physical process operating under the laws of nature can be simulated algorithmically by a computing machine.
- Underpins *Markov algorithms*, *Post canonical systems*, and *partial recursive functions*, all of which were shown to be equivalent to Turing computability, reinforcing confidence in the universality of the thesis.

## connections

- [[computability]] — defines the formal study of decidable functions and computational limits governed by the thesis.
- [[turing-machine]] — provides the definitive tape-based automaton model equated to algorithmic calculability.
- [[algorithm]] — represents the intuitive concept of step-by-step calculation formalized by the conjecture.
- [[functional-programming]] — implements declarative computation derived from *Alonzo Church's* lambda calculus.
- [[recursion]] — forms the basis of general recursive functions shown to be equivalent to Turing computability.
- [[formal-logic]] — provides the theoretical framework within which *Hilbert's* decision problem was addressed.
- [[central-processing-unit]] — realizes physical implementations of the computational equivalence established by the thesis.

## see also

- [[computability]] · [[turing-machine]] · [[algorithm]] · [[formal-logic]]

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
