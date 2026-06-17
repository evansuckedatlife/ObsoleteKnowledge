---
type: list
category: misc
read: false
---

# quintuples

The quintuples most worth knowing for quiz bowl.

## nodes

- [[cinque-ports|Cinque Ports]] — The Cinque Ports (French for "five ports") are a historic maritime confederation of five fortified English coastal…
- [[five-civilized-tribes|Five Civilized Tribes]] — The Five Civilized Tribes are the five major Native American nations—the Cherokee, Chickasaw, Choctaw, Creek, and Seminole—who…
- [[five-classical-orders|Five Classical Orders of Architecture]] — The Five Classical Orders of Architecture are the standardized systems of proportion, style, and ornamentation used in ancient…
- [[five-good-emperors|Five Good Emperors]] — The Five Good Emperors were five successive Roman emperors of the second century A.D.—Nerva, Trajan, Hadrian, Antoninus Pius,…
- [[five-great-lakes|Five Great Lakes]] — The Five Great Lakes are the largest system of fresh water by surface area on Earth, straddling the border between the United…
- [[five-pillars-of-islam|Five Pillars of Islam]] — The Five Pillars of Islam are the foundational religious obligations for all Muslims, codified in Islamic theology and law.
- [[five-senses|Five Senses]] — The Five Senses—sight, hearing, taste, smell, and touch—are the classical categorization of human sensory systems, through…
- [[pentateuch|Pentateuch]] — The Pentateuch (Greek for "five scrolls") is the first five books of the Hebrew Bible—Genesis, Exodus, Leviticus, Numbers, and…
- [[platonic-solids|Platonic Solids]] — The Platonic Solids are the five three-dimensional geometric shapes in which all faces are identical regular polygons, all…

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
