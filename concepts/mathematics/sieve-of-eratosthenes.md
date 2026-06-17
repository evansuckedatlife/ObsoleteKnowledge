---
type: concept
category: mathematics
defines: ["Sieve of Eratosthenes", "Sieve algorithm"]
related: ["[[prime-number-theorem]]", "[[infinitude-of-primes]]"]
requires: []
lists:
  - "[[statements-about-prime-numbers]]"
tour_order: 0
read: false
---

# Sieve of Eratosthenes

## summary

The Sieve of Eratosthenes is an ancient and highly efficient algorithm for finding all prime numbers up to any given limit. It works by iteratively marking the multiples of each prime number as composite, starting from the first prime number, 2. The numbers that remain unmarked at the end of the process are recognized as primes.

## you gotta know

- It is one of the oldest known algorithms for finding all small prime numbers up to a specified limit.
- The algorithm optimizes its search by stopping the marking of multiples when the square of the current prime exceeds the limit $n$ (i.e., $p^2 > n$), since any remaining composite numbers must have a smaller prime factor.
- It has a time complexity of $O(n \log \log n)$ operations, making it extremely fast for generating lists of primes, though it requires $O(n)$ space to store the status of each number.
- The algorithm is named after *Eratosthenes of Cyrene*, a Greek mathematician who is also famous for calculating the circumference of the Earth.
- Modern variants, such as segmented sieves, reduce the memory footprint by processing the range in smaller blocks, while the *Sieve of Atkin* uses modular arithmetic to achieve slightly better theoretical runtimes.

## connections

- [[fundamental-theorem-of-arithmetic]] — generates the prime factors that uniquely decompose integers.
- [[prime-number-theorem]] — helps analyze the proportion of numbers that remain unmarked by the sieve.
- [[infinitude-of-primes]] — shows that running the sieve indefinitely will continuously yield new prime numbers.
- [[primality-testing]] — provides a deterministic way to find primes, contrasting with modern randomized tests.

## see also

- [[fundamental-theorem-of-arithmetic]] · [[prime-number-theorem]] · [[primality-testing]]

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
