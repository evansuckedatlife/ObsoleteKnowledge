---
type: term
category: science
defines: [Compiler, compilation]
related: ["[[programming-language]]", "[[type-system]]", "[[algorithm]]"]
lists: ["[[programming-terms]]"]
read: false
---

# Compiler

## summary

A *compiler* is a program that translates source code written in a high-level language into lower-level code (machine code, bytecode, or another language) that can be executed. The compilation process involves multiple phases: *lexical analysis* (tokenization), *parsing* (building syntax trees), *semantic analysis* (type checking), *optimization* (improving efficiency), and *code generation*. Compilers bridge the gap between human-readable programs and machine-executable instructions.

## you gotta know

### Compilation Phases
- *Lexical analysis*: break source code into tokens (keywords, identifiers, operators, literals).
- *Parsing*: organize tokens into a *parse tree* or *abstract syntax tree* (AST) respecting grammar rules.
- *Semantic analysis*: check type consistency, variable declarations, scope rules; build a symbol table.
- *Intermediate representation (IR)*: convert AST into a language-independent form for optimization.
- *Optimization*: eliminate dead code, inline functions, unroll loops, improve register allocation.
- *Code generation*: translate IR into target machine code or bytecode.

### Compilation vs. Interpretation
- *Compiled*: translate before execution; slower upfront, fast at runtime (C, C++, Rust).
- *Interpreted*: translate and execute on-the-fly; faster development, slower execution (Python, JavaScript).
- *Just-in-time (JIT)*: compile during execution; used by Java, C#, V8 (JavaScript); balances speed and flexibility.

### Compiler Optimizations
- *Constant folding*: evaluate constant expressions at compile time.
- *Dead code elimination*: remove unreachable or unused code.
- *Function inlining*: replace function calls with the function body to reduce overhead.
- *Loop unrolling*: replicate loop body multiple times to reduce branch overhead.
- *Register allocation*: assign variables to CPU registers; reduces memory access.

### Common Tools & Concepts
- *Parser generators*: tools like yacc, bison, ANTLR automate parser construction from grammar.
- *Lexer generators*: lex, flex generate tokenizers from regex patterns.
- *Intermediate languages*: LLVM IR (widely used), Java bytecode, WebAssembly; target-independent form.
- *Static analysis*: analyze code without running it; find bugs, prove properties.

### Error Detection & Reporting
- *Compile-time errors*: syntax, type, scope violations; caught by the compiler, no execution occurs.
- *Runtime errors*: exceptions, segfaults, division by zero; occur during execution (e.g., in interpreted languages).
- Good error messages (position, context, suggestions) are critical for developer productivity.

## context

A compiler is the gatekeeper between source code and execution. Understanding how compilers work—what they check, what they optimize, what they miss—is invaluable for writing efficient code. Type systems exist in compilers to catch bugs early. Performance-critical code demands knowledge of what the compiler produces (e.g., vectorization, inlining). Compiler design is also a fascinating corner of CS: parsing is a beautiful application of formal languages; optimization is a rich algorithmic field; code generation requires deep knowledge of machine architecture. Every modern language has a compiler or interpreter; studying compiler internals teaches profound lessons about computation itself.

## connections

- [[programming-language]] — compilers are the runtime for languages.
- [[type-system]] — compilers enforce type checking; type system design influences compiler complexity.
- [[algorithm]] — compiler construction uses parsing (recursive descent, shift-reduce), graph coloring for register allocation.
- [[formal-languages]] — grammars and parsing theory are core compiler foundations.

## see also

- [[programming-language]] · [[type-system]] · [[algorithm]]

<!-- footer -->

---

Lists: [[programming-terms]] · Mark read: `INPUT[toggle:read]`
