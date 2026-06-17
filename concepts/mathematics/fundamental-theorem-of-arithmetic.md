---
type: concept
category: mathematics
defines: ["Fundamental Theorem of Arithmetic", "Unique Factorization"]
related: ["[[prime-number-theorem]]", "[[infinitude-of-primes]]", "[[greatest-common-divisor]]", "[[integer-factorization]]"]
requires: ["[[number-theory]]"]
lists:
  - "[[statements-about-prime-numbers]]"
tour_order: 1
read: false
---

# Fundamental Theorem of Arithmetic


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The Fundamental Theorem of Arithmetic states that every integer greater than 1 is either a prime number itself or can be represented uniquely as a product of prime numbers, up to the order of the factors. This theorem serves as the bedrock of number theory, establishing prime numbers as the fundamental "building blocks" of all integers. The existence part of the theorem guarantees that any composite number can be broken down, while the uniqueness part ensures that this decomposition is distinct. This dual property enables the systematic study of divisibility, modular arithmetic, and algebraic structures. Its principles also underpin modern cryptographic algorithms, where the difficulty of finding these unique factorizations secures global communications.

## you gotta know

### statement & components

- *Existence*: Every integer $n > 1$ can be written as a product of one or more prime numbers, which can be expressed in canonical form as $n = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$ where $p_i$ are distinct primes in increasing order and $a_i \ge 1$.
- *Uniqueness*: The factorization is unique up to the order of the prime factors; no integer can have two different prime decompositions.
- *Role of 1*: The number 1 is excluded from being a prime specifically to preserve the uniqueness of factorization (otherwise, $6 = 2 \cdot 3 = 2 \cdot 3 \cdot 1 = 2 \cdot 3 \cdot 1^2 \dots$).

### algebraic extensions & failures

- *Unique Factorization Domains (UFDs)*: The theorem generalizes to abstract algebra; rings where every non-zero non-unit factors uniquely into irreducibles are called UFDs.
- *Failure of Uniqueness*: In some algebraic number fields, unique factorization fails; for example, in the ring $\mathbb{Z}[\sqrt{-5}]$, the number 6 has two distinct factorizations: $2 \cdot 3$ and $(1 + \sqrt{-5})(1 - \sqrt{-5})$.
- *Invention of Ideals*: The failure of unique factorization in rings of algebraic integers led Ernst Kummer and Richard Dedekind to introduce the concept of *ideals* (specifically, *prime ideals* factor uniquely in Dedekind domains).

### algorithmic & computational aspects

- *Asymmetric Hardness*: While checking if a factorization is correct is extremely fast (polynomial time), finding the prime factorization of a very large composite number is computationally difficult.
- *RSA Cryptography*: This computational asymmetry—factoring is hard, multiplication is easy—directly underpins the security of the *RSA* public-key cryptosystem.
- *Euclid's Lemma*: The proof of uniqueness relies crucially on Euclid's Lemma, which states that if a prime $p$ divides a product $ab$, then $p$ must divide $a$ or $b$.

## connections

- [[infinitude-of-primes]] — guarantees that an infinite supply of prime building blocks exists.
- [[dirichlets-theorem-on-arithmetic-progressions]] — extends prime existence to arithmetic progressions.
- [[euclid]] — proved the foundational lemma and early forms of the theorem in the *Elements*.
- [[carl-friedrich-gauss]] — provided the first modern rigorous proof of the theorem in *Disquisitiones Arithmeticae*.
- [[rsa-encryption]] — cryptographic system whose security relies on the hardness of integer factorization.
- [[sieve-of-eratosthenes]] — an ancient algorithm used to generate the primes needed for factorization.
- [[integer-factorization]] — the computational problem of finding the prime factors guaranteed by the theorem.
- [[goldbach-conjecture]] — an additive question about primes, contrasting with this multiplicative theorem.

## context

The Fundamental Theorem of Arithmetic, though simple in its assertion, represents one of humanity's earliest steps toward formalizing mathematical structures. Originally formulated in Euclid's *Elements* (Book IX, Proposition 14) for products of primes, it was not given a modern, rigorous proof of both existence and uniqueness until Carl Friedrich Gauss's *Disquisitiones Arithmeticae* in 1801. In quiz bowl, the theorem is a frequent source of questions, often clued via its algebraic generalizations (UFDs), its reliance on Euclid's Lemma, or the historical crisis surrounding the failure of unique factorization in rings like $\mathbb{Z}[\sqrt{-5}]$ which prompted the creation of modern ring theory.

## see also

- [[infinitude-of-primes]] · [[modular-arithmetic]] · [[rsa-encryption]] · [[integer-factorization]]

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
