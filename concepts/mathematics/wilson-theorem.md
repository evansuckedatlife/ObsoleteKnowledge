---
type: concept
category: mathematics
defines: ["Wilson's Theorem"]
related:
  - "[[modular-arithmetic]]"
  - "[[prime-factorization]]"
  - "[[john-wilson]]"
lists: []
read: false
---

# Wilson's Theorem

## summary

Wilson's Theorem states that a positive integer p > 1 is prime if and only if (p-1)! ≡ -1 (mod p). This elegant characterization of primes via factorials, named after *John Wilson* (and proved rigorously by *Joseph-Louis Lagrange*), is a beautiful theoretical result, though computationally inefficient for primality testing compared to modern algorithms.

## you gotta know

- The theorem is an if-and-only-if characterization: p is prime exactly when (p-1)! ≡ -1 (mod p), where (p-1)! is (p-1) factorial.
- Example: for p = 5, we have 4! = 24 ≡ -1 ≡ 4 (mod 5), so 5 is prime.
- The converse also holds: if p is composite and p > 4, then (p-1)! ≡ 0 (mod p) because p divides the factorial.
- Although theoretically elegant, Wilson's Theorem is impractical for primality testing of large numbers because computing (p-1)! mod p becomes computationally prohibitive.
- The theorem reveals a deep symmetry in modular arithmetic and has inspired generalizations in abstract algebra.

## connections

- [[modular-arithmetic]] — a fundamental theorem characterizing primes through congruence properties.
- [[fermat-little-theorem]] — another important characterization of primes and properties modulo p.
- [[primality-testing]] — historically motivated investigations into efficient algorithms to detect primes.
- [[john-wilson]] — the mathematician credited with the observation, formalized by Lagrange.

## see also

- [[fermat-little-theorem]] · [[modular-arithmetic]] · [[primality-testing]]

<!-- footer -->

---

Lists:  · Mark read: `INPUT[toggle:read]`
