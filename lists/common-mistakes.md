---
type: list
category: misc
read: false
---

# common mistakes

The common mistakes most worth knowing for quiz bowl.

## nodes

- [[bloody-mary-confusion|Bloody Mary Confusion]] — A frequent conflation mistakes Mary I of England with Mary, Queen of Scots or uses "Bloody Mary" to refer to both…
- [[centripetal-centrifugal-force|Centripetal and Centrifugal Force]] — A widespread misconception treats centripetal and centrifugal force as equal-and-opposite real forces; in fact, only…
- [[et-tu-brute|Et tu, Brute?]] — The famous phrase "Et tu, Brute?" (And you, Brutus?) is attributed to Julius Caesar upon recognizing his ally Marcus Brutus…
- [[frankenstein-authorship|Frankenstein Authorship Myth]] — A widespread misconception holds that Frankenstein refers to the monster itself; in fact, Frankenstein is the name of the…
- [[holy-roman-empire|Holy Roman Empire]] — A persistent misconception portrays the Holy Roman Empire as a continuous monolithic realm spanning medieval and early modern…
- [[hudson-bay-geography|Hudson Bay Geography]] — A common misconception places Hudson Bay in the Arctic Ocean or confuses it with Hudson Strait.
- [[jekyll-and-hyde|Jekyll and Hyde]] — A persistent confusion mistakes Dr.
- [[john-adams-confusion|John Adams Confusion]] — Multiple historical figures named John or Adams from the early American era are frequently conflated.
- [[mary-wollstonecraft-shelley|Mary Wollstonecraft Shelley]] — Mary Wollstonecraft Shelley is often confused with or conflated with her mother, the philosopher and feminist Mary…
- [[oliver-wendell-holmes-confusion|Oliver Wendell Holmes Confusion]] — Two prominent Americans named Oliver Wendell Holmes, a father and son, lived overlapping lifespans and made significant…
- [[primates-classification|Primates Classification]] — A persistent misconception distinguishes primates from humans, treating humans as fundamentally separate from the primate…
- [[saint-augustine-confusion|Saint Augustine Confusion]] — Two major figures named Saint Augustine lived over two centuries apart, and they are frequently conflated despite very…
- [[invisible-man-authorship|The Invisible Man Authorship]] — Two major novels titled The Invisible Man or Invisible Man exist by different authors in different centuries, and they are…
- [[merchant-of-venice-antisemitism|The Merchant of Venice and Antisemitism]] — The Merchant of Venice is frequently misread as a redemptive or sympathetic portrait of the Jewish moneylender Shylock, when…

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
