---
type: term
category: mathematics
defines: [Number theory, number-theoretic, elementary number theory]
related: ["[[prime-number]]", "[[modular-arithmetic]]", "[[fundamental-theorem-of-arithmetic]]", "[[prime-number-theorem]]", "[[fermat-little-theorem]]", "[[wilson-theorem]]", "[[perfect-numbers]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Number Theory

## summary

**Number theory** is the study of properties and relationships among integers, particularly prime numbers, divisibility, and congruences. Often called "the queen of mathematics" for its deep elegance and seemingly effortless generation of unsolved problems, number theory bridges abstract algebra and concrete numerical phenomena. Though it originated in curiosity-driven play with integers, modern number theory underlies cryptography (RSA encryption), computer science, and some of mathematics' greatest conjectures.

## you gotta know

### Foundational Concepts
- **Divisibility** and **factors**: one integer divides another if the result is a whole number; the *greatest common divisor* (GCD) and *least common multiple* (LCM) capture this structure.
- **Prime numbers** are integers greater than 1 with no divisors except 1 and themselves; infinitely many primes exist (Euclid's proof).
- The **fundamental theorem of arithmetic**: every integer greater than 1 factors uniquely (up to order) into primes—the atomic building blocks.
- **Congruences** and **modular arithmetic**: two integers are congruent modulo n if their difference is divisible by n; written a ≡ b (mod n).

### Classical Theorems
- **Fermat's Little Theorem**: if p is prime and a is not divisible by p, then a^(p-1) ≡ 1 (mod p)—crucial for primality testing.
- **Wilson's Theorem**: (p-1)! ≡ -1 (mod p) if and only if p is prime—a theoretical characterization of primality.
- **Dirichlet's Theorem on Arithmetic Progressions**: infinitely many primes exist in any arithmetic progression a + kn (where gcd(a, n) = 1).
- **Prime Number Theorem**: the number of primes less than x is approximately x / ln(x)—formalising how primes thin out.

### Special Integer Classes
- **Perfect numbers**: equal the sum of their proper divisors (e.g., 6 = 1+2+3); connected to Mersenne primes via the Euclid-Euler theorem.
- **Mersenne primes**: primes of the form 2^p - 1; among the largest known primes and tested computationally.
- **Twin primes**: pairs of primes differing by 2 (e.g., 11 and 13); the twin prime conjecture asserts infinitely many exist (unproven).
- **Goldbach's conjecture**: every even integer greater than 2 is the sum of two primes; famous unsolved problem (tested to astronomical numbers).

### Advanced Themes
- **Quadratic reciprocity**: a law governing when solutions to x² ≡ a (mod p) exist—a cornerstone of analytic number theory.
- **Diophantine equations**: polynomial equations in integers (e.g., Fermat's Last Theorem: x^n + y^n = z^n has no positive integer solutions for n ≥ 3, proved by Andrew Wiles in 1995).
- **Analytic number theory** uses calculus and complex analysis (zeta function, Riemann hypothesis) to study prime distribution.

## context

Number theory emerged from Greek mathematics (Euclid's *Elements*) as curiosity about integer properties, later enriched by Islamic scholars and Renaissance mathematicians. For centuries it seemed "useless"—pure abstraction with no application. The 20th century proved otherwise: modular arithmetic and prime factorization underlie RSA encryption, securing Internet commerce; computational number theory tests and searches for large primes. The field has produced some of mathematics' greatest unsolved conjectures (Riemann hypothesis, Goldbach's conjecture, twin prime conjecture), which remain tantalising frontiers. Yet the deep structure—the interplay between primes, congruences, and algebraic integers—has revealed unexpected unity and richness, connecting number theory to geometry, analysis, and even quantum physics through the Langlands program.

## connections

- [[prime-number-theorem]] — how primes are distributed asymptotically.
- [[fundamental-theorem-of-arithmetic]] — uniqueness of prime factorization.
- [[modular-arithmetic]] — congruences and arithmetic modulo n.
- [[perfect-numbers]] — integers equalling the sum of proper divisors.
- [[fermat-little-theorem]] — a cornerstone for primality testing and cryptography.
- [[wilson-theorem]] — characterising primes via factorials modulo n.
- [[riemann-hypothesis]] — the deepest unsolved problem in number theory.
- [[goldbach-conjecture]] — every even number > 2 is a sum of two primes.
- [[twin-prime-conjecture]] — infinitely many twin primes (unproven).

## see also

- [[prime-number-theorem]] · [[modular-arithmetic]] · [[fundamental-theorem-of-arithmetic]]

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
