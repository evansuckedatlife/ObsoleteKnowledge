---
type: list
category: literature
read: false
---

# African-American authors

The African-American authors most worth knowing for quiz bowl.

## nodes

- [[alice-walker|Alice Walker]] — Alice Walker is an American novelist, poet, and essayist known for The Color Purple (1982), a Pulitzer Prize-winning novel…
- [[frederick-douglass|Frederick Douglass]] — Frederick Douglass (1818–1895) was an escaped enslaved American who became the most prominent Black intellectual and orator of…
- [[gwendolyn-brooks|Gwendolyn Brooks]] — Gwendolyn Brooks was an American poet known for her precise, accessible verse that examined the lives of ordinary Black…
- [[james-baldwin|James Baldwin]] — James Baldwin was an American writer and social critic whose essays, novels, and plays explored identity, race, sexuality, and…
- [[langston-hughes|Langston Hughes]] — Langston Hughes was an American poet, writer, and cultural innovator central to the Harlem Renaissance, known for infusing his…
- [[lorraine-hansberry|Lorraine Hansberry]] — Lorraine Hansberry was an American playwright whose debut A Raisin in the Sun (1959) became the first play by an…
- [[maya-angelou|Maya Angelou]] — Maya Angelou (1928–2014) was an American autobiographer, poet, and performer known for I Know Why the Caged Bird Sings (1969),…
- [[phillis-wheatley|Phillis Wheatley]] — Phillis Wheatley (c.
- [[ralph-ellison|Ralph Ellison]] — Ralph Ellison was an American novelist best known for Invisible Man (1952), a masterwork of modernist literature that explored…
- [[richard-wright|Richard Wright]] — Richard Wright (1908–1960) was an American novelist whose unsparing social realist works depicted Black poverty, racism, and…
- [[toni-morrison|Toni Morrison]] — Toni Morrison was an American novelist whose work transformed American literature by centering Black interiority, history, and…
- [[w-e-b-du-bois|W.E.B. Du Bois]] — W.E.B.
- [[zora-neale-hurston|Zora Neale Hurston]] — Zora Neale Hurston was an American novelist, folklorist, and anthropologist who celebrated Black Southern vernacular culture…

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
