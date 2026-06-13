---
type: concept
category: mathematics
defines: [Bijective, bijection, "bijective function", "one-to-one correspondence"]
related: ["[[injective]]", "[[surjective]]", "[[inverse-function]]", "[[symmetric-group]]", "[[cardinality]]"]
lists: ["[[classifications-of-functions]]"]
read: false
---

# Bijective

## summary

A function is *bijective* if it is both injective (one-to-one) and surjective (onto), establishing a perfect one-to-one correspondence between the elements of two sets. This means every element in the domain maps to a unique element in the codomain, and every element in the codomain is mapped to by exactly one element in the domain. Bijections are mathematically pivotal because they are the only functions that possess a well-defined inverse function. In set theory, bijections serve as the formal foundation for defining cardinality and comparing the sizes of both finite and infinite sets.

## you gotta know

### Definition and Inverses

- A function *f* from set *A* to set *B* is bijective if for every *b* in *B*, there is exactly one *a* in *A* such that *f*(*a*) = *b*.
- A function is bijective if and only if it is *invertible*; the inverse function *f*⁻¹ exists and is also a bijection.
- On a coordinate graph, a real-valued function is bijective if it passes both the *Vertical Line Test* (making it a function) and the *Horizontal Line Test* (making it one-to-one), and its range equals its codomain.

### Set Theory and Cardinality

- Two sets *A* and *B* have the same *cardinality* (size) if and only if there exists a bijection between them.
- A set is *countably infinite* if there exists a bijection between it and the set of natural numbers $\mathbb{N}$.
- *Cantor's diagonal argument* uses bijections to show that the real numbers $\mathbb{R}$ cannot be placed in bijection with $\mathbb{N}$, proving the existence of different sizes of infinity.
- The *Schröder–Bernstein theorem* states that if there exist injective functions from *A* to *B* and from *B* to *A*, then a bijective function exists between *A* and *B*.

### Algebraic and Group Structures

- A bijection from a set *X* to itself is called a *permutation*; the set of all such bijections forms the *symmetric group* under function composition.
- In abstract algebra, an *isomorphism* is a bijective homomorphism, preserving algebraic structures between two systems.
- In topology, a *homeomorphism* is a continuous bijection with a continuous inverse, preserving topological properties.

## context

Bijections are the mathematical gold standard for equivalence, demonstrating that two structures are, for all practical purposes, identical in size or behavior. By pairing elements up without leaving any out or repeating any, bijections allow mathematicians to transport problems from difficult domains into simpler ones—such as using logarithms to turn multiplication into addition, or using Fourier transforms to analyze differential equations in frequency space. In quiz bowl, bijections appear as the condition for invertibility, the basis of Georg Cantor's transfinite cardinalities, and the defining characteristic of isomorphisms, homeomorphisms, and permutations.

## connections

- [[injective]] — a bijection must be one-to-one.
- [[surjective]] — a bijection must be onto.
- [[inverse-function]] — a function has an inverse if and only if it is bijective.
- [[cardinality]] — set sizes are compared and defined via bijections.
- [[symmetric-group]] — group of bijections from a set to itself.
- [[continuous-functions]] — continuous bijections with continuous inverses are homeomorphisms.

## see also

- [[injective]] · [[surjective]] · [[monotonic-functions]] · [[continuous-functions]] · [[analytic-functions]]

<!-- footer -->

---

Lists: [[classifications-of-functions]] · Mark read: `INPUT[toggle:read]`
