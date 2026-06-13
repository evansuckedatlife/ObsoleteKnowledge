---
type: list
category: science
read: false
---

# functional groups

The functional groups most worth knowing for quiz bowl.

## nodes

- [[alcohol|Alcohol]] — An alcohol is an organic compound in which a hydroxyl functional group (-OH) is covalently bonded to a saturated carbon atom.
- [[aldehyde|Aldehyde]] — An aldehyde is an organic compound containing a carbonyl functional group (C=O) where the carbonyl carbon is bonded to at…
- [[amide|Amide]] — An amide is an organic functional group characterized by a carbonyl carbon atom bonded to a nitrogen atom, represented by the…
- [[amine|Amine]] — An amine is a functional group and class of organic compounds containing a basic nitrogen atom with a lone pair, structurally…
- [[carboxylic-acid|Carboxylic Acid]] — A carboxylic acid is an organic functional group characterized by a carbon atom double-bonded to an oxygen atom and…
- [[ester|Ester]] — An ester is a class of organic compounds derived from an acid (usually a carboxylic acid) and an alcohol, characterized by the…
- [[ether|Ether]] — An ether is a class of organic compounds characterized by an oxygen atom bonded to two alkyl or aryl groups, represented by…
- [[ketone|Ketone]] — A ketone is an organic compound characterized by a carbonyl functional group (C=O) bonded to two carbon atoms, represented by…
- [[organic-halide|Organic Halide]] — An organic halide (commonly called a haloalkane or alkyl halide) is an organic compound containing one or more halogen atoms…
- [[thiol|Thiol]] — A thiol (historically referred to as a mercaptan) is an organosulfur compound containing a sulfhydryl functional group (-SH)…

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
