---
type: list
category: visual-art
read: false
---

# architects

The architects most worth knowing for quiz bowl.

## nodes

- [[andrea-palladio|Andrea Palladio]] — Andrea Palladio (1508–1580) was a Venetian architect whose rational interpretation of classical Roman design established…
- [[antoni-gaudi|Antoni Gaudí]] — Antoni Gaudí (1852–1926) was a Catalan architect whose organic, sculptural approach created fantastical buildings that seemed…
- [[christopher-wren|Christopher Wren]] — Sir Christopher Wren (1632–1723) was an English polymath—mathematician, astronomer, and architect—whose work defined English…
- [[filippo-brunelleschi|Filippo Brunelleschi]] — Filippo Brunelleschi (1377–1446) was a Florentine architect and engineer who pioneered Renaissance architecture and linear…
- [[frank-gehry|Frank Gehry]] — Frank Gehry (born 1929) is a Canadian-American architect known for deconstructionist and expressionist buildings that…
- [[frank-lloyd-wright|Frank Lloyd Wright]] — Frank Lloyd Wright (1867–1959) was an American architect who pioneered organic architecture—a philosophy that integrated…
- [[i-m-pei|I. M. Pei]] — I.
- [[le-corbusier|Le Corbusier]] — Le Corbusier (1887–1965), born Charles-Édouard Jeanneret, was a Swiss-French architect who championed modernism and the…
- [[louis-sullivan|Louis Sullivan]] — Louis Sullivan (1856–1924) was an American architect and theorist who pioneered the modern skyscraper and championed…
- [[mies-van-der-rohe|Mies van der Rohe]] — Ludwig Mies van der Rohe (1886–1969) was a German-American architect and a master of minimalism who distilled buildings to…
- [[renzo-piano|Renzo Piano]] — Renzo Piano (born 1937) is an Italian architect known for high-tech, transparent designs that celebrate structure and materials.
- [[zaha-hadid|Zaha Hadid]] — Zaha Hadid (1950–2016) was an Iraqi-British architect pioneering parametric and computational design to create sweeping,…

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
