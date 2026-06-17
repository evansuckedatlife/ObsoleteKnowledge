---
type: list
category: visual-art
read: false
---

# art museums

The art museums most worth knowing for quiz bowl.

## nodes

- [[guggenheim|Guggenheim]] — The Solomon R.
- [[hermitage|Hermitage]] — The Hermitage in Saint Petersburg, housed in the Winter Palace and adjacent buildings, is the largest art museum in Russia and…
- [[metropolitan-museum-of-art|Metropolitan Museum of Art]] — The Metropolitan Museum of Art, located on Fifth Avenue in New York City, is one of the world's largest and most comprehensive…
- [[museo-del-prado|Museo del Prado]] — The Prado, Spain's national art museum in Madrid, opened in 1819 and showcases the finest Spanish paintings alongside works…
- [[moma|Museum of Modern Art]] — MoMA, the Museum of Modern Art in New York, opened in 1929 and established the canonical taste for 20th-century modernism and…
- [[national-gallery-london|National Gallery, London]] — The National Gallery in London, founded in 1824, preserves one of the world's most comprehensive collections of European…
- [[rijksmuseum|Rijksmuseum]] — The Rijksmuseum in Amsterdam, the Netherlands' national art museum, was founded in 1798 and housed in its iconic 1880s Gothic…
- [[tate-modern|Tate Modern]] — Tate Modern, located in London in a converted power station on the Thames, opened in 2000 and is the world's leading museum of…
- [[the-louvre|The Louvre]] — The Louvre is the world's largest art museum by floor area, located in Paris and housed in a former royal palace.
- [[uffizi-gallery|Uffizi Gallery]] — The Uffizi Gallery in Florence is one of the world's oldest and most revered art museums, housing the most comprehensive…

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
