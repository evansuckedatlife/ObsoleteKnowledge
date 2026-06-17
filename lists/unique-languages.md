---
type: list
category: social-science
read: false
---

# unique languages

The unique languages most worth knowing for quiz bowl.

## nodes

- [[basque|Basque]] — Basque is a language isolate spoken in the Basque Country of northern Spain and southwestern France, with no known linguistic…
- [[esperanto|Esperanto]] — Esperanto is a planned auxiliary language created in 1887 by L.
- [[georgian|Georgian]] — Georgian is a Caucasian language spoken in Georgia, remarkable for its unique writing system—the Mkhedruli script—which is…
- [[hungarian|Hungarian]] — Hungarian is a Uralic language spoken primarily in Hungary and neighboring regions, linguistically isolated within Central…
- [[maltese|Maltese]] — Maltese is the national language of Malta, a Mediterranean island republic.
- [[navajo-language|Navajo (language)]] — Navajo is an Athabaskan language spoken by the Navajo people across the southwestern United States, most notably in the Navajo…
- [[pirahã|Pirahã]] — Pirahã is an Amazonian language spoken by the Pirahã people in Brazil, famous in linguistic circles for its alleged absence of…
- [[silbo-gomero|Silbo Gomero]] — Silbo Gomero is a whistled language spoken on the island of La Gomera in the Canary Islands, used by shepherd and fishermen…
- [[welsh|Welsh]] — Welsh is a Celtic language spoken primarily in Wales and the only surviving Celtic language with a continuous literary…
- [[xhosa|Xhosa]] — Xhosa is a Bantu language spoken in South Africa, most notably by the Xhosa people of the Eastern and Western Cape.

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
