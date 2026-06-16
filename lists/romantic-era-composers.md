---
type: list
category: music
read: false
---

# Romantic-era composers

The leading composers of the 19th-century Romantic era, who expanded emotional expression, programmatic narrative, and orchestral scale.

## nodes

- [[antonin-dvorak|Antonín Dvořák]] — Czech nationalist composer who integrated Slavic folk music with classical form and composed the "New World" Symphony.
- [[felix-mendelssohn|Felix Mendelssohn]] — German conservative Romantic child prodigy who revived Bach's music and composed the Italian and Scottish symphonies.
- [[franz-liszt|Franz Liszt]] — Hungarian virtuoso pianist who generated the frenzy of Lisztomania, invented the symphonic poem, and wrote the B-minor Sonata.
- [[franz-schubert|Franz Schubert]] — Austrian pioneer of early Romanticism who wrote over 600 Lieder and the Trout Quintet before dying at 31.
- [[giuseppe-verdi|Giuseppe Verdi]] — King of Italian opera whose music became synonymous with Italian unification and who composed Rigoletto and Aida.
- [[hector-berlioz|Hector Berlioz]] — French orchestrator and pioneer of program music who wrote the drug-hallucination program of the Symphonie fantastique.
- [[johannes-brahms|Johannes Brahms]] — Traditionalist German composer of the "Beethoven's Tenth" First Symphony and a German Requiem.
- [[pyotr-ilyich-tchaikovsky|Pyotr Ilyich Tchaikovsky]] — Preeminent Russian symphonist who wrote the ballets Swan Lake and The Nutcracker, and the tragic Pathétique Symphony.
- [[richard-wagner|Richard Wagner]] — Controversial German giant of the Ring cycle who pioneered the Gesamtkunstwerk and Bayreuth opera house.
- [[robert-schumann|Robert Schumann]] — Introspective German critic and composer who edited the Neue Zeitschrift für Musik and married Clara Wieck.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
