---
type: list
category: science
read: false
---

# Functional Groups

Specific groupings of atoms within molecules that have their own characteristic properties, regardless of the other atoms present in the molecule.

## nodes

- [[carboxylic-acid|Carboxylic Acid]] — acidic group with a carbonyl and hydroxyl group on the same carbon, represented by -COOH.
- [[alcohol|Alcohol (Hydroxyl)]] — polar group containing an oxygen atom bonded to a hydrogen atom, represented by -OH.
- [[ether|Ether]] — group containing an oxygen atom bonded between two alkyl or aryl groups, represented by R-O-R'.
- [[aldehyde|Aldehyde]] — terminal carbonyl group bonded to at least one hydrogen atom, represented by -CHO.
- [[ketone|Ketone]] — internal carbonyl group bonded between two carbon atoms, represented by R-CO-R'.
- [[ester|Ester]] — group derived from condensation of carboxylic acid and alcohol, represented by R-CO-OR'.
- [[amine|Amine]] — basic group containing a nitrogen atom with a lone pair, derived from ammonia.
- [[amide|Amide]] — group containing a carbonyl carbon bonded to a nitrogen atom, represented by R-CO-NR'R''.
- [[organic-halide|Organic Halide]] — group containing a halogen atom covalently bonded to a carbon atom.
- [[thiol|Thiol]] — group containing a sulfur atom bonded to a hydrogen atom, represented by -SH.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
