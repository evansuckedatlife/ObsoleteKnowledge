---
type: list
category: history
read: false
---

# Chinese dynasties

The Chinese dynasties most worth knowing for quiz bowl.

## nodes

- [[han-dynasty|Han Dynasty]] — The Han Dynasty (206 BCE–220 CE) was China's second imperial dynasty and one of its most influential, lasting over 400 years…
- [[ming-dynasty|Ming Dynasty]] — The Ming Dynasty (1368–1644 CE) was a restoration of Han Chinese rule after the Mongol Yuan Dynasty, lasting nearly 300 years…
- [[qin-dynasty|Qin Dynasty]] — The Qin Dynasty (221–206 BCE) was China's first centralized empire, founded by Qin Shi Huang after his state conquered all…
- [[qing-dynasty|Qing Dynasty]] — The Qing Dynasty (1644–1912 CE) was the final imperial dynasty of China, established by the Manchus (a Jurchen people from…
- [[shang-dynasty|Shang Dynasty]] — The Shang Dynasty was China's first historically confirmed civilization, ruling the Yellow River valley from approximately…
- [[song-dynasty|Song Dynasty]] — The Song Dynasty (960–1279 CE) was a period of remarkable intellectual, technological, and economic advancement, despite its…
- [[sui-dynasty|Sui Dynasty]] — The Sui Dynasty (581–618 CE) was a short-lived but transformative dynasty that reunified China after nearly four centuries of…
- [[tang-dynasty|Tang Dynasty]] — The Tang Dynasty (618–907 CE) is widely regarded as the golden age of Chinese civilization, a period of unprecedented…
- [[yuan-dynasty|Yuan Dynasty]] — The Yuan Dynasty (1271–1368 CE) was the rule of the Mongol Empire over China, established by Kublai Khan, the grandson of…
- [[zhou-dynasty|Zhou Dynasty]] — The Zhou Dynasty (1046–256 BCE) was China's longest-lasting dynasty, spanning nearly 800 years and encompassing some of its…

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
