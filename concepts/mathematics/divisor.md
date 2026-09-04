---
type: concept
category: mathematics
defines: [divisor, factor, aliquot divisor]
related: ["[[number-theory]]", "[[prime-factorization]]", "[[fundamental-theorem-of-arithmetic]]", "[[modular-arithmetic]]", "[[euclid]]", "[[fermat-little-theorem]]"]
requires: ["[[number-theory]]", "[[fundamental-theorem-of-arithmetic]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# divisor

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **divisor**, or factor, of an integer $n$ is an integer $d$ that divides $n$ without leaving a remainder, producing an exact integer quotient. Studied systematically since the work of [[euclid]] in *ancient-greece*, divisibility constitutes the primary structural relationship in classical arithmetic. Analyzing the properties, counts, and sums of factors underpins modern cryptography, modular computation, and elementary [[number-theory]].

## you gotta know

- An integer $d$ is a **divisor** of $n$ (written $d \mid n$) if there exists an integer $k$ such that $n = k \cdot d$, with non-zero divisors dividing zero, while division by zero remains undefined.
- A proper divisor, or aliquot factor, of a positive integer $n$ is any positive factor of $n$ strictly excluding $n$ itself.
- Positive integers are classified by their aliquot sums: a number is perfect if its proper factors sum to $n$ (such as 6 and 28), deficient if the sum is smaller, and abundant if the sum exceeds $n$.
- The divisor function $\sigma_0(n)$ counts the total number of positive factors, while $\sigma_1(n)$ sums them; both are multiplicative arithmetic functions.
- The greatest common factor of two integers is computed efficiently using the Euclidean algorithm, one of the oldest numerical algorithms known.
- The [[fundamental-theorem-of-arithmetic]] dictates that every integer greater than 1 factors uniquely into primes, from which the total count of positive factors can be calculated via prime exponent products.
- Primes are strictly defined as positive integers possessing exactly two distinct positive factors: 1 and the prime itself.

## connections

- [[number-theory]] — the mathematical field founded directly upon the arithmetic properties and patterns of divisibility.
- [[prime-factorization]] — the unique decomposition of integers into prime building blocks that generate every factor.
- [[fundamental-theorem-of-arithmetic]] — guarantees the uniqueness of canonical factor decompositions across the integers.
- [[modular-arithmetic]] — the framework of congruences structured upon divisibility by an established integer modulus.
- [[euclid]] — classical mathematician who codified divisibility proofs, the Euclidean algorithm, and early theorems on perfect numbers.
- [[fermat-little-theorem]] — fundamental modular identity describing divisibility properties of prime powers.

## see also

- [[number-theory]] · [[prime-factorization]] · [[fundamental-theorem-of-arithmetic]] · [[modular-arithmetic]]

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
