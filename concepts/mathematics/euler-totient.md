---
type: concept
category: mathematics
defines: [Euler's totient function, Euler's phi function, totient function, Euler totient]
related: ["[[modular-arithmetic]]", "[[fermat-little-theorem]]", "[[fundamental-theorem-of-arithmetic]]", "[[prime-factorization]]", "[[euclidean-algorithm]]", "[[number-theory]]"]
requires: ["[[number-theory]]", "[[modular-arithmetic]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Euler's totient function

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Euler's totient function**, traditionally designated by the Greek letter $\varphi$ (phi), is an arithmetic function that counts the positive integers up to a given integer $n$ that are coprime to $n$. Introduced by *Leonhard Euler* in 1763 to generalize *Pierre de Fermat*'s modular arithmetic theorems and later dubbed the "totient" by *J. J. Sylvester*, it plays a foundational role in abstract algebra, cryptography, and analytical number theory.

## you gotta know

- Defined mathematically as $\varphi(n) = |\{k \in \mathbb{N} : 1 \le k \le n \text{ and } \gcd(k, n) = 1\}|$, measuring the size of the multiplicative group of integers modulo $n$.
- Serves as the central component of *Euler's totient theorem*, stating that if $a$ and $n$ are coprime, then $a^{\varphi(n)} \equiv 1 \pmod n$.
- Directly generalizes [[fermat-little-theorem]], which corresponds to the special case where the modulus $n$ is a prime number $p$ and $\varphi(p) = p - 1$.
- Operates as a multiplicative function, meaning $\varphi(mn) = \varphi(m)\varphi(n)$ whenever $\gcd(m, n) = 1$, enabling computation via prime factorization: $\varphi(n) = n \prod_{p|n} (1 - 1/p)$.
- Provides the key mathematical underpinning for the key-generation step in the RSA cryptosystem, where the totient of a product of two primes $pq$ is $(p-1)(q-1)$.
- Satisfies Gauss's divisor identity, which states that the sum of $\varphi(d)$ over all positive divisors $d$ of $n$ equals $n$.
- Generates the degrees of cyclotomic polynomials, meaning the cyclotomic [[field-extension]] $\mathbb{Q}(\zeta_n)$ has degree $\varphi(n)$ over the rationals.

## connections

- [[modular-arithmetic]] — algebraic setting where the totient measures the order of invertible residue classes.
- [[fermat-little-theorem]] — earlier number-theoretic result that Euler generalized using the totient function.
- [[euclidean-algorithm]] — standard algorithmic technique for checking coprimality to evaluate whether an element contributes to the totient count.
- [[prime-factorization]] — decomposition of an integer into prime components required to compute the totient product formula.
- [[fundamental-theorem-of-arithmetic]] — structural property ensuring the unique prime decomposition on which multiplicativity of the totient depends.
- [[number-theory]] — central discipline of pure mathematics in which arithmetic functions like the totient are analyzed.

## see also

- [[modular-arithmetic]] · [[fermat-little-theorem]] · [[euclidean-algorithm]]

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
