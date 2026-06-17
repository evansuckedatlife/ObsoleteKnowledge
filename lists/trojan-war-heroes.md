---
type: list
category: mythology
read: false
---

# Trojan War heroes

The Greek and Trojan warriors, kings, and casualties of the Trojan War.

## nodes

- [[achilles|Achilles]] — Achilles was the mightiest warrior of the Trojan War, nearly invulnerable and unmatched in combat prowess.
- [[aeneas|Aeneas]] — Trojan hero and son of the goddess Aphrodite, Aeneas escaped Troy's destruction to become the ancestor of Rome.
- [[agamemnon|Agamemnon]] — The king of Mycenae and supreme commander of the Greek forces at Troy, Agamemnon led the thousand-ship expedition against the…
- [[ajax-the-great|Ajax the Great]] — Ajax the Great, also called Telamonian Ajax, was the mightiest Greek warrior after Achilles, renowned for his enormous size,…
- [[andromache|Andromache]] — Wife of Hector and mother of Astyanax, Andromache stands as the tragic image of the devoted woman watching helplessly as her…
- [[cassandra|Cassandra]] — Princess of Troy cursed by Apollo to speak truth that no one would believe, Cassandra witnessed the Trojan War unfold exactly…
- [[diomedes|Diomedes]] — Diomedes was a formidable Greek warrior at the Trojan War, second only to Achilles in martial prowess and remarkable for his…
- [[hector|Hector]] — Prince of Troy and mightiest of the Trojan warriors, Hector was the defender of his city and a figure of tragic nobility.
- [[hecuba|Hecuba]] — Queen of Troy and wife of Priam, Hecuba endured unimaginable tragedy as she witnessed her sons' deaths and her city's destruction.
- [[laocoon|Laocoon]] — Trojan priest of Apollo or Poseidon, Laocoon stands as the figure who warned Troy against accepting the wooden horse but was…
- [[menelaus|Menelaus]] — King of Sparta and husband of Helen, Menelaus was the nominal cause of the Trojan War when Paris abducted his wife.
- [[nestor|Nestor]] — King of Pylos and the eldest statesman of the Greek forces at Troy, Nestor earned respect through his wisdom and experience…
- [[odysseus|Odysseus]] — Odysseus was the legendary king of Ithaca, renowned equally for his cunning intellect as for his warrior's prowess.
- [[paris|Paris]] — Prince of Troy, famous for his beauty and weakness, Paris abducted Helen of Sparta and triggered the ten-year Trojan War.
- [[patroclus|Patroclus]] — Companion and closest friend to Achilles, Patroclus fought alongside the greatest Greek warrior at Troy.
- [[priam|Priam]] — King of Troy throughout the ten-year war, Priam witnessed the destruction of his kingdom while grieving the loss of his sons.

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
