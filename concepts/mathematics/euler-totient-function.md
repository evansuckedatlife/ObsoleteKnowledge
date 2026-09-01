---
type: concept
category: mathematics
defines: [Euler totient function, φ(n)]
related: ["[[modular-arithmetic]]", "[[fermat-little-theorem]]", "[[cryptography]]", "[[number-theory]]", "[[euler]]"]
requires: ["[[modular-arithmetic]]", "[[prime-number]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Euler Totient Function

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Euler totient function**, denoted φ(n), counts how many positive integers up to n are *relatively prime* to n (i.e., share no common factors other than 1). *Euler* proved a remarkable generalization of *Fermat's Little Theorem*: if gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n). This function is indispensable to modern cryptography, underpinning RSA key generation and the security of digital commerce.

## you gotta know

- φ(n) counts integers k where 1 ≤ k ≤ n and gcd(k, n) = 1 (relatively prime to n); equivalently, φ(n) is the order of the multiplicative group of units modulo n.
- For a prime p: φ(p) = p − 1 (all nonzero residues mod p are coprime to p, forming a cyclic group).
- For prime powers: φ(p^k) = p^(k−1)(p − 1), accounting for multiples of p in the range [1, p^k].
- *Multiplicative property*: if gcd(m, n) = 1, then φ(mn) = φ(m)φ(n), making the function fundamental to multiplicative number theory.
- The *Euler totient function* satisfies the remarkable identity: Σ φ(d) = n, where the sum is over all divisors d of n (a consequence of counting residue classes).
- Generalizes *Fermat's Little Theorem*: a^φ(n) ≡ 1 (mod n) for gcd(a, n) = 1; this is *Euler's theorem*, proven using group theory.
- Critical for RSA cryptography: public key generation requires computing φ(pq) = (p − 1)(q − 1) where p, q are secret primes; the security of RSA hinges on factoring being computationally hard.
- The totient is never computed by factoring in practice; instead, n is chosen as a product of large primes so that factoring n remains computationally infeasible, securing RSA's secrecy.
- Applications extend beyond cryptography: φ(n) appears in Möbius inversion, counting primitive roots, and Carmichael's theorem on universal exponents.

## connections

- [[modular-arithmetic]] — φ(n) measures the group of units modulo n.
- [[fermat-little-theorem]] — φ(n) generalizes Fermat's exponent to any modulus.
- [[cryptography]] — RSA relies on φ(n) to generate public and private key pairs.
- [[euler]] — *Leonhard Euler* discovered this function and its generalisation.
- [[prime-number]] — φ(n) depends critically on the prime factorization of n.
- [[number-theory]] — a fundamental object in the study of integer arithmetic.

## see also

[[modular-arithmetic]] · [[fermat-little-theorem]] · [[cryptography]] · [[euler]]

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
