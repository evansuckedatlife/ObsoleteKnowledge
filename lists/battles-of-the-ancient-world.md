---
type: list
category: history
read: false
---

# battles of the ancient world

The battles of the ancient world most worth knowing for quiz bowl.

## nodes

- [[battle-of-actium|Battle of Actium]] — The Battle of Actium (31 BC) was a decisive naval battle off the Greek coast where Octavian defeated the combined forces of…
- [[battle-of-cannae|Battle of Cannae]] — The Battle of Cannae (216 BC) was the most catastrophic Roman military defeat in history, where Hannibal Barca of Carthage…
- [[battle-of-gaugamela|Battle of Gaugamela]] — The Battle of Gaugamela (331 BC) was the definitive clash between Alexander the Great and the Persian King Darius III, fought…
- [[battle-of-marathon|Battle of Marathon]] — The Battle of Marathon (490 BC) was a pivotal clash between the Athenian and Eretrian forces against invading Persian armies.
- [[battle-of-pharsalus|Battle of Pharsalus]] — The Battle of Pharsalus (48 BC) was the decisive engagement of the Roman Civil War, where Julius Caesar crushed the forces of…
- [[battle-of-plataea|Battle of Plataea]] — The Battle of Plataea (479 BC) was the final major land engagement of the Persian Wars, where a united Greek coalition…
- [[battle-of-salamis|Battle of Salamis]] — The Battle of Salamis (480 BC) was a decisive naval engagement where the allied Greek fleet, commanded by the Athenian…
- [[battle-of-teutoburg-forest|Battle of Teutoburg Forest]] — The Battle of Teutoburg Forest (9 AD) was a catastrophic Roman defeat where Germanic tribes led by Arminius annihilated three…
- [[battle-of-thermopylae|Battle of Thermopylae]] — The Battle of Thermopylae (480 BC) saw a small Greek coalition led by Spartan King Leonidas make a legendary stand against the…
- [[battle-of-zama|Battle of Zama]] — The Battle of Zama (202 BC) saw the Roman general Scipio Africanus decisively defeat Hannibal on African soil, ending the…

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
