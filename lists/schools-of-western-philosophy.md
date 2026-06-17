---
type: list
category: philosophy
read: false
---

# schools of Western philosophy

The schools of Western philosophy most worth knowing for quiz bowl.

## nodes

- [[empiricism|Empiricism]] — Empiricism is the epistemological position that all knowledge derives ultimately from sensory experience, not innate ideas or…
- [[epicureanism|Epicureanism]] — Epicureanism is the ancient philosophical school founded by Epicurus (~307 BCE) teaching that the goal of life is pleasure,…
- [[existentialism|Existentialism]] — Existentialism is a 20th-century philosophical movement asserting that existence precedes essence—that we are radically free…
- [[positivism|Positivism]] — Positivism is a philosophical movement originating with Auguste Comte (19th century) holding that only empirically verifiable…
- [[pragmatism|Pragmatism]] — Pragmatism is an American philosophical tradition that judges the truth and meaning of a claim by its practical consequences…
- [[rationalism|Rationalism]] — Rationalism is the epistemological view that reason—particularly deductive logic and a priori thought—is the primary source of…
- [[scholasticism|Scholasticism]] — Scholasticism is the medieval Christian intellectual tradition that sought to reconcile Greek philosophy—especially…
- [[skepticism|Skepticism]] — Skepticism in philosophy is the position that knowledge—or at least certainty—cannot be reliably attained, and that rational…
- [[stoicism|Stoicism]] — Stoicism is a Hellenistic and Roman philosophy teaching that virtue is the highest good and the path to a fulfilling life.
- [[utilitarianism|Utilitarianism]] — Utilitarianism is a consequentialist ethical theory holding that the morally right action is the one that maximises overall…

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
