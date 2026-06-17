---
type: list
category: history
read: false
---

# Supreme Court cases

The Supreme Court cases most worth knowing for quiz bowl.

## nodes

- [[baker-v-carr|Baker v. Carr]] — Baker v.
- [[bush-v-gore|Bush v. Gore]] — Bush v.
- [[citizens-united-v-fec|Citizens United v. FEC]] — Citizens United v.
- [[dartmouth-college-v-woodward|Dartmouth College v. Woodward]] — Dartmouth College v.
- [[engel-v-vitale|Engel v. Vitale]] — Engel v.
- [[new-york-times-co-v-sullivan|New York Times Co. v. Sullivan]] — New York Times Co.
- [[tinker-v-des-moines|Tinker v. Des Moines]] — Tinker v.
- [[united-states-v-nixon|United States v. Nixon]] — United States v.
- [[wickard-v-filburn|Wickard v. Filburn]] — Wickard v.
- [[youngstown-sheet-tube-co-v-sawyer|Youngstown Sheet & Tube Co. v. Sawyer]] — Youngstown Sheet & Tube Co.

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
