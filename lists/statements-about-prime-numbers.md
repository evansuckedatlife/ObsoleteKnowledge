---
type: list
category: mathematics
read: false
---

# statements about prime numbers

The statements about prime numbers most worth knowing for quiz bowl.

## nodes

- [[fundamental-theorem-of-arithmetic|Fundamental Theorem of Arithmetic]] — States that every integer greater than 1 has a unique prime factorization.
- [[goldbach-conjecture|Goldbach's Conjecture]] — Conjectures that every even integer greater than 2 is the sum of two primes.
- [[riemann-hypothesis|Riemann Hypothesis]] — Conjectures that all non-trivial zeros of the zeta function lie on the critical line of real part 1/2.
- [[twin-prime-conjecture|Twin Prime Conjecture]] — Asserts that there are infinitely many pairs of prime numbers that differ by exactly 2.
- [[prime-number-theorem|Prime Number Theorem]] — Describes the asymptotic distribution and density of prime numbers.
- [[infinitude-of-primes|Infinitude of Primes]] — States that there is no largest prime number and the sequence of primes is infinite.
- [[sieve-of-eratosthenes|Sieve of Eratosthenes]] — An ancient algorithm that systematically marks multiples to find all primes up to a limit.
- [[fermat-little-theorem|Fermat's Little Theorem]] — States that if $p$ is prime and $a$ is coprime to $p$, then $a^{p-1} \equiv 1 \pmod p$.
- [[mersenne-primes|Mersenne Primes]] — Prime numbers that can be written in the form $2^p - 1$, where $p$ is also prime.
- [[dirichlets-theorem-on-arithmetic-progressions|Dirichlet's Theorem on Arithmetic Progressions]] — States that any arithmetic progression $a + nd$ with coprime $a$ and $d$ contains infinitely many primes.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
