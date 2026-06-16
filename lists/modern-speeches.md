---
type: list
category: history
read: false
---

# modern speeches

The modern speeches most worth knowing for quiz bowl.

## nodes

- [[aint-i-a-woman|Ain't I a Woman?]] — Sojourner Truth's extemporaneous speech delivered at an 1851 women's rights convention in Akron, Ohio, fused abolitionist and…
- [[blood-toil-tears-and-sweat|Blood, Toil, Tears and Sweat]] — Winston Churchill's maiden address as Prime Minister to Parliament on May 13, 1940, just days after taking office amid Nazi…
- [[cross-of-gold|Cross of Gold]] — William Jennings Bryan's electrifying address at the 1896 Democratic National Convention, "You shall not press down upon the…
- [[four-freedoms|Four Freedoms]] — Franklin D.
- [[gettysburg-address|Gettysburg Address]] — Abraham Lincoln's brief remarks delivered at the dedication of the Soldiers' National Cemetery in Gettysburg, Pennsylvania on…
- [[mandela-i-am-prepared-to-die|I Am Prepared to Die]] — Nelson Mandela's statement from the dock at the Rivonia Trial on April 20, 1964, articulated his rationale for armed…
- [[i-have-a-dream|I Have a Dream]] — Martin Luther King Jr.'s defining oration delivered during the 1963 March on Washington for Jobs and Freedom, it articulates…
- [[ich-bin-ein-berliner|Ich bin ein Berliner]] — President John F.
- [[tear-down-this-wall|Tear Down This Wall]] — Ronald Reagan's speech at the Brandenburg Gate on June 12, 1987, issued a direct challenge to Soviet leader Mikhail Gorbachev…
- [[we-shall-fight-on-the-beaches|We Shall Fight on the Beaches]] — Winston Churchill's defiant address to Parliament on June 4, 1940, delivered after the Allied evacuation from Dunkirk, steels…

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
