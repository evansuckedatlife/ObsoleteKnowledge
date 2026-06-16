---
type: list
category: literature
read: false
---

# ancient Greek plays

The ancient Greek plays most worth knowing for quiz bowl.

## nodes

- [[antigone|Antigone]] — Antigone is Sophocles' tragedy about defiance, duty, and the collision between familial piety and political law.
- [[electra|Electra]] — Electra exists as two separate tragic treatments—one by Sophocles and one by Euripides—both centered on the loyal daughter of…
- [[lysistrata|Lysistrata]] — Lysistrata is Aristophanes' farcical antiwar comedy where the women of Athens and Sparta refuse sexual relations with their…
- [[medea-play|Medea]] — Medea is Euripides' shocking tragedy of a spurned woman who commits infanticide rather than bear the humiliation of her…
- [[oedipus-rex|Oedipus Rex]] — Oedipus Rex is Sophocles' masterpiece tragedy, performed around 429 BCE, examining fate, knowledge, and the limits of human…
- [[prometheus-bound|Prometheus Bound]] — Prometheus Bound is Aeschylus' stark tragedy of defiance and suffering, depicting the Titan Prometheus chained to a rock as…
- [[the-bacchae|The Bacchae]] — The Bacchae is Euripides' final masterpiece, a tragedy of religious ecstasy and divine vengeance in which the god Dionysus…
- [[the-clouds|The Clouds]] — The Clouds is Aristophanes' vicious satire of intellectualism and the sophists, featuring Socrates as a ridiculous figure…
- [[the-frogs|The Frogs]] — The Frogs is Aristophanes' satirical comedy in which Dionysus descends to the Underworld to bring back a dead playwright to…
- [[the-oresteia|The Oresteia]] — The Oresteia is Aeschylus' monumental trilogy—the only surviving Greek dramatic trilogy—spanning three generations of the…

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
