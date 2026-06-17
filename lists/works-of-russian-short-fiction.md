---
type: list
category: literature
read: false
---

# works of Russian short fiction

The works of Russian short fiction most worth knowing for quiz bowl.

## nodes

- [[first-love|First Love]] — Turgenev's First Love captures the emotional turbulence of adolescence through a young man's tender infatuation with a…
- [[how-much-land-does-a-man-need|How Much Land Does a Man Need?]] — Tolstoy's How Much Land Does a Man Need?
- [[the-bet|The Bet]] — The Bet is Chekhov's lean philosophical dialogue between a banker and a prisoner who wager over whether the condemned man can…
- [[the-death-of-ivan-ilyich|The Death of Ivan Ilyich]] — Tolstoy's The Death of Ivan Ilyich chronicles the terminal illness and spiritual transformation of a conventional judge whose…
- [[the-kreutzer-sonata|The Kreutzer Sonata]] — The Kreutzer Sonata is Tolstoy's dark meditation on marriage, jealousy, and sexual desire, told through a passenger's…
- [[the-lady-with-the-dog|The Lady with the Dog]] — The Lady with the Dog is Chekhov's meditation on unexpected love, following a bored married man who encounters a woman at a…
- [[the-nose|The Nose]] — The Nose is a surreal comedy in which a St.
- [[the-overcoat|The Overcoat]] — The Overcoat is Gogol's masterpiece of bureaucratic absurdity and human tragedy, following a minor copying clerk whose sole…
- [[the-queen-of-spades|The Queen of Spades]] — Pushkin's The Queen of Spades is a supernatural novella of gambling obsession and buried secrets.
- [[ward-no-6|Ward No. 6]] — Ward No.

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
