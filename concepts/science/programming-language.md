---
type: term
category: science
defines: [Programming language, language]
related: ["[[compiler]]", "[[type-system]]", "[[object-oriented-programming]]", "[[functional-programming]]"]
requires: []
lists: ["[[programming-terms]]"]
tour_order: 0
read: false
---

# Programming language

## summary

A *programming language* is a formal system of communication with a computer, consisting of syntax (grammatical rules), semantics (meaning of constructs), and pragmatics (how programs are run). Languages range from low-level (assembly, close to CPU instructions) to high-level (Python, JavaScript, abstracted from hardware details). Every language embodies design choices about type systems, memory management, concurrency, and abstraction—choices that influence how you think and solve problems.

## you gotta know

### Language Levels
- *Machine code*: raw binary instructions executed by the CPU; tedious and hardware-specific.
- *Assembly*: symbolic names for machine code; still low-level but readable.
- *High-level languages*: Python, Java, C++; closer to human notation, require compilation or interpretation.
- *Domain-specific languages* (DSLs): SQL, Regex, HTML; optimized for a specific problem class.

### Execution Models
- *Compiled*: source code translated to machine code before execution (C, C++, Rust); fast, but compile step required.
- *Interpreted*: source code read and executed step-by-step at runtime (Python, JavaScript); flexible but slower.
- *Just-in-time (JIT)*: hybrid; code compiled during execution (Java, C#); balances speed and flexibility.

### Type Systems
- *Statically typed*: types checked at compile time (Java, C++, Rust); catches errors early, verbose.
- *Dynamically typed*: types checked at runtime (Python, JavaScript); flexible, prone to runtime errors.
- *Strongly typed*: strict type rules; operations on incompatible types fail.
- *Weakly typed*: loose type coercion; implicit conversions can hide bugs.

### Memory Management
- *Manual*: programmer allocates and deallocates memory (C, C++); efficient but error-prone.
- *Garbage collection*: automatic reclamation of unused memory (Java, Python); safer but adds runtime overhead.
- *Ownership model*: enforced by compiler (Rust); memory-safe without GC overhead.

### Programming Paradigms
- *Imperative*: sequences of statements that modify state (C, Python).
- *Object-oriented*: organize code around objects with data and methods (Java, Python, C++).
- *Functional*: functions as first-class values; emphasize immutability (Lisp, Haskell, ML).
- *Declarative*: describe *what* to compute, not *how* (SQL, Prolog).

## context

The choice of programming language shapes your solution space. A language with strong static typing encourages careful design; a dynamically typed language with closures promotes functional techniques. Systems programming (OS, embedded, high-performance) demands low-level languages like C and Rust. Web frontends benefit from JavaScript's event-driven model. Data science leans Python for its ecosystem and readability. Understanding language design—trade-offs in type systems, memory models, concurrency primitives—gives you intuition for why languages differ and which tool fits which job. Most expert programmers know multiple languages deeply, not to be versatile for its own sake, but to understand the landscape of linguistic possibilities.

## connections

- [[compiler]] — translates language to executable form.
- [[type-system]] — a core design choice in every language.
- [[object-oriented-programming]] — a major paradigm realized in many languages.
- [[functional-programming]] — another major paradigm; some languages emphasize it.
- [[data-structure]] — language choice influences which data structures are idiomatic.

## see also

- [[compiler]] · [[type-system]] · [[object-oriented-programming]] · [[functional-programming]]

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
