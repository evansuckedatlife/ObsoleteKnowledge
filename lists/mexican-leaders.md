---
type: list
category: history
read: false
---

# Mexican leaders

The Mexican leaders most worth knowing for quiz bowl.

## nodes

- [[agustin-de-iturbide|Agustín de Iturbide]] — Agustín de Iturbide was a Mexican general and statesman who completed the independence war begun by Miguel Hidalgo, crowned…
- [[antonio-lopez-de-santa-anna|Antonio López de Santa Anna]] — Antonio López de Santa Anna was a Mexican military general and politician who served as president multiple times, alternating…
- [[benito-juarez|Benito Juárez]] — Benito Juárez was a Zapotec Mexican president who led the country through the Reform War and French intervention, ultimately…
- [[emiliano-zapata|Emiliano Zapata]] — Emiliano Zapata was a Mexican agrarian revolutionary leader whose 1911 Plan de Ayala became the moral centre of the Mexican…
- [[francisco-madero|Francisco Madero]] — Francisco Madero was a Mexican politician and revolutionary who challenged Porfirio Díaz's dictatorship in 1910 and briefly…
- [[lazaro-cardenas|Lázaro Cárdenas]] — Lázaro Cárdenas was a Mexican president (1934–1940) who implemented the social revolution promised by the Constitution of 1917.
- [[miguel-hidalgo|Miguel Hidalgo]] — Miguel Hidalgo was a Mexican Catholic priest whose 1810 Grito de Dolores (Cry of Dolores) launched the Mexican War of…
- [[pancho-villa|Pancho Villa]] — Pancho Villa (born Doroteo Arango) was a northern Mexican revolutionary general whose Division del Norte became the largest…
- [[porfirio-diaz|Porfirio Díaz]] — Porfirio Díaz was a Mexican military general and statesman who ruled the country for 30 years (1876–1911), bringing…
- [[vicente-fox|Vicente Fox]] — Vicente Fox was a Mexican businessman and politician who served as president (2000–2006), becoming the first non-PRI president…

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
