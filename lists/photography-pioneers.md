---
type: list
category: visual-art
read: false
---

# photography pioneers

The photography pioneers most worth knowing for quiz bowl.

## nodes

- [[alfred-stieglitz|Alfred Stieglitz]] — Alfred Stieglitz was an American photographer and tastemaker who championed photography as a fine art in the early 20th century.
- [[ansel-adams|Ansel Adams]] — Ansel Adams was an American landscape and environmental photographer renowned for his dramatic black-and-white photographs of…
- [[dorothea-lange|Dorothea Lange]] — Dorothea Lange was an American documentary photographer best known for her work documenting the Great Depression and…
- [[eadweard-muybridge|Eadweard Muybridge]] — Eadweard Muybridge was a British photographer famous for pioneering motion photography—using sequences of rapid sequential…
- [[henri-cartier-bresson|Henri Cartier-Bresson]] — Henri Cartier-Bresson was a French photographer and photojournalist who pioneered the philosophy of the "decisive moment"—the…
- [[julia-margaret-cameron|Julia Margaret Cameron]] — Julia Margaret Cameron was a British photographer of the Victorian era who pioneered artistic portraiture and narrative…
- [[louis-daguerre|Louis Daguerre]] — Louis Daguerre was a French painter and inventor who pioneered the daguerreotype, the first commercially viable photographic…
- [[man-ray|Man Ray]] — Man Ray was an American photographer, painter, and filmmaker who pioneered cameraless photography—techniques like the…
- [[nicephore-niepce|Nicéphore Niépce]] — Nicéphore Niépce was a French inventor who created the first permanent photograph using a process called heliography around 1822.
- [[william-henry-fox-talbot|William Henry Fox Talbot]] — William Henry Fox Talbot was an English scientist and inventor who created the calotype, the first negative-positive…

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
