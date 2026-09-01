---
type: list
category: philosophy
read: false
---

# Philosophy hubs

Branches, problems and positions the individual philosophers argue about.

## nodes

- [[jean-paul-sartre|Jean-Paul Sartre]] — Jean-Paul Sartre (1905–1980) was a French philosopher, novelist, and political activist who became the public face of existentialism in the mid-20th c…
- [[mathematics|Mathematics]] — Mathematics is the study of abstract entities—numbers, shapes, and logical relationships—governed by proof and axioms rather than empirical observatio…
- [[medieval-philosophy|Medieval Philosophy]] — Medieval philosophy is the Western philosophical tradition spanning roughly the 5th to 15th centuries, dominated by the integration of Aristotelian lo…
- [[metaphysics|Metaphysics]] — Metaphysics is the philosophical inquiry into the fundamental nature of reality: what exists, what is the relationship between mind and matter, whethe…
- [[mind-body-problem|Mind-body problem]] — The mind-body problem is the central puzzle of modern philosophy of mind: how does consciousness—subjective, private, qualitative experience—relate to…
- [[morality|Morality]] — Morality is the system of principles concerning the distinction between right and wrong, good and bad action.
- [[phenomenology|Phenomenology]] — Phenomenology is a philosophical method and discipline that investigates the structure of consciousness from the first-person perspective: what is it …
- [[reason|Reason]] — Reason is the faculty of mind that processes logic, derives conclusions from premises, and aspires to universal truth independent of sensory experienc…

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
