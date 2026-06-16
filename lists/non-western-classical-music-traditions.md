---
type: list
category: music
read: false
---

# non-western classical music traditions

The non-western classical music traditions most worth knowing for quiz bowl.

## nodes

- [[maqam|Arabic Maqam]] — The maqam is a melodic system fundamental to Arabic classical music, analogous to the Indian raga.
- [[carnatic-music|Carnatic Music]] — Carnatic music is the classical music tradition of South India, characterized by elaborate melodic ornamentation, structured…
- [[guqin|Chinese Guqin Music]] — The guqin (or qin) is an ancient Chinese plucked-string instrument and its associated repertoire, revered for over 2,500 years…
- [[hindustani-classical-music|Hindustani Classical Music]] — Hindustani classical music is the principal art-music tradition of North India, emphasizing melodic improvisation within a…
- [[gamelan|Indonesian Gamelan]] — Gamelan is the ensemble music of Indonesia, most prominently Java and Bali, built around metallophone percussion instruments…
- [[gagaku|Japanese Gagaku]] — Gagaku is Japan's ancient imperial court music, performed continuously for over 1,200 years.
- [[gugak|Korean Gugak]] — Gugak ("national music") is the indigenous music tradition of Korea, encompassing court music, folk instrumental pieces, and…
- [[dastgah|Persian Dastgah]] — The dastgah is the modal-melodic framework of Persian classical music, comprising a system of hierarchical melodic formulas…
- [[qawwali|Qawwali]] — Qawwali is a form of Sufi devotional music from South Asia, most strongly associated with Pakistan but also performed in India…
- [[west-african-drumming|West African Drumming Traditions]] — West African drumming traditions represent the most sophisticated percussion music systems in the world, built on interlocking…

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
