---
type: list
category: literature
read: false
---

# translations and translators

The translations and translators most worth knowing for quiz bowl.

## nodes

- [[arthur-waley|Arthur Waley]] — Arthur Waley (1889–1966) was a British translator and orientalist whose renderings of Chinese and Japanese classics—including…
- [[chapmans-homer|Chapman's Homer]] — Chapman's Homer is George Chapman's English verse translation of Homer's Iliad (1611–1615) and Odyssey (1614–1616), written in…
- [[constance-garnett|Constance Garnett]] — Constance Garnett (1861–1946) was an English translator whose prodigious output of Russian literature in the early 20th…
- [[fitzgerald-rubaiyat|FitzGerald's Rubáiyát of Omar Khayyám]] — Edward FitzGerald's Rubáiyát of Omar Khayyám (1859) is an English verse translation and radical reinterpretation of a…
- [[gregory-rabassa|Gregory Rabassa]] — Gregory Rabassa (1922–2016) was an American translator of Latin American literature whose translations of García Márquez's One…
- [[king-james-bible|King James Bible]] — The King James Bible is a 1611 English translation of the Hebrew Bible and Christian New Testament commissioned by King James…
- [[popes-iliad|Pope's Iliad]] — Alexander Pope's translation of Homer's Iliad (1715–1720) is an English verse rendering in heroic couplets that became the…
- [[seamus-heaney-beowulf|Seamus Heaney's Beowulf]] — Seamus Heaney's Beowulf (1999) is an English verse translation of the Old English epic that combines literal fidelity with…
- [[septuagint|Septuagint]] — The Septuagint (LXX) is a Greek translation of the Hebrew scriptures produced in Alexandria, Egypt around the 3rd and 2nd…
- [[vulgate|Vulgate]] — The Vulgate is a Latin translation of the Hebrew Bible and New Testament completed by Jerome between 390 and 405 CE,…

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
