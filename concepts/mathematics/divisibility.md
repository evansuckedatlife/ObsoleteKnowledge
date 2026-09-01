---
type: concept
category: mathematics
defines: [divisibility, divisible]
related: ["[[number-theory]]", "[[modular-arithmetic]]", "[[prime-factorization]]"]
requires: ["[[fundamental-theorem-of-arithmetic]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Divisibility

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Divisibility** is a fundamental concept in number theory: an integer *a* divides an integer *b* (written *a* | *b*) if there exists an integer *k* such that *b* = *ak*. This simple notion underlies prime factorization, the structure of the integers, and is the foundation for modular arithmetic and cryptography.

## you gotta know

- A divisor of *n* is a number *d* such that *n* = *dk* for some integer *k*; every integer *n* is divisible by 1 and itself (trivial divisors).
- Divisibility is transitive: if *a* divides *b* and *b* divides *c*, then *a* divides *c*, forming a partial ordering on the integers.
- The greatest common divisor (GCD) of two numbers is the largest integer that divides both; the Euclidean algorithm efficiently computes it, underlying cryptography and number theory.
- A number greater than 1 is prime if and only if it is divisible only by 1 and itself; composite numbers have other divisors, and primes are the building blocks of all integers.
- The [[fundamental-theorem-of-arithmetic]] states that every integer greater than 1 has a unique factorization into prime divisors, making divisibility the foundation of multiplicative number theory.
- Divisibility patterns are preserved under modular arithmetic: if *a* divides (*b* − *c*), then *b* ≡ *c* (mod *a*), connecting divisibility to congruence classes.
- The divisor function τ(*n*) counts how many divisors *n* has; understanding divisor distributions reveals structure in the integers and connects to analytic number theory.
- Divisibility structures in other algebraic systems (Gaussian integers, polynomial rings) generalize the classical notion and reveal that unique factorization is *not* always guaranteed in non-integer rings; this discovery profoundly influenced modern algebra.
- In cryptography, divisibility forms the basis of the RSA algorithm: the security rests on the difficulty of determining divisors (factoring) of products of large primes.

## connections

- [[number-theory]] — divisibility is a core structural concept in number theory.
- [[modular-arithmetic]] — divisibility defines the equivalence relation underlying congruence classes.
- [[prime-factorization]] — the unique representation of a number as a product of prime divisors.
- [[fundamental-theorem-of-arithmetic]] — guarantees the unique prime factorization structure divisibility enables.
- [[fermat-little-theorem]] — a divisibility statement about residues of powers in modular arithmetic.
- [[prime-number-theorem]] — describes the distribution of primes and divisibility patterns.

## see also

- [[number-theory]] · [[modular-arithmetic]] · [[prime-factorization]]

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
