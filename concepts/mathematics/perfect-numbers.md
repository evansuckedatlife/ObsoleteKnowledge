---
type: term
category: mathematics
defines: [Perfect number, perfect integers]
related: ["[[number-theory]]", "[[divisor]]", "[[mersenne-primes]]", "[[euclid-euler-theorem]]", "[[aliquot-sum]]"]
lists: []
read: false
---

# Perfect Numbers

## summary

A **perfect number** is a positive integer equal to the sum of its proper divisors (all divisors except the number itself). The first perfect number is 6 = 1 + 2 + 3. Perfect numbers are exceedingly rare—only 51 are known, the largest having over 41 million digits. They carry deep historical and mystical significance, studied since antiquity, and are intimately connected to **Mersenne primes** through the Euclid-Euler theorem.

## you gotta know

- **Definition**: a perfect number n satisfies σ(n) − n = n, where σ(n) is the sum of all divisors. Equivalently, the sum of proper divisors equals n.
- The first four perfect numbers are **6**, **28**, **496**, and **8128**—each separated by centuries of searching.
- All known perfect numbers are *even*; whether odd perfect numbers exist remains an unsolved problem (if one exists, it must exceed 10^1500).
- **Euclid-Euler theorem**: an even number is perfect if and only if it has the form 2^(p-1) · (2^p − 1), where 2^p − 1 is a Mersenne prime.
- Because of the theorem, finding perfect numbers reduces to finding Mersenne primes; computationally, this is done via the **Lucas-Lehmer test**.
- The 51st known perfect number (discovered in 2018) has 49,724,095 digits—so large that writing it out would fill a million pages.
- **Aliquot sums** generalise the concept: a number's aliquot sum is the sum of its proper divisors; perfect numbers have aliquot sum equal to themselves.

## connections

- [[number-theory]] — perfect numbers are a central topic in the study of integers.
- [[mersenne-primes]] — every even perfect number corresponds to a Mersenne prime via Euclid-Euler.
- [[euclid-euler-theorem]] — characterises all even perfect numbers via Mersenne primes.
- [[euclid]] — first proved that 2^(p-1) · (2^p − 1) is perfect when 2^p − 1 is prime.
- [[euler]] — completed the characterisation, proving the converse.
- [[divisor]] — proper divisors are summed to determine perfection.

## see also

- [[mersenne-primes]] · [[number-theory]] · [[euclid-euler-theorem]]

<!-- footer -->

---

Lists: Mark read: `INPUT[toggle:read]`
