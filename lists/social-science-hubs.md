---
type: list
category: social-science
read: false
---

# Social Science hubs

Concepts and frameworks the individual studies and thinkers apply.

## nodes

- [[endangered-languages|Endangered Languages]] — Endangered languages are languages with so few remaining speakers that they face extinction within one to three generations.
- [[ethics-in-psychology|Ethics in Psychology]] — Ethics in psychology is the field of moral and professional standards governing research on human and animal subjects, including requirements for info…
- [[indigenous-languages-americas|Indigenous Languages of the Americas]] — The indigenous languages of the Americas comprise the languages spoken by the diverse pre-Columbian civilizations and their descendants, ranging from …
- [[linguistic-typology|Linguistic Typology]] — Linguistic typology is the classification of languages by their recurrent structural features—how they form words (morphology), arrange them (syntax),…
- [[magic|Magic]] — Magic is the belief and practice that thoughts, words, or ritual actions can directly influence the physical world through supernatural means—a univer…

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
