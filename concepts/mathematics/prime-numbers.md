---
type: concept
category: mathematics
defines: [Prime Numbers, primes]
related: ["[[fundamental-theorem-of-arithmetic]]", "[[prime-factorization]]", "[[prime-number-theorem]]", "[[fermat-little-theorem]]", "[[modular-arithmetic]]", "[[euclid]]", "[[ancient-greece]]"]
requires: ["[[number-theory]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Prime Numbers

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Prime numbers** (or **primes**) are natural numbers strictly greater than 1 that cannot be formed by multiplying two smaller positive integers, possessing no positive divisors other than 1 and themselves. First treated systematically in [[ancient-greece]] within the axiomatic framework of *The Elements* by [[euclid|Euclid]], primes represent the irreducible multiplicative atoms of the integer number line. In modern mathematical sciences, the enigmatic distribution and deep structural symmetries of primes animate advanced research in [[number-theory]], while their computational properties form the indispensable backbone of modern digital cryptography.

## you gotta know

- The [[fundamental-theorem-of-arithmetic]] guarantees that every positive integer strictly greater than 1 can be factored into a product of primes in exactly one way, up to the ordering of the factors, establishing [[prime-factorization]] as arithmetic's primary foundation.
- In *Book IX, Proposition 20* of *The Elements*, [[euclid|Euclid]] established the infinitude of primes through a classic proof by contradiction, demonstrating that any finite list of primes can be used to construct a larger integer that must yield a new prime divisor.
- The *Sieve of Eratosthenes* provides an ancient and intuitive algorithm for discovering all primes up to an arbitrary integer limit by sequentially crossing out the composite multiples of each newly identified prime starting with 2.
- The asymptotic density and growth of primes among the integers is described by the [[prime-number-theorem]], which states that the prime-counting function $\pi(x)$ asymptotically approaches $x / \ln(x)$, a landmark discovery whose deepest properties depend upon the non-trivial zeros of the *Riemann zeta function* in the *Riemann hypothesis*.
- Famous unsolved problems in mathematics continue to focus on additive and positional arrangements of primes, notably the *Goldbach conjecture*—which asserts that every even integer greater than 2 is a sum of two primes—and the *Twin Prime conjecture*, concerning infinitely recurring pairs differing by exactly two.
- Notable special classes include *Mersenne primes*, written in the form $2^p - 1$, which correspond bijectively to even *perfect numbers* via the *Euclid-Euler theorem*, and *Fermat primes*, defined as $2^{2^n} + 1$, which dictate the geometric constructibility of regular polygons with straightedge and compass.
- Primality testing diverges sharply from factorization in computational complexity; while randomized algorithms like the *Miller-Rabin test* and deterministic algorithms like the *AKS primality test* determine primality in polynomial time, the intractability of factoring large semiprimes remains the core security assumption of *RSA* encryption.

## connections

- [[euclid]] — proved the infinitude of primes in *Book IX* of *The Elements* via an elegant proof by contradiction.
- [[fundamental-theorem-of-arithmetic]] — proves that every integer greater than 1 decomposes into a unique product of prime numbers.
- [[prime-factorization]] — the fundamental mathematical process of decomposing a composite integer into its unique prime constituents.
- [[prime-number-theorem]] — describes the asymptotic distribution and logarithmic frequency of primes across the real number system.
- [[fermat-little-theorem]] — foundational identity in [[modular-arithmetic]] stating that $a^p \equiv a \pmod p$ for any prime $p$.
- [[modular-arithmetic]] — algebraic framework where modular reduction by a prime produces a finite field with invertibility.
- [[number-theory]] — the overarching branch of pure mathematics centered on integer arithmetic, for which primes are the foundational atoms.

## see also

- [[fundamental-theorem-of-arithmetic]] · [[prime-number-theorem]] · [[prime-factorization]] · [[modular-arithmetic]]

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
