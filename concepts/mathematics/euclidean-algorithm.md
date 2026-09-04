---
type: concept
category: mathematics
defines: [Euclidean algorithm, Euclidean division algorithm, extended Euclidean algorithm]
related: ["[[fundamental-theorem-of-arithmetic]]", "[[modular-arithmetic]]", "[[prime-factorization]]", "[[euler-totient]]", "[[euclid]]", "[[number-theory]]"]
requires: ["[[number-theory]]", "[[euclid]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Euclidean algorithm

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Euclidean algorithm** is an efficient method for computing the greatest common divisor of two integers without requiring prime factorization. First recorded in *Euclid*'s *Elements* around 300 BCE in geometric terms as mutual subtraction, it operates by repeatedly replacing the larger integer with the remainder of its division by the smaller until reaching a zero remainder. It forms a cornerstone of computational number theory, modern cryptography, and abstract algebra.

## you gotta know

- Computes the greatest common divisor ($\gcd$) of two integers by exploiting the identity $\gcd(a, b) = \gcd(b, a \pmod b)$ until the remainder vanishes.
- First appeared in Books VII and X of *Euclid*'s *Elements*, originally formulated as *anthyphairesis*, or reciprocal subtraction of geometric line segments.
- The **extended Euclidean algorithm** computes the greatest common divisor while simultaneously determining integers $x$ and $y$ that satisfy *Bézout's identity*, $ax + by = \gcd(a, b)$.
- Provides the standard method for calculating modular multiplicative inverses in [[modular-arithmetic]], a vital step in public-key cryptography algorithms like RSA.
- Gabriel Lamé proved in 1844 that the number of division steps never exceeds five times the number of digits in the smaller input, representing the earliest result in computational complexity theory.
- The worst-case input for the algorithm occurs when the two inputs are consecutive Fibonacci numbers, forcing every quotient in the division sequence to equal one.
- Generalizes beyond the integers to any Euclidean domain, including polynomial rings with coefficients in a field, where it finds polynomial greatest common divisors.

## connections

- [[euclid]] — classical mathematician whose *Elements* first codified the algorithm.
- [[number-theory]] — foundational branch of mathematics where the algorithm serves as an essential calculation tool.
- [[modular-arithmetic]] — framework where the extended version computes modular inverses.
- [[prime-factorization]] — alternative, computationally expensive method for finding greatest common divisors.
- [[euler-totient]] — arithmetic function whose values count integers coprime to a base as identified by the algorithm.
- [[fundamental-theorem-of-arithmetic]] — structural theorem whose proof fundamentally depends on *Euclid's lemma*, established via this algorithm.

## see also

- [[modular-arithmetic]] · [[euler-totient]] · [[fundamental-theorem-of-arithmetic]]

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
