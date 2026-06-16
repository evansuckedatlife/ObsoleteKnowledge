---
type: list
category: literature
read: false
---

# short story authors

The short story authors most worth knowing for quiz bowl.

## nodes

- [[alice-munro|Alice Munro]] — Alice Munro (b.
- [[anton-chekhov|Anton Chekhov]] — Anton Chekhov (1860–1904) was a Russian physician-turned-writer who revolutionised modern drama and the short story through…
- [[edgar-allan-poe|Edgar Allan Poe]] — Edgar Allan Poe (1809–1849) was an American writer, poet, and editor who pioneered the modern detective story and perfected…
- [[ernest-hemingway|Ernest Hemingway]] — Ernest Hemingway (1899–1961) was an American novelist and short-story writer who stripped prose to its essentials, perfecting…
- [[flannery-oconnor|Flannery O'Connor]] — Flannery O'Connor (1925–1964) was an American short-story writer and novelist whose work fused Southern Gothic grotesquerie…
- [[guy-de-maupassant|Guy de Maupassant]] — Guy de Maupassant (1850–1893) was a French short-story master and novelist whose work epitomised the aesthetic and moral…
- [[jorge-luis-borges|Jorge Luis Borges]] — Jorge Luis Borges (1899–1986) was an Argentine writer and poet who revolutionised the short story by treating fiction as…
- [[o-henry|O. Henry]] — O.
- [[raymond-carver|Raymond Carver]] — Raymond Carver (1938–1988) was an American short-story writer and poet who perfected the art of minimalism in fiction—stories…
- [[saki|Saki]] — Saki (1870–1916), born H.H.

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
