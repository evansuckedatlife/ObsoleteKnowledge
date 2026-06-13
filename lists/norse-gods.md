---
type: list
category: mythology
read: false
---

# Norse Gods

The principal deities of Norse mythology, from Odin to the Norns.

## nodes

- [[balder|Balder]] — Balder is the god of light, beauty, and goodness—the most beloved of all the Aesir.
- [[frey|Frey]] — Frey is the god of fertility, summer, sunshine, and prosperity.
- [[freya|Freya]] — Freya is the goddess of love, beauty, fertility, magic, and war—embodying the full range of female power in Norse mythology.
- [[frigg|Frigg]] — Frigg is the queen of the Aesir and goddess of marriage, motherhood, home, and domestic life.
- [[heimdall|Heimdall]] — Heimdall is the watchman of the gods, eternally vigilant at the entrance to Asgard.
- [[loki|Loki]] — Loki is the trickster god, a shape-shifter whose schemes both aid and threaten the Aesir.
- [[norns|Norns]] — The Norns are three ancient beings—Urd, Verdandi, and Skuld—who weave and guard the fates of all things.
- [[odin|Odin]] — Odin is the king of the Aesir, the chief Norse god of wisdom, war, death, and magic.
- [[thor|Thor]] — Thor is the god of thunder, strength, and protection of the common people.
- [[ymir|Ymir]] — Ymir is the primordial giant whose body became the physical world itself.

## progress

Live read-status for this list (requires the **Bases** core plugin). Flip a node's `read` from its footer toggle and it moves here.

```base
filters:
  and:
    - lists.containsLinkTo(this.file.asLink())
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

## source

Scoped from NAQT's *You Gotta Know* topic [`norse-gods`](https://www.naqt.com/you-gotta-know/norse-gods.html). Content authored originally; NAQT used as a topic map only.
