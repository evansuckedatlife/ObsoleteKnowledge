---
type: list
category: history
read: false
---

# British prime ministers

The British prime ministers most worth knowing for quiz bowl.

## nodes

- [[arthur-wellesley-duke-of-wellington|Arthur Wellesley, Duke of Wellington]] — Arthur Wellesley, Duke of Wellington (1769–1852) was the paramount British military figure of the Napoleonic Wars, defeating…
- [[benjamin-disraeli|Benjamin Disraeli]] — Benjamin Disraeli (1804–1881) was the first Prime Minister of Jewish descent and a master of political theatre who transformed…
- [[clement-attlee|Clement Attlee]] — Clement Attlee (1883–1967) was the unassuming Labour Prime Minister who fundamentally reshaped post-war Britain by building…
- [[lloyd-george|David Lloyd George]] — David Lloyd George (1863–1945) was the last Liberal Prime Minister and a decisive wartime leader who mobilized Britain for…
- [[henry-john-temple-duke-of-palmerston|Henry John Temple, 3rd Viscount Palmerston]] — Henry John Temple, 3rd Viscount Palmerston (1784–1865) embodied mid-Victorian assertiveness as Foreign Secretary and Prime…
- [[margaret-thatcher|Margaret Thatcher]] — Margaret Thatcher (1925–2013) was Britain's first female Prime Minister and the architect of a radical rightward shift in…
- [[robert-peel|Robert Peel]] — Robert Peel (1788–1850) was a reforming Conservative who modernized British policing and shattered his own party over free trade.
- [[robert-walpole|Robert Walpole]] — Robert Walpole (1676–1745) is recognized as Britain's first Prime Minister, dominating Parliament for over two decades under…
- [[tony-blair|Tony Blair]] — Tony Blair (1953–) was the architect of New Labour and the longest-serving Labour Prime Minister in British history,…
- [[william-ewart-gladstone|William Ewart Gladstone]] — William Ewart Gladstone (1809–1898) was the dominant Liberal statesman of the Victorian era and a moralist in politics,…
- [[william-pitt-the-younger|William Pitt the Younger]] — William Pitt the Younger (1759–1806) was Britain's youngest Prime Minister at 24 and dominated Parliament through the French…
- [[winston-churchill|Winston Churchill]] — Winston Churchill (1874–1965) was the paramount wartime leader of the 20th century, rallying Britain to resist Nazi Germany…

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
