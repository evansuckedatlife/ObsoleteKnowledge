---
type: list
category: science
read: false
---

# organic reactions

The organic reactions most worth knowing for quiz bowl.

## nodes

- [[aldol-condensation|Aldol Condensation]] — The aldol condensation is a classic carbon-carbon bond-forming reaction in which an enol or enolate ion reacts with a carbonyl…
- [[diels-alder-reaction|Diels-Alder Reaction]] — The Diels-Alder reaction is a landmark organic chemical reaction that proceeds via a single-step, concerted mechanism to form…
- [[electrophilic-addition|Electrophilic Addition]] — Electrophilic addition is an organic reaction where a pi bond in an unsaturated compound (such as an alkene or alkyne) is…
- [[elimination-reaction|Elimination Reaction]] — An elimination reaction is a class of organic reactions in which two substituents are removed from a molecule in either a one-…
- [[esterification|Esterification]] — Esterification is a chemical reaction that synthesizes an ester by reacting an organic acid (typically a carboxylic acid) with…
- [[friedel-crafts-reaction|Friedel-Crafts Reaction]] — The Friedel-Crafts reaction is a set of organic reactions developed by Charles Friedel and James Crafts in 1877 to attach…
- [[grignard-reaction|Grignard Reaction]] — The Grignard reaction is a fundamental organometallic chemical reaction in which alkyl, allyl, vinyl, or aryl-magnesium…
- [[nucleophilic-substitution|Nucleophilic Substitution]] — Nucleophilic substitution is a fundamental class of organic reactions where an electron-rich nucleophile selectively bonds…
- [[ozonolysis|Ozonolysis]] — Ozonolysis is an organic chemical reaction that uses ozone (O3) to cleave the unsaturated carbon-carbon double or triple bonds…
- [[saponification|Saponification]] — Saponification is an organic chemical reaction that hydrolyzes an ester under basic conditions to yield an alcohol and the…

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
