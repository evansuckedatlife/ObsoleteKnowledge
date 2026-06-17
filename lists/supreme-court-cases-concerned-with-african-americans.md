---
type: list
category: history
read: false
---

# Supreme Court cases concerned with African-Americans

The Supreme Court cases concerned with African-Americans most worth knowing for quiz bowl.

## nodes

- [[brown-v-board-of-education|Brown v. Board of Education]] — Brown v.
- [[dred-scott-v-sandford|Dred Scott v. Sandford]] — Dred Scott v.
- [[grutter-v-bollinger|Grutter v. Bollinger]] — Grutter v.
- [[heart-of-atlanta-motel-v-united-states|Heart of Atlanta Motel v. United States]] — Heart of Atlanta Motel v.
- [[loving-v-virginia|Loving v. Virginia]] — Loving v.
- [[plessy-v-ferguson|Plessy v. Ferguson]] — Plessy v.
- [[regents-v-bakke|Regents v. Bakke]] — Regents of the University of California v.
- [[shelby-county-v-holder|Shelby County v. Holder]] — Shelby County v.
- [[sweatt-v-painter|Sweatt v. Painter]] — Sweatt v.
- [[civil-rights-cases-1883|The Civil Rights Cases (1883)]] — The Civil Rights Cases (1883) struck down the Civil Rights Act of 1875, which had prohibited racial discrimination by private…

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
