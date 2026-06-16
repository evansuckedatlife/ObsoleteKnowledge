---
type: list
category: social-science
read: false
---

# psychologists

The psychologists most worth knowing for quiz bowl.

## nodes

- [[abraham-maslow|Abraham Maslow]] — Abraham Maslow (1908–1970) was an American psychologist and the founder of humanistic psychology, a movement that recentered…
- [[alfred-adler|Alfred Adler]] — Alfred Adler (1870–1937) was an Austrian psychiatrist and the third major figure in early 20th-century psychoanalysis,…
- [[b-f-skinner|B.F. Skinner]] — Burrhus Frederic Skinner (1904–1990) was an American psychologist and the most influential behaviorist of the late 20th…
- [[carl-jung|Carl Jung]] — Carl Jung (1875–1961) was a Swiss psychiatrist and one of the earliest and most original students of Freud, whom he eventually…
- [[erik-erikson|Erik Erikson]] — Erik Erikson (1902–1994) was a German-American psychoanalyst and developmental psychologist who extended Freud's theory of…
- [[ivan-pavlov|Ivan Pavlov]] — Ivan Pavlov (1849–1936) was a Russian physiologist whose accidental discovery of classical conditioning launched the…
- [[jean-piaget|Jean Piaget]] — Jean Piaget (1896–1980) was a Swiss psychologist and founder of developmental psychology, whose theories of how children's…
- [[john-b-watson|John B. Watson]] — John Broadus Watson (1878–1958) was an American psychologist and the founding architect of behaviorism, psychology's most…
- [[sigmund-freud|Sigmund Freud]] — Sigmund Freud (1856–1939) was an Austrian neurologist and the founder of psychoanalysis, a revolutionary approach to…
- [[stanley-milgram|Stanley Milgram]] — Stanley Milgram (1933–1984) was an American social psychologist famous for his controversial experiments on obedience to…
- [[wilhelm-wundt|Wilhelm Wundt]] — Wilhelm Wundt (1832–1920) was a German physiologist and psychologist who founded experimental psychology as an academic…
- [[william-james|William James]] — William James (1842–1910) was an American psychologist, philosopher, and polymath who, despite battling chronic illness…

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
