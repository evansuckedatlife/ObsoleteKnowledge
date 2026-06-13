---
type: list
category: mathematics
read: false
---

# mathematicians

The mathematicians most worth knowing for quiz bowl.

## nodes

- [[andrew-wiles|Andrew Wiles]] — Andrew Wiles (born 1953) is a British mathematician best known for proving Fermat's Last Theorem in 1995, ending a 358-year quest.
- [[archimedes|Archimedes]] — Archimedes (c.
- [[carl-friedrich-gauss|Carl Friedrich Gauss]] — Carl Friedrich Gauss (1777–1855) was a German mathematician and astronomer whose contributions span number theory, statistics,…
- [[euclid|Euclid]] — Euclid (c.
- [[gottfried-leibniz|Gottfried Leibniz]] — Gottfried Leibniz (1646–1716) was a German polymath—mathematician, philosopher, physicist, logician, and diplomat—who…
- [[isaac-newton|Isaac Newton]] — Isaac Newton (1642–1727) was an English mathematician, physicist, and astronomer whose Principia Mathematica (1687) founded…
- [[kurt-godel|Kurt Gödel]] — Kurt Gödel (1906–1978) was an Austrian-American logician and mathematician whose Incompleteness Theorems (1931) revealed…
- [[leonhard-euler|Leonhard Euler]] — Leonhard Euler (1707–1783) was a Swiss mathematician and physicist whose prolific output—roughly one paper per week for 56…
- [[pierre-de-fermat|Pierre de Fermat]] — Pierre de Fermat (1607–1665) was a French lawyer and mathematician whose work in number theory, calculus, and probability was…
- [[william-rowan-hamilton|William Rowan Hamilton]] — William Rowan Hamilton (1805–1865) was an Irish mathematician and physicist who revolutionised mechanics through his…

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
