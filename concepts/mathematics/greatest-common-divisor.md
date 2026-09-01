---
type: concept
category: mathematics
defines: [greatest common divisor, GCD, gcd]
related: ["[[prime-factorization]]", "[[fundamental-theorem-of-arithmetic]]", "[[euclidean-algorithm]]", "[[least-common-multiple]]", "[[modular-arithmetic]]", "[[divisibility]]"]
requires: ["[[prime-factorization]]", "[[divisibility]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Greatest Common Divisor

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **greatest common divisor** (GCD) of two integers is the largest positive integer that divides both. Denoted gcd(a, b), the GCD is fundamental to number theory and plays a hidden role in countless algorithms. The *Euclidean algorithm* efficiently computes it in logarithmic time—one of the oldest and most elegant algorithms in mathematics. GCD is indispensable for simplifying fractions, solving Diophantine equations, and constructing cryptographic systems.

## you gotta know

- gcd(a, b) is the largest positive integer d such that a = dm and b = dn for some integers m, n; equivalently, it is the largest divisor common to both a and b.
- gcd(a, b) divides any linear combination of a and b; this is *Bézout's identity*: there exist integers x, y (not unique) with ax + by = gcd(a, b), a fundamental result in number theory.
- The *Euclidean algorithm* computes gcd(a, b) by repeated division: gcd(a, b) = gcd(b, a mod b), until one argument becomes 0; the time complexity is O(log(min(a, b))), making it extremely efficient.
- If gcd(a, b) = 1, then a and b are *coprime* (relatively prime); they share no common prime factors and their residues generate the entire multiplicative group modulo their product.
- gcd(a, b) × lcm(a, b) = a × b (the product of GCD and LCM equals the product of the numbers), a beautiful symmetric relationship connecting the two operations.
- The prime factorization reveals gcd: if a = p₁^α₁ × p₂^α₂ × ... and b = p₁^β₁ × p₂^β₂ × ..., then gcd(a, b) = p₁^min(α₁, β₁) × p₂^min(α₂, β₂) × ..., taking the minimum exponent for each prime.
- Essential for cryptography: RSA's security relies on computing φ(pq) = (p−1)(q−1) when gcd is tractable for known primes, but factoring remains hard for unknown large primes.
- The extended Euclidean algorithm computes not just gcd(a, b) but also the Bézout coefficients x, y satisfying ax + by = gcd(a, b), enabling modular inverse computation crucial to cryptography.
- Applications permeate mathematics: simplifying fractions, solving linear Diophantine equations, constructing finite fields, and analyzing number-theoretic properties in algebra.

## connections

- [[prime-factorization]] — gcd's most direct computation, factorizing and taking minimum powers.
- [[fundamental-theorem-of-arithmetic]] — the prime factorization that underlies GCD's structure.
- [[euclidean-algorithm]] — the efficient algorithm for computing GCD without factoring.
- [[least-common-multiple]] — the dual concept; LCM and GCD are inversely related via their product.
- [[modular-arithmetic]] — coprimality (gcd = 1) determines invertibility modulo n.
- [[divisibility]] — the foundational concept on which GCD is defined.

## see also

[[prime-factorization]] · [[euclidean-algorithm]] · [[least-common-multiple]] · [[modular-arithmetic]]

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
