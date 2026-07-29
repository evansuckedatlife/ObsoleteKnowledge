---
type: concept
category: mathematics
defines:
  - Prime factorization
  - Prime factorisation
  - Unique factorization
related:
  - "[[prime-number]]"
  - "[[number-theory]]"
  - "[[fundamental-theorem-of-arithmetic]]"
  - "[[divisibility]]"
  - "[[greatest-common-divisor]]"
  - "[[least-common-multiple]]"
  - "[[cryptography]]"
  - "[[integer-factorization]]"
requires: ["[[prime-number]]"]
lists: []
tour_order: 1
read: false
---

# Prime Factorization


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Prime factorization** is the representation of an integer as a product of *prime numbers*, unique up to order. The *fundamental theorem of arithmetic* guarantees that every integer greater than 1 has a unique prime factorization, making primes the "building blocks" of the integers. Prime factorization is central to number theory and has practical applications in cryptography, divisibility, and algorithm design.

## you gotta know

- Every integer n > 1 can be written uniquely as a product of primes: n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ, where p₁, p₂, ..., pₖ are distinct primes and a₁, a₂, ..., aₖ are positive exponents.
- The *fundamental theorem of arithmetic* formalizes the uniqueness: the prime factorization is unique regardless of the order in which primes are listed; this uniqueness is non-obvious and requires proof.
- Factorizing large numbers is computationally hard: while small numbers factor quickly, large composite numbers (especially products of two large primes) require exponential time with known algorithms, a fact leveraged in RSA *cryptography*.
- The *greatest common divisor (GCD)* of two numbers is the product of common prime factors with minimum exponents; the *least common multiple (LCM)* is the product with maximum exponents; both derive naturally from prime factorization.
- Prime factorization enables divisibility tests: a number is divisible by d if and only if all prime factors of d (with their exponents) appear in the number's factorization.
- Trial division (testing divisibility by successive primes) works for small factorizations but becomes slow for large numbers; more sophisticated algorithms (Pollard's rho, quadratic sieve) are used in practice.
- The *Riemann Hypothesis*, one of mathematics' greatest unsolved problems, intimately concerns the distribution of primes and thus the typical difficulty of factorization; its truth or falsity affects cryptographic security.

## connections

- [[prime-number]] — the fundamental units whose product gives all integers.
- [[number-theory]] — prime factorization is central to number-theoretic investigation.
- [[fundamental-theorem-of-arithmetic]] — the theorem guaranteeing unique factorization.
- [[divisibility]] — prime factorization clarifies when one integer divides another.
- [[greatest-common-divisor]] — derived from the common prime factors in factorizations.
- [[least-common-multiple]] — derived from the maximum prime-factor exponents.
- [[cryptography]] — RSA cryptography relies on the difficulty of factorizing large numbers.
- [[integer-factorization]] — the computational problem of finding prime factorizations.

## see also

- [[prime-number]] · [[number-theory]] · [[fundamental-theorem-of-arithmetic]] · [[cryptography]]

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

Lists:  · Mark read: `INPUT[toggle:read]`
