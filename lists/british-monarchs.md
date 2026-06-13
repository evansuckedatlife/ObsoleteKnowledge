---
type: list
category: history
read: false
---

# British monarchs

The British monarchs most worth knowing for quiz bowl.

## nodes

- [[charles-i|Charles I]] — Charles I was King of England, Scotland, and Ireland from 1625 until his execution in 1649.
- [[elizabeth-i|Elizabeth I]] — Elizabeth I was Queen of England and Ireland from 1558 to 1603, the last Tudor monarch.
- [[george-iii|George III]] — George III was King of Great Britain and Ireland from 1760 until his death in 1820.
- [[henry-ii|Henry II]] — Henry II was King of England from 1154 to 1189, initiating the Plantagenet dynasty.
- [[henry-viii|Henry VIII]] — Henry VIII was King of England from 1509 to 1547.
- [[james-i|James I]] — James I (r.
- [[king-john|John]] — John was King of England from 1199 until his death in 1216.
- [[richard-i|Richard I]] — Richard I, widely known as Richard the Lionheart, was King of England from 1189 to 1199.
- [[victoria|Victoria]] — Victoria was Queen of the United Kingdom of Great Britain and Ireland from 1837 to 1901, and Empress of India from 1876.
- [[william-i|William I]] — William I, also known as William the Conqueror, was the first Norman king of England, reigning from 1066 until his death in 1087.

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
