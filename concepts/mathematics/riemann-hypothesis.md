---
type: concept
category: mathematics
defines: ["Riemann Hypothesis", "Riemann Zeta Function"]
related: ["[[prime-number-theorem]]", "[[complex-analysis]]", "[[millennium-prize-problems]]"]
requires: []
lists:
  - "[[statements-about-prime-numbers]]"
tour_order: 0
read: false
---

# Riemann Hypothesis

## summary

The Riemann Hypothesis is one of the most famous and profound unsolved problems in mathematics, conjecturing that all non-trivial zeros of the Riemann zeta function lie on a single vertical line in the complex plane. Proposed by Bernhard Riemann in his seminal 1859 paper, the hypothesis provides deep insight into the distribution of prime numbers. If true, it would establish the tightest possible bounds on the error term of the prime number theorem and confirm that prime numbers are distributed as regularly as possible. Due to its foundational status and difficulty, it has been designated as one of the seven Millennium Prize Problems, carrying a one-million-dollar reward for its resolution.

## you gotta know

### the zeta function & zeros

- *Riemann Zeta Function*: The function $\zeta(s) = \sum_{n=1}^\infty n^{-s}$ is defined for complex numbers with real part $> 1$ and can be analytically continued to the entire complex plane (except for a simple pole at $s = 1$).
- *Trivial Zeros*: The function has "trivial" zeros at all negative even integers ($s = -2, -4, -6, \dots$).
- *Critical Strip & Critical Line*: The "non-trivial" zeros lie within the critical strip $0 < \text{Re}(s) < 1$. The Riemann Hypothesis asserts that all these non-trivial zeros actually lie on the critical line $\text{Re}(s) = 1/2$.

### connections to prime numbers

- *Prime Number Theorem Link*: Riemann showed that the distribution of primes is intimately linked to the locations of the non-trivial zeros; the proof of the Prime Number Theorem relies on showing that no zeros lie on the boundary lines $\text{Re}(s) = 1$ and $\text{Re}(s) = 0$.
- *Error Term Bounds*: If the hypothesis is true, the number of primes up to $x$, denoted $\pi(x)$, is approximated by the logarithmic integral $\text{Li}(x)$ with an error term bounded by $O(\sqrt{x} \log x)$, the optimal possible bound.
- *Equivalent Formulations*: The hypothesis is equivalent to statements about the growth of the Mobius function (specifically, Mertens conjecture, though Mertens itself was disproven, the bound $M(x) = O(x^{1/2 + \epsilon})$ is equivalent to RH) and the divisor function (Robin's theorem).

### computational & physical aspects

- *Numerical Verification*: Computational searches have verified that the first 10 trillion non-trivial zeros lie precisely on the critical line, but this does not constitute a mathematical proof.
- *Hilbert-Polya Conjecture*: Suggests that the zeros of the zeta function correspond to the eigenvalues of a self-adjoint operator on a Hilbert space, which has connected RH to quantum mechanics and random matrix theory.
- *Millennium Prize*: The Clay Mathematics Institute named the Riemann Hypothesis one of the seven Millennium Prize Problems in 2000, offering a \$1 million reward for its proof or disproof.

## connections

- [[prime-number-theorem]] — RH provides the optimal error bound for the prime density function.
- [[infinitude-of-primes]] — the Euler product formula for the zeta function connects it directly to all primes.
- [[dirichlets-theorem-on-arithmetic-progressions]] — uses Dirichlet L-functions, which generalize the Riemann zeta function.
- [[goldbach-conjecture]] — another famous unsolved prime conjecture, related through analytic methods.
- [[twin-prime-conjecture]] — prime gaps are bounded and studied using tools from the zeta function.
- [[sieve-of-eratosthenes]] — prime generation algorithm that contrasts with analytic prime distribution models.

## context

The Riemann Hypothesis is widely regarded as the holy grail of modern pure mathematics, as hundreds of mathematical theorems begin with the clause "Assuming the Riemann Hypothesis is true." Its formulation in 1859 marked the birth of analytic number theory, transforming the study of discrete prime numbers through the continuous tools of complex analysis. In quiz bowl, the hypothesis and the zeta function are frequent subjects, with clues focusing on the definition of the critical line, trivial vs. non-trivial zeros, its equivalent formulation via Robin's inequality, or the Hilbert-Polya conjecture linking it to physical spectral operators.

## see also

- [[prime-number-theorem]] · [[infinitude-of-primes]] · [[millennium-prize-problems]]

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
