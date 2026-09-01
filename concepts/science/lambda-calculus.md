---
type: concept
category: science
defines: ["Lambda calculus", "λ-calculus"]
related: ["[[functional-programming]]", "[[recursion]]", "[[computability]]", "[[turing-machine]]", "[[formal-logic]]", "[[church-turing-thesis]]", "[[fixed-point-combinator]]"]
requires: ["[[functional-programming]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Lambda Calculus

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Lambda calculus** is a formal system in mathematical logic for expressing computation using function abstraction and application, developed by Alonzo Church in the 1930s. It shows that any computable function can be expressed and evaluated using only function definitions and substitution, providing a theoretical foundation for functional programming and proving equivalent in power to the Turing machine. Lambda calculus underpins languages like Lisp, Haskell, and Scheme, and remains central to computer science theory and proof verification.

## you gotta know

- The core syntax is minimal: *variables* (x, y), *abstractions* (λx.M, meaning "a function of x that returns M"), and *applications* (M N, meaning "apply function M to argument N").
- *Beta reduction* is the evaluation rule: applying a function (λx.M) to an argument N substitutes N for all free occurrences of x in M, written (λx.M)N → M[N/x]. It is the only reduction rule needed.
- *Recursion* is expressed using *fixed-point combinators* (like the Y combinator), which allow a function to reference itself without explicit naming. This shows that recursion is not primitive—it emerges from function application.
- *Church numerals* encode integers as functions: 0 = λf.λx.x (returns x unchanged), 1 = λf.λx.f x (applies f once), etc. Arithmetic operations are defined as functions operating on these encodings.
- Lambda calculus is *Turing-complete*: any problem computable by a Turing machine is computable in lambda calculus, and vice versa (*Church-Turing thesis*). This equivalence shows multiple models of computation are fundamentally equivalent.
- *Higher-order functions* (functions that take or return other functions) are native to lambda calculus, enabling elegant abstractions like currying (breaking multi-argument functions into chains of single-argument functions) and function composition.

- Combinatory logic is related: instead of lambda abstractions, combinators (like K, S, I) combine to express computation. Both lambda calculus and combinatory logic are Turing-complete.
- Type systems in languages like Haskell add types to lambda calculus, enabling compile-time error checking while preserving its elegance. Untyped lambda calculus has no type constraints.
- Lazy evaluation (used in Haskell) defers computation until results are needed, unlike eager evaluation. Lambda calculus formalizes both strategies, showing they produce the same results (confluence property).

## connections

- [[functional-programming]] — the programming paradigm based on lambda calculus principles; functions as first-class objects.
- [[recursion]] — expressed formally in lambda calculus via fixed-point combinators; shown to emerge from function application.
- [[computability]] — lambda calculus defines what is computable; Church's thesis equates its power to Turing machines.
- [[turing-machine]] — an alternative formal model of computation; Church-Turing thesis proves lambda calculus and Turing machines are equivalent.
- [[church-turing-thesis]] — the conjecture that lambda calculus and Turing machines capture all computable functions.
- [[formal-logic]] — lambda calculus is grounded in logic; it shows how to express logical proofs as computational processes (Curry-Howard correspondence).
- [[fixed-point-combinator]] — the tool enabling recursion in lambda calculus without explicit self-reference.

## see also

- [[functional-programming]] · [[recursion]] · [[computability]] · [[turing-machine]]

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

Lists: [[science-hubs]] · Mark read: `INPUT[toggle:read]`
