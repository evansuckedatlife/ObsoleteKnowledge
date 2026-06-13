---
type: list
category: religion
read: false
---

# Popes

The leaders of the Roman Catholic Church who have shaped European history, Christian theology, and global politics from late antiquity to the modern era.

## nodes

- [[peter|Peter]] — Simon Peter, the leader of the apostles and traditionally the first Bishop of Rome.
- [[leo-i|Leo I]] — the first pope styled "the Great," who defined Christ's dual natures and turned away Attila the Hun.
- [[gregory-i|Gregory I]] — the first monk to become pope, who sent the Gregorian mission to England and codified liturgical reforms.
- [[gregory-vii|Gregory VII]] — the reformist pope who battled Holy Roman Emperor Henry IV in the Investiture Controversy.
- [[urban-ii|Urban II]] — the pope who launched the First Crusade at the Council of Clermont.
- [[innocent-iii|Innocent III]] — the peak of medieval papal power who convened the Fourth Lateran Council and launched the Fourth Crusade.
- [[boniface-viii|Boniface VIII]] — the pope who issued the bull *Unam Sanctam* and clashed with Philip IV of France.
- [[alexander-vi|Alexander VI]] — the notorious Borgia pope who divided the New World and advanced Cesare and Lucrezia's political power.
- [[julius-ii|Julius II]] — the "Warrior Pope" who rebuilt St. Peter's Basilica and commissioned Michelangelo and Raphael.
- [[leo-x|Leo X]] — the Medici pope who excommunicated Martin Luther and authorized the sale of indulgences.
- [[clement-vii|Clement VII]] — the Medici pope who refused Henry VIII's annulment and witnessed the Sack of Rome.
- [[john-paul-ii|John Paul II]] — the modern Polish pope who helped dismantle Eastern European communism and survived a 1981 assassination attempt.

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
