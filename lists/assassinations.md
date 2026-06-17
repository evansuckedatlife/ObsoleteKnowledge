---
type: list
category: history
read: false
---

# assassinations

The assassinations most worth knowing for quiz bowl.

## nodes

- [[assassination-of-abraham-lincoln|Assassination of Abraham Lincoln]] — On April 14, 1865, President Abraham Lincoln was shot by actor John Wilkes Booth at Ford's Theatre in Washington, D.C., dying…
- [[assassination-of-anwar-sadat|Assassination of Anwar Sadat]] — On October 6, 1981, Egyptian President Anwar Sadat was shot and killed by members of the militant Islamic group Egyptian…
- [[assassination-of-archduke-franz-ferdinand|Assassination of Archduke Franz Ferdinand]] — On June 28, 1914, Archduke Franz Ferdinand, heir to the Austro-Hungarian throne, was shot and killed in Sarajevo by Gavrilo…
- [[assassination-of-james-garfield|Assassination of James A. Garfield]] — On July 2, 1881, President James A.
- [[assassination-of-jfk|Assassination of John F. Kennedy]] — On November 22, 1963, President John F.
- [[assassination-of-julius-caesar|Assassination of Julius Caesar]] — On March 15, 44 BCE (the Ides of March), Julius Caesar was stabbed to death in Rome by a group of senators including his…
- [[assassination-of-martin-luther-king-jr|Assassination of Martin Luther King Jr.]] — On April 4, 1968, Dr.
- [[assassination-of-gandhi|Assassination of Mohandas Gandhi]] — On January 30, 1948, Mohandas Gandhi, the spiritual leader of India's independence struggle and pioneer of nonviolent…
- [[assassination-of-tsar-alexander-ii|Assassination of Tsar Alexander II]] — On March 13, 1881, Tsar Alexander II of Russia was mortally wounded by a bomb thrown by members of the revolutionary group…
- [[assassination-of-yitzhak-rabin|Assassination of Yitzhak Rabin]] — On November 4, 1995, Israeli Prime Minister Yitzhak Rabin was shot and killed by Yigal Amir, a right-wing Israeli extremist…

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
