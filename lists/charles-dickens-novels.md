---
type: list
category: literature
read: false
---

# Charles Dickens novels

The Charles Dickens novels most worth knowing for quiz bowl.

## nodes

- [[a-christmas-carol|A Christmas Carol]] — A Christmas Carol, published in 1843, is Dickens's novella of spiritual redemption: the miserly Ebenezer Scrooge is visited by…
- [[a-tale-of-two-cities|A Tale of Two Cities]] — A Tale of Two Cities, serialized from 1859 to 1860, is Dickens's historical novel of the French Revolution, set in London and…
- [[bleak-house|Bleak House]] — Bleak House, serialized from 1852 to 1853, is Dickens's darkest novel, weaving together multiple narratives in a sprawling…
- [[david-copperfield|David Copperfield]] — David Copperfield, serialized from 1849 to 1850, is Dickens's semi-autobiographical novel following a boy from birth through…
- [[great-expectations|Great Expectations]] — Great Expectations, serialized from 1860 to 1861 and narrated by the protagonist Pip in adulthood, follows a young orphan's…
- [[hard-times|Hard Times]] — Hard Times, serialized in 1854, is Dickens's shortest novel and his only explicitly political one, set in the industrial town…
- [[nicholas-nickleby|Nicholas Nickleby]] — Nicholas Nickleby, serialized from 1838 to 1839, follows a young gentleman's struggles after his father's death, his abuse at…
- [[oliver-twist|Oliver Twist]] — Oliver Twist is Dickens's second novel, serialized from 1837 to 1839, depicting the orphaned Oliver's suffering in a…
- [[our-mutual-friend|Our Mutual Friend]] — Our Mutual Friend, serialized from 1864 to 1865, is Dickens's final completed novel, set in Victorian London's world of money,…
- [[the-old-curiosity-shop|The Old Curiosity Shop]] — The Old Curiosity Shop, serialized from 1840 to 1841, follows a young orphan girl, Little Nell, and her grandfather, whose…
- [[the-pickwick-papers|The Pickwick Papers]] — The Pickwick Papers is Charles Dickens's debut novel, published serially from 1836 to 1837, following the adventures of an…

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
