---
type: concept
category: mathematics
defines: [Congruence, Congruence Relation]
related: ["[[number-theory]]", "[[modular-arithmetic]]", "[[fermat-little-theorem]]", "[[fundamental-theorem-of-arithmetic]]", "[[prime-factorization]]", "[[computational-complexity]]", "[[euclid]]"]
requires: ["[[number-theory]]", "[[modular-arithmetic]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Congruence

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Congruence** is an equivalence relation on integers asserting that two numbers have the same remainder when divided by a given positive integer, called the modulus. Introduced systematically by *Carl Friedrich Gauss* in his seminal 1801 treatise *Disquisitiones Arithmeticae*, the concept transformed classical arithmetic into modern algebraic number theory. It provides the mathematical syntax for quotient rings, clock arithmetic, and modern public-key cryptography.

## you gotta know

- Formally defined such that two integers *a* and *b* are equivalent modulo *n* if their difference *a* minus *b* is an exact integer multiple of *n*.
- *Carl Friedrich Gauss* introduced the standard triple-bar notation and established that modular relations behave compatibly with addition, subtraction, and multiplication.
- Serves as the operational foundation for [[modular-arithmetic]], allowing the integers to be partitioned into residue classes that form cyclic groups and finite commutative rings.
- The Chinese Remainder Theorem guarantees a unique solution across coprime moduli, an algorithmic method documented in ancient China by *Sun Tzu* and generalized by *Gauss*.
- Underpins [[fermat-little-theorem]], which establishes that raising any integer to a prime power yields a value congruent to the base modulo that prime.
- The division operation requires finding modular inverses using the extended algorithm developed by [[euclid]], which succeeds precisely when the base and modulus are coprime.
- Wilson's theorem utilizes the relation to characterize primality, stating that *(p - 1)!* is congruent to negative one modulo *p* if and only if *p* is prime.
- Forms the core mathematical framework of modern cryptosystems like RSA, whose security rests on the asymmetric difficulty characterized by [[computational-complexity]].

## connections

- [[number-theory]] — the mathematical discipline in which modular relations serve as the primary tool for investigating divisibility, primes, and equations.
- [[modular-arithmetic]] — the algebraic system of residue classes structured around equivalence modulo an integer modulus.
- [[fermat-little-theorem]] — fundamental number-theoretic theorem expressing prime exponentiation as an equivalence relation on integers.
- [[fundamental-theorem-of-arithmetic]] — the unique prime factorization theorem that guarantees the structure of coprime factorizations in modular reductions.
- [[prime-factorization]] — the computational task of decomposing composite moduli, whose difficulty guarantees the security of modular encryption.
- [[computational-complexity]] — the theoretical classification framework measuring the tractability of modular exponentiation and the difficulty of integer factorization.
- [[euclid]] — classical Greek mathematician whose greatest common divisor algorithm provides the computational method for computing modular inverses.

## see also

- [[modular-arithmetic]] · [[number-theory]] · [[fermat-little-theorem]] · [[prime-factorization]] · [[computational-complexity]]

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
