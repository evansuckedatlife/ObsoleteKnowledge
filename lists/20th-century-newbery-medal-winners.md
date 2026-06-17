---
type: list
category: literature
read: false
---

# 20th-century Newbery Medal winners

The 20th-century Newbery Medal winners most worth knowing for quiz bowl.

## nodes

- [[a-wrinkle-in-time|A Wrinkle in Time]] — A Wrinkle in Time is a science-fiction adventure by Madeleine L'Engle about a girl named Meg Murry who travels across…
- [[bridge-to-terabithia|Bridge to Terabithia]] — Bridge to Terabithia is Katherine Paterson's novel about Jess Aarons, a shy, artistic boy who forms a deep friendship with a…
- [[dear-mr-henshaw|Dear Mr. Henshaw]] — Dear Mr.
- [[holes|Holes]] — Holes is Louis Sachar's novel about Stanley Yelnats, a boy wrongly imprisoned at Camp Green Lake, a brutal detention center in…
- [[mrs-frisby-and-the-rats-of-nimh|Mrs. Frisby and the Rats of NIMH]] — Mrs.
- [[roll-of-thunder-hear-my-cry|Roll of Thunder, Hear My Cry]] — Roll of Thunder, Hear My Cry is Mildred D.
- [[sounder|Sounder]] — Sounder is William H.
- [[the-giver|The Giver]] — The Giver is Lois Lowry's dystopian novel about a seemingly perfect, colorless society where all pain, choice, and emotion…
- [[the-view-from-saturday|The View from Saturday]] — The View from Saturday is Lois Lowry's novel about a sixth-grade Academic Quiz Bowl team competing at the state championship…
- [[the-westing-game|The Westing Game]] — The Westing Game is Ellen Raskin's intricate mystery novel about sixteen characters brought together by a will to solve the…

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
