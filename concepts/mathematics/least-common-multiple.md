---
type: concept
category: mathematics
defines: [Least common multiple, LCM]
related: ["[[prime-factorization]]", "[[greatest-common-divisor]]", "[[divisibility]]"]
requires: ["[[prime-number]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Least Common Multiple

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **least common multiple (LCM)** of two or more integers is the smallest positive integer divisible by each of them. The LCM is a dual concept to the greatest common divisor (GCD): while GCD finds the largest common factor, LCM finds the smallest common multiple. Together, they encode the factorization structure underlying divisibility.

## you gotta know

- The **LCM** of *a* and *b* is the smallest positive integer *m* such that *a* | *m* and *b* | *m* (both divide *m*); denoted LCM(*a*, *b*) or lcm(*a*, *b*).
- *Formula via prime factorization*: if *a* = *p₁^{e₁}* · ... · *pₖ^{eₖ}* and *b* = *p₁^{f₁}* · ... · *pₖ^{fₖ}*, then LCM(*a*, *b*) = *p₁^{max(e₁,f₁)}* · ... · *pₖ^{max(eₖ,fₖ)}*.
- *Fundamental relationship*: LCM(*a*, *b*) · GCD(*a*, *b*) = *a* · *b*; both encode the prime factorization structure; knowing one determines the other.
- *Periodic cycles*: if events repeat every *a* and *b* time units respectively, they synchronize (occur together) every LCM(*a*, *b*) time units.
- *Fractions*: to add or compare *a*/*b* + *c*/*d*, convert to common denominator LCM(*b*, *d*); smallest common denominator minimizes arithmetic.
- *Efficient computation*: use Euclidean algorithm to find GCD(*a*, *b*) in O(log(min(*a*, *b*))) time, then LCM(*a*, *b*) = *a* · *b* / GCD(*a*, *b*).
- *Generalizations*: LCM extends to finite sets of integers, to polynomials over fields, and to ideals in abstract algebra; captures the notion of smallest common multiple in any ring.
- For more than two numbers, LCM(*a*, *b*, *c*) = LCM(LCM(*a*, *b*), *c*); useful in scheduling problems and finding common cycles in systems with multiple periodic components.
- In modular arithmetic, LCM(*a*, *b*) is the smallest positive *n* such that any value *x* congruent to *a* and *b* modulo their respective moduli must satisfy congruences modulo LCM(*a*, *b*).

## connections

- [[prime-factorization]] — LCM is computed by taking maximum exponents of prime factors.
- [[greatest-common-divisor]] — dual concept; together they characterize divisibility relationships.
- [[divisibility]] — LCM and GCD are the fundamental tools encoding divisibility structure.
- [[fundamental-theorem-of-arithmetic]] — the unique factorization that makes LCM computation via prime exponents work.
- [[modular-arithmetic]] — LCM determines the period of congruence cycles.

## see also

[[greatest-common-divisor]] · [[prime-factorization]] · [[divisibility]] · [[fundamental-theorem-of-arithmetic]]

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
