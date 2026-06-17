---
type: list
category: history
read: false
---

# Secretaries of State

The Secretaries of State most worth knowing for quiz bowl.

## nodes

- [[cordell-hull|Cordell Hull]] — Cordell Hull was Secretary of State under President Franklin D.
- [[daniel-webster|Daniel Webster]] — Daniel Webster was a dominant figure of 19th-century American politics, serving as Secretary of State under President William…
- [[dean-acheson|Dean Acheson]] — Dean Acheson was Secretary of State under President Harry S.
- [[george-marshall|George Marshall]] — George Marshall was Secretary of State under President Harry S.
- [[henry-kissinger|Henry Kissinger]] — Henry Kissinger was National Security Adviser and then Secretary of State under President Richard Nixon from 1969 to 1977,…
- [[john-hay|John Hay]] — John Hay was Secretary of State under President Theodore Roosevelt from 1901 to 1905, a pivotal figure in establishing…
- [[john-quincy-adams|John Quincy Adams]] — John Quincy Adams was Secretary of State under President James Monroe from 1817 to 1825, during which he orchestrated some of…
- [[madeleine-albright|Madeleine Albright]] — Madeleine Albright was Secretary of State under President Bill Clinton from 1997 to 2001, the first female to hold the office…
- [[thomas-jefferson|Thomas Jefferson]] — Thomas Jefferson was the primary author of the Declaration of Independence and the nation's first Secretary of State under…
- [[william-seward|William Seward]] — William Seward was Secretary of State under President Abraham Lincoln from 1861 to 1869, playing a crucial role in securing…

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
