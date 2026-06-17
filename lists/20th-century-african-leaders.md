---
type: list
category: history
read: false
---

# 20th-century African leaders

The 20th-century African leaders most worth knowing for quiz bowl.

## nodes

- [[gamal-abdel-nasser|Gamal Abdel Nasser]] — Gamal Abdel Nasser was Egypt's second president (1954–1970) and the architect of Arab nationalism and non-alignment in the…
- [[haile-selassie|Haile Selassie]] — Haile Selassie I was Emperor of Ethiopia from 1930 until his overthrow in 1974, the last ruling member of Ethiopia's Solomonic…
- [[idi-amin|Idi Amin]] — Idi Amin was Uganda's military dictator (1971–1979), notorious for his brutality, arbitrary violence, and economic destruction.
- [[jomo-kenyatta|Jomo Kenyatta]] — Jomo Kenyatta was Kenya's first president and founding father, leading the nation from British colonial rule to independence…
- [[julius-nyerere|Julius Nyerere]] — Julius Nyerere was Tanzania's founding president (1964–1985) and one of Africa's most intellectually respected leaders.
- [[kwame-nkrumah|Kwame Nkrumah]] — Kwame Nkrumah was Ghana's first president and a driving force behind African independence and pan-Africanism.
- [[leopold-senghor|Léopold Senghor]] — Léopold Senghor was Senegal's founding president (1960–1980) and one of Africa's most celebrated intellectuals and poets.
- [[nelson-mandela|Nelson Mandela]] — Nelson Mandela was a South African anti-apartheid revolutionary and statesman who became the country's first Black president,…
- [[patrice-lumumba|Patrice Lumumba]] — Patrice Lumumba was the first Prime Minister of the Democratic Republic of Congo, leading his nation to independence from…
- [[robert-mugabe|Robert Mugabe]] — Robert Mugabe was Zimbabwe's founding president, leading the nation from Rhodesian white-minority rule to independence in 1980.

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
