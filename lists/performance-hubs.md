---
type: list
category: performance
read: false
---

# Performance hubs

Forms and traditions behind the individual productions and performers.

## nodes

- [[ballets-russes|Ballets Russes]] — The Ballets Russes was a groundbreaking ballet company founded by impresario Sergei Diaghilev in 1909 that revolutionized dance and art through radica…
- [[fokine|Michel Fokine]] — Michel Fokine was a Russian-born choreographer and dancer who revolutionized ballet in the early 20th century by rejecting rigid classical conventions.
- [[minkus|Ludwig Minkus]] — Ludwig Minkus was an Austrian composer whose ballets scores became pillars of classical ballet repertoire in 19th-century Russia.
- [[musical-theatre|Musical Theatre]] — Musical theatre is a theatrical form that synthesizes dramatic narrative, music, choreography, and elaborate spectacle into a live performance.
- [[new-york-city-ballet|New York City Ballet]] — New York City Ballet (NYCB) is an American ballet company founded in 1948 by choreographer George Balanchine and Lincoln Kirstein, establishing New Yo…
- [[russian-folklore|Russian Folklore]] — Russian folklore encompasses the mythology, fairy tales, folk customs, and carnival traditions of Russian culture stretching back centuries.

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
