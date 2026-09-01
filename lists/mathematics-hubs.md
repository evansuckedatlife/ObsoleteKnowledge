---
type: list
category: mathematics
read: false
---

# Mathematics hubs

The underlying objects and ideas the individual theorems and figures depend on.

## nodes

- [[cryptography|Cryptography]] — Cryptography is the mathematical science of secure communication, using algorithms to encode messages so that only intended recipients can decode them.
- [[fundamental-theorem-of-algebra|Fundamental Theorem of Algebra]] — The Fundamental Theorem of Algebra states that every non-constant polynomial of degree n with complex coefficients has exactly n roots in the complex …
- [[inner-product|Inner Product]] — An inner product is a generalisation of the familiar dot product from Euclidean space to abstract vector spaces, assigning to each pair of vectors a s…
- [[non-euclidean-geometry|Non-Euclidean Geometry]] — Non-Euclidean geometry refers to geometric systems that do not satisfy Euclid's parallel postulate—the claim that through a point not on a line, exact…
- [[pascal|Blaise Pascal]] — Blaise Pascal (1623–1662) was a French mathematician, physicist, and religious philosopher whose contributions spanned geometry, probability, fluid me…

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
      - property: tour_order
        direction: ASC
      - property: file.name
        direction: ASC
```
