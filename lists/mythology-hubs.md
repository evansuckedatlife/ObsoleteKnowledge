---
type: list
category: mythology
read: false
---

# Mythology hubs

Places, cycles and concepts that recur across the individual myths.

## nodes

- [[akhenaten|Akhenaten]] — Akhenaten, born Amenhotep IV, was an 18th Dynasty Egyptian pharaoh (r.
- [[ares|Ares]] — Ares is the Olympian god of war, bloodlust, and violent chaos in Greek mythology.
- [[astyanax|Astyanax]] — Astyanax was the infant son of Hector and Andromache, prince of Troy who never reached manhood.
- [[avalon|Avalon]] — Avalon is the mystical, otherworldly island in Arthurian legend where King Arthur is taken to heal from his mortal wounds after the Battle of Camlann.
- [[camelot|Camelot]] — Camelot is the legendary capital of King Arthur's kingdom, the idealized medieval court where chivalry, justice, and fellowship are meant to flourish.
- [[circe|Circe]] — Circe is a divine enchantress in Homer's Odyssey, a goddess or semi-divine being who inhabits an isolated island where she transforms men into animals…
- [[dharma|Dharma]] — Dharma is a foundational Sanskrit concept in both Hinduism and Buddhism referring to cosmic law, moral duty, and the righteous order of the universe.
- [[dido|Dido]] — Dido, also called Elissa, was a legendary queen and founder of Carthage who appears in Virgil's Aeneid as a tragic figure at the intersection of love …
- [[greek-mythology|Greek Mythology]] — Greek Mythology comprises the religious beliefs, narratives, and deities of ancient Greece, spanning from the Bronze Age through the Classical period …
- [[hera|Hera]] — Hera is the queen of the Olympian gods and goddess of marriage, family, and women in Greek mythology.
- [[hermes|Hermes]] — Hermes is the Olympian god of messages, boundaries, commerce, thieves, and the dead in Greek mythology.
- [[karma|Karma]] — Karma is the Hindu and Buddhist principle of cosmic cause and effect, where every action in one life generates consequences that ripple across lifetim…
- [[orpheus|Orpheus]] — Orpheus was a legendary musician and poet whose voice and lyre possessed magical power to move gods, beasts, and nature itself.
- [[pegasus|Pegasus]] — Pegasus is the legendary winged horse of Greek mythology, born from the blood of the slain Gorgon Medusa when she was beheaded by Perseus.
- [[ravana|Ravana]] — Ravana is the primary antagonist of the Hindu epic Ramayana, a demon king of extraordinary power and intellect whose abduction of Sita precipitates th…
- [[telemachus|Telemachus]] — Telemachus is the son of Odysseus and Penelope, introduced in Homer's Odyssey as a young man on the threshold of adulthood.
- [[the-twelve-labors|The Twelve Labors]] — The Twelve Labors are the heroic tasks imposed upon Heracles as atonement for a crime committed under Hera's curse-driven madness.
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
