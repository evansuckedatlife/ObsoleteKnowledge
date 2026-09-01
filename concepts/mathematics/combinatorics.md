---
type: concept
category: mathematics
defines: ["combinatorics", "combinatorial analysis"]
related: ["[[pascal-triangle]]", "[[probability]]", "[[statistics]]", "[[permutation]]", "[[graph-theory]]"]
requires: ["[[set-theory]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Combinatorics

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Combinatorics** is the branch of mathematics devoted to counting, arranging, and selecting objects from finite sets. It answers fundamental questions: "How many ways can we arrange these items?" and "In how many ways can we choose a subset?" These techniques underpin probability theory, algorithm analysis, and many fields of applied mathematics.

## you gotta know

- At its core, **combinatorics** counts discrete structures: permutations (ordered arrangements) and combinations (unordered selections).
- The *n choose k* notation, $\binom{n}{k}$, counts the number of ways to select *k* items from *n* items without regard to order.
- [[pascal-triangle]] encodes all binomial coefficients, making combinatorial identities visible as number patterns.
- Permutations count ordered arrangements; an *n*-element set has *n!* different orderings.
- The *inclusion-exclusion principle* is a fundamental counting technique that avoids double-counting by systematically adding and subtracting overlapping cases.
- **Combinatorics** directly underpins [[probability]] by enumerating favorable and total outcomes.
- Many algorithmic problems reduce to combinatorial optimization: finding the best arrangement among an astronomically large set.
- Multinomial coefficients generalize binomial coefficients, counting partitions of *n* objects into *k* labeled groups of specified sizes.
- Stirling numbers of the first and second kind enumerate permutations by cycle structure and partitions of sets into subsets, respectively.
- Generating functions encode combinatorial sequences as power series, transforming counting problems into algebraic manipulations and recurrence relations.
- The pigeonhole principle is a fundamental combinatorial tool: if *n* + 1 objects are placed into *n* boxes, at least one box must contain two or more objects.
- Combinatorial designs (like Latin squares and block designs) have applications in experimental design, cryptography, and error-correcting codes.

## connections

- [[pascal-triangle]] — the table that displays all binomial coefficients.
- [[probability]] — relies on combinatorial counting to compute outcome frequencies.
- [[statistics]] — sampling and sampling distributions depend on combinatorial methods.
- [[linear-algebra]] — counting linear subspaces and bases involves combinatorial reasoning.
- [[number-theory]] — partition functions and divisor-counting are combinatorial problems.

## see also

- [[pascal-triangle]] · [[probability]] · [[statistics]] · [[number-theory]]

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
