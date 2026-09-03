---
type: concept
category: mathematics
defines: [Russell's Paradox, Bertrand Russell's Paradox]
related: ["[[decision-problem]]", "[[turing-machine]]", "[[number-theory]]", "[[england]]", "[[germany]]", "[[linguistics]]", "[[modernism]]"]
requires: ["[[number-theory]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Russell's Paradox

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Russell's paradox** (also known as **Bertrand Russell's paradox**) is an essential contradiction within naive set theory discovered in 1901 by the British philosopher and mathematician *Bertrand Russell* in *[[england]]*. The paradox investigates the set of all sets that do not contain themselves, demonstrating that any such entity must contain itself if and only if it does not contain itself. Initially uncovered while analyzing *Gottlob Frege's* formal attempt to derive arithmetic and [[number-theory]] from pure logic, the paradox dismantled early logicist foundations and prompted the formulation of modern axiomatic set theory and formal type systems.

## you gotta know

- Formulated formally by defining the set of all sets that are not members of themselves, producing the inescapable logical contradiction that the set belongs to itself if and only if it does not belong to itself.
- Popularized intuitively as the *barber paradox*, which describes an isolated town where a male barber shaves all men, and only those men, who do not shave themselves, meaning the barber shaves himself if and only if he does not shave himself.
- Delivered in a famous 1902 correspondence to German logician *Gottlob Frege*, arriving just as the second volume of *Frege's* foundational treatise *Grundgesetze der Arithmetik* went to press, causing *Frege* to append an acknowledged surrender of his logical system.
- Demolished the unrestricted comprehension axiom of early naive set theory, which had previously assumed that any well-formed condition or predicate unconditionally defines a valid mathematical set.
- Motivated *Bertrand Russell* and *Alfred North Whitehead* to spend a decade composing *Principia Mathematica*, introducing the ramified theory of types to stratify sets into strict hierarchical levels where a set can only contain elements of lower types.
- Prompted *Ernst Zermelo*—who had independently identified the contradiction in *[[germany]]* around 1900—and *Adolf Fraenkel* to establish Zermelo-Fraenkel set theory, restricting set comprehension through the axiom of specification to forbid self-containing collections.
- Served as the conceptual ancestor for diagonal arguments in twentieth-century theoretical computer science, directly influencing *Kurt Gödel's* incompleteness theorems and *Alan Turing's* proof of the undecidability of the [[decision-problem]] using the [[turing-machine]].

## connections

- [[decision-problem]] — classical challenge concerning mechanical decidability whose negative resolution relies on diagonal self-referential paradoxes directly descended from Russell's construction.
- [[turing-machine]] — foundational computational model used to demonstrate the halting problem, which mirrors Russell's paradox through algorithmic self-application.
- [[number-theory]] — mathematical branch whose logicist grounding was disrupted when the set-theoretic axioms supporting arithmetic were shown to be internally inconsistent.
- [[england]] — country where Russell devised the paradox while working at Trinity College, Cambridge, and composing *The Principles of Mathematics*.
- [[germany]] — philosophical home of Frege and Zermelo, who grappled with the contradiction and spearheaded the structural reconstruction of formal mathematics.
- [[linguistics]] — field fundamentally reshaped by Russell's subsequent work on semantic ambiguity, reference, and the philosophy of language.
- [[modernism]] — broader twentieth-century cultural and intellectual movement characterized by profound skepticism toward absolute foundational systems.

## see also

- [[decision-problem]] · [[turing-machine]] · [[number-theory]]

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
