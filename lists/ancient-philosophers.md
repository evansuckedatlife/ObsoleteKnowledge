---
type: list
category: philosophy
read: false
---

# ancient philosophers

The ancient philosophers most worth knowing for quiz bowl.

## nodes

- [[aristotle|Aristotle]] — Aristotle (384–322 BCE) was a Greek philosopher born in Macedonia who studied under Plato, founded his own school (the…
- [[diogenes|Diogenes of Sinope]] — Diogenes of Sinope (c.
- [[epicurus|Epicurus]] — Epicurus (341–270 BCE) was a Greek philosopher who founded an influential school teaching that pleasure is the highest good,…
- [[heraclitus|Heraclitus]] — Heraclitus (c.
- [[parmenides|Parmenides]] — Parmenides (c.
- [[plato|Plato]] — Plato (428–348 BCE) was an Athenian philosopher and student of Socrates who founded the Academy and authored the dialogues…
- [[pythagoras|Pythagoras]] — Pythagoras (c.
- [[socrates|Socrates]] — Socrates (469–399 BCE) was an Athenian philosopher who revolutionized Western thought by turning away from natural philosophy…
- [[thales|Thales of Miletus]] — Thales of Miletus (c.
- [[zeno-of-elea|Zeno of Elea]] — Zeno of Elea (c.

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
