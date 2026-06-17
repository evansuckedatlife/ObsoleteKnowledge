---
type: list
category: science
read: false
---

# chemical elements

The chemical elements most worth knowing for quiz bowl.

## nodes

- [[carbon|Carbon]] — Carbon is a nonmetallic tetravalent element that serves as the chemical basis for all known organic life.
- [[copper|Copper]] — Copper is a soft, malleable, and ductile transition metal with exceptionally high thermal and electrical conductivity.
- [[gold|Gold]] — Gold is a dense, soft, malleable, and highly ductile transition metal with a distinctive bright, warm yellow color.
- [[helium|Helium]] — Helium is a colorless, odorless, tasteless, and chemically inert monatomic gas that heads the noble gas group in the periodic…
- [[iron|Iron]] — Iron is a lustrous, ductile, and magnetic transition metal that is the most common element on Earth by mass, forming much of…
- [[mercury|Mercury]] — Mercury is a heavy, silvery transition metal that is the only metal that remains liquid at standard temperature and pressure.
- [[nitrogen|Nitrogen]] — Nitrogen is a nonmetallic element that forms a colorless, odorless, tasteless, and relatively inert diatomic gas making up…
- [[oxygen|Oxygen]] — Oxygen is a highly reactive, electronegative chalcogen nonmetal that is the third most abundant element in the universe by…
- [[sodium|Sodium]] — Sodium is a soft, silvery-white, highly reactive alkali metal that belongs to Group 1 of the periodic table.
- [[uranium|Uranium]] — Uranium is a heavy, silvery-white, weakly radioactive actinide metal that is the heaviest naturally occurring element in…

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
