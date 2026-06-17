---
type: list
category: mythology
read: false
---

# mortal women in Greek myth

Famous mortal women of Greek mythology — queens, sorceresses, and tragic figures.

## nodes

- [[arachne|Arachne]] — A mortal weaver whose extraordinary skill rivaled that of Athena, the goddess of crafts.
- [[ariadne|Ariadne]] — Princess of Crete who fell in love with the hero Theseus and saved him from the Minotaur by giving him a thread to navigate…
- [[atalanta|Atalanta]] — Atalanta was the legendary huntress and warrior, unique among Greek heroes for her determination to remain independent and…
- [[cassandra|Cassandra]] — Princess of Troy cursed by Apollo to speak truth that no one would believe, Cassandra witnessed the Trojan War unfold exactly…
- [[clytemnestra|Clytemnestra]] — Queen of Argos and wife of Agamemnon, she is remembered as one of Greek mythology's most complex figures—a woman driven to…
- [[danae|Danaë]] — Princess of Argos who became the mother of the hero Perseus after Zeus visited her in her tower as a shower of gold.
- [[hecuba|Hecuba]] — Queen of Troy and wife of Priam, Hecuba endured unimaginable tragedy as she witnessed her sons' deaths and her city's destruction.
- [[helen-of-troy|Helen of Troy]] — The legendary beauty whose abduction by Paris triggered the Trojan War, one of the greatest conflicts in Greek mythology.
- [[medea|Medea]] — A powerful sorceress and princess of Colchis who became legendary for her passionate love, her mastery of magic, and her…
- [[pandora|Pandora]] — The first woman in Greek mythology, created by the gods as punishment for humanity after Prometheus stole fire.
- [[penelope|Penelope]] — The faithful wife of Odysseus, king of Ithaca, who waited twenty years for her husband's return from the Trojan War.

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
