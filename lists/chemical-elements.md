---
type: list
category: science
read: false
---

# Chemical Elements

Fundamental chemical substances consisting of atoms with the same number of protons in their atomic nuclei, forming the building blocks of all matter.

## nodes

- [[helium|Helium]] — light, inert noble gas discovered in solar spectra, displays superfluidity at low temperatures.
- [[carbon|Carbon]] — tetravalent basis of organic life, existing as diamond, graphite, and fullerenes.
- [[nitrogen|Nitrogen]] — diatomic gas composing 78% of the atmosphere, fixed via the Haber-Bosch process.
- [[oxygen|Oxygen]] — highly reactive chalcogen gas, paramagnet when liquid, essential for aerobic respiration.
- [[sodium|Sodium]] — soft alkali metal isolated by Humphry Davy, reacts violently with water.
- [[iron|Iron]] — common transition metal forming the Earth's core, alloyed with carbon to make steel.
- [[copper|Copper]] — highly conductive reddish metal used in wiring, forms bronze and brass alloys.
- [[gold|Gold]] — noble coinage metal resistant to corrosion, dissolves in aqua regia, used in Rutherford's foil experiment.
- [[mercury|Mercury]] — liquid transition metal extracted from cinnabar, forms amalgams, used in barometers.
- [[uranium|Uranium]] — heavy radioactive actinide, discovered in pitchblende, enriched for nuclear fuel.

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
