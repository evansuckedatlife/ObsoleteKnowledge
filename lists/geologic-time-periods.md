---
type: list
category: science
read: false
---

# geologic time periods

The geologic time periods most worth knowing for quiz bowl.

## nodes

- [[archean-eon|Archean Eon]] — The Archean Eon (4.1–2.5 billion years ago) witnessed the formation of Earth's first stable continents and the emergence of life.
- [[cambrian-period|Cambrian Period]] — The Cambrian Period (541–485 million years ago) marks the beginning of the Paleozoic Era and the Cambrian Explosion—a burst of…
- [[carboniferous-period|Carboniferous Period]] — The Carboniferous Period (359–299 million years ago) was the age of vast swamp forests, whose dead vegetation compacted into…
- [[cenozoic-era|Cenozoic Era]] — The Cenozoic Era (66 million years ago–present) is the "Age of Mammals," spanning the recovery from the K-Pg extinction…
- [[cretaceous-period|Cretaceous Period]] — The Cretaceous Period (145–66 million years ago) saw the final flourishing of dinosaurs alongside the rise of flowering…
- [[devonian-period|Devonian Period]] — The Devonian Period (419–359 million years ago) is called the Age of Fishes because jawed fish diversified explosively and…
- [[hadean-eon|Hadean Eon]] — The Hadean Eon spans Earth's first ~500 million years (4.6–4.1 billion years ago), named for the underworld Hades because of…
- [[jurassic-period|Jurassic Period]] — The Jurassic Period (201–145 million years ago) was the golden age of dinosaurs, when sauropods reached colossal…
- [[ordovician-period|Ordovician Period]] — The Ordovician Period (485–444 million years ago) saw an explosion of marine diversity—fishes emerged, corals and cephalopods…
- [[permian-period|Permian Period]] — The Permian Period (299–252 million years ago) saw synapsids rule the land while Pangaea reached its full assembly.
- [[proterozoic-eon|Proterozoic Eon]] — The Proterozoic Eon (2.5 billion–541 million years ago) saw the rise of oxygen in the atmosphere, the evolution of…
- [[silurian-period|Silurian Period]] — The Silurian Period (444–419 million years ago) witnessed the colonisation of land by plants for the first time—humble…
- [[triassic-period|Triassic Period]] — The Triassic Period (252–201 million years ago) marks the recovery from the Permian extinction and the rise of dinosaurs.

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
