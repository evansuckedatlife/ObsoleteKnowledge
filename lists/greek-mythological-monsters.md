---
type: list
category: mythology
read: false
---

# Greek mythological monsters

The beasts and hybrid horrors of Greek myth and the heroes who slew them.

## nodes

- [[calydonian-boar|Calydonian Boar]] — A massive, supernatural wild boar sent by the goddess Artemis to ravage the land of Calydon as punishment for a king's…
- [[cerberus|Cerberus]] — The three-headed monstrous hound of the underworld, Cerberus stood guard at the gates of Hades, ensuring that no living soul…
- [[chimera|Chimera]] — A fire-breathing composite monster combining the front parts of a lion, the middle of a goat, and the rear of a serpent, the…
- [[lernaean-hydra|Lernaean Hydra]] — A serpentine monstrosity with nine heads—eight mortal and one immortal—the Lernaean Hydra terrorized the marshes of Lerna in…
- [[medusa|Medusa]] — Once a beautiful woman transformed into a horrifying monster with serpents for hair, Medusa possessed the terrifying power to…
- [[minotaur|Minotaur]] — A hybrid creature with the head of a bull and the body of a man, the Minotaur was imprisoned in an elaborate labyrinth on the…
- [[polyphemus|Polyphemus]] — A Cyclops giant with a single massive eye in the center of his forehead, Polyphemus is famous for his encounter with Odysseus…
- [[sirens|Sirens]] — Supernatural beings that blended feminine beauty with bestial form—variously described as women with bird wings or fish…
- [[sphinx|Sphinx]] — A winged creature with a human head, typically depicted as female, and the body of a lion, the Sphinx posed a deadly riddle to…
- [[typhon|Typhon]] — The most fearsome of all primordial monsters, Typhon was a fire-breathing giant born from Gaia herself as a weapon against the…

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
