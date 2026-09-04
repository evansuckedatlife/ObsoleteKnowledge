---
type: concept
category: mathematics
defines: [Diophantine equation, Diophantine equations]
related: ["[[number-theory]]", "[[modular-arithmetic]]", "[[fundamental-theorem-of-arithmetic]]", "[[euclid]]", "[[decision-problem]]", "[[pierre-de-fermat]]", "[[andrew-wiles]]"]
requires: ["[[number-theory]]", "[[polynomial-function]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Diophantine Equation

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **Diophantine equation** is an algebraic equation—most commonly a [[polynomial-function]] in two or more variables—for which solutions are restricted exclusively to integers or rational numbers. Originating in *ancient Greece* with the third-century mathematician *Diophantus of Alexandria* in his pioneering treatise *Arithmetica*, these equations lie at the historical core of modern [[number-theory]]. Their deceptive simplicity often conceals profound mathematical depth, inspiring major advancements across algebra, geometry, and logic while establishing fundamental boundaries in computability.

## you gotta know

- Named for the Hellenistic mathematician *Diophantus of Alexandria*, whose foundational text *Arithmetica* systematically investigated systems of indeterminate equations seeking rational and integer solutions.
- The simplest non-trivial class consists of linear equations of the form $ax + by = c$, which possess integer solutions if and only if the greatest common divisor of $a$ and $b$ divides $c$, an analysis enabled by the algorithmic methods of [[euclid]] and *Bézout's identity*.
- *Fermat's Last Theorem*, famously conjectured by *Pierre de Fermat* in the margin of his copy of *Arithmetica*, asserted that $x^n + y^n = z^n$ has no positive integer solutions for integer exponents $n > 2$, defying proof until resolved by *Andrew Wiles* using [[modular-forms]] and [[elliptic-curves]].
- *Hilbert's Tenth Problem*, presented by *David Hilbert* at the 1900 International Congress of Mathematicians, asked for a universal mechanical algorithm capable of deciding whether an arbitrary Diophantine equation has integer solutions, framed today as a formal [[decision-problem]].
- The algorithmic solvability of the general problem was proven impossible in 1970 through the *MRDP theorem*, completed by *Yuri Matiyasevich* following critical groundwork by *Martin Davis*, *Hilary Putnam*, and *Julia Robinson*, demonstrating that recursively enumerable sets are Diophantine and tying arithmetic intimately to the limits of a [[turing-machine]].
- *Pell's equation*, a classic quadratic form written as $x^2 - d y^2 = 1$ for a non-square positive integer $d$, admits infinitely many integer solutions systematically generated from the periodic continued fraction expansion of $\sqrt{d}$.
- The *Catalan conjecture*, posed by *Eugène Charles Catalan* in 1844 and resolved by *Preda Mihăilescu* in 2002, proved that $8$ and $9$ are the only consecutive non-zero integer powers, establishing $3^2 - 2^3 = 1$ as the unique solution to $x^a - y^b = 1$ for $x, y, a, b > 1$.
- Modern investigations often rely on *local-global principles*, such as the *Hasse principle*, which tests whether equations that have real solutions and solutions in [[modular-arithmetic]] for every prime power must necessarily possess a global integer solution.

## connections

- [[number-theory]] — the branch of pure mathematics devoted to integer properties, divisibility, and Diophantine analysis.
- [[modular-arithmetic]] — provides essential congruence obstructions modulo prime powers to disprove the existence of integer solutions.
- [[fundamental-theorem-of-arithmetic]] — guarantees unique factorization into prime numbers, enabling algebraic factorization of equations into integer divisors.
- [[polynomial-function]] — defines the algebraic expressions whose integer zeros and solution sets are classified in Diophantine geometry.
- [[euclid]] — introduced the classical Euclidean algorithm used to resolve linear Diophantine equations and find greatest common divisors.
- [[decision-problem]] — frames *Hilbert's Tenth Problem* regarding the algorithmic decidability of integer solvability.
- [[turing-machine]] — provides the theoretical framework of computability underpinning the undecidability of the *MRDP theorem*.

## see also

- [[modular-arithmetic]] · [[number-theory]] · [[fundamental-theorem-of-arithmetic]] · [[decision-problem]]

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
