---
type: list
category: misc
read: false
---

# new-year celebrations

The new-year celebrations most worth knowing for quiz bowl.

## nodes

- [[chinese-new-year|Chinese New Year]] — Chinese New Year, also called the Spring Festival or Lunar New Year, is the most important celebration in Chinese culture,…
- [[hijri-new-year|Hijri New Year]] — The Hijri New Year (Islamic New Year), also called the celebration of Muharram, marks the beginning of the Islamic lunar…
- [[hogmanay|Hogmanay]] — Hogmanay is the Scottish celebration of New Year on December 31 and January 1, featuring street festivals, midnight bonfires,…
- [[junkanoo|Junkanoo]] — Junkanoo is a vibrant Bahamian street parade celebrating the New Year (held on Boxing Day and New Year's Day), featuring…
- [[nowruz|Nowruz]] — Nowruz (meaning "new day" in Persian) is the Persian New Year celebrated on the spring equinox, typically March 20 or 21, and…
- [[rose-bowl-parade|Rose Bowl Parade]] — The Tournament of Roses Parade, commonly known as the Rose Bowl Parade, is an elaborate New Year's Day celebration held…
- [[rosh-hashanah|Rosh Hashanah]] — Rosh Hashanah marks the Jewish New Year and falls on the first and second days of Tishrei (September or October).
- [[shogatsu|Shogatsu]] — Shogatsu, the Japanese New Year, is celebrated on January 1 and is the most important holiday in the Japanese calendar.
- [[songkran|Songkran]] — Songkran, known as the Water Festival, is the Thai New Year celebration observed from April 13–15, marking the beginning of…
- [[times-square-ball-drop|Times Square Ball Drop]] — The Times Square Ball Drop is an American New Year's Eve tradition centered in Manhattan, where a large illuminated crystal…
- [[tet|Tết]] — Tết, or Tết Nguyên Đán ("Festival of the First Morning"), is the Vietnamese New Year celebrated at the same moment as Chinese…

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
