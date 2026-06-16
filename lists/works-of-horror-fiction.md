---
type: list
category: literature
read: false
---

# works of horror fiction

The works of horror fiction most worth knowing for quiz bowl.

## nodes

- [[dracula|Dracula]] — Bram Stoker's 1897 novel is a masterwork of epistolary Gothic horror depicting the invasion of Victorian England by Count…
- [[frankenstein|Frankenstein]] — Mary Shelley's 1818 novel is the foundational text of Gothic horror and science fiction, telling the story of Victor…
- [[something-wicked-this-way-comes|Something Wicked This Way Comes]] — Ray Bradbury's 1962 novel presents a gothic Americana vision of two boys confronted with Cooger & Dark's Pandemonium Shadow…
- [[the-call-of-cthulhu|The Call of Cthulhu]] — H.P.
- [[the-fall-of-the-house-of-usher|The Fall of the House of Usher]] — Edgar Allan Poe's 1839 masterwork of psychological terror follows an unnamed narrator's visit to a childhood friend, Roderick…
- [[the-haunting-of-hill-house|The Haunting of Hill House]] — Shirley Jackson's 1959 novel tells the story of Eleanor Vance, a lonely woman invited to participate in a parapsychological…
- [[the-monkeys-paw|The Monkey's Paw]] — William Wymark Jacobs's 1902 short story presents a supernatural artifact that grants wishes with devastating consequences.
- [[the-strange-case-of-dr-jekyll-and-mr-hyde|The Strange Case of Dr. Jekyll and Mr. Hyde]] — Robert Louis Stevenson's 1886 novella explores the Gothic terror of the divided self through the story of Dr.
- [[the-turn-of-the-screw|The Turn of the Screw]] — Henry James's 1898 novella is a masterwork of ambiguous horror centered on a governess who takes a position at an isolated…
- [[the-yellow-wallpaper|The Yellow Wallpaper]] — Charlotte Perkins Gilman's 1892 short story traces a woman's psychological descent while confined to a room for rest cure…

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
