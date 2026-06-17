---
type: list
category: social-science
read: false
---

# economists

The economists most worth knowing for quiz bowl.

## nodes

- [[adam-smith|Adam Smith]] — Adam Smith was an 18th-century Scottish economist and moral philosopher whose The Wealth of Nations (1776) established the…
- [[alfred-marshall|Alfred Marshall]] — Alfred Marshall was a late 19th and early 20th-century British economist who synthesized classical political economy with…
- [[david-ricardo|David Ricardo]] — David Ricardo was an early 19th-century British economist whose theories of rent, comparative advantage, and value dominated…
- [[francois-quesnay|François Quesnay]] — François Quesnay was an 18th-century French physician and economist who founded the Physiocratic school, which held that…
- [[john-kenneth-galbraith|John Kenneth Galbraith]] — John Kenneth Galbraith was a 20th-century American economist and prolific public intellectual who challenged both…
- [[john-maynard-keynes|John Maynard Keynes]] — John Maynard Keynes was a 20th-century British economist whose General Theory of Employment, Interest and Money (1936)…
- [[john-stuart-mill|John Stuart Mill]] — John Stuart Mill was a 19th-century British philosopher and economist who synthesized Ricardian political economy with…
- [[karl-marx|Karl Marx]] — Karl Marx was a 19th-century German philosopher and economist whose theories of historical materialism and class struggle…
- [[milton-friedman|Milton Friedman]] — Milton Friedman was a 20th-century American economist and public intellectual who championed free-market capitalism and…
- [[thorstein-veblen|Thorstein Veblen]] — Thorstein Veblen was a late 19th and early 20th-century American institutionalist economist who critiqued both classical…

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
