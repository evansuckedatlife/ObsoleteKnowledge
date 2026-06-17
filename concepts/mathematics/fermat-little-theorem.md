---
type: concept
category: mathematics
defines: ["Fermat's Little Theorem", "Fermat Little Theorem"]
related: ["[[modular-arithmetic]]", "[[pierre-de-fermat]]", "[[euler-totient]]"]
requires: ["[[number-theory]]", "[[modular-arithmetic]]"]
lists:
  - "[[statements-about-prime-numbers]]"
tour_order: 2
read: false
---

# Fermat's Little Theorem


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

Fermat's Little Theorem states that if p is a prime and a is any integer not divisible by p, then a^(p-1) ≡ 1 (mod p). This elegant result, discovered by *Pierre de Fermat* in the 17th century, is fundamental to modular arithmetic and forms the basis of many cryptographic algorithms including early versions of public-key cryptography.

## you gotta know

- The theorem states: for prime p and integer a with gcd(a, p) = 1, we have a^(p-1) ≡ 1 (mod p).
- A useful variant: a^p ≡ a (mod p) holds for any integer a, even if a is divisible by p.
- The proof uses the properties of multiplicative groups modulo p and does not require the full machinery of *Euler's theorem*.
- Fermat's Little Theorem is used to test primality probabilistically (*Fermat primality test*) and to construct cryptographic systems like *RSA*.
- *Leonhard Euler* later generalized this to *Euler's theorem*, which extends the result to any modulus, not just primes.

## connections

- [[pierre-de-fermat]] — the mathematician who discovered this theorem.
- [[modular-arithmetic]] — the theorem is a core result in modular number systems.
- [[euler-totient]] — Euler's generalization uses the Euler totient function φ(n).
- [[rsa-encryption]] — relies on Fermat's Little Theorem and the difficulty of computing discrete logarithms.

## see also

- [[modular-arithmetic]] · [[euler-totient]] · [[rsa-encryption]]

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

Lists: [[statements-about-prime-numbers]] · Mark read: `INPUT[toggle:read]`
