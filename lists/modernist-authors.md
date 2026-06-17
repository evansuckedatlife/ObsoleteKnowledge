---
type: list
category: literature
read: false
---

# modernist authors

The modernist authors most worth knowing for quiz bowl.

## nodes

- [[d-h-lawrence|D. H. Lawrence]] — D.
- [[e-e-cummings|E. E. Cummings]] — E.
- [[ezra-pound|Ezra Pound]] — Ezra Pound (1885–1972) was an American poet, critic, and literary impresario whose ambition was to "make it new"—to radically…
- [[franz-kafka|Franz Kafka]] — Franz Kafka (1883–1924) was a Prague-born writer whose surreal, haunting fiction explores themes of alienation, bureaucratic…
- [[gertrude-stein|Gertrude Stein]] — Gertrude Stein (1874–1946) was an American writer and art collector whose radical experiments with language and narrative made…
- [[hart-crane|Hart Crane]] — Hart Crane (1899–1932) was an American modernist poet whose brief, turbulent life produced some of the 20th century's most…
- [[james-joyce|James Joyce]] — James Joyce (1882–1941) was an Irish modernist writer whose experimental novels revolutionized the form of fiction.
- [[marcel-proust|Marcel Proust]] — Marcel Proust (1871–1922) was a French novelist whose monumental work In Search of Lost Time (À la recherche du temps perdu)…
- [[t-s-eliot|T. S. Eliot]] — T.
- [[virginia-woolf|Virginia Woolf]] — Virginia Woolf (1882–1941) was a British modernist novelist whose works pioneered stream-of-consciousness technique and…
- [[william-faulkner|William Faulkner]] — William Faulkner (1897–1962) was an American modernist novelist who brought stream-of-consciousness and radical structural…

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
