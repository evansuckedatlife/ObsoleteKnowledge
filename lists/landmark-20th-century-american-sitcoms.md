---
type: list
category: pop-culture
read: false
---

# landmark 20th-century American sitcoms

The landmark 20th-century American sitcoms most worth knowing for quiz bowl.

## nodes

- [[all-in-the-family|All in the Family]] — All in the Family aired on CBS from 1971 to 1979 and starred Carroll O'Connor as Archie Bunker, a bigoted, working-class…
- [[cheers|Cheers]] — Cheers aired on NBC from 1982 to 1993 and centered on the staff and patrons of a Boston dive bar called Cheers, where regulars…
- [[friends|Friends]] — Friends aired on NBC from 1994 to 2004 and followed six twentysomethings—Rachel, Monica, Phoebe, Ross, Chandler, and…
- [[i-love-lucy|I Love Lucy]] — I Love Lucy is the groundbreaking sitcom that premiered on CBS in 1951 and ran for six seasons, starring Lucille Ball as the…
- [[mash|M*A*S*H]] — MASH aired on CBS from 1972 to 1983 and followed a unit of American surgeons and support staff at a Mobile Army Surgical…
- [[seinfeld|Seinfeld]] — Seinfeld aired on NBC from 1989 to 1998 and starred stand-up comic Jerry Seinfeld as a fictionalized version of himself,…
- [[the-cosby-show|The Cosby Show]] — The Cosby Show aired on NBC from 1984 to 1992 and centered on Cliff Huxtable (Bill Cosby), an obstetrician, and his attorney…
- [[the-honeymooners|The Honeymooners]] — The Honeymooners was a sketch-comedy-turned-sitcom that aired on CBS from 1955 to 1956, starring Jackie Gleason as Ralph…
- [[the-mary-tyler-moore-show|The Mary Tyler Moore Show]] — The Mary Tyler Moore Show aired on CBS from 1970 to 1977 and centered on Mary Tyler Moore as Mary Richards, a single working…
- [[the-simpsons|The Simpsons]] — The Simpsons premiered on Fox in 1989 as an animated sitcom following the dysfunctional Simpson family—Homer, Marge, Bart,…

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
