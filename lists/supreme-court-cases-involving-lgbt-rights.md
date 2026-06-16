---
type: list
category: history
read: false
---

# Supreme Court cases involving LGBT+ rights

The Supreme Court cases involving LGBT+ rights most worth knowing for quiz bowl.

## nodes

- [[303-creative-v-elenis|303 Creative v. Elenis]] — 303 Creative v.
- [[bostock-v-clayton-county|Bostock v. Clayton County]] — Bostock v.
- [[bowers-v-hardwick|Bowers v. Hardwick]] — Bowers v.
- [[hollingsworth-v-perry|Hollingsworth v. Perry]] — Hollingsworth v.
- [[lawrence-v-texas|Lawrence v. Texas]] — Lawrence v.
- [[masterpiece-cakeshop-v-colorado|Masterpiece Cakeshop v. Colorado]] — Masterpiece Cakeshop v.
- [[obergefell-v-hodges|Obergefell v. Hodges]] — Obergefell v.
- [[one-inc-v-olesen|One Inc. v. Olesen]] — One Inc.
- [[romer-v-evans|Romer v. Evans]] — Romer v.
- [[united-states-v-windsor|United States v. Windsor]] — United States v.

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
