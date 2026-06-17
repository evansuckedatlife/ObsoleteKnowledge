---
type: list
category: visual-art
read: false
---

# sculptors

The sculptors most worth knowing for quiz bowl.

## nodes

- [[rodin|Auguste Rodin]] — Auguste Rodin (1840–1917) was a French sculptor who bridged the 19th and 20th centuries, founding modern sculpture through…
- [[brancusi|Constantin Brancusi]] — Constantin Brancusi (1876–1957) was a Romanian-French modernist sculptor who pioneered abstraction and formal reduction in…
- [[french|Daniel Chester French]] — Daniel Chester French (1850–1931) was an American sculptor who dominated the Beaux-Arts tradition in the United States,…
- [[donatello|Donatello]] — Donatello (c.
- [[bartholdi|Frédéric-Auguste Bartholdi]] — Frédéric-Auguste Bartholdi (1834–1904) was a French sculptor best known for conceiving and overseeing the creation of the…
- [[bernini|Gian Lorenzo Bernini]] — Gian Lorenzo Bernini (1598–1680) was an Italian Baroque sculptor and architect who dominated 17th-century Rome, defining the…
- [[borglum|Gutzon Borglum]] — Gutzon Borglum (1867–1941) was an American sculptor famous for monumental public works carved directly into stone and granite.
- [[ghiberti|Lorenzo Ghiberti]] — Lorenzo Ghiberti (c.
- [[michelangelo|Michelangelo]] — Michelangelo Buonarroti (1475–1564) was an Italian Renaissance master of sculpture, painting, and architecture whose works…
- [[phidias|Phidias]] — Phidias (c.

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
