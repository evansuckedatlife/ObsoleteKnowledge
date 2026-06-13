---
type: list
category: history
read: false
---

# British Monarchs

This topic covers key monarchs of England, Scotland, and Great Britain who have had the greatest impact on history, constitutionality, and culture.

## nodes

- [[william-i|William I]] — the first Norman king who conquered England and ordered the Domesday Book.
- [[henry-ii|Henry II]] — the first Plantagenet king, lord of the Angevin Empire, who clashed with Thomas Becket.
- [[richard-i|Richard I]] — the Lionheart, a Crusader king who spent nearly his entire reign abroad.
- [[king-john|John]] — the unpopular king who lost Normandy and was forced to seal the Magna Carta.
- [[henry-viii|Henry VIII]] — the Tudor king who broke with Rome, dissolved the monasteries, and married six times.
- [[elizabeth-i|Elizabeth I]] — the Virgin Queen whose reign saw the defeat of the Spanish Armada and a cultural golden age.
- [[james-i|James I]] — the Stuart king who unified the English and Scottish crowns and targeted in the Gunpowder Plot.
- [[charles-i|Charles I]] — the monarch whose struggles with Parliament led to his execution during the English Civil War.
- [[george-iii|George III]] — the king who lost the American colonies and suffered from severe mental illness.
- [[victoria|Victoria]] — the Empress of India who reigned over the height of the British Empire.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
