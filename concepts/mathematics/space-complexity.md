---
type: term
category: mathematics
defines:
  - "Space complexity"
  - Space complexity
related: ["[[time-complexity]]", "[[p-complexity-class]]", "[[np-complexity-class]]", "[[turing-machine]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Space Complexity

## summary

**Space complexity** measures the amount of memory (auxiliary storage) an algorithm uses as a function of input size, expressed in Big O notation (`O(1)`, `O(log n)`, `O(n)`, etc.). While time complexity dominates practical concern, space complexity is critical for resource-constrained systems and theoretical understanding of computational limits.

## you gotta know

- Measures the maximum amount of extra memory (tape cells on a Turing machine) needed, as a function of input size `n`.
- **Constant space** (`O(1)`): algorithms using a fixed amount of memory regardless of input (e.g., comparing two numbers).
- **Logarithmic space** (`O(log n)`): many divide-and-conquer algorithms; more efficient than linear.
- **Linear space** (`O(n)`): many sorting and tree algorithms; proportional to input size.
- **Exponential space** (`O(2^n)`): infeasible for large inputs; some exhaustive search and dynamic programming solutions.
- **PSPACE** is the class of problems solvable with polynomial space (may take exponential time); **P ⊆ NP ⊆ PSPACE** (all proven).
- **Space-time tradeoff**: often can reduce space by using more time (e.g., recomputing values instead of storing them) or vice versa.
- **Savitch's theorem**: nondeterministic space is at most quadratic worse than deterministic; `NSPACE(f(n)) ⊆ DSPACE(f(n)²)`.

## connections

- [[time-complexity]] — dual measure of efficiency; often a tradeoff between time and space.
- [[p-complexity-class]] — problems in **P** use polynomial time; their space is typically polynomial too.
- [[np-complexity-class]] — **NP ⊆ PSPACE** proven; NP problems use at most polynomial space.
- [[turing-machine]] — space complexity is measured on Turing machines via tape usage.

## see also

- [[time-complexity]] · [[p-complexity-class]] · [[np-complexity-class]] · [[turing-machine]]

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

Lists:  · Mark read: `INPUT[toggle:read]`
