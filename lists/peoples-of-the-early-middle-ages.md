---
type: list
category: history
read: false
---

# peoples of the early Middle Ages

The peoples of the early Middle Ages most worth knowing for quiz bowl.

## nodes

- [[angles-and-saxons|Angles and Saxons]] — The Angles and Saxons were Germanic peoples who migrated to Britain in the 5th and 6th centuries, progressively conquering…
- [[burgundians|Burgundians]] — The Burgundians were a Germanic people who settled in the Rhône valley and eastern Gaul in the 5th century, establishing a…
- [[franks|Franks]] — The Franks were a Germanic people who rose from the Rhine frontier to become the dominant power in Western Europe,…
- [[gepids|Gepids]] — The Gepids were a Germanic people closely related to the Goths who initially ruled the region of Pannonia (modern Hungary) and…
- [[huns|Huns]] — The Huns were a nomadic people from Central Asia whose invasions under Attila in the 5th century posed an existential threat…
- [[lombards|Lombards]] — The Lombards were a Germanic people who invaded and settled northern Italy in 568, establishing a kingdom that lasted over two…
- [[ostrogoths|Ostrogoths]] — The Ostrogoths were the eastern branch of the Gothic peoples, ruled by Theodoric the Great, who conquered and governed Italy…
- [[suebi|Suebi]] — The Suebi were a Germanic people who invaded the Iberian Peninsula in the 5th century, establishing a kingdom in the northwest…
- [[vandals|Vandals]] — The Vandals were a Germanic people who established a powerful naval kingdom in North Africa under Gaiseric, notorious for…
- [[visigoths|Visigoths]] — The Visigoths were a Germanic people who became the dominant power in the Iberian Peninsula after the Western Roman Empire's…

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
