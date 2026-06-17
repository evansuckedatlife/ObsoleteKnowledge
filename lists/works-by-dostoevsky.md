---
type: list
category: literature
read: false
---

# works by Fyodor Dostoevsky

The works by Fyodor Dostoevsky most worth knowing for quiz bowl.

## nodes

- [[an-honest-thief|An Honest Thief]] — An Honest Thief (1848), a brief, poignant story, depicts Aleksandr, an aging former soldier and thief, and Emelyan, his…
- [[crime-and-punishment|Crime and Punishment]] — Crime and Punishment is Dostoevsky's monumental psychological novel (1866) following Raskolnikov, an impoverished St.
- [[demons|Demons]] — Demons (alternately The Possessed, 1872) is Dostoevsky's caustic political novel depicting a revolutionary cell infiltrating a…
- [[notes-from-underground|Notes from Underground]] — Notes from Underground (1864), Dostoevsky's novella, presents the alienated voice of a former bureaucrat exposing the…
- [[poor-folk|Poor Folk]] — Poor Folk (1846), Dostoevsky's debut novel composed as an epistolary exchange, depicts the quiet tragedy of Makar Devushkin, a…
- [[the-brothers-karamazov|The Brothers Karamazov]] — The Brothers Karamazov (1880) is Dostoevsky's final and most ambitious novel, exploring faith, doubt, and morality through…
- [[the-double|The Double]] — The Double (1846), Dostoevsky's second published work, presents Yakov Petrovich Golyadkin, a meek copying clerk whose fragile…
- [[the-gambler|The Gambler]] — The Gambler (1867), a short novel set in a decadent European casino town, chronicles the descent of Alexei, a poor tutor…
- [[the-idiot|The Idiot]] — The Idiot (1869) follows Prince Myshkin, a saint-like innocent returning to St.
- [[white-nights|White Nights]] — White Nights (1848), a novella set during St.

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
