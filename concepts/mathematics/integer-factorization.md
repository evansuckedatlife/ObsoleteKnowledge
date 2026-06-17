---
type: concept
category: mathematics
defines: ["Integer Factorization", "Prime Factorization"]
related: ["[[fundamental-theorem-of-arithmetic]]", "[[p-vs-np-problem]]", "[[primality-testing]]"]
requires: ["[[number-theory]]"]
lists:
  - "[[computation-types]]"
tour_order: 1
read: false
---

# Integer Factorization


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

Integer factorization is the process of decomposing a composite integer into a product of smaller integers, typically prime numbers. While the fundamental theorem of arithmetic guarantees that every integer greater than 1 has a unique prime factorization, finding these factors for very large numbers is computationally difficult. This asymmetry—that multiplying numbers is easy, but factoring their product is hard—forms the basis of modern public-key cryptography.

## you gotta know

- The problem is believed to lie outside the class P, but it is also not believed to be NP-complete, occupying an intermediate complexity status (NP $\cap$ co-NP).
- The most efficient known classical algorithm for factoring large integers is the *General Number Field Sieve* (GNFS), which runs in sub-exponential but super-polynomial time.
- On a quantum computer, *Shor's algorithm* can solve the integer factorization problem in polynomial time, meaning that the realization of quantum computing would compromise RSA-based encryption.
- The security of the *RSA cryptosystem* relies directly on the computational hardness of factoring the product of two large, secret prime numbers.
- Simple, historically significant factoring methods include trial division, Fermat's factorization method, and Pollard's rho algorithm.

## connections

- [[fundamental-theorem-of-arithmetic]] — guarantees that a unique prime factorization exists for every integer greater than 1.
- [[p-vs-np-problem]] — factorization is a famous example of a problem in NP whose polynomial-time solvability remains unknown.
- [[primality-testing]] — highlights the computational gap between verifying that a number is prime (easy, in P) and finding its factors (hard).
- [[fermat-little-theorem]] — serves as the mathematical foundation for Pollard's $p-1$ factoring algorithm.

## see also

- [[fundamental-theorem-of-arithmetic]] · [[p-vs-np-problem]] · [[primality-testing]] · [[fermat-little-theorem]]

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

Lists: [[computation-types]] · Mark read: `INPUT[toggle:read]`
