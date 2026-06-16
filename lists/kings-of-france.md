---
type: list
category: history
read: false
---

# kings of France

The kings of France most worth knowing for quiz bowl.

## nodes

- [[charlemagne|Charlemagne]] — Charlemagne (c.
- [[clovis|Clovis]] — Clovis (c.
- [[francis-i|Francis I]] — Francis I (1494–1547), the first French Renaissance king, was a patron of arts and letters who made France a cultural power…
- [[henry-iv|Henry IV]] — Henry IV (1553–1610), originally king of Navarre, founded the Bourbon dynasty and ended the French Wars of Religion through…
- [[louis-ix|Louis IX]] — Louis IX (1214–1270), canonized as Saint Louis, was a French king revered for his piety, justice, and military ambition.
- [[louis-xiii|Louis XIII]] — Louis XIII (1601–1643), called the Just, reigned during one of France's most transformative periods.
- [[louis-xiv|Louis XIV]] — Louis XIV (1638–1715), called the Sun King, was the longest-reigning European monarch and the embodiment of absolute monarchy.
- [[louis-xvi|Louis XVI]] — Louis XVI (1754–1793), the last Bourbon king of France, inherited the throne at a moment of fiscal crisis and deep social…
- [[philip-ii-augustus|Philip II Augustus]] — Philip II (1165–1223), called Augustus, transformed France from a minor feudal kingdom into the dominant European power.
- [[philip-iv|Philip IV]] — Philip IV (1268–1314), called the Fair, was a centralizing king who challenged papal authority and expanded royal power in France.

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
