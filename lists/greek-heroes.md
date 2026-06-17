---
type: list
category: mythology
read: false
---

# Greek heroes

The great mortal and demigod heroes of Greek mythology and their legendary exploits.

## nodes

- [[achilles|Achilles]] — Achilles was the mightiest warrior of the Trojan War, nearly invulnerable and unmatched in combat prowess.
- [[ajax-the-great|Ajax the Great]] — Ajax the Great, also called Telamonian Ajax, was the mightiest Greek warrior after Achilles, renowned for his enormous size,…
- [[atalanta|Atalanta]] — Atalanta was the legendary huntress and warrior, unique among Greek heroes for her determination to remain independent and…
- [[bellerophon|Bellerophon]] — Bellerophon was a warrior of noble birth who became the hero most renowned for slaying the Chimera, a fire-breathing monster…
- [[diomedes|Diomedes]] — Diomedes was a formidable Greek warrior at the Trojan War, second only to Achilles in martial prowess and remarkable for his…
- [[heracles|Heracles]] — The strongest man who ever lived, Heracles was the illegitimate son of Zeus and the mortal woman Alcmene.
- [[jason|Jason]] — Jason was the rightful heir to the throne of Thessaly, robbed of his kingdom in infancy.
- [[odysseus|Odysseus]] — Odysseus was the legendary king of Ithaca, renowned equally for his cunning intellect as for his warrior's prowess.
- [[perseus|Perseus]] — Perseus was the son of Zeus and the mortal princess Danaë, raised in exile and destined for greatness.
- [[theseus|Theseus]] — Theseus was the legendary king of Athens and one of the greatest heroes of ancient Greece.

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
