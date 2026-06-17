---
type: concept
category: mathematics
defines: ["Euclid–Euler Theorem", "Euclid-Euler Theorem"]
related: ["[[perfect-numbers]]", "[[mersenne-primes]]", "[[euclid]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Euclid–Euler Theorem

## summary

The Euclid–Euler theorem establishes a complete characterization of even perfect numbers: an even number is perfect (equal to the sum of its proper divisors) if and only if it is of the form 2^(p-1)(2^p - 1) where 2^p - 1 is a prime Mersenne number. This theorem beautifully unites two classical subjects—perfect numbers and Mersenne primes—in a single biconditional.

## you gotta know

- An even number n is perfect exactly when n = 2^(p-1) · M_p, where M_p = 2^p - 1 is a Mersenne prime.
- *Euclid* proved the forward direction in the *Elements*: if 2^p - 1 is prime, then 2^(p-1)(2^p - 1) is perfect.
- *Euler* proved the converse: every even perfect number must have this form.
- Examples: 6 = 2^1(2^2 - 1), 28 = 2^2(2^3 - 1), 496 = 2^4(2^5 - 1), 8128 = 2^6(2^7 - 1).
- The theorem implies that finding new Mersenne primes is equivalent to finding new even perfect numbers, motivating intensive computational searches.

## connections

- [[perfect-numbers]] — completely characterized by this theorem for the even case.
- [[mersenne-primes]] — each Mersenne prime yields exactly one new even perfect number.
- [[euclid]] — proved the foundational direction in ancient times.
- [[infinitude-of-primes]] — relates to whether infinitely many perfect numbers (and Mersenne primes) exist.

## see also

- [[perfect-numbers]] · [[mersenne-primes]] · [[infinitude-of-primes]]

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
