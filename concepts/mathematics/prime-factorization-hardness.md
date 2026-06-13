---
type: concept
category: mathematics
defines: ["Hardness of Prime Factorization", "Integer Factorization Problem"]
related:
  - "[[rsa-encryption]]"
  - "[[computational-complexity]]"
  - "[[public-key-cryptography]]"
lists: []
read: false
---

# Hardness of Prime Factorization

## summary

The hardness of prime factorization is the computational observation that determining the prime factors of a large integer appears to require no known polynomial-time algorithm, despite the fundamental theorem of arithmetic guaranteeing a unique factorization exists. This asymmetry—factorization is hard, but verification is easy—underpins the security of modern public-key cryptography systems like *RSA*.

## you gotta know

- Factoring a number n into its prime factors appears to require time exponential in the number of bits of n (e.g., exponential in log n).
- In contrast, checking whether a proposed factorization is correct is fast (polynomial time)—this asymmetry is the essential basis for *RSA* encryption.
- The fastest known classical algorithms for factoring (e.g., the *general number field sieve*) have sub-exponential but still impractical runtime for very large numbers.
- *Quantum computers*, if built at scale, could factor efficiently using *Shor's algorithm*, which would break current *RSA*-based encryption.
- Whether factorization is inherently hard (complexity-theoretically) or merely appears hard (no algorithm found yet) remains an open question.

## connections

- [[rsa-encryption]] — security depends entirely on the presumed hardness of factorization.
- [[public-key-cryptography]] — built on computational one-way functions, especially factorization hardness.
- [[computational-complexity]] — factorization is a central problem in complexity theory and cryptography.
- [[shor-algorithm]] — demonstrates that quantum computers could solve factorization efficiently.

## see also

- [[rsa-encryption]] · [[public-key-cryptography]] · [[computational-complexity]]

<!-- footer -->

---

Lists:  · Mark read: `INPUT[toggle:read]`
