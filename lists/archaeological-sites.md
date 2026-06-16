---
type: list
category: social-science
read: false
---

# archaeological sites

The archaeological sites most worth knowing for quiz bowl.

## nodes

- [[chichen-itza|Chichén Itzá]] — Chichén Itzá is a major ceremonial center in the Yucatan Peninsula, Mexico, representing the syncretism of Maya and Toltec…
- [[gobekli-tepe|Göbekli Tepe]] — Göbekli Tepe is a Neolithic sanctuary in southeastern Turkey, dating to around 9600 BCE, making it one of the world's oldest…
- [[knossos|Knossos]] — Knossos is the largest Minoan palace on the island of Crete, Greece, occupied from approximately 2000 to 1370 BCE.
- [[lanse-aux-meadows|L'Anse aux Meadows]] — L'Anse aux Meadows is a Norse settlement on the northern tip of Newfoundland, Canada, dating to around 1000 CE, representing…
- [[lascaux|Lascaux]] — Lascaux is a cave in southwestern France containing some of the world's finest Paleolithic wall paintings, created roughly…
- [[machu-picchu|Machu Picchu]] — Machu Picchu is a 15th-century Inca citadel set high in the Andes mountains of Peru, built at the height of Inca imperial power.
- [[mohenjo-daro|Mohenjo-daro]] — Mohenjo-daro is the largest city of the Indus Valley Civilization, flourishing from approximately 2600 to 1900 BCE in what is…
- [[olduvai-gorge|Olduvai Gorge]] — Olduvai Gorge is a ravine in Tanzania containing some of the world's most important fossil evidence of human evolution and…
- [[pompeii|Pompeii]] — Pompeii is a Roman city preserved in volcanic ash after the catastrophic eruption of Mount Vesuvius in 79 CE.
- [[stonehenge|Stonehenge]] — Stonehenge is a monumental circle of standing stones on the Salisbury Plain in England, built in stages over more than 1,500…
- [[catalhoyuk|Çatalhöyük]] — Çatalhöyük is a Neolithic settlement in central Turkey, occupied from approximately 7500 to 5700 BCE, representing one of the…

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
