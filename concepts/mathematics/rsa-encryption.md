---
type: term
category: mathematics
defines: [RSA, RSA encryption, public-key cryptography, modular exponentiation]
related: ["[[prime-number-theorem]]", "[[fundamental-theorem-of-arithmetic]]", "[[integer-factorization]]", "[[primality-testing]]", "[[fermats-little-theorem]]", "[[algorithm]]", "[[polynomial-function]]"]
requires: ["[[modular-arithmetic]]", "[[number-theory]]"]
lists: []
tour_order: 2
read: false
---

# RSA Encryption


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

*RSA* (Rivest-Shamir-Adleman) is a public-key cryptographic algorithm that enables secure communication over insecure channels. It relies on the mathematical difficulty of factoring large composite numbers—a number that is trivial to verify as a product of two large primes is computationally hard to factor back into its components. An RSA keypair consists of a public key (used to encrypt) and a private key (used to decrypt); the public key can be freely shared without compromising security, because deriving the private key would require factoring a product of two 1024- or 2048-bit primes, a task far beyond current computational capability. RSA is the foundational technology underlying HTTPS, digital signatures, and secure email.

## you gotta know

### Core Algorithm
- Choose two large distinct primes p and q; compute n = p·q and φ(n) = (p-1)·(q-1) (Euler's totient function).
- Choose an integer e coprime to φ(n) (typically e = 65537); compute d such that e·d ≡ 1 (mod φ(n)) (using the extended Euclidean algorithm).
- *Public key*: (n, e); *Private key*: (n, d). Publish (n, e) freely; keep d secret.
- *Encryption*: ciphertext c ≡ plaintext^e (mod n).
- *Decryption*: plaintext ≡ c^d (mod n). Works because c^d ≡ (m^e)^d ≡ m^(ed) ≡ m (mod n) by Fermat's Little Theorem.

### Security Basis
- The security of RSA rests entirely on the computational hardness of integer factorization: deriving d from (n, e) would require factoring n = p·q, a task with no known subexponential algorithm for large n.
- With 2048-bit keys, the product n is roughly 2048 bits (more than 600 decimal digits); factoring it is infeasible with known algorithms.
- If a quantum computer (running Shor's algorithm) is ever realized, RSA would be broken; this is a recognized threat, motivating post-quantum cryptography research.

### Practical Deployment
- *Padding*: plaintext is never encrypted directly; instead it is padded via OAEP (Optimal Asymmetric Encryption Padding) to prevent deterministic ciphertexts and chosen-plaintext attacks.
- *Digital signatures*: the private key is used to sign; anyone with the public key can verify. Signature = plaintext^d (mod n); verification checks signature^e ≡ plaintext (mod n).
- *Key generation*: selecting p and q requires generating large random numbers and testing them for primality (probabilistic tests like Miller-Rabin).
- *Performance*: modular exponentiation is computed via fast exponentiation (binary exponentiation, O(log exponent) multiplications); still slow compared to symmetric algorithms like AES.

### Mathematical Foundations
- RSA relies on Fermat's Little Theorem: if n = p·q and gcd(m, n) = 1, then m^φ(n) ≡ 1 (mod n), ensuring e·d ≡ 1 (mod φ(n)) makes decryption work.
- The extended Euclidean algorithm efficiently computes the modular inverse d in O(log n) time.

## context

RSA revolutionized cryptography when it was published in 1977 by enabling secure communication without a pre-shared secret—the hallmark of public-key cryptography. Before RSA, parties needed to exchange secret keys in person or via a secure channel; with RSA, Alice can broadcast her public key globally, and anyone can send her encrypted messages that only she can decrypt. This asymmetry is why RSA powers TLS/HTTPS: a web server publishes its public key in a certificate, allowing browsers to encrypt session keys that only the server can decrypt. RSA's security has held for decades despite intense cryptanalysis, making it one of the most studied and trusted algorithms in existence. However, RSA is slower than symmetric encryption by orders of magnitude; modern practice uses RSA only to exchange symmetric keys, then uses those keys to encrypt bulk data. The rise of quantum computing threatens RSA's security, motivating the National Institute of Standards and Technology (NIST) to standardize post-quantum algorithms; lattice-based and code-based systems are the leading candidates to replace RSA in the post-quantum era.

## connections

- [[prime-number-theorem]] — RSA security depends on the abundance of large primes; generation tests primality probabilistically.
- [[fundamental-theorem-of-arithmetic]] — RSA's hardness rests on the unique factorization of n into p and q.
- [[integer-factorization]] — the inverse problem: given n, find p and q; no known polynomial-time algorithm.
- [[primality-testing]] — Miller-Rabin and AKS tests are used to verify that p and q are prime during key generation.
- [[fermat-little-theorem]] — the mathematical foundation that makes RSA decryption work: m^φ(n) ≡ 1 (mod n).
- [[polynomial-function]] — RSA modular exponentiation takes O(k³) bit operations for k-bit numbers (or O(k² log k) with advanced techniques).
- [[algorithm]] — RSA is an algorithm; its correctness and security are analyzed algorithmically.
- [[big-o-notation]] — analysis of RSA's computational cost and breaking difficulty uses Big O and cryptographic complexity.

## see also

- [[integer-factorization]] · [[primality-testing]] · [[fermat-little-theorem]] · [[fundamental-theorem-of-arithmetic]]

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

Lists: · Mark read: `INPUT[toggle:read]`
