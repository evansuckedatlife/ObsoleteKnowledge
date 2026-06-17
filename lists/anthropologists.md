---
type: list
category: social-science
read: false
---

# anthropologists

The anthropologists most worth knowing for quiz bowl.

## nodes

- [[a-r-radcliffe-brown|A.R. Radcliffe-Brown]] — A.R.
- [[bronislaw-malinowski|Bronisław Malinowski]] — Bronisław Malinowski (1884–1942) was a Polish-born British anthropologist who revolutionized ethnographic method through years…
- [[claude-levi-strauss|Claude Lévi-Strauss]] — Claude Lévi-Strauss (1908–2009) was a French anthropologist who founded structuralism, arguing that beneath the surface…
- [[clifford-geertz|Clifford Geertz]] — Clifford Geertz (1926–2006) was an American anthropologist who pioneered interpretive anthropology, arguing that cultural…
- [[e-e-evans-pritchard|E.E. Evans-Pritchard]] — E.E.
- [[franz-boas|Franz Boas]] — Franz Boas (1858–1942) was a German-born American anthropologist who fundamentally reshaped the discipline by championing…
- [[james-frazer|James Frazer]] — James Frazer (1854–1941) was a Scottish anthropologist and classicist whose monumental The Golden Bough synthesized…
- [[margaret-mead|Margaret Mead]] — Margaret Mead (1901–1978) was an American cultural anthropologist who brought ethnography into the public consciousness…
- [[mary-douglas|Mary Douglas]] — Mary Douglas (1921–2007) was a British anthropologist who analyzed how societies use classification systems, ritual, and…
- [[ruth-benedict|Ruth Benedict]] — Ruth Benedict (1887–1948) was an American anthropologist and student of Franz Boas who examined the relationship between…

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
