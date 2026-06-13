---
type: concept
category: mathematics
defines: ["Fundamental Theorem of Arithmetic", "Unique Factorization"]
related:
  - "[[prime-number-theorem]]"
  - "[[infinitude-of-primes]]"
  - "[[greatest-common-divisor]]"
lists:
  - "[[statements-about-prime-numbers]]"
read: false
---

# Fundamental Theorem of Arithmetic

## summary

The fundamental theorem of arithmetic states that every integer greater than 1 can be represented uniquely as a product of prime numbers, up to the order of the factors. This uniqueness—that there is exactly one way to factor a number into primes—is a cornerstone of number theory and algebra.

## you gotta know

- Every integer n > 1 is either prime itself or factors into a product of primes: n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ where the pᵢ are distinct primes and aᵢ ≥ 1.
- The prime factorization of any number is unique except for the order in which primes appear (e.g., 12 = 2² · 3 always, never any other prime product).
- This uniqueness fails in some algebraic number systems, which motivated the invention of *ideals* in abstract algebra.
- The theorem is sometimes called the "Fundamental Theorem" because factorization underlies divisibility, greatest common divisors, least common multiples, and modular arithmetic.
- For cryptography and primality testing, knowing or computing prime factorizations efficiently is computationally hard—a property exploited by *RSA* encryption.

## connections

- [[infinitude-of-primes]] — demonstrates that enough primes exist to factor any integer.
- [[euclid]] — rigorously established the concept of prime divisibility that grounds this theorem.
- [[modular-arithmetic]] — relies on unique factorization to define residue classes and ring structure.
- [[rsa-encryption]] — security depends on factorization being hard for very large numbers.
- [[greatest-common-divisor]] — computed using prime factorization.

## see also

- [[infinitude-of-primes]] · [[modular-arithmetic]] · [[rsa-encryption]]

<!-- footer -->

---

Lists: [[statements-about-prime-numbers]] · Mark read: `INPUT[toggle:read]`
