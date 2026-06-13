---
type: list
category: science
read: false
---

# scientific scales

The scientific scales most worth knowing for quiz bowl.

## nodes

- [[beaufort-wind-force-scale|Beaufort wind force scale]] — The Beaufort wind force scale ranks wind strength from 0 (calm) to 12+ (hurricane) based on observable effects on land and sea.
- [[celsius-scale|Celsius scale]] — The Celsius scale is a practical temperature scale where 0 °C is the freezing point of water and 100 °C is its boiling point…
- [[decibel-scale|decibel scale]] — The decibel (dB) is a logarithmic unit measuring the ratio of a physical quantity (most commonly sound intensity or power)…
- [[fahrenheit-scale|Fahrenheit scale]] — The Fahrenheit scale is a temperature scale developed by German physicist Daniel Gabriel Fahrenheit in the early 18th century,…
- [[fujita-pearson-scale|Fujita–Pearson scale]] — The Enhanced Fujita scale (EF scale) rates tornado intensity from EF0 to EF5 based on wind speed estimates derived from…
- [[kelvin-scale|Kelvin scale]] — The Kelvin scale is the SI unit for measuring absolute temperature, starting at zero at the lowest possible temperature…
- [[mach-number|Mach number]] — Mach number is a dimensionless ratio expressing the speed of an object relative to the speed of sound in the surrounding medium.
- [[mohs-scale|Mohs scale]] — The Mohs scale ranks minerals by hardness from 1 (softest) to 10 (hardest), based on the ability of one mineral to scratch…
- [[pauling-scale|Pauling scale]] — The Pauling scale quantifies the electronegativity of chemical elements—their tendency to attract electrons in a chemical bond.
- [[ph-scale|pH scale]] — The pH scale measures the acidity or basicity of a solution on a logarithmic scale from 0 to 14, where 7 is neutral.
- [[richter-scale|Richter scale]] — The Richter scale measures the local magnitude of earthquakes, quantifying the energy released by seismic waves as recorded on…
- [[saffir-simpson-scale|Saffir–Simpson scale]] — The Saffir–Simpson scale classifies tropical cyclones (hurricanes) into five categories (1–5) based on sustained wind speed…

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
