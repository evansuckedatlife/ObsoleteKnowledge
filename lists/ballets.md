---
type: list
category: performance
read: false
---

# ballets

The ballets most worth knowing for quiz bowl.

## nodes

- [[coppelia|Coppelia]] — A lighthearted, comedic classical ballet in three acts, Coppelia features music by Léo Delibes and choreography originally by…
- [[giselle|Giselle]] — A landmark Romantic ballet in two acts, Giselle features music by Adolphe Adam and choreography originally created by Jean…
- [[sleeping-beauty|Sleeping Beauty]] — A three-act classical ballet composed by Pyotr Ilyich Tchaikovsky, Sleeping Beauty is one of the most celebrated works in the…
- [[swan-lake|Swan Lake]] — A canonical four-act ballet composed by Pyotr Ilyich Tchaikovsky, Swan Lake is one of the most famous and frequently performed…
- [[the-nutcracker|The Nutcracker]] — A beloved two-act classical ballet composed by Pyotr Ilyich Tchaikovsky, The Nutcracker has become a staple Christmas…
- [[the-rite-of-spring|The Rite of Spring]] — Composed by Igor Stravinsky and originally choreographed by Vaslav Nijinsky, The Rite of Spring (Le Sacre du printemps) is a…

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
