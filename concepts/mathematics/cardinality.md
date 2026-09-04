---
type: concept
category: mathematics
defines: [cardinality, set size, transfinite cardinal]
related: ["[[injective]]", "[[surjective]]", "[[inverse-function]]", "[[symmetric-group]]", "[[composite-function]]", "[[decision-problem]]", "[[turing-machine]]"]
requires: ["[[number-theory]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Cardinality

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

In set theory and foundational mathematics, **cardinality** is the formal measure of the size or number of elements in a set. Developed primarily by *Georg Cantor* in the late nineteenth century in *Germany*, the concept revolutionized mathematical logic by demonstrating that infinite collections can possess distinct, strictly unequal magnitudes. Today, understanding transfinite sizes is fundamental across pure mathematics, theoretical computer science, and logic.

## you gotta know

- Two sets share the same size if and only if there exists a bijective correspondence between their elements, meaning each element pairs uniquely with one from the other.
- Countably infinite collections match the size of the natural numbers, denoted by the Hebrew symbol aleph-null ($\aleph_0$).
- *Cantor's diagonal argument* proved that the real numbers are uncountably infinite, establishing that the continuum strictly exceeds the size of the counting numbers.
- *Cantor's theorem* states that every set has a strictly smaller size than its power set, implying an endless hierarchy of ever-larger infinities.
- The *continuum hypothesis* proposes that no intermediate infinite size exists between the integers and the real numbers; *Kurt Gödel* and *Paul Cohen* proved it independent of standard *Zermelo–Fraenkel* set theory.
- The *Schröder–Bernstein theorem* guarantees that if two sets admit injective mappings into each other, an invertible bijection exists between them.
- Operations on infinite cardinal numbers generalize everyday addition, multiplication, and exponentiation, where cardinal exponentiation $2^\kappa$ describes the magnitude of power sets.

## connections

- [[composite-function]] — invertible bijections whose associative compositions verify equinumerosity between sets.
- [[number-theory]] — provides the baseline infinite collection of counting numbers whose size defines aleph-null.
- [[turing-machine]] — models of computation whose countable collection explains why uncountably many real problems remain uncomputable.
- [[decision-problem]] — questions whose unsolvability follows directly from comparing countable programs against uncountable languages.
- [[euclid]] — ancient pioneer of deductive geometry whose classical axioms assumed whole magnitudes always exceed their proper parts.
- [[p-vs-np-problem]] — foundational theoretical question regarding whether polynomial verification implies polynomial solvability across finite structures.

## see also

- [[composite-function]] · [[clock-arithmetic]] · [[decision-problem]]

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
