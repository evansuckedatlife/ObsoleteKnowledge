---
type: concept
category: mathematics
defines: ["Dirichlet's Theorem on Arithmetic Progressions", "Dirichlet's Theorem"]
related: ["[[infinitude-of-primes]]", "[[prime-number-theorem]]"]
requires: ["[[number-theory]]"]
lists:
  - "[[statements-about-prime-numbers]]"
tour_order: 1
read: false
---

# Dirichlet's Theorem on Arithmetic Progressions


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

Dirichlet's Theorem on Arithmetic Progressions states that if $a$ and $d$ are coprime positive integers, then the arithmetic progression $a, a+d, a+2d, a+3d, \dots$ contains infinitely many prime numbers. Proved by *Peter Gustav Lejeune Dirichlet* in 1837, it generalizes Euclid's proof of the infinitude of primes to linear progressions. This landmark result marked the birth of analytic number theory by introducing methods from analysis to solve algebraic questions.

## you gotta know

- The theorem requires the starting term $a$ and the common difference $d$ to be coprime (i.e., $\gcd(a, d) = 1$), because if they shared a common divisor $g > 1$, every term in the progression would be a multiple of $g$, allowing at most one prime.
- An intuitive example is the progression $4n + 3$ (yielding 3, 7, 11, 19, 23, 31, ...), which contains infinitely many primes.
- To prove the theorem, Dirichlet introduced *Dirichlet characters* and *Dirichlet L-functions*, which are complex analytic generalizations of the Riemann zeta function.
- The proof demonstrates that the sum of the reciprocals of the primes in the progression diverges, showing that the primes not only exist in infinite quantity but also possess a non-zero density.
- The theorem implies that the primes are distributed asymptotically equally among the $\varphi(d)$ coprime residue classes modulo $d$, where $\varphi$ is Euler's totient function.

## connections

- [[infinitude-of-primes]] — generalizes the basic result that primes are infinite to specific arithmetic progressions.
- [[riemann-hypothesis]] — generalizes to the Generalized Riemann Hypothesis (GRH) for Dirichlet L-functions.
- [[prime-number-theorem]] — has a specialized variant (the prime number theorem for arithmetic progressions) that quantifies prime distribution in these sequences.
- [[fundamental-theorem-of-arithmetic]] — provides the basis for the Euler product representation of Dirichlet L-functions.

## see also

- [[infinitude-of-primes]] · [[riemann-hypothesis]] · [[prime-number-theorem]]

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

Lists: [[statements-about-prime-numbers]] · Mark read: `INPUT[toggle:read]`
