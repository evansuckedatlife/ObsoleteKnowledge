---
type: list
category: history
read: false
---

# magazines from American history

The magazines from American history most worth knowing for quiz bowl.

## nodes

- [[harpers-magazine|Harper's Magazine]] — Harper's Magazine, founded in 1850, is one of the oldest continuously published American magazines.
- [[ladies-home-journal|Ladies' Home Journal]] — Ladies' Home Journal, founded in 1883, was the first magazine explicitly designed and edited for women, reaching unprecedented…
- [[life-magazine|Life Magazine]] — Life magazine, launched in 1936 by Henry Luce, pioneered the picture-magazine format and became the dominant visual chronicle…
- [[mcclures-magazine|McClure's Magazine]] — McClure's Magazine, founded in 1893 by S.
- [[national-geographic|National Geographic]] — National Geographic Magazine, founded in 1888 by the National Geographic Society, is an illustrated journal of exploration,…
- [[readers-digest|Reader's Digest]] — Reader's Digest, founded in 1922 by DeWitt Wallace and Lila Acheson Wallace, revolutionized magazine publishing by condensing…
- [[the-atlantic|The Atlantic]] — The Atlantic (originally The Atlantic Monthly), founded in 1857, is an influential American magazine of literature, politics,…
- [[the-new-yorker|The New Yorker]] — The New Yorker, founded in 1925 by Harold Ross, is an influential American magazine of commentary, criticism, fiction, and…
- [[the-saturday-evening-post|The Saturday Evening Post]] — The Saturday Evening Post is an American weekly magazine founded in 1821 that became the most widely circulated periodical in…
- [[time-magazine|Time Magazine]] — Time magazine, founded in 1923 by Henry Luce and Briton Hadden, revolutionized American journalism by condensing the week's…

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
