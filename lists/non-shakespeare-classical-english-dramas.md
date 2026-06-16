---
type: list
category: literature
read: false
---

# non-Shakespeare classical English dramas

The non-Shakespeare classical English dramas most worth knowing for quiz bowl.

## nodes

- [[tis-pity-shes-a-whore|'Tis Pity She's a Whore]] — John Ford's 'Tis Pity She's a Whore is a bold, unsettling Jacobean tragedy of forbidden love between siblings in Renaissance…
- [[doctor-faustus|Doctor Faustus]] — Doctor Faustus is Christopher Marlowe's tragic play about an overreaching scholar who sells his soul to the devil for…
- [[everyman|Everyman]] — Everyman is a late-medieval morality play (c.
- [[tamburlaine|Tamburlaine]] — Christopher Marlowe's Tamburlaine the Great, written in two parts (1587–1588), is an epic chronicle of a Scythian shepherd who…
- [[the-alchemist|The Alchemist]] — Ben Jonson's The Alchemist is a masterpiece of satirical comedy set in plague-stricken London, where a con-artist alchemist,…
- [[the-duchess-of-malfi|The Duchess of Malfi]] — John Webster's The Duchess of Malfi is a Jacobean revenge tragedy of obsession, corruption, and misogyny, centring on a…
- [[the-revengers-tragedy|The Revenger's Tragedy]] — The Revenger's Tragedy, attributed variously to Thomas Middleton or Cyril Tourneur (the question unresolved), is a visceral…
- [[the-spanish-tragedy|The Spanish Tragedy]] — Thomas Kyd's The Spanish Tragedy is the foundational revenge tragedy of English drama, depicting an aging father's descent…
- [[the-way-of-the-world|The Way of the World]] — William Congreve's The Way of the World (1700) is a brilliant Restoration comedy of wit, intrigue, and marriage negotiation…
- [[volpone|Volpone]] — Ben Jonson's Volpone, or The Fox is a ruthless satirical comedy exposing avarice, deceit, and social parasitism in Venice.

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
