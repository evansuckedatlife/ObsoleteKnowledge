---
type: list
category: mythology
read: false
---

# Mythology hubs

Places, cycles and concepts that recur across the individual myths.

## nodes

- [[avalon|Avalon]] — Avalon is the mystical, otherworldly island in Arthurian legend where King Arthur is taken to heal from his mortal wounds after the Battle of Camlann.
- [[camelot|Camelot]] — Camelot is the legendary capital of King Arthur's kingdom, the idealized medieval court where chivalry, justice, and fellowship are meant to flourish.
- [[dharma|Dharma]] — Dharma is a foundational Sanskrit concept in both Hinduism and Buddhism referring to cosmic law, moral duty, and the righteous order of the universe.
- [[pegasus|Pegasus]] — Pegasus is the legendary winged horse of Greek mythology, born from the blood of the slain Gorgon Medusa when she was beheaded by Perseus.
- [[ravana|Ravana]] — Ravana is the primary antagonist of the Hindu epic Ramayana, a demon king of extraordinary power and intellect whose abduction of Sita precipitates th…
- [[troy|Troy]] — Troy was an ancient city in what is now northwest Turkey, the legendary center of the Trojan War immortalized in Homer's Iliad.

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
