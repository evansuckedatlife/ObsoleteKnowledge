---
type: list
category: literature
read: false
---

# Latin American authors

The Latin American authors most worth knowing for quiz bowl.

## nodes

- [[carlos-fuentes|Carlos Fuentes]] — Carlos Fuentes (1928–2012) was a Mexican novelist, essayist, and intellectual whose ambitious, formally experimental novels…
- [[gabriel-garcia-marquez|Gabriel García Márquez]] — Gabriel García Márquez (1927–2014) was a Colombian novelist and short-story writer who became the voice of magical realism,…
- [[gabriela-mistral|Gabriela Mistral]] — Gabriela Mistral (1889–1957) was a Chilean poet, teacher, and diplomat who won the Nobel Prize in Literature as the first…
- [[isabel-allende|Isabel Allende]] — Isabel Allende (born 1942) is a Chilean-American novelist whose debut novel The House of the Spirits announced her as a major…
- [[jorge-luis-borges|Jorge Luis Borges]] — Jorge Luis Borges (1899–1986) was an Argentine writer and poet who revolutionised the short story by treating fiction as…
- [[jose-marti|José Martí]] — José Martí (1853–1895) was a Cuban poet, essayist, and revolutionary who wielded the pen as a weapon against Spanish…
- [[mario-vargas-llosa|Mario Vargas Llosa]] — Mario Vargas Llosa (born 1936) is a Peruvian novelist, critic, and politician whose novels interrogate power, totalitarianism,…
- [[miguel-asturias|Miguel Ángel Asturias]] — Miguel Ángel Asturias (1899–1974) was a Guatemalan novelist, poet, and diplomat whose work draws on Mayan mythology and the…
- [[octavio-paz|Octavio Paz]] — Octavio Paz (1914–1998) was a Mexican poet, essayist, and intellectual whose vast and ambitious work wrestled with Mexican…
- [[pablo-neruda|Pablo Neruda]] — Pablo Neruda (1904–1973) was a Chilean poet whose voice ranged from intimate romantic reverie to epic political witness,…

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
