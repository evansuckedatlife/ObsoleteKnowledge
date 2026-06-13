---
type: term
category: science
defines: [Recursion, recursive]
related: ["[[algorithm]]", "[[divide-and-conquer]]", "[[dynamic-programming]]"]
lists: ["[[programming-terms]]"]
read: false
---

# Recursion

## summary

*Recursion* is a programming technique where a function calls itself to solve a problem by breaking it into smaller, self-similar subproblems. Each recursive call operates on a smaller or simpler input until reaching a *base case* that terminates the process. Recursion is powerful for problems with inherent recursive structure—trees, fractals, factorial computation—and directly mirrors mathematical induction.

## you gotta know

### Core Mechanism
- A recursive function must have a *base case* (termination condition) and a *recursive case* (self-call on smaller input).
- Without a proper base case, recursion runs forever and causes a *stack overflow*.
- Each recursive call consumes *stack memory*; deep recursion can exhaust available stack.

### Classic Examples
- *Factorial*: n! = n × (n-1)!, with base case 0! = 1.
- *Fibonacci*: fib(n) = fib(n-1) + fib(n-2), base cases fib(0)=0, fib(1)=1.
- *Tree traversal*: visit node, then recursively visit left and right subtrees.
- *Backtracking*: explore all paths via recursion, undo (backtrack) when reaching dead ends.

### Optimization Strategies
- *Memoization*: cache results of subproblems to avoid redundant recursive calls—transforms naive exponential recursion into polynomial time.
- *Tail recursion*: when the recursive call is the last operation; some compilers optimize this to a loop, avoiding stack growth.
- *Iteration*: manually maintain a stack to simulate recursion when recursion is deep or unavailable in the language.

### Conceptual Strengths
- Elegant expression of problems with recursive structure (trees, graphs, divide-and-conquer).
- Easier to reason about mathematically; mirrors problem definition.
- Promotes modular thinking: solve a small case, trust the recursion handles larger ones.

## context

Recursion is central to computer science education because it embodies two profound ideas: self-reference and reduction to a simpler problem. It appears everywhere: parsing nested syntax (compiler design), exploring network topology (graph algorithms), implementing undo/redo (stack-based history), and building search trees in games and constraint solvers. However, recursion isn't always the best tool—iterative solutions are often faster and more memory-efficient. The skill is knowing when recursive elegance is worth the trade-off.

## connections

- [[algorithm]] — recursion is a fundamental algorithmic technique.
- [[divide-and-conquer]] — exploits recursive structure by dividing and conquering.
- [[dynamic-programming]] — memoization combines recursion with caching for efficiency.
- [[tree-data-structure]] — tree operations are naturally recursive.
- [[backtracking]] — recursive exploration of solution spaces.
- [[lambda-calculus]] — recursion defined formally via fixed-point combinators.

## see also

- [[divide-and-conquer]] · [[dynamic-programming]] · [[tree-data-structure]]

<!-- footer -->

---

Lists: [[programming-terms]] · Mark read: `INPUT[toggle:read]`
