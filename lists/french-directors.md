---
type: list
category: visual-art
read: false
---

# French directors

The French directors most worth knowing for quiz bowl.

## nodes

- [[agnes-varda|Agnès Varda]] — Agnès Varda was a Belgian-French director and pioneer of the cinéma-vérité documentary style who brought radical subjectivity…
- [[alain-resnais|Alain Resnais]] — Alain Resnais was a French filmmaker whose obsession with memory, narrative structure, and the gap between word and image…
- [[claire-denis|Claire Denis]] — Claire Denis is a contemporary French director known for her sensuous, formally precise films that inhabit marginal…
- [[francois-truffaut|François Truffaut]] — François Truffaut was a French New Wave director and influential film critic who championed the auteur theory and turned it…
- [[georges-melies|Georges Méliès]] — Georges Méliès was a French pioneering filmmaker and illusionist who invented trick cinematography and the language of special…
- [[jacques-demy|Jacques Demy]] — Jacques Demy was a French New Wave director whose romantic, musically inclined sensibility set him apart from his…
- [[jacques-tati|Jacques Tati]] — Jacques Tati was a French filmmaker, actor, and mime who created a singular comedy of observation, using elaborately designed…
- [[jean-renoir|Jean Renoir]] — Jean Renoir was a French master filmmaker of the 1930s–1960s, the son of Impressionist painter Pierre-Auguste Renoir, who…
- [[jean-luc-godard|Jean-Luc Godard]] — Jean-Luc Godard is a Swiss-French filmmaker and theorist who became the most radical voice of the French New Wave, radically…
- [[jean-pierre-melville|Jean-Pierre Melville]] — Jean-Pierre Melville was a French director who prefigured the New Wave through his cooler, more economical style—spare…
- [[louis-lumiere|Louis Lumière]] — Louis Lumière and his brother Auguste were French inventors and filmmakers who pioneered cinematography and the motion-picture…
- [[robert-bresson|Robert Bresson]] — Robert Bresson was a French ascetic filmmaker whose austere, crystalline style distilled narrative to its essence—minimal…

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
