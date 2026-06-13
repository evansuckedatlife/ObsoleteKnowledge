---
type: list
category: science
read: false
---

# rocket scientists

The rocket scientists most worth knowing for quiz bowl.

## nodes

- [[gene-kranz|Gene Kranz]] — American aerospace engineer and flight director (1933–present) who led NASA Mission Control during the Apollo program, most…
- [[hellmuth-walter|Hellmuth Walter]] — German rocket and propulsion engineer (1900–1980) who pioneered hydrogen peroxide and methanol powered engines and turbopump…
- [[hermann-oberth|Hermann Oberth]] — Austro-Hungarian physicist (1894–1989) who published the pioneering treatise Die Rakete zu den Planetenräumen (The Rocket into…
- [[homer-hickam|Homer Hickam]] — American author, engineer, and former NASA employee (1949–present) who is best known for his memoir October Sky (1999), which…
- [[konstantin-tsiolkovsky|Konstantin Tsiolkovsky]] — Russian schoolteacher and visionary (1857–1935) who developed the mathematical rocket equation and conceived the entire…
- [[robert-goddard|Robert Goddard]] — American physicist and engineer (1882–1945) who pioneered liquid-fueled rocket propulsion and laid the theoretical and…
- [[sergei-korolev|Sergei Korolev]] — Soviet chief rocket designer (1906–1966) who led the Soviet space program from Sputnik through the Vostok manned missions.
- [[theodore-von-karman|Theodore von Kármán]] — Hungarian-American aerodynamicist and physicist (1881–1963) who pioneered the theory of transonic and supersonic flow,…
- [[wernher-von-braun|Wernher von Braun]] — German-American rocket engineer (1912–1977) who designed the V-2 ballistic missile for Nazi Germany and later became the chief…

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
