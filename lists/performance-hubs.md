---
type: list
category: performance
read: false
---

# Performance hubs

Forms and traditions behind the individual productions and performers.

## nodes

- [[andrew-lloyd-webber|Andrew Lloyd Webber]] — Andrew Lloyd Webber is a British composer who revolutionized musical theatre in the 1980s with a series of commercially colossal productions that blen…
- [[ballets-russes|Ballets Russes]] — The Ballets Russes was a groundbreaking ballet company founded by impresario Sergei Diaghilev in 1909 that revolutionized dance and art through radica…
- [[brothers-grimm|Brothers Grimm]] — Jacob Grimm (1785–1863) and Wilhelm Grimm (1786–1859) were two German brothers whose collection and curation of European fairy tales became the canoni…
- [[evita-musical|Evita]] — Evita is a 1978 musical by composer Andrew Lloyd Webber and lyricist Tim Rice that chronicles the rise of Eva Perón from illegitimate poverty to First…
- [[fairy-tale|Fairy Tale]] — A fairy tale is a narrative genre featuring magical elements, archetypal characters (princes, witches, enchanted forests), and moral lessons wrapped i…
- [[fokine|Michel Fokine]] — Michel Fokine was a Russian-born choreographer and dancer who revolutionized ballet in the early 20th century by rejecting rigid classical conventions.
- [[german-literature|German literature]] — German literature encompasses the written and oral traditions of the German-speaking world, evolving from medieval heroic epics and the intellectual f…
- [[hans-christian-andersen|Hans Christian Andersen]] — Hans Christian Andersen was a nineteenth-century Danish author and poet whose original literary fairy tales transformed storytelling and became lastin…
- [[imperial-ballet|Imperial Ballet]] — The Imperial Ballet was the state ballet company of Imperial Russia, centered at the Mariinsky Theatre in St.
- [[literature-genre|Literature Genre]] — A literature genre is a systematic classification of written works based on shared formal, thematic, or structural characteristics that readers recogn…
- [[minkus|Ludwig Minkus]] — Ludwig Minkus was an Austrian composer whose ballets scores became pillars of classical ballet repertoire in 19th-century Russia.
- [[musical-theatre|Musical Theatre]] — Musical theatre is a theatrical form that synthesizes dramatic narrative, music, choreography, and elaborate spectacle into a live performance.
- [[new-york-city-ballet|New York City Ballet]] — New York City Ballet (NYCB) is an American ballet company founded in 1948 by choreographer George Balanchine and Lincoln Kirstein, establishing New Yo…
- [[nijinsky|Vaslav Nijinsky]] — Vaslav Nijinsky was a Russian dancer and choreographer of unparalleled technical virtuosity and artistic daring whose brief but revolutionary career r…
- [[russian-folklore|Russian Folklore]] — Russian folklore encompasses the mythology, fairy tales, folk customs, and carnival traditions of Russian culture stretching back centuries.
- [[the-sleeping-beauty|The Sleeping Beauty]] — The Sleeping Beauty is a grand three-act ballet with a prologue composed by Pyotr Ilyich Tchaikovsky and choreographed by Marius Petipa, which premier…
- [[tim-rice|Tim Rice]] — Tim Rice (born 1944) is an acclaimed English lyricist and author who transformed modern musical-theatre through celebrated collaborations with compose…

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
