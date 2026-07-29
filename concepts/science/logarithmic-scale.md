---
type: term
category: science
defines: [Logarithmic Scale, log scale]
related: ["[[decibel-scale]]", "[[richter-scale]]", "[[ph-scale]]", "[[mathematics]]", "[[exponential-function]]"]
requires: []
lists: []
tour_order: 0
read: false
---

# Logarithmic Scale

## summary

**A logarithmic scale** is a measurement system where each unit step represents a multiplicative (rather than additive) change in the quantity being measured—typically a factor of 10 or 2. Logarithmic scales compress vast ranges of data (from billions to fractions) into manageable ranges, revealing patterns invisible on linear scales and are essential in measuring phenomena ranging from earthquake magnitude to sound intensity to acidity. They are defined mathematically by the logarithm function, where each increase of one unit represents multiplication by the scale's base.

## you gotta know

- A *base-10 logarithmic scale* measures each unit as a 10-fold change; a value of 3 on such a scale represents 10³ = 1,000 times a reference value; this allows representing quantities from 10⁰ = 1 to 10⁶ = 1,000,000 within a 0–6 range.
- The [[decibel-scale]], measuring sound intensity, is logarithmic (base 10); an increase of 10 decibels represents a 10-fold increase in power, or roughly doubling of perceived loudness, compressing the human hearing range (from threshold of hearing to pain) into a 0–140 dB scale.
- The [[richter-scale]], measuring earthquake magnitude, is logarithmic (base 10); each unit increase represents roughly 31 times more energy released; thus, a magnitude 7 earthquake releases about 32 times more energy than a magnitude 6.
- The [[ph-scale]], measuring acidity/alkalinity, is logarithmic (base 10); pH = –log₁₀[H⁺], so pH 6 is 10 times more acidic than pH 7 (neutral); the scale compresses vast differences in hydrogen-ion concentration into a 0–14 range.
- *Logarithmic compression* is not merely mathematical convenience—it reflects how human sensation works; the ear perceives sound intensity logarithmically (the "Weber-Fechner law"), so a logarithmic scale aligns with human perception.
- *Semi-log plots* use a logarithmic scale on one axis and a linear scale on the other; they reveal exponential relationships as straight lines, making pattern recognition and data fitting easier.
- Logarithmic scales are widespread in science and engineering: bacterial growth (exponential, shown as linear on log scale), pandemic modeling, star brightness (apparent magnitude), and chemical concentration in titration curves.

## connections

- [[decibel-scale]] — the logarithmic scale compressing sound-intensity measurements to human hearing range.
- [[richter-scale]] — the logarithmic scale measuring earthquake magnitude; each unit represents ~31× more energy.
- [[ph-scale]] — the logarithmic scale measuring acidity/alkalinity of solutions.
- [[mathematics]] — logarithmic functions are the mathematical foundation of these scales.
- [[exponential-function]] — logarithmic scales linearize exponential growth, making patterns visible.

## see also

- [[decibel-scale]] · [[richter-scale]] · [[ph-scale]] · [[exponential-function]]

<!-- crosslinks -->
```dataviewjs
dv.view("_dv/crosslinks")
```
<!-- /crosslinks -->

<!-- tournav -->
```dataviewjs
dv.view("_dv/tournav")
```
<!-- /tournav -->

<!-- footer -->

---

Lists:  · Mark read: `INPUT[toggle:read]`
