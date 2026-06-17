---
type: list
category: history
read: false
---

# massacres

The massacres most worth knowing for quiz bowl.

## nodes

- [[boston-massacre|Boston Massacre]] — The Boston Massacre was a violent street confrontation on March 5, 1770, in colonial Boston between British soldiers and an…
- [[jallianwala-bagh|Jallianwala Bagh]] — The Jallianwala Bagh Massacre took place on April 13, 1919, in Amritsar, Punjab, when British Brigadier General Reginald Dyer…
- [[katyn|Katyn]] — The Katyn Massacre was the systematic execution of between 4,400 and 21,857 Polish military officers, intellectuals, and state…
- [[massacre-of-glencoe|Massacre of Glencoe]] — The Massacre of Glencoe occurred on February 13, 1692, in the Scottish Highlands, when government soldiers, billeted among the…
- [[my-lai|My Lai]] — The My Lai Massacre was the systematic slaughter of between 347 and 504 South Vietnamese civilians, including women, children,…
- [[nanjing-massacre|Nanjing Massacre]] — The Nanjing Massacre was a six-week campaign of mass killing, rape, and pillage perpetrated by the Japanese Imperial Army…
- [[peterloo|Peterloo]] — The Peterloo Massacre occurred on August 16, 1819, in Manchester, England, when British cavalry and militia charged into a…
- [[sand-creek|Sand Creek]] — The Sand Creek Massacre occurred on November 29, 1864, when Colorado cavalry volunteers under Colonel John Milton Chivington…
- [[st-bartholomews-day-massacre|St. Bartholomew's Day Massacre]] — The St.
- [[wounded-knee|Wounded Knee]] — The Wounded Knee Massacre occurred on December 29, 1890, when the U.S.

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
