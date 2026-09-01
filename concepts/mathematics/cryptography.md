---
type: concept
category: mathematics
defines: [Cryptography, Encryption, Decryption]
related: ["[[modular-arithmetic]]", "[[number-theory]]", "[[prime-factorization]]", "[[np-complexity-class]]", "[[fermat-little-theorem]]"]
requires: ["[[modular-arithmetic]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Cryptography

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Cryptography** is the mathematical science of secure communication, using algorithms to encode messages so that only intended recipients can decode them. The discipline rests on number-theoretic hardness—problems that are computationally easy to verify but extraordinarily hard to solve backwards—making modern cryptography possible. Since the invention of *RSA encryption* in 1977, which exploited the difficulty of factoring large composite numbers, cryptography has become the security backbone of all digital commerce, authentication, and privacy.

## you gotta know

- *RSA encryption* relies on modular exponentiation and the difficulty of factoring large products of two primes; a public key encodes one exponent and the modulus, while a private key encodes the inverse exponent, computing c ≡ m^e (mod n) to encrypt and m ≡ c^d (mod n) to decrypt.
- The security of RSA hinges on the assumption that *prime factorization* is hard: while multiplication is fast, finding the prime factors of a large composite is computationally infeasible on classical computers.
- *One-way functions* are the theoretical foundation: functions that are quick to compute but whose inverse (given the output) is computationally prohibitive; cryptographic systems exploit this asymmetry.
- *Modular arithmetic* is the mathematical engine: all modern public-key systems operate in modular rings Z/nZ, where exponentiation becomes efficient via repeated squaring and properties like Fermat's Little Theorem enable fast decryption.
- *P vs NP problem*: cryptography assumes that certain problems (like factorization) are in NP but not in P; if P = NP (likely false but unproven), most modern cryptography would collapse.
- *Hash functions* map arbitrary input to fixed-length outputs in a way that is easy to compute but effectively impossible to reverse; they are the basis of digital signatures and password security.
- *Symmetric vs asymmetric*: symmetric systems (AES, older ciphers) use a shared secret key; asymmetric (RSA, elliptic curves) use paired public and private keys, enabling secure communication without pre-shared secrets.
- *Euler's totient function* φ(n) counts integers coprime to n; in RSA, the choice of the encryption exponent and its inverse relies on properties of φ(pq) = (p-1)(q-1).

## connections

- [[modular-arithmetic]] — the mathematical foundation; RSA operates in modular rings.
- [[prime-factorization]] — breaking RSA requires factoring the modulus into primes.
- [[number-theory]] — primes, residues, and algebraic properties underpin all cryptographic systems.
- [[fermat-little-theorem]] — used in modular exponentiation and primality testing.
- [[np-complexity-class]] — cryptography's security assumes NP-hardness of factorization.
- [[euler-totient-function]] — φ(n) is essential to RSA key generation.

## see also

- [[modular-arithmetic]] · [[prime-factorization]] · [[np-complexity-class]] · [[number-theory]]

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
