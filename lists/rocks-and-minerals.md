---
type: list
category: science
read: false
---

# rocks and minerals

The rocks and minerals most worth knowing for quiz bowl.

## nodes

- [[basalt|Basalt]] — Basalt is a fine-grained, dark mafic igneous rock formed from the rapid cooling of low-silica lava flows.
- [[calcite|Calcite]] — Calcite is calcium carbonate (CaCO₃), a ubiquitous mineral found in sedimentary, metamorphic, and igneous rocks.
- [[corundum|Corundum]] — Corundum is aluminium oxide (Al₂O₃), the second hardest mineral after diamond.
- [[diamond|Diamond]] — Diamond is a metastable allotrope of carbon, crystallised under extreme pressure and temperature deep within the Earth's mantle.
- [[feldspar|Feldspar]] — Feldspar is the most abundant mineral in Earth's crust, comprising about 60% of all igneous rocks.
- [[granite|Granite]] — Granite is a coarse-grained, light-coloured felsic igneous rock composed primarily of quartz, feldspar, and mica.
- [[limestone|Limestone]] — Limestone is a sedimentary rock composed primarily of calcium carbonate (calcite), typically formed from the skeletal material…
- [[mica|Mica]] — Mica is a group of silicate minerals characterised by perfect basal cleavage, producing thin, flexible sheets.
- [[quartz|Quartz]] — Quartz is silicon dioxide (SiO₂), the second most abundant mineral in Earth's crust.
- [[sandstone|Sandstone]] — Sandstone is a clastic sedimentary rock composed of sand-sized mineral grains (0.0625–2 mm) cemented together, most commonly…

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
