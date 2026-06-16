---
type: list
category: history
read: false
---

# medieval Islamic dynasties

The medieval Islamic dynasties most worth knowing for quiz bowl.

## nodes

- [[abbasid-caliphate|Abbasid Caliphate]] — The Abbasid Caliphate (750–1258 CE) was the longest-lived Islamic dynasty, founded by the revolutionary Abbasid family and…
- [[almohad-caliphate|Almohad Caliphate]] — The Almohad Caliphate (1121–1269 CE) was a North African Berber dynasty that emerged as a reformist reaction against the…
- [[almoravid-dynasty|Almoravid Dynasty]] — The Almoravid Dynasty (1056–1147 CE) was a Berber military movement that emerged from the Sahara Desert, conquered the western…
- [[ayyubid-dynasty|Ayyubid Dynasty]] — The Ayyubid Dynasty (1169–1260 CE) was a Kurdish military clan founded by Saladin (Salah ad-Din al-Ayyubi), who unified Egypt…
- [[fatimid-caliphate|Fatimid Caliphate]] — The Fatimid Caliphate (909–1171 CE) was a Shiite dynasty centered in North Africa and later Egypt, which claimed descent from…
- [[ghaznavid-dynasty|Ghaznavid Dynasty]] — The Ghaznavid Dynasty (977–1186 CE) was a Turkish military empire centered in Ghazni (in present-day Afghanistan), which…
- [[mamluk-sultanate|Mamluk Sultanate]] — The Mamluk Sultanate (1250–1517 CE) was a unique military state ruled by mamluks, enslaved soldiers of Caucasian or Central…
- [[rashidun-caliphate|Rashidun Caliphate]] — The Rashidun Caliphate (632–661 CE) comprises the first four Islamic caliphs—Abu Bakr, Umar, Uthman, and Ali—who were chosen…
- [[seljuk-empire|Seljuk Empire]] — The Seljuk Empire (1037–1194 CE) was a Turkish dynasty descended from the Oghuz nomads, which conquered Central Asia, Persia,…
- [[umayyad-caliphate|Umayyad Caliphate]] — The Umayyad Caliphate (661–750 CE) was the first hereditary Islamic dynasty, centered in Damascus and ruled by Arab…

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
