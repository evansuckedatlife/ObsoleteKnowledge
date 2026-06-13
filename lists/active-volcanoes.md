---
type: list
category: science
read: false
---

# Active Volcanoes

Geologically active volcanic vents, stratovolcanoes, and shield volcanoes whose eruptions have shaped Earth's climate, geography, and human history.

## nodes

- [[vesuvius|Mount Vesuvius]] — Italian stratovolcano that buried Pompeii in 79 AD.
- [[krakatoa|Krakatoa]] — Indonesian caldera island famous for its massive 1883 explosion and resulting global tsunami.
- [[mount-saint-helens|Mount Saint Helens]] — Cascade stratovolcano that erupted in a major lateral blast in May 1980.
- [[mount-pinatubo|Mount Pinatubo]] — Philippine volcano that erupted in 1991, causing global cooling via stratospheric aerosols.
- [[mount-pelee|Mount Pelée]] — Martinique volcano whose 1902 pyroclastic flow wiped out the city of Saint-Pierre.
- [[mount-tambora|Mount Tambora]] — Indonesian volcano whose 1815 eruption caused the "Year Without a Summer" in 1816.
- [[mount-cotopaxi|Mount Cotopaxi]] — high-altitude Ecuadorian stratovolcano capped by an equatorial glacier.
- [[mount-erebus|Mount Erebus]] — southernmost active volcano on Earth, located in Antarctica and possessing an active lava lake.
- [[mount-etna|Mount Etna]] — Europe's highest active volcano, located in Sicily and connected to Greek myths of Typhon.
- [[mauna-loa|Mauna Loa]] — world's largest shield volcano by volume, located on the Big Island of Hawaii.
- [[kilauea|Kilauea]] — highly active Hawaiian shield volcano regarded as the home of the goddess Pele.

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
