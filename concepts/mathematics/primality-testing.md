---
type: concept
category: mathematics
defines: ["Primality Testing", "Primality Test"]
related: ["[[p-vs-np-problem]]", "[[integer-factorization]]", "[[fermat-little-theorem]]"]
requires: ["[[number-theory]]", "[[algorithm]]"]
lists:
  - "[[computation-types]]"
tour_order: 6
read: false
---

# Primality Testing


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

Primality testing is the computational process of determining whether a given input integer is prime. Unlike the much harder problem of integer factorization, which actually finds the factors of a composite number, primality testing only requires a yes-or-no decision. The creation of rapid primality tests is a crucial foundation of modern public-key cryptography, which requires generating very large prime numbers.

## you gotta know

- In 2002, the *AKS primality test* proved that primality testing is in the complexity class P, meaning it can be solved in deterministic polynomial time.
- In practical applications, randomized algorithms like the *Miller-Rabin primality test* are preferred because they run much faster, though they have a small, controllable probability of misidentifying a composite number (a "strong pseudoprime") as prime.
- The *Fermat primality test* is a simple check based on Fermat's Little Theorem, but it is unreliable because of *Carmichael numbers*, which are composite numbers that satisfy the Fermat congruence for all bases coprime to them.
- For Mersenne numbers (primes of the form $2^p - 1$), the *Lucas-Lehmer primality test* is a highly specialized, extremely fast deterministic test used by projects like GIMPS to find record-breaking large primes.
- Most probabilistic tests work by looking for "witnesses" to compositeness; if a number is composite, the test will find a witness with high probability, but if the number is prime, no witnesses exist.

## connections

- [[p-vs-np-problem]] — the AKS proof placed primality testing in P, resolving a classic open question in complexity theory.
- [[integer-factorization]] — illustrates the computational gap between deciding if a number is prime (easy) and finding its factors (hard).
- [[fermat-little-theorem]] — the mathematical identity that underlies Fermat's test and its randomized extensions.
- [[sieve-of-eratosthenes]] — an ancient algorithm that finds all primes up to a limit, serving as an early, brute-force primality filter.
- [[mersenne-primes]] — the target of the Lucas-Lehmer test, which is used to discover the largest known primes.

## see also

- [[p-vs-np-problem]] · [[integer-factorization]] · [[fermat-little-theorem]] · [[sieve-of-eratosthenes]] · [[mersenne-primes]]

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

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
