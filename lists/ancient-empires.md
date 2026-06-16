---
type: list
category: history
read: false
---

# ancient empires of the Mediterranean and Near East

The ancient empires of the Mediterranean and Near East most worth knowing for quiz bowl.

## nodes

- [[achaemenid-empire|Achaemenid Empire]] — The Achaemenid Persian Empire (550–330 BCE) was the ancient world's largest territorial state, stretching from the…
- [[akkadian-empire|Akkadian Empire]] — The Akkadian Empire was the first multi-ethnic empire in history, ruling Mesopotamia from approximately 2334 to 2154 BCE.
- [[assyrian-empire|Assyrian Empire]] — The Assyrian Empire was the ancient world's first truly militaristic state, dominating the Near East from approximately 2025…
- [[babylonian-empire|Babylonian Empire]] — Babylon was a Mesopotamian city-state that rose to imperial dominance twice: first under Hammurabi (1792–1750 BCE), who…
- [[carthaginian-empire|Carthaginian Empire]] — The Carthaginian Empire (814–146 BCE) was the Mediterranean's dominant naval and commercial power before its confrontation…
- [[hittite-empire|Hittite Empire]] — The Hittite Empire (1650–1180 BCE) was the ancient Near East's dominant power during the Bronze Age, centered on Anatolia…
- [[macedonian-empire|Macedonian Empire]] — The Macedonian Empire (336–323 BCE) was the shortest-lived yet culturally most transformative empire of the ancient world.
- [[mauryan-empire|Mauryan Empire]] — The Mauryan Empire (322–185 BCE) was the Indian subcontinent's first unified imperial state, spanning most of modern India,…
- [[mongol-empire|Mongol Empire]] — The Mongol Empire (1206–1368 CE in the East; its khanates persisted to the 17th century) was history's largest contiguous land…
- [[roman-empire|Roman Empire]] — The Roman Empire (27 BCE–476 CE in the West; 1453 CE in the East as the Byzantine Empire) was the Western world's…

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
