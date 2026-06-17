---
type: list
category: social-science
read: false
---

# psychological experiments and studies

The psychological experiments and studies most worth knowing for quiz bowl.

## nodes

- [[learned-helplessness|Learned Helplessness Experiments]] — Martin Seligman and Steven Maier conducted experiments in the 1960s in which dogs exposed to inescapable electric shocks later…
- [[pavlovs-classical-conditioning|Pavlov's Classical Conditioning Experiments]] — Ivan Pavlov discovered classical conditioning through experiments with dogs in the 1890s–1900s, demonstrating that animals…
- [[asch-conformity|The Asch Conformity Experiment]] — Solomon Asch conducted experiments in 1951–1956 in which participants were asked to match the length of a line against three…
- [[bobo-doll|The Bobo Doll Experiment]] — Albert Bandura, Dorothy Ross, and Sheila Ross conducted experiments in 1961 in which children watched a video or live model…
- [[clark-doll-experiment|The Clark Doll Experiment]] — Kenneth and Mamie Clark conducted experiments in the 1940s asking Black children to choose between white and Black dolls,…
- [[little-albert|The Little Albert Experiment]] — John B.
- [[milgram-obedience|The Milgram Obedience Experiment]] — Stanley Milgram conducted experiments in 1961–1962 in which ordinary participants administered apparently lethal electric…
- [[skinner-box|The Skinner Box]] — B.F.
- [[small-world-experiment|The Small-World Experiment]] — Stanley Milgram conducted experiments in 1967 in which he asked people to send letters to a distant stranger by passing them…
- [[stanford-prison|The Stanford Prison Experiment]] — Philip Zimbardo conducted an experiment in 1971 in which college students were randomly assigned to play prisoners or guards…

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
