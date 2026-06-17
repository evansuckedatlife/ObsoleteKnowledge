---
type: list
category: music
read: false
---

# works by Mozart

The works by Mozart most worth knowing for quiz bowl.

## nodes

- [[cosi-fan-tutte|Così fan tutte]] — Wolfgang Amadeus Mozart's Così fan tutte, ossia La scuola degli amanti (1790) is a two-act Italian opera buffa (comic opera)…
- [[last-three-symphonies-mozart|Mozart last three symphonies]] — Wolfgang Amadeus Mozart's final three symphonies—No.
- [[piano-concertos-mozart|Mozart piano concertos]] — Wolfgang Amadeus Mozart composed 27 numbered piano concertos between 1767 and 1791, creating what is widely regarded as one of…
- [[piano-sonatas-mozart|Mozart piano sonatas]] — Wolfgang Amadeus Mozart composed 18 numbered piano sonatas between 1774 and 1789.
- [[serenades-and-divertimentos-mozart|Mozart serenades and divertimentos]] — Wolfgang Amadeus Mozart composed numerous serenades and divertimentos throughout his career, originally intended as light,…
- [[string-quartets-mozart|Mozart string quartets]] — Wolfgang Amadeus Mozart composed 23 string quartets, which represent a cornerstone of Classical chamber music.
- [[other-symphonies-mozart|Other Mozart symphonies]] — Before composing his final three masterpieces in 1788, Wolfgang Amadeus Mozart wrote dozens of symphonies (officially numbered…
- [[requiem-mozart|Requiem in D minor]] — Wolfgang Amadeus Mozart's Requiem Mass in D minor (K.
- [[the-abduction-from-the-seraglio|The Abduction from the Seraglio]] — Wolfgang Amadeus Mozart's The Abduction from the Seraglio (1782) is a three-act German Singspiel (comic opera with spoken…
- [[the-magic-flute|The Magic Flute]] — Wolfgang Amadeus Mozart's The Magic Flute (1791) is a two-act Singspiel (a German opera form featuring spoken dialogue) that…

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
