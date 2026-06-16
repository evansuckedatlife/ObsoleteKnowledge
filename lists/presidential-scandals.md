---
type: list
category: history
read: false
---

# presidential scandals

The presidential scandals most worth knowing for quiz bowl.

## nodes

- [[corrupt-bargain|Corrupt Bargain]] — The Corrupt Bargain of 1824 refers to the alleged secret deal between John Quincy Adams and Henry Clay that resulted in Adams'…
- [[credit-mobilier|Crédit Mobilier]] — The Crédit Mobilier scandal involved the construction company Crédit Mobilier of America, created to build the Union Pacific…
- [[iran-contra|Iran-Contra]] — The Iran-Contra affair was a covert operation during the Reagan administration in which officials secretly facilitated arms…
- [[petticoat-affair|Petticoat Affair]] — The Petticoat Affair (also called the Eaton Affair) was a social scandal during President Andrew Jackson's administration…
- [[teapot-dome|Teapot Dome]] — Teapot Dome is the scandal that emerged from secret leases of federal oil reserves during President Warren G.
- [[the-lewinsky-scandal|The Lewinsky Scandal]] — The Lewinsky scandal erupted when President Bill Clinton's sexual relationship with White House intern Monica Lewinsky became…
- [[watergate|Watergate]] — Watergate is the political scandal arising from the 1972 break-in at the Democratic National Committee headquarters and the…
- [[whiskey-ring|Whiskey Ring]] — The Whiskey Ring was a nationwide conspiracy of distillers, government revenue agents, and corrupt officials who falsified tax…
- [[whitewater|Whitewater]] — Whitewater refers to an investigation into the Clintons' involvement in the Whitewater Development Corporation, a failed…
- [[xyz-affair|XYZ Affair]] — The XYZ Affair was a diplomatic scandal of 1797–1798 in which French diplomatic intermediaries demanded bribes from American…

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
