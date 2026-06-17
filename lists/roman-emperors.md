---
type: list
category: history
read: false
---

# Roman emperors

The Roman emperors most worth knowing for quiz bowl.

## nodes

- [[augustus|Augustus]] — Augustus was the first emperor of the Roman Empire, ruling from 27 BC until his death in AD 14.
- [[caligula|Caligula]] — Caligula was the third Roman emperor, ruling from AD 37 until his assassination in AD 41.
- [[claudius|Claudius]] — Claudius was the fourth Roman emperor, ruling from AD 41 to 54.
- [[constantine-the-great|Constantine the Great]] — Constantine the Great was a Roman emperor who ruled from AD 306 to 337.
- [[diocletian|Diocletian]] — Diocletian was a Roman emperor who ruled from AD 284 to 305.
- [[hadrian|Hadrian]] — Hadrian was a Roman emperor who ruled from AD 117 to 138, known as the third of the "Five Good Emperors." Unlike his…
- [[marcus-aurelius|Marcus Aurelius]] — Marcus Aurelius was a Roman emperor who ruled from AD 161 to 180, often considered the last of the "Five Good Emperors." He is…
- [[nero|Nero]] — Nero was the fifth Roman emperor and the last of the Julio-Claudian dynasty, ruling from AD 54 to 68.
- [[tiberius|Tiberius]] — Tiberius was the second Roman emperor, ruling from AD 14 to 37.
- [[trajan|Trajan]] — Trajan was a Roman emperor who ruled from AD 98 to 117.

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
