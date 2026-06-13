---
type: list
category: science
read: false
---

# active volcanoes

The active volcanoes most worth knowing for quiz bowl.

## nodes

- [[kilauea|Kilauea]] — An active shield volcano located on the southeastern part of the Big Island of Hawaii, Kilauea is one of the most active…
- [[krakatoa|Krakatoa]] — Located in the Sunda Strait between Java and Sumatra in Indonesia, Krakatoa is famous for its cataclysmic 1883 eruption.
- [[mauna-loa|Mauna Loa]] — An active basaltic shield volcano on the Big Island of Hawaii, Mauna Loa is the largest subaerial volcano on Earth by both…
- [[mount-cotopaxi|Mount Cotopaxi]] — An active stratovolcano located in the Andes Mountains of Ecuador, Mount Cotopaxi is one of the highest active volcanoes in…
- [[mount-erebus|Mount Erebus]] — Located on Ross Island in Antarctica, Mount Erebus is the southernmost active volcano on Earth.
- [[mount-etna|Mount Etna]] — Located on the east coast of Sicily, Italy, Mount Etna is the highest active volcano in Europe outside the Caucasus.
- [[mount-pelee|Mount Pelée]] — An active stratovolcano on the Caribbean island of Martinique, Mount Pelée is infamous for its devastating eruption in May 1902.
- [[mount-pinatubo|Mount Pinatubo]] — Located on the island of Luzon in the Philippines, Mount Pinatubo is an active stratovolcano.
- [[mount-saint-helens|Mount Saint Helens]] — An active stratovolcano located in Skamania County, Washington, Mount Saint Helens is part of the Cascade Volcanic Arc.
- [[mount-tambora|Mount Tambora]] — An active stratovolcano on the island of Sumbawa in Indonesia, Mount Tambora is the site of the largest volcanic eruption in…
- [[vesuvius|Mount Vesuvius]] — A sommo-stratovolcano located on the Gulf of Naples in Campania, Italy, Mount Vesuvius is one of the world's most famous and…

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
