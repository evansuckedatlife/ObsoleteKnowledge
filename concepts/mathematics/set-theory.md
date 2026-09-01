---
type: concept
category: mathematics
defines: [Set Theory, Set-theoretic]
related: ["[[topology]]", "[[bertrand-russell]]", "[[kurt-godel]]"]
requires: ["[[limit]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Set Theory

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Set theory** is the branch of mathematics that studies collections of objects called sets, their properties, and operations. Since the late 19th century, it has served as the foundational language for nearly all of mathematics. Set theory deals with membership, union, intersection, power sets, and the axiomatic principles that prevent logical paradoxes.

## you gotta know

- A *set* is defined by its members; two sets are equal if they have exactly the same members (the axiom of extensionality); membership is denoted ∈.
- *Russell's paradox* (1901): consider the set *R* = {*x* : *x* ∉ *x*}; does *R* ∈ *R*? Both yes and no lead to contradiction; exposed naive set theory's inconsistency.
- Paradox prompted the *ZFC axioms* (Zermelo-Fraenkel + Choice): a rigorous axiomatic system avoiding paradoxes through careful restriction on set formation; the standard foundation for mathematics.
- *Cardinality* compares sizes of sets via bijections; ℕ and ℚ are countably infinite; ℝ is uncountably infinite (Cantor proved no bijection between them).
- *Power set* *P*(*S*) of a set *S* is the set of all subsets; Cantor's theorem: card(*P*(*S*)) > card(*S*) for any set, creating an infinite hierarchy of infinities.
- The *axiom of choice* (independent of ZF): given any collection of nonempty sets, we can simultaneously select one element from each; equivalent to Zorn's lemma and well-ordering principle.
- Set theory provides rigorous underpinnings for topology (open sets), analysis (limits, continuity), functions, relations, and abstract algebra; nearly all modern mathematics is formalized set-theoretically.
- *Transfinite numbers* and ordinal arithmetic extend the concept of number beyond finite quantities; the first infinite ordinal ω represents the ordering of natural numbers.
- *Foundations of mathematics*: Gödel's incompleteness theorems showed that no consistent axiomatic system (including ZFC) can prove all truths about sets; profound implications for mathematical certainty.

## connections

- [[topology]] — defined in the language of sets; open and closed sets are fundamental topological objects.
- [[bertrand-russell]] — his paradox revealed the need for axiomatic care in set theory.
- [[kurt-godel]] — proved deep results about the completeness and consistency limits of formal systems based on set theory.
- [[limit]] — defined rigorously using sets and membership, core to analysis.
- [[continuous-functions]] — defined via set-theoretic notions of open preimages.

## see also

[[topology]] · [[bertrand-russell]] · [[kurt-godel]] · [[continuous-functions]]

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
