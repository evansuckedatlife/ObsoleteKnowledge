---
type: list
category: music
read: false
---

# works by Ludwig van Beethoven

The works by Ludwig van Beethoven most worth knowing for quiz bowl.

## nodes

- [[appassionata-sonata|Appassionata Sonata]] — Ludwig van Beethoven's Piano Sonata No.
- [[fidelio|Fidelio]] — Fidelio, Op.
- [[missa-solemnis|Missa solemnis]] — Ludwig van Beethoven's Missa solemnis in D major, Op.
- [[moonlight-sonata|Moonlight Sonata]] — Ludwig van Beethoven's Piano Sonata No.
- [[piano-concerto-no-5-beethoven|Piano Concerto No. 5 in E-flat major]] — Ludwig van Beethoven's Piano Concerto No.
- [[symphony-no-3-beethoven|Symphony No. 3 in E-flat major]] — Ludwig van Beethoven's Symphony No.
- [[symphony-no-5-beethoven|Symphony No. 5 in C minor]] — Ludwig van Beethoven's Symphony No.
- [[symphony-no-6-beethoven|Symphony No. 6 in F major]] — Ludwig van Beethoven's Symphony No.
- [[symphony-no-9-beethoven|Symphony No. 9 in D minor]] — Ludwig van Beethoven's Symphony No.
- [[wellingtons-victory|Wellington's Victory]] — Ludwig van Beethoven's Wellington's Victory, or the Battle of Vitoria, Op.

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
