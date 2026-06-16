---
type: list
category: history
read: false
---

# explorers

The explorers most worth knowing for quiz bowl.

## nodes

- [[christopher-columbus|Christopher Columbus]] — Christopher Columbus was a Genoese navigator whose 1492 voyage across the Atlantic Ocean reached the Caribbean islands,…
- [[ernest-shackleton|Ernest Shackleton]] — Ernest Shackleton was an Irish polar explorer whose attempts to reach the South Pole and cross Antarctica resulted in…
- [[ferdinand-magellan|Ferdinand Magellan]] — Ferdinand Magellan was a Portuguese navigator who led the first expedition to circumnavigate the globe, departing in 1519…
- [[henry-hudson|Henry Hudson]] — Henry Hudson was an English navigator who conducted multiple Arctic and North American expeditions seeking the fabled…
- [[james-cook|James Cook]] — Captain James Cook was an 18th-century British naval officer whose methodical voyages charted vast regions of the Pacific…
- [[john-cabot|John Cabot]] — John Cabot was a Venetian-born explorer who sailed under the English flag to explore the North American coast in 1497,…
- [[marco-polo|Marco Polo]] — Marco Polo was a 13th-century Venetian merchant and explorer whose account of his journey to the court of Kublai Khan opened…
- [[meriwether-lewis|Meriwether Lewis]] — Meriwether Lewis was a 19th-century American explorer who co-led the Lewis and Clark Expedition, a landmark American journey…
- [[roald-amundsen|Roald Amundsen]] — Roald Amundsen was a Norwegian explorer who achieved both the Northwest Passage and the South Pole, becoming the first person…
- [[vasco-da-gama|Vasco da Gama]] — Vasco da Gama was a Portuguese explorer who established the first direct sea route from Europe to Asia by sailing around…
- [[zheng-he|Zheng He]] — Zheng He was a 15th-century Chinese admiral and explorer who commanded massive maritime expeditions across the Indian Ocean,…

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
