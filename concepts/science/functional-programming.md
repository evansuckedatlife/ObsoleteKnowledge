---
type: term
category: science
defines: [Functional programming, FP, functional]
related: ["[[programming-language]]", "[[object-oriented-programming]]", "[[lambda-calculus]]", "[[logic]]"]
requires: []
lists: ["[[programming-terms]]"]
tour_order: 0
read: false
---

# Functional programming

## summary

*Functional programming* (FP) is a paradigm that treats computation as the evaluation of mathematical functions, emphasizing *immutability* (data doesn't change), *pure functions* (no side effects), and *first-class functions* (functions as values). FP avoids mutable state and shared memory, which reduces bugs in concurrent systems. Languages like Haskell, Lisp, and ML are purely functional; others like Python, JavaScript, and Rust support functional techniques alongside imperative or OOP styles.

## you gotta know

### Core Principles
- *Pure function*: same input always produces the same output; no side effects (no state modification, I/O, or randomness).
- *Immutability*: data, once created, never changes; modifications create new data structures.
- *First-class functions*: functions are values; can be passed as arguments, returned from functions, stored in variables.
- *Higher-order functions*: functions that take or return other functions (map, filter, reduce).

### Key Techniques
- *Map*: apply a function to each element of a collection, returning a new collection.
- *Filter*: select elements matching a predicate.
- *Reduce* (fold): combine elements iteratively to produce a single value.
- *Recursion*: iteration via function calls; loops are rare in pure FP.
- *Lazy evaluation*: compute values only when needed; avoids unnecessary work.

### Functional Data Structures
- *Linked lists*: naturally functional; cons (prepend) creates a new list sharing the tail.
- *Persistent data structures*: support multiple versions in memory efficiently via structural sharing.
- *Algebraic data types*: tagged unions allowing pattern matching (Rust, Haskell, Scala).

### Advantages
- *Concurrency safety*: immutability eliminates race conditions and lock contention.
- *Testability*: pure functions are deterministic; no hidden state to mock.
- *Composability*: functions combine naturally; function composition mirrors mathematical composition.
- *Parallel evaluation*: pure functions can be parallelized without synchronization.

### Challenges
- *Learning curve*: unfamiliar if your background is imperative; requires rethinking state management.
- *Performance*: immutability and recursion can incur overhead; lazy evaluation complicates debugging.
- *I/O and state*: necessary for real systems; FP handles these via monads or effect systems (complex).

## context

Functional programming is not new—Lisp predates most imperative languages—but it has surged in relevance with the rise of concurrent and distributed systems. Immutable, side-effect-free code is easier to reason about in multi-threaded environments. JavaScript's map/filter/reduce became a lingua franca for data transformation; Python embraced lambda and functional idioms. Rust's ownership model enforces a form of functional discipline. Even Java added streams and functional interfaces to accommodate FP patterns. The practical convergence is *multiparadigm*: most modern languages support OOP, imperative loops, and functional techniques. The skill is using each paradigm where it shines, rather than dogmatically adhering to one.

## connections

- [[programming-language]] — most modern languages support functional idioms.
- [[object-oriented-programming]] — contrasting paradigm; modern languages blend both.
- [[lambda-calculus]] — mathematical foundation of functional programming.
- [[recursion]] — iteration in FP is achieved via recursion.
- [[algorithm]] — algorithm design is orthogonal to paradigm; sort algorithm works in FP or OOP.

## see also

- [[object-oriented-programming]] · [[programming-language]] · [[lambda-calculus]]

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

Lists: [[programming-terms]] · Mark read: `INPUT[toggle:read]`
