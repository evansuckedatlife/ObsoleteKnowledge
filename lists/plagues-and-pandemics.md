---
type: list
category: history
read: false
---

# plagues and pandemics

The plagues and pandemics most worth knowing for quiz bowl.

## nodes

- [[antonine-plague|Antonine Plague]] — The Antonine Plague was a pandemic that ravaged the Roman Empire between 165 and 180 CE, killing an estimated 5 to 10 million…
- [[black-death|Black Death]] — The Black Death was a catastrophic pandemic of bubonic plague that swept across Eurasia and North Africa between 1347 and…
- [[cholera-pandemics|Cholera Pandemics]] — Cholera pandemics refer to seven major waves of cholera epidemic that spread globally from 1817 onward, killing millions and…
- [[covid-19-pandemic|COVID-19 Pandemic]] — The COVID-19 pandemic began in late 2019 in Wuhan, China, when a novel coronavirus (SARS-CoV-2) emerged and spread globally,…
- [[great-plague-of-london|Great Plague of London]] — The Great Plague of London was a major outbreak of bubonic plague in 1665–1666 that killed an estimated 70,000 to 100,000…
- [[hiv-aids-pandemic|HIV/AIDS Pandemic]] — The HIV/AIDS pandemic emerged in the early 1980s as a global health crisis, killing an estimated 40 to 45 million people since…
- [[plague-of-justinian|Plague of Justinian]] — The Plague of Justinian was a major bubonic plague pandemic that ravaged the Byzantine Empire and Mediterranean region from…
- [[smallpox-in-the-americas|Smallpox in the Americas]] — Smallpox in the Americas refers to a catastrophic wave of epidemics triggered by the introduction of Old World…
- [[spanish-flu|Spanish Flu]] — The Spanish Flu was a catastrophic global influenza pandemic caused by the H1N1 virus that killed an estimated 50 to 100…
- [[third-plague-pandemic|Third Plague Pandemic]] — The Third Plague Pandemic was a global resurgence of bubonic plague that began in China in 1855 and spread to every inhabited…

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
