---
type: list
category: science
read: false
---

# Organic Reactions

Standard classes of chemical reactions involving organic compounds, describing how functional groups are interconverted and carbon-carbon bonds are constructed.

## nodes

- [[grignard-reaction|Grignard reaction]] — carbon-carbon bond-forming reaction using organomagnesium halides to attack carbonyls.
- [[diels-alder-reaction|Diels-Alder reaction]] — concerted pericyclic [4+2] cycloaddition to synthesize cyclohexene rings.
- [[nucleophilic-substitution|Nucleophilic substitution]] — reaction where an electron-rich nucleophile displaces a leaving group.
- [[elimination-reaction|Elimination reaction]] — reaction where two substituents are removed to form a new pi bond.
- [[electrophilic-addition|Electrophilic addition]] — reaction where a pi bond is broken to add an electrophilic species.
- [[esterification|Esterification]] — acid-catalyzed condensation of a carboxylic acid and an alcohol to produce an ester.
- [[friedel-crafts-reaction|Friedel-Crafts reaction]] — electrophilic aromatic substitution to attach alkyl or acyl groups to a benzene ring.
- [[aldol-condensation|Aldol condensation]] — reaction of an enol/enolate with a carbonyl to form a beta-hydroxy carbonyl or enone.
- [[saponification|Saponification]] — basic hydrolysis of an ester to yield an alcohol and a carboxylate salt.
- [[ozonolysis|Ozonolysis]] — cleavage of alkene or alkyne double/triple bonds using ozone.

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
