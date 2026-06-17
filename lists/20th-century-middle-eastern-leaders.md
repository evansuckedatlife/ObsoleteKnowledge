---
type: list
category: history
read: false
---

# 20th-century Middle Eastern leaders

The 20th-century Middle Eastern leaders most worth knowing for quiz bowl.

## nodes

- [[anwar-sadat|Anwar Sadat]] — Anwar Sadat (1918–1981) was the third president of Egypt and a pivotal figure in Middle Eastern diplomacy, transforming…
- [[ayatollah-khomeini|Ayatollah Khomeini]] — Ayatollah Ruhollah Khomeini (1902–1989) was the supreme leader and principal architect of the Iranian Islamic Revolution,…
- [[david-ben-gurion|David Ben-Gurion]] — David Ben-Gurion (1886–1973) was the founding prime minister of Israel and principal architect of its establishment as a…
- [[gamal-abdel-nasser|Gamal Abdel Nasser]] — Gamal Abdel Nasser was Egypt's second president (1954–1970) and the architect of Arab nationalism and non-alignment in the…
- [[golda-meir|Golda Meir]] — Golda Meir (1898–1978) was the fourth and first female prime minister of Israel, serving from 1969 to 1974.
- [[hafez-al-assad|Hafez al-Assad]] — Hafez al-Assad (1930–2000) was the dictator of Syria for 29 years, ruling through the Ba'athist Party with iron-fisted…
- [[king-faisal|King Faisal]] — Faisal ibn Abdulaziz Al Saud (1906–1975) was the third king of Saudi Arabia and a transformative figure in modern Middle…
- [[shah-mohammad-reza-pahlavi|Mohammad Reza Pahlavi]] — Mohammad Reza Pahlavi (1919–1980), the last Shah of Iran, ruled for 37 years and attempted to modernize Iran into a secular,…
- [[mustafa-kemal-ataturk|Mustafa Kemal Atatürk]] — Mustafa Kemal Atatürk (1881–1938) was the founder and first president of the modern Turkish Republic, transforming the Ottoman…
- [[saddam-hussein|Saddam Hussein]] — Saddam Hussein (1937–2003) was the dictator of Iraq from 1979 to 2003, ruling through the Ba'athist Party with authoritarian…
- [[yasser-arafat|Yasser Arafat]] — Yasser Arafat (1929–2004) was the founder and longtime leader of the Palestine Liberation Organization and the principal…

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
