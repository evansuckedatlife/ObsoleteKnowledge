---
type: concept
category: mathematics
defines: [Pascal's triangle, Binomial triangle]
related: ["[[pascal]]", "[[probability]]", "[[combinatorics]]"]
requires: ["[[combinatorics]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Pascal's Triangle

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Pascal's triangle** is a triangular array of numbers where each entry is the sum of the two entries above it. Despite its simple construction rule, it encodes profound combinatorial and algebraic structure: each row contains binomial coefficients, and the triangle's entries and patterns relate to probability, algebra, and even fractal geometry. Named after *Blaise Pascal*, it was known centuries earlier in the Islamic world and China.

## you gotta know

- *Construction rule*: start with 1 at the apex; each interior entry is the sum of the two entries diagonally above it; borders are all 1s; yields a symmetric triangle.
- The *n*th row (row 0 = apex) contains binomial coefficients: entry *k* is C(*n*, *k*) = *n*! / (*k*!(*n*−*k*)!), the number of *k*-element subsets of *n* objects.
- *Binomial theorem*: (*x* + *y*)^*n* = Σ_{k=0}^{n} C(*n*, *k*) *x*^{n−k} *y*^k; coefficients are exactly the *n*th row, providing an elegant algebraic interpretation.
- *Row sums*: the *n*th row sums to 2^*n*, equal to the number of all subsets of an *n*-element set; follows from binomial theorem setting *x* = *y* = 1.
- *Hidden sequences*: diagonals sum to Fibonacci numbers F_{n+1}; many other integer sequences emerge from sums and patterns in the triangle.
- *Probability applications*: counts the number of paths in binomial random walks; row *n* gives the distribution of successes in *n* independent coin flips (binomial distribution).
- *Fractal property*: coloring entries modulo 2 (odd entries black, even white) reveals the *Sierpinski triangle*, a fractal with perfect self-similarity at all scales.
- *Hockey stick identity*: sums of diagonals follow patterns; Σ_{i=r}^{n} C(*i*, *r*) = C(*n*+1, *r*+1); useful in combinatorial identities and proofs.
- **Pascal's triangle** appears in many areas: binomial expansions, combinatorial identities, probability problems, and even in the structure of certain polynomials and recurrence relations.

## connections

- [[pascal]] — the mathematician whose name the triangle bears, though he credited earlier sources.
- [[probability]] — binomial coefficients arise naturally in probability and counting problems.
- [[combinatorics]] — Pascal's triangle is the enumeration table for binomial coefficients.
- [[algebra]] — coefficients of the binomial expansion; power series and polynomial identities.
- [[fibonacci-sequence]] — hidden in the diagonals of Pascal's triangle.

## see also

[[pascal]] · [[probability]] · [[combinatorics]] · [[algebra]]

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
