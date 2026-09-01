---
type: list
category: music
read: false
---

# Music hubs

Forms, eras and concepts underlying the individual composers and works.

## nodes

- [[classical-music|Classical Music]] — Classical music refers to the musical period and aesthetic that emerged in the mid-18th century as a reaction against the complexity and ornamentation…
- [[cool-jazz|Cool Jazz]] — Cool jazz emerged in the late 1940s as a deliberate reaction against bebop's frenetic intensity and harmonic complexity.
- [[count-basie|Count Basie]] — Count Basie (1904–1984), born William James Basie, was an American pianist and bandleader whose orchestra became one of the defining engines of the sw…
- [[literature|Literature and Music]] — Literature and music have been intertwined since antiquity, but operatic composers from the 18th century onward made literary adaptation a central cre…
- [[medieval-music|Medieval Music]] — Medieval music encompasses the musical traditions of Europe from roughly the 6th to the 15th centuries, a period defined by the dominance of the Catho…
- [[modal-music|Modal Music]] — Modal music is a system of melody and improvisation organized around modes—recurring melodic and harmonic frameworks distinct from Western major and m…
- [[opera-buffa|Opera Buffa]] — Opera buffa is a comic operatic form that flourished in 18th and 19th-century Italy, characterized by witty, often farcical plots, popular appeal, and…
- [[soprano|Soprano]] — Soprano is the highest standard female voice classification in Western classical and operatic music, characterized by brightness, agility, and project…
- [[tabla|Tabla]] — The tabla is a pair of hand drums central to Indian classical music, consisting of a smaller, higher-pitched drum (dayan) and a larger, lower-pitched …
- [[verismo-opera|Verismo Opera]] — Verismo opera is an operatic movement that emerged in late 19th-century Italy, emphasizing realism, contemporary settings, and raw emotional directnes…

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
