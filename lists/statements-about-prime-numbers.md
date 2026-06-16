---
type: list
category: mathematics
read: false
---

# statements about prime numbers

The statements about prime numbers most worth knowing for quiz bowl.

## nodes

- [[dirichlets-theorem-on-arithmetic-progressions|Dirichlet's Theorem on Arithmetic Progressions]] — Dirichlet's Theorem on Arithmetic Progressions states that if $a$ and $d$ are coprime positive integers, then the arithmetic…
- [[fermat-little-theorem|Fermat's Little Theorem]] — Fermat's Little Theorem states that if p is a prime and a is any integer not divisible by p, then a^(p-1) ≡ 1 (mod p).
- [[fundamental-theorem-of-arithmetic|Fundamental Theorem of Arithmetic]] — The Fundamental Theorem of Arithmetic states that every integer greater than 1 is either a prime number itself or can be…
- [[goldbach-conjecture|Goldbach's Conjecture]] — Goldbach's conjecture, posed by the Prussian mathematician Christian Goldbach in 1742, states that every even integer greater…
- [[infinitude-of-primes|Infinitude of Primes]] — The infinitude of primes states that there is no largest prime number — the sequence of primes continues forever.
- [[mersenne-primes|Mersenne Primes]] — A Mersenne prime is a prime number of the form 2^p - 1, where p is itself prime.
- [[prime-number-theorem|Prime Number Theorem]] — The prime number theorem describes the asymptotic distribution of primes: the number of primes less than or equal to x…
- [[riemann-hypothesis|Riemann Hypothesis]] — The Riemann Hypothesis is one of the most famous and profound unsolved problems in mathematics, conjecturing that all…
- [[sieve-of-eratosthenes|Sieve of Eratosthenes]] — The Sieve of Eratosthenes is an ancient and highly efficient algorithm for finding all prime numbers up to any given limit.
- [[twin-prime-conjecture|Twin Prime Conjecture]] — The twin prime conjecture asserts that there are infinitely many pairs of primes that differ by exactly 2—such as (3, 5), (5,…

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
