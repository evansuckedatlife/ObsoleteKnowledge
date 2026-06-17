---
type: list
category: religion
read: false
---

# popes

The popes most worth knowing for quiz bowl.

## nodes

- [[alexander-vi|Alexander VI]] — Reigning as pope from 1492 to 1503, Alexander VI (born Rodrigo Borgia) is the most notorious of the Renaissance popes, with a…
- [[boniface-viii|Boniface VIII]] — Reigning as pope from 1294 to 1303, Boniface VIII (born Benedetto Caetani) is remembered for his extreme claims of papal…
- [[clement-vii|Clement VII]] — Reigning as pope from 1523 to 1534, Clement VII (born Giulio de' Medici) had a tumultuous pontificate defined by the rapid…
- [[gregory-i|Gregory I]] — Reigning from 590 to 604, Gregory I was a transformative pope who bridged the transition from the classical Roman world to the…
- [[gregory-vii|Gregory VII]] — Reigning as pope from 1073 to 1085, Gregory VII (originally named Hildebrand) was a zealous reformer who fought to establish…
- [[innocent-iii|Innocent III]] — Reigning from 1198 to 1216, Innocent III represents the absolute zenith of medieval papal authority and influence.
- [[john-paul-ii|John Paul II]] — Reigning as pope from 1978 to 2005, John Paul II (born Karol Wojtyła) was the first non-Italian pope in 455 years and the…
- [[julius-ii|Julius II]] — Reigning from 1503 to 1513, Julius II was one of the most powerful, active, and influential popes of the High Renaissance.
- [[leo-i|Leo I]] — Reigning as pope from 440 to 461, Leo I was a key figure in establishing the authority of the bishop of Rome as the supreme…
- [[leo-x|Leo X]] — Reigning as pope from 1513 to 1521, Leo X (born Giovanni de' Medici) was a lavish patron of the arts and the son of Lorenzo…
- [[peter|Peter]] — One of Jesus's most prominent apostles, originally a fisherman named Simon who became the rock upon which Jesus built his church.
- [[urban-ii|Urban II]] — Reigning as pope from 1088 to 1099, Urban II (originally Odo of Châtillon) was a key administrative reformer who continued the…

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
