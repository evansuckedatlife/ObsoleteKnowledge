---
type: list
category: history
read: false
---

# Russian tsars

The Russian tsars most worth knowing for quiz bowl.

## nodes

- [[alexander-i|Alexander I]] — Alexander I (1777–1825) ascended to the throne after his father Paul I's assassination and became Russia's preeminent…
- [[alexander-ii|Alexander II]] — Alexander II (1818–1881), known as the Tsar Liberator, inherited a humbled empire from his father Nicholas I and embarked on…
- [[alexander-iii|Alexander III]] — Alexander III (1845–1894) was the reactionary tsar who reversed his father Alexander II's progressive reforms and ushered in a…
- [[boris-godunov-tsar|Boris Godunov]] — Boris Godunov (1551–1605) was a powerful regent and tsar who bridged the decline of Ivan IV's dynasty and the beginning of the…
- [[catherine-ii|Catherine II]] — Catherine II (1729–1796), known as Catherine the Great, was the longest-reigning Russian empress and one of history's most…
- [[ivan-iii|Ivan III]] — Ivan III (1440–1505), known as Ivan the Great, transformed Moscow from a subordinate principality into the dominant power of…
- [[ivan-iv|Ivan IV]] — Ivan IV (1530–1584), known as Ivan the Terrible, was the first tsar of Russia, transforming Moscow from a principality into a…
- [[michael-romanov|Michael Romanov]] — Michael Romanov (1596–1645), founding tsar of the Romanov dynasty, emerged from the chaos of the Time of Troubles as a…
- [[nicholas-i|Nicholas I]] — Nicholas I (1796–1855) was the apotheosis of Russian autocratic reaction, ruling with militant conservatism and Orthodox…
- [[nicholas-ii|Nicholas II]] — Nicholas II (1868–1918) was the last tsar of Russia, presiding over a doomed empire during the final age of autocracy.
- [[peter-i|Peter I]] — Peter I (1672–1725), known as Peter the Great, transformed Russia from a semi-feudal Eurasian power into a modern European empire.

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
