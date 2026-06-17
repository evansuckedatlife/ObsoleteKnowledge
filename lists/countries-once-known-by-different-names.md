---
type: list
category: history
read: false
---

# countries once known by different names

The countries once known by different names most worth knowing for quiz bowl.

## nodes

- [[abyssinia-ethiopia|Abyssinia → Ethiopia]] — Abyssinia was the classical and colonial-era name for the ancient Christian empire in the Horn of Africa, derived from Greek…
- [[burma-myanmar|Burma → Myanmar]] — Burma was the name of the Southeast Asian nation during and after British colonial rule, derived from the Bamar ethnic majority.
- [[ceylon-sri-lanka|Ceylon → Sri Lanka]] — Ceylon was the island nation's name during British colonial rule, derived from Portuguese and Dutch corruption of Sanskrit Ceilao.
- [[dahomey-benin|Dahomey → Benin]] — Dahomey was the historical kingdom and French colonial territory in West Africa, lasting from the 17th century until…
- [[formosa-taiwan|Formosa → Taiwan]] — Formosa ("beautiful island" in Portuguese) was the name European traders gave to the island off the southeast coast of…
- [[gold-coast-ghana|Gold Coast → Ghana]] — Gold Coast was the British colonial territory in West Africa, named for the region's historical abundance of gold and its…
- [[persia-iran|Persia → Iran]] — Persia was the ancient and classical name for the vast empire and region centered on what is now modern-day Iran.
- [[rhodesia-zimbabwe|Rhodesia → Zimbabwe]] — Rhodesia was the name of the British colony in south-central Africa, named after the imperialist Cecil Rhodes, who chartered…
- [[siam-thailand|Siam → Thailand]] — Siam was the historical name for the Southeast Asian kingdom, used since the 13th century to denote territories ruled by Thai…
- [[zaire-democratic-republic-of-the-congo|Zaire → Democratic Republic of the Congo]] — The Democratic Republic of the Congo underwent a dramatic renaming to Zaire in 1971 under dictator Mobutu Sese Seko as part of…

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
