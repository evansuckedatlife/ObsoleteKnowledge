---
type: list
category: history
read: false
---

# Roman Emperors

This topic covers the most significant and well-known rulers of the Roman Empire, from its foundation by Augustus through the pivotal transition under Constantine the Great.

## nodes

- [[augustus|Augustus]] — the first emperor, victor of Actium and founder of the Pax Romana.
- [[tiberius|Tiberius]] — the reluctant second emperor who spent his later years in paranoid seclusion on Capri.
- [[caligula|Caligula]] — the cruel and unpredictable tyrant who planned to make his horse a consul.
- [[claudius|Claudius]] — the unexpectedly capable emperor who conquered Britain despite physical ailments.
- [[nero|Nero]] — the extravagant final Julio-Claudian who supposedly fiddled while Rome burned.
- [[trajan|Trajan]] — the successful soldier-emperor who led Rome to its greatest territorial extent.
- [[hadrian|Hadrian]] — the Hellenophile who consolidated the empire and built a famous wall in Britain.
- [[marcus-aurelius|Marcus Aurelius]] — the Stoic philosopher-emperor whose death ended the Pax Romana.
- [[diocletian|Diocletian]] — the reformer who ended the Third Century Crisis by dividing rule into a Tetrarchy.
- [[constantine-the-great|Constantine the Great]] — the first Christian emperor who moved the capital to Byzantium.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
