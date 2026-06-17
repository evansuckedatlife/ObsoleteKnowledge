---
type: term
category: mathematics
defines: [Modular arithmetic, modular congruence, modulus]
related: ["[[number-theory]]", "[[congruence]]", "[[divisibility]]", "[[fermat-little-theorem]]", "[[wilson-theorem]]", "[[cryptography]]", "[[clock-arithmetic]]"]
requires: ["[[number-theory]]"]
lists: []
tour_order: 1
read: false
---

# Modular Arithmetic


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Modular arithmetic** is a system of arithmetic for integers where numbers "wrap around" after reaching a certain value called the *modulus*. Two integers are congruent modulo n if their difference is divisible by n, written a ≡ b (mod n). Modular arithmetic abstracts the idea of remainders (clock arithmetic, days of the week) into a rigorous algebraic system. It is foundational to number theory, underpins modern cryptography (RSA encryption), and enables efficient computation via the Chinese Remainder Theorem.

## you gotta know

- **Definition**: a ≡ b (mod n) means n divides (a − b), or equivalently, a and b have the same remainder when divided by n.
- **Residue classes**: the integers partition into n equivalence classes modulo n; each class contains all integers congruent to a fixed residue 0, 1, ..., n−1.
- **Addition and multiplication modulo n**: (a + b) mod n = [(a mod n) + (b mod n)] mod n; similarly for multiplication, preserving structure.
- **Fermat's Little Theorem**: if p is prime and gcd(a, p) = 1, then a^(p-1) ≡ 1 (mod p)—essential for fast exponentiation and primality testing.
- **Modular inverse**: a has a multiplicative inverse modulo n if gcd(a, n) = 1; written a^(-1) such that a·a^(-1) ≡ 1 (mod n).
- **Chinese Remainder Theorem (CRT)**: a system of congruences a ≡ b_i (mod n_i) for coprime n_i has a unique solution modulo the product ∏n_i; enables parallel computation.
- **Cryptographic applications**: RSA encryption relies on modular exponentiation (a^b mod n); breaking it requires factoring n into primes.
- **Euler's totient function φ(n)**: counts integers ≤ n coprime to n; satisfies a^φ(n) ≡ 1 (mod n) for gcd(a,n)=1 (generalises Fermat).

## context

Modular arithmetic crystallised as a discipline through Carl Friedrich Gauss's *Disquisitiones Arithmeticae* (1801), though clock arithmetic is ancient. It reveals deep structure in the integers—the algebraic properties of the ring Z/nZ (integers modulo n). In the 20th century, modular arithmetic became computational: fast algorithms for modular exponentiation and the Chinese Remainder Theorem enabled efficient cryptography. RSA (Rivest–Shamir–Adleman), published in 1977, uses the computational hardness of factoring large n = pq in Z/nZ; this single idea secured digital commerce for decades. Beyond cryptography, modular arithmetic appears in error-correcting codes (Reed-Solomon), pseudorandom number generation, and discrete Fourier transforms. For programmers, modular arithmetic is intuitive via the modulo operator (%); for mathematicians, it is the gateway to abstract algebra and ring theory.

## connections

- [[number-theory]] — modular arithmetic is central to number-theoretic proofs.
- [[congruence]] — congruence modulo n is the defining relation.
- [[divisibility]] — a ≡ b (mod n) iff n divides (a−b).
- [[fermat-little-theorem]] — a^(p-1) ≡ 1 (mod p) for prime p; cornerstone of cryptography.
- [[wilson-theorem]] — (p-1)! ≡ -1 (mod p) characterises primes.
- [[euler-totient-function]] — a^φ(n) ≡ 1 (mod n) generalises Fermat.
- [[cryptography]] — RSA encryption is built on modular exponentiation.
- [[chinese-remainder-theorem]] — solves systems of modular congruences.
- [[clock-arithmetic]] — the intuitive model of modular arithmetic.

## see also

- [[number-theory]] · [[fermat-little-theorem]] · [[cryptography]]

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

Lists: Mark read: `INPUT[toggle:read]`
