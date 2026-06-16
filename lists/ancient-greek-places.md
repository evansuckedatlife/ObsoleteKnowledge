---
type: list
category: history
read: false
---

# ancient Greek places

The ancient Greek places most worth knowing for quiz bowl.

## nodes

- [[argos|Argos]] — Argos, one of the oldest cities in Greece located in the northeastern Peloponnese, was a major Mycenaean power and later a…
- [[athens|Athens]] — Athens is the birthplace of Western democracy and a dominant force in ancient Greece, celebrated for its innovations in…
- [[corinth|Corinth]] — Corinth, perched on the isthmus connecting mainland Greece to the Peloponnese, was a wealthy maritime and commercial hub that…
- [[delos|Delos]] — Delos, a small island in the Aegean Sea at the center of the Cyclades, was a sacred sanctuary dedicated to the birthplace of…
- [[delphi|Delphi]] — Delphi, nestled high in the slopes of Mount Parnassus in central Greece, was the sacred heart of the Greek world and home to…
- [[knossos|Knossos]] — Knossos, the grand palace complex on Crete, was the ceremonial and administrative center of the Minoan civilization, Europe's…
- [[mycenae|Mycenae]] — Mycenae, a fortress city in the Peloponnese, was the dominant political and military power of the Late Bronze Age (1600–1100…
- [[olympia|Olympia]] — Olympia, a sacred sanctuary in the western Peloponnese dedicated to Zeus, was the religious and athletic center of the Greek…
- [[sparta|Sparta]] — Sparta is an austere warrior society located in the Peloponnese that dominated the classical Greek world through military…
- [[thebes|Thebes]] — Thebes, the major city of Boeotia in central Greece, rose from cultural obscurity to become a military superpower under…

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
