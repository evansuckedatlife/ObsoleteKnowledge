---
type: term
category: science
defines: [Object-oriented programming, OOP, object-oriented]
related: ["[[programming-language]]", "[[functional-programming]]", "[[type-system]]"]
lists: ["[[programming-terms]]"]
read: false
---

# Object-oriented programming

## summary

*Object-oriented programming* (OOP) is a paradigm that organizes code around *objects*—entities that bundle data (*state*) and behavior (*methods*) together. OOP emphasizes modularity, reusability, and extensibility through *encapsulation* (hiding internals), *inheritance* (code reuse via hierarchies), and *polymorphism* (objects responding differently to the same message). While powerful for large systems, OOP has trade-offs in complexity and sometimes enforces structures that may be unnatural for certain problems.

## you gotta know

### Four Pillars
- *Encapsulation*: bundle data and methods in a class; use access modifiers (public, private) to control visibility.
- *Abstraction*: hide implementation details; expose only necessary interfaces.
- *Inheritance*: derive new classes from existing ones; reuse and extend behavior.
- *Polymorphism*: objects of different types respond to the same method call differently (method overriding, interfaces).

### Core Concepts
- *Class*: template defining an object's structure and behavior; instances are *objects*.
- *Instance variable*: data associated with an object (state).
- *Method*: function associated with an object; operates on the object's state.
- *Constructor*: special method that initializes an object when created.
- *Static member*: data or method shared by all instances of a class (belongs to the class, not instances).

### Inheritance & Hierarchies
- *Single inheritance*: a class inherits from one parent (Java, C++, Python).
- *Multiple inheritance*: a class inherits from multiple parents (C++, Python); can cause ambiguity (diamond problem).
- *Interfaces*: contracts specifying methods without implementation; a class implements an interface.
- *Abstract classes*: partial implementation; cannot be instantiated, only inherited.

### Design Principles
- *DRY* (Don't Repeat Yourself): write code once, reuse via inheritance or composition.
- *SOLID*: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.
- *Composition over inheritance*: sometimes using objects as components is cleaner than deep hierarchies.

### Common Pitfalls
- *Tight coupling*: objects depend heavily on each other; refactoring breaks multiple places.
- *Deep inheritance hierarchies*: hard to understand and maintain; prefer shallow trees or composition.
- *Violation of Liskov Substitution Principle*: subclass doesn't properly replace parent; breaks polymorphism.

## context

OOP dominated software engineering for 30+ years and remains the paradigm of choice for large, team-developed systems: operating systems, game engines, enterprise applications. Its strength lies in modularity and the intuitive mapping between code and real-world entities (users, accounts, transactions). However, OOP is not a universal solution. Functional programming is gaining favor for concurrent and distributed systems where immutability and pure functions offer clarity. Modern languages often blend paradigms: Python supports OOP but encourages functional techniques; Rust uses OOP-like traits alongside functional patterns. The skill is knowing when OOP is the right fit and when its complexity is more burden than benefit.

## connections

- [[programming-language]] — most modern languages support OOP (Java, C++, Python, C#).
- [[functional-programming]] — contrasting paradigm; often combined in modern languages.
- [[type-system]] — OOP relies on class hierarchies and type checking.
- [[algorithm]] — algorithm choice is independent of paradigm, but OOP structures how algorithms are implemented.

## see also

- [[functional-programming]] · [[programming-language]] · [[type-system]]

<!-- footer -->

---

Lists: [[programming-terms]] · Mark read: `INPUT[toggle:read]`
