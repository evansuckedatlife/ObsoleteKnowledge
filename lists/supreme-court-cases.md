---
type: list
category: history
read: false
---

# Supreme Court cases

The Supreme Court cases most worth knowing for quiz bowl.

## nodes

- [[gibbons-v-ogden|Gibbons v. Ogden]] — Gibbons v.
- [[gideon-v-wainwright|Gideon v. Wainwright]] — Gideon v.
- [[korematsu-v-united-states|Korematsu v. United States]] — Korematsu v.
- [[lochner-v-new-york|Lochner v. New York]] — Lochner v.
- [[mapp-v-ohio|Mapp v. Ohio]] — Mapp v.
- [[marbury-v-madison|Marbury v. Madison]] — Marbury v.
- [[mcculloch-v-maryland|McCulloch v. Maryland]] — McCulloch v.
- [[miranda-v-arizona|Miranda v. Arizona]] — Miranda v.
- [[roe-v-wade|Roe v. Wade]] — Roe v.
- [[schenck-v-united-states|Schenck v. United States]] — Schenck v.

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
