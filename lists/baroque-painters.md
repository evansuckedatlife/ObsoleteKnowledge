---
type: list
category: visual-art
read: false
---

# baroque painters

The baroque painters most worth knowing for quiz bowl.

## nodes

- [[anthony-van-dyck|Anthony van Dyck]] — Anthony van Dyck is a Flemish Baroque painter and master of aristocratic portraiture who served as court painter to Charles I…
- [[artemisia-gentileschi|Artemisia Gentileschi]] — Artemisia Gentileschi is a Baroque painter and one of the first widely recognized female artists in European history, renowned…
- [[caravaggio|Caravaggio]] — Caravaggio is an Italian Baroque painter celebrated for his dramatic use of chiaroscuro—violent contrasts between deep shadows…
- [[diego-velazquez|Diego Velázquez]] — Diego Velázquez is a Spanish Baroque master and one of the greatest painters of the 17th century, celebrated for his…
- [[frans-hals|Frans Hals]] — Frans Hals is a Dutch Golden Age painter celebrated for his loose, gestural brushwork and his vivid group portraits and…
- [[johannes-vermeer|Johannes Vermeer]] — Johannes Vermeer is a Dutch Golden Age painter whose intimate domestic scenes of women in interiors, suffused with cool,…
- [[judith-leyster|Judith Leyster]] — Judith Leyster is a Dutch Golden Age painter renowned for her intimate domestic scenes, flirtations, and music-making moments…
- [[nicolas-poussin|Nicolas Poussin]] — Nicolas Poussin is a French Baroque painter celebrated for his intellectualized, classically composed historical and…
- [[peter-paul-rubens|Peter Paul Rubens]] — Peter Paul Rubens is a Flemish Baroque painter and diplomat whose dynamic, sensuous compositions and energetic brushwork made…
- [[rembrandt-van-rijn|Rembrandt van Rijn]] — Rembrandt van Rijn is a Dutch Golden Age master celebrated as the greatest printmaker and painter of his era, renowned for his…

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
