---
type: term
category: science
defines: [Type system, typing, static typing, dynamic typing]
related: ["[[programming-language]]", "[[compiler]]", "[[object-oriented-programming]]"]
requires: []
lists: ["[[programming-terms]]"]
tour_order: 0
read: false
---

# Type system

## summary

A *type system* is a set of rules determining which operations are valid on which data, preventing certain kinds of errors. Types classify values (integers, strings, booleans, objects) and enforce constraints on how they can be combined. A language's type system ranges from *static* (types checked at compile time) to *dynamic* (checked at runtime), and from *weak* (lenient coercion) to *strong* (strict rules). Well-designed type systems catch bugs early and serve as executable documentation.

## you gotta know

### Static vs. Dynamic
- *Statically typed*: type of every variable determined before execution; errors caught at compile time (Java, C++, Rust).
- *Dynamically typed*: types determined at runtime; errors caught when code runs (Python, JavaScript, Ruby).
- *Static*: safer (errors early), verbose (type annotations), better performance (no runtime type checks).
- *Dynamic*: flexible (no annotations), rapid development, slower (runtime checks), errors harder to debug.

### Strong vs. Weak
- *Strong typing*: operations respect type boundaries; 5 + "string" is an error.
- *Weak typing*: implicit coercion allowed; 5 + "5" may become "55" (concatenation) or 10 (addition).
- *Strong* prevents unexpected conversions; *weak* offers convenience but hides bugs.

### Type Inference
- Compiler deduces types without explicit annotations (Rust, Haskell, even modern Python via type hints).
- Reduces boilerplate while preserving safety of static typing.
- Example: `let x = 5;` compiler infers x is an integer without declaration.

### Advanced Type Concepts
- *Generics*: functions or classes parameterized by type; reuse code for multiple types (List<Integer>, List<String>).
- *Union types*: a value can be one of several types (TypeScript, Rust's enum).
- *Nullable types*: explicit distinction between T and Optional<T>; Rust's Option<T>, Kotlin's T?.
- *Type narrowing*: refining a variable's type in a conditional branch.

### Common Type System Rules
- *Compatibility*: can a value of type A be used where type B is expected? (subtyping, covariance).
- *Assignment*: rules for assigning values to variables.
- *Function parameters and returns*: parameter types constrain arguments; return types enable composition.
- *Method resolution*: which method is called depends on the receiver type (polymorphism).

### Benefits & Trade-offs
- *Benefits*: catch errors at compile time, enable optimizations, self-documenting code.
- *Trade-offs*: static typing requires annotations (verbosity); dynamic typing allows runtime discovery (flexibility).
- *Sweet spot*: type inference in statically typed languages reduces annotation burden while preserving safety.

## context

Type systems are a subtle and powerful tool in programming language design. The choice between static and dynamic typing shapes how you debug, refactor, and reason about code. Static typing is indispensable for large teams and long-lived codebases; dynamic typing shines in rapid prototyping and data-science scripts. Modern languages increasingly converge: Python added optional type hints (mypy); JavaScript has TypeScript; even Ruby has type checkers. Understanding type system design—variance, subtyping, generics, dependent types—opens doors to advanced language features and helps you write polymorphic code that is both safe and reusable. For teams adopting static typing, investing in good type design pays dividends in code clarity and maintainability.

## connections

- [[programming-language]] — type system is a core language design choice.
- [[compiler]] — compilers enforce and check type rules.
- [[object-oriented-programming]] — class hierarchies and subtyping are part of type systems.
- [[functional-programming]] — FP relies on strong static typing for safety; algebraic data types.
- [[algorithm]] — algorithm correctness often depends on respecting type constraints.

## see also

- [[programming-language]] · [[compiler]] · [[object-oriented-programming]]

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
