---
type: concept
category: mathematics
defines: ["Fibonacci sequence", "Fibonacci numbers"]
related: ["[[pascal-triangle]]", "[[spiral]]", "[[golden-ratio]]", "[[recurrence-relation]]", "[[exponential-function]]"]
requires: ["[[number-theory]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Fibonacci Sequence

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Fibonacci sequence** is the integer sequence defined by the recurrence $F(n) = F(n-1) + F(n-2)$ with $F(1) = 1$ and $F(2) = 1$, yielding 1, 1, 2, 3, 5, 8, 13, 21, ... This seemingly simple recurrence produces numbers ubiquitous in nature—spiral seed arrangements in sunflowers, the branching of trees, the spirals of shells—and connects to the golden ratio, making it one of the most recognizable sequences in mathematics.

## you gotta know

- The **Fibonacci sequence** grows exponentially, with $F(n) \approx \phi^n / \sqrt{5}$, where $\phi = (1 + \sqrt{5})/2$ is the golden ratio.
- The ratio of consecutive Fibonacci numbers, $F(n+1)/F(n)$, converges to the golden ratio $\phi \approx 1.618$.
- Fibonacci numbers appear hidden in [[pascal-triangle]]: the diagonals sum to Fibonacci numbers.
- The sequence satisfies the closed-form *Binet's formula*: $F(n) = (\phi^n - (1-\phi)^n) / \sqrt{5}$.
- Fibonacci numbers are intimately connected to the golden spiral and logarithmic [[spiral|spirals]] in nature.
- The sequence has deep connections to number theory: gcd(F(m), F(n)) = F(gcd(m,n)), and Fibonacci numbers exhibit divisibility properties.
- Fibonacci recurrence appears in combinatorics: the number of ways to tile a $1 \times n$ board with $1 \times 2$ dominoes is $F(n+1)$.
- Every positive integer can be uniquely represented as a sum of non-consecutive Fibonacci numbers (Zeckendorf's theorem), connecting the sequence to number systems.
- Fibonacci numbers appear in plant phyllotaxis, branching patterns, and seed arrangements—demonstrating nature's preference for mathematical optimization.
- The generalized Fibonacci sequence (with different initial conditions) and Lucas numbers provide extensions useful in number theory and algebraic geometry.

## connections

- [[pascal-triangle]] — Fibonacci numbers appear along diagonals of Pascal's triangle.
- [[spiral]] — the Fibonacci sequence generates logarithmic spirals found throughout nature.
- [[golden-ratio]] — the limit of ratios of consecutive Fibonacci numbers.
- [[recurrence-relation]] — the Fibonacci sequence is the canonical example of a linear recurrence.
- [[exponential-function]] — Fibonacci numbers grow exponentially like powers of the golden ratio.

## see also

- [[pascal-triangle]] · [[spiral]] · [[golden-ratio]] · [[recurrence-relation]]

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
