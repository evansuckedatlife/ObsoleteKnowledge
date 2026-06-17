---
type: list
category: social-science
read: false
---

# accents and dialects of English

The accents and dialects of English most worth knowing for quiz bowl.

## nodes

- [[aave|African American Vernacular English]] — African American Vernacular English (AAVE) is a variety of English spoken by many African Americans, arising from the complex…
- [[australian-english|Australian English]] — Australian English is the accent and dialect of Australia, marked by a distinctive vowel system, non-rhotic pronunciation…
- [[cockney|Cockney]] — Cockney is the traditional working-class accent of East London, historically marked by distinctive vowel shifts, glottal…
- [[estuary-english|Estuary English]] — Estuary English is a modern accent emerging in Southeast England and the Thames Estuary region, representing a blend between…
- [[general-american|General American]] — General American is the prestige accent of the United States, standardized in network television and radio broadcasting in the…
- [[geordie|Geordie]] — Geordie is the accent and dialect of Newcastle upon Tyne and Northeast England, marked by distinctive vowel pronunciations,…
- [[received-pronunciation|Received Pronunciation]] — Received Pronunciation (RP) is the prestige accent of English associated with educated speakers in southeastern England,…
- [[scottish-english|Scottish English]] — Scottish English is the accent and dialect of Scotland, influenced by Scots Gaelic and the native Scots language.
- [[scouse|Scouse]] — Scouse is the distinctive accent and dialect of Liverpool, England, characterized by strong nasalization, unique vowel shifts,…
- [[southern-american-english|Southern American English]] — Southern American English encompasses the accents and dialects of the American South, ranging from conservative…

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
