---
type: list
category: religion
read: false
---

# Jewish Holidays

The major festivals and holy days of the Jewish calendar.

## nodes

- [[hanukkah|Hanukkah]] — Hanukkah, the Festival of Lights, is an eight-day celebration beginning on the 25th day of Kislev (November or December).
- [[passover|Passover]] — Passover, known in Hebrew as Pesach, is an eight-day festival beginning on the 15th of Nisan (March or April).
- [[purim|Purim]] — Purim, celebrated on the 14th of Adar (February or March), commemorates the deliverance of Jews from persecution in ancient…
- [[rosh-hashanah|Rosh Hashanah]] — Rosh Hashanah marks the Jewish New Year and falls on the first and second days of Tishrei (September or October).
- [[shavuot|Shavuot]] — Shavuot, the Feast of Weeks, is a two-day festival occurring fifty days after Passover, typically in May or June.
- [[sukkot|Sukkot]] — Sukkot, the Feast of Tabernacles, is a seven-day festival beginning on the 15th of Tishrei (September or October).
- [[tisha-bav|Tisha b'Av]] — Tisha b'Av, the Ninth of Av, is a day of mourning and fasting observed in July or August.
- [[yom-kippur|Yom Kippur]] — Yom Kippur, the Day of Atonement, is the holiest day in the Jewish calendar, falling on the tenth day of Tishrei (September or…

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
