---
type: list
category: mathematics
read: false
---

# classifications of functions

The classifications of mathematical functions most worth knowing for quiz bowl.

## nodes

- [[analytic-functions|Analytic Function]] — A function locally represented by a convergent power series (specifically, a Taylor series).
- [[bijective|Bijective]] — A function that is both injective (one-to-one) and surjective (onto), establishing a perfect one-to-one correspondence.
- [[continuous-functions|Continuous Function]] — A function with no jumps, breaks, or holes in its graph, meaning its limit equals its value everywhere.
- [[differentiable-functions|Differentiable Function]] — A function that has a well-defined derivative at every point in its domain, implying smoothness.
- [[even-odd-functions|Even and Odd Functions]] — Classes of functions characterized by symmetry under additive inversion of their inputs.
- [[injective|Injective]] — A function that maps distinct domain elements to distinct codomain elements, meaning it is one-to-one.
- [[monotonic-functions|Monotonic Function]] — A function that preserves or reverses order, being either non-increasing or non-decreasing.
- [[periodic-function|Periodic Function]] — A function that repeats its values at regular intervals, satisfying f(x + p) = f(x).
- [[surjective|Surjective]] — A function whose range equals its codomain, meaning it maps onto the entire target set.
- [[transcendental-functions|Transcendental Function]] — A function that does not satisfy any polynomial equation with polynomial coefficients.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
