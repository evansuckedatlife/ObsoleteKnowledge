---
type: concept
category: mathematics
defines: [Gaussian integers, ring of Gaussian integers]
related: ["[[number-theory]]", "[[modular-arithmetic]]", "[[fundamental-theorem-of-arithmetic]]", "[[prime-factorization]]", "[[polynomial-function]]", "[[fermat-little-theorem]]"]
requires: ["[[number-theory]]", "[[modular-arithmetic]]", "[[fundamental-theorem-of-arithmetic]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Gaussian integers

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Gaussian integers** form a complex number ring whose elements have integer real and imaginary parts, formally denoted as the ring of adjoined imaginary units. Introduced by *Carl Friedrich Gauss* in 1832 to formulate higher-order reciprocity laws, the system extends elementary arithmetic into the complex plane. Because the ring admits a division algorithm and a multiplicative norm, it satisfies unique prime factorization, illustrating the rich structure of algebraic number fields.

## you gotta know

- Defined as the set of all complex numbers of the form a plus b times i, where a and b are standard rational integers.
- Forms an integral domain equipped with four units: 1, negative 1, i, and negative i.
- Utilizes the field norm defined as the sum of the squares of the real and imaginary components, satisfying a strictly multiplicative property.
- Serves as a Euclidean domain where a division algorithm holds, directly implying that it is a principal ideal domain and a unique factorization domain.
- Generalizes the *[[fundamental-theorem-of-arithmetic]]*, ensuring that every nonzero non-unit element factors uniquely into Gaussian primes up to units.
- Splits ordinary integer primes into distinct behaviors: 2 ramifies as a product involving 1 plus i, primes congruent to 3 mod 4 remain inert primes, and primes congruent to 1 mod 4 split into conjugate pairs.
- Yields a direct algebraic proof of *Fermat's theorem on sums of two squares*, proving that an odd prime is a sum of two squares if and only if it is congruent to 1 mod 4.

## connections

- [[number-theory]] — the mathematical discipline in which algebraic integer rings provide deeper arithmetic insights.
- [[fundamental-theorem-of-arithmetic]] — the classical unique factorization theorem generalized by the Gaussian integer ring.
- [[modular-arithmetic]] — framework characterizing how rational primes split, ramify, or remain inert in quadratic extensions.
- [[prime-factorization]] — structural decomposition of elements into irreducible building blocks preserved in Euclidean domains.
- [[fermat-little-theorem]] — foundational modular result tied to Fermat's investigations into representations of primes by quadratic forms.
- [[polynomial-function]] — algebraic framework generating the ring as the quotient of integer polynomials by the ideal of x squared plus one.

## see also

- [[number-theory]] · [[modular-arithmetic]] · [[fundamental-theorem-of-arithmetic]]

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
