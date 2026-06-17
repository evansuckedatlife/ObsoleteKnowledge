---
type: list
category: history
read: false
---

# British reform movements

The British reform movements most worth knowing for quiz bowl.

## nodes

- [[anti-corn-law-league|Anti-Corn Law League]] — The Anti-Corn Law League (1839–1846) was a mass political movement that successfully campaigned for the repeal of Britain's…
- [[british-abolitionism|British Abolitionism]] — British Abolitionism was the political and moral movement to end slavery throughout the British Empire, driven by a coalition…
- [[catholic-emancipation|Catholic Emancipation]] — Catholic Emancipation refers to the removal of legal disabilities imposed on Roman Catholics in Britain and Ireland, achieved…
- [[chartism|Chartism]] — Chartism was a mass working-class political movement in Britain from the 1830s to 1850s demanding democratic reforms codified…
- [[factory-acts-movement|Factory Acts Movement]] — The Factory Acts movement was a sustained nineteenth-century campaign to regulate industrial working conditions, particularly…
- [[great-reform-act-of-1832|Great Reform Act of 1832]] — The Great Reform Act of 1832 fundamentally restructured British electoral representation, abolishing rotten boroughs (sparsely…
- [[levellers|Levellers]] — The Levellers were a radical democratic and egalitarian movement in England during the English Civil War and Interregnum…
- [[luddites|Luddites]] — The Luddites were textile workers in the Midlands and North of England who, from 1811 to 1816, engaged in organized…
- [[tolpuddle-martyrs|Tolpuddle Martyrs]] — The Tolpuddle Martyrs were six agricultural laborers from the village of Tolpuddle in Dorset, England, who were arrested,…
- [[wspu|Women's Social and Political Union (Suffragettes)]] — The Women's Social and Political Union (WSPU), founded by Emmeline Pankhurst in Manchester in 1903, became the most militant…

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
