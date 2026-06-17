---
type: term
category: mathematics
defines:
  - P
  - P (complexity class)
  - Polynomial time
related: ["[[np-complexity-class]]", "[[np-complete]]", "[[decision-problem]]", "[[time-complexity]]"]
requires: ["[[algorithm]]"]
lists: []
tour_order: 6
read: true
---

# P (Complexity Class)


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**P** (polynomial time) is the complexity class of decision problems solvable by a deterministic algorithm in polynomial time—that is, in a number of steps bounded by a polynomial function of the input size. It represents the realm of computationally *feasible* or *tractable* problems and is one of the two central classes in the **P vs. NP** problem, the most important open question in computer science. Understanding **P** is essential to grasping computational feasibility and the limits of known algorithms.

## you gotta know

### Definition and Characterization
- **P** stands for "polynomial time"; formally, it is the set of decision problems (languages) decidable by a deterministic Turing machine in `O(n^k)` time for some fixed constant `k` (independent of the input *n*).
- A problem is in **P** if there exists an algorithm that, for any input of size *n*, returns a yes/no answer in at most `cn^k` steps for constants *c*, *k*.
- *Deterministic*: the Turing machine follows a unique computational path (unlike nondeterministic machines, which explore multiple paths in parallel).
- *Decision problem*: the output is yes or no; optimization variants (find the best solution) are outside **P** by definition, though related.

### Examples of **P** Problems
- *Sorting*: given an array, sort it in O(n log n) time (e.g., merge sort, quicksort).
- *Searching*: given a sorted array and a target, find it via binary search in O(log n).
- *Graph reachability*: is there a path from vertex *u* to vertex *v*? Solvable in O(*n* + *m*) time via BFS/DFS.
- *Primality testing*: is *n* prime? Solvable in polynomial time via the AKS primality test (though not the simplest method in practice).
- *Integer multiplication*: multiply two *n*-bit integers in O(*n*²) time (or faster via Karatsuba, Strassen).
- *Greatest common divisor*: Euclidean algorithm in O(log min(*a*, *b*)) time.

### Relationship to Other Complexity Classes
- **P ⊆ NP** (proven): every problem solvable in polynomial time is also verifiable in polynomial time—if you can solve it, you can verify it.
- **P ⊆ EXPTIME** (proven): polynomial-time problems are solved faster than exponential-time.
- **NP ⊆ PSPACE** (proven): nondeterministic polynomial-time problems fit in polynomial space (often with exponential time).
- **P vs. NP** is open: it is unknown whether **P = NP**; if true, then every verifiable problem is solvable, a revolutionary result that would break modern cryptography.

### The Hardness and Importance of **P = NP?**
- *Millennium Prize Problem*: the Clay Mathematics Institute offers a $1 million reward for proving or disproving **P = NP**.
- *Cryptographic implications*: if **P = NP**, then integer factorization (underlying RSA) would be solvable in polynomial time, destroying modern encryption. Conversely, if **P ≠ NP**, then one-way functions exist, justifying cryptography.
- *Optimization implications*: thousands of optimization problems (knapsack, traveling salesman, graph coloring) are NP-complete; if **P = NP**, all would be efficiently solvable.
- *Practical assumption*: cryptography, computational complexity theory, and algorithm research all assume **P ≠ NP** (though unproven).

## context

**P** is the foundation of computational feasibility. In the absence of the ability to actually run exponential-time algorithms (which blow up for *n* > 20–30), polynomial time is the practical boundary of what is considered "solvable" in computer science. The class **P** emerged formally in the 1970s (Cook, Karp) and immediately became central to understanding algorithm design and computational limits. The **P vs. NP** problem captures the essential mystery: can verification (a seemingly easier task) be as hard as solving from scratch? If not, an enormous class of practical problems (optimization, constraint satisfaction, combinatorial search) would unlock. If yes, then cryptography and many heuristic algorithms are justified. **P** appears in every complexity-theory context and in quiz bowl whenever computational feasibility or the hardness of a specific problem is discussed.

## connections

- [[np-complexity-class]] — the potentially larger class of verifiable problems; equality with **P** is open.
- [[np-complete]] — the hardest problems in **NP**; if any is in **P**, then **P = NP**.
- [[np-hard]] — problems at least as hard as **NP**-complete; need not be in **NP** themselves.
- [[decision-problem]] — **P** is defined for decision/language problems (yes/no answers).
- [[turing-machine]] — **P** is formally defined via deterministic Turing machines.
- [[time-complexity]] — **P** is the class of problems solvable in polynomial time complexity.
- [[algorithm]] — algorithms with polynomial-time bounds belong to **P**; the existence of polynomial-time algorithms is the question.
- [[rsa-cryptography]] — depends on the assumption that integer factorization is not in **P**.

## see also

- [[np-complexity-class]] · [[np-complete]] · [[np-hard]] · [[decision-problem]]

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
