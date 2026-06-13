---
type: list
category: mathematics
read: false
---

# statements about prime numbers

The statements about prime numbers most worth knowing for quiz bowl.

## nodes

- [[euclid-euler-theorem|Euclid–Euler Theorem]] — The Euclid–Euler theorem establishes a complete characterization of even perfect numbers: an even number is perfect (equal to…
- [[fermat-little-theorem|Fermat's Little Theorem]] — Fermat's Little Theorem states that if p is a prime and a is any integer not divisible by p, then a^(p-1) ≡ 1 (mod p).
- [[fundamental-theorem-of-arithmetic|Fundamental Theorem of Arithmetic]] — The fundamental theorem of arithmetic states that every integer greater than 1 can be represented uniquely as a product of…
- [[goldbach-conjecture|Goldbach's Conjecture]] — Goldbach's conjecture, posed by the Prussian mathematician Christian Goldbach in 1742, states that every even integer greater…
- [[prime-factorization-hardness|Hardness of Prime Factorization]] — The hardness of prime factorization is the computational observation that determining the prime factors of a large integer…
- [[infinitude-of-primes|Infinitude of Primes]] — The infinitude of primes states that there is no largest prime number — the sequence of primes continues forever.
- [[mersenne-primes|Mersenne Primes]] — A Mersenne prime is a prime number of the form 2^p - 1, where p is itself prime.
- [[prime-number-theorem|Prime Number Theorem]] — The prime number theorem describes the asymptotic distribution of primes: the number of primes less than or equal to x…
- [[riemann-hypothesis|Riemann Hypothesis]] — The Riemann hypothesis is one of the most famous unsolved problems in mathematics, conjecturing that all non-trivial zeros of…
- [[twin-prime-conjecture|Twin Prime Conjecture]] — The twin prime conjecture asserts that there are infinitely many pairs of primes that differ by exactly 2—such as (3, 5), (5,…
- [[wilson-theorem|Wilson's Theorem]] — Wilson's Theorem states that a positive integer p > 1 is prime if and only if (p-1)!

## progress

Live read-status for this list (requires the **Bases** core plugin). Flip a node's `read` from its footer toggle and it moves here.

```base
filters:
  and:
    - file.hasLink(this.file)
views:
  - type: table
    name: Progress
    order:
      - file.name
      - read
      - type
    sort:
      - property: read
        direction: ASC
      - property: file.name
        direction: ASC
```
