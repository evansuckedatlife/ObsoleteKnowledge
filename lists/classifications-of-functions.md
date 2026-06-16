---
type: list
category: mathematics
read: false
---

# classifications of mathematical functions

The classifications of mathematical functions most worth knowing for quiz bowl.

## nodes

- [[analytic-functions|Analytic Function]] — An analytic function is a function that can be locally represented by a convergent power series (specifically, a Taylor series).
- [[bijective|Bijective]] — A function is bijective if it is both injective (one-to-one) and surjective (onto), establishing a perfect one-to-one…
- [[continuous-functions|Continuous Function]] — A continuous function is a mathematical function that displays no sudden changes in value, meaning there are no jumps, breaks,…
- [[differentiable-functions|Differentiable Function]] — A differentiable function is one that has a well-defined derivative at every point in its domain—a measure of how the…
- [[even-odd-functions|Even and odd functions]] — Even and odd functions are classes of functions characterized by specific symmetry properties under additive inversion of…
- [[injective|Injective]] — A function is injective (or one-to-one) if it maps distinct elements of its domain to distinct elements of its codomain.
- [[monotonic-functions|Monotonic Function]] — A monotonic function is a function between ordered sets that preserves or reverses the given order.
- [[periodic-function|Periodic Function]] — A periodic function repeats its values at regular intervals; it satisfies `f(x + p) = f(x)` for all x, where p is the period.
- [[surjective|Surjective]] — A function is surjective (or onto) if its range is equal to its codomain, meaning every element in the target set is mapped to…
- [[transcendental-functions|Transcendental Function]] — A transcendental function is a function that does not satisfy any polynomial equation whose coefficients are themselves…

## progress

Live read-status for this list (requires the **Bases** core plugin). Flip a node's `read` from its footer toggle and it moves here.

```base
filters:
  and:
    - file.hasLink(this.file)
views:
  - type: table
    name: Progress
    order:
      - file.name
      - read
      - type
    sort:
      - property: read
        direction: ASC
      - property: file.name
        direction: ASC
```
