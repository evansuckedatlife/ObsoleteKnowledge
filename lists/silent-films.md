---
type: list
category: pop-culture
read: false
---

# silent films

The silent films most worth knowing for quiz bowl.

## nodes

- [[battleship-potemkin|Battleship Potemkin]] — Battleship Potemkin is Sergei Eisenstein's 1925 Soviet propaganda epic depicting a 1905 naval mutiny against the Tsarist regime.
- [[intolerance|Intolerance]] — Intolerance is D.W.
- [[metropolis-film|Metropolis]] — Metropolis is Fritz Lang's 1927 German science-fiction epic depicting a futuristic city divided between a wealthy elite living…
- [[nosferatu|Nosferatu]] — Nosferatu, an unauthorized 1922 adaptation of Bram Stoker's Dracula, is F.W.
- [[sherlock-jr|Sherlock Jr.]] — Sherlock Jr.
- [[sunrise|Sunrise]] — Sunrise is F.W.
- [[the-birth-of-a-nation|The Birth of a Nation]] — The Birth of a Nation is D.W.
- [[the-cabinet-of-dr-caligari|The Cabinet of Dr. Caligari]] — The Cabinet of Dr.
- [[the-general|The General]] — The General is Buster Keaton's 1926 silent comedy set during the American Civil War, in which a railroad engineer pursues a…
- [[the-gold-rush|The Gold Rush]] — The Gold Rush is Charlie Chaplin's 1925 masterpiece following a hapless prospector during the Yukon gold rush who endures…

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
