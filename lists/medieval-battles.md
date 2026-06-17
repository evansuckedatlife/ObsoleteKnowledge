---
type: list
category: history
read: false
---

# medieval battles

The medieval battles most worth knowing for quiz bowl.

## nodes

- [[battle-of-agincourt|Battle of Agincourt]] — The Battle of Agincourt was fought on 25 October 1415 in northern France during the Hundred Years' War, where a heavily…
- [[battle-of-bannockburn|Battle of Bannockburn]] — The Battle of Bannockburn was fought on 23–24 June 1314 near Stirling in Scotland, where Robert the Bruce's Scottish forces…
- [[battle-of-bosworth-field|Battle of Bosworth Field]] — The Battle of Bosworth Field was fought on 22 August 1485 in Leicestershire, England, where Henry Tudor's forces defeated…
- [[battle-of-crécy|Battle of Crécy]] — The Battle of Crécy was fought on 26 August 1346 in northern France, where Edward III of England's forces decisively defeated…
- [[battle-of-hastings|Battle of Hastings]] — The Battle of Hastings was fought on 14 October 1066 in southeastern England, deciding the succession to the English throne…
- [[battle-of-hattin|Battle of Hattin]] — The Battle of Hattin was fought on 4 July 1187 in the Levant, where Saladin's Muslim forces decisively defeated the combined…
- [[battle-of-manzikert|Battle of Manzikert]] — The Battle of Manzikert was fought on 26 August 1071 in eastern Anatolia (modern Turkey), where the Seljuk Sultan Alp Arslan's…
- [[battle-of-stamford-bridge|Battle of Stamford Bridge]] — The Battle of Stamford Bridge was fought on 25 September 1066 in Yorkshire, England, where King Harold Godwinson defeated an…
- [[battle-of-tours|Battle of Tours]] — The Battle of Tours was fought in 732 CE between the Frankish forces of Charles Martel and a Muslim Umayyad army led by Abd…
- [[fall-of-constantinople|Fall of Constantinople]] — The Fall of Constantinople on 29 May 1453 marked the final collapse of the Byzantine Empire when Ottoman forces under Mehmed…

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
