---
type: list
category: history
read: false
---

# elections

The elections most worth knowing for quiz bowl.

## nodes

- [[election-of-1800|Election of 1800]] — The 1800 presidential election marked the first peaceful transfer of power between opposing political parties in American history.
- [[election-of-1824|Election of 1824]] — The 1824 election was thrown into the House of Representatives when no candidate won an Electoral College majority, resulting…
- [[election-of-1860|Election of 1860]] — Abraham Lincoln's 1860 election victory without a single southern electoral vote precipitated the secession crisis that…
- [[election-of-1876|Election of 1876]] — The 1876 election between Republican Rutherford B.
- [[election-of-1912|Election of 1912]] — The 1912 election split the Republican Party and ushered in an era of progressive reform under Woodrow Wilson.
- [[election-of-1932|Election of 1932]] — Franklin D.
- [[election-of-1948|Election of 1948]] — Harry Truman's shocking upset victory over heavily favored Thomas Dewey in 1948 defied virtually every poll and political…
- [[election-of-1960|Election of 1960]] — John F.
- [[election-of-1968|Election of 1968]] — Richard Nixon's comeback victory in 1968 over Vice President Hubert Humphrey ended a generation of Democratic dominance and…
- [[election-of-2000|Election of 2000]] — George W.

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
