---
type: list
category: history
read: false
---

# Native American peoples

The Native American peoples most worth knowing for quiz bowl.

## nodes

- [[apache|Apache]] — The Apache are a southwestern Athabaskan people traditionally inhabiting Arizona, New Mexico, and parts of Texas, Colorado,…
- [[cherokee|Cherokee]] — The Cherokee are one of the largest Native American nations, originally occupying the southeastern Appalachian region…
- [[cheyenne|Cheyenne]] — The Cheyenne (Tsitsistas, meaning "the People") are a Great Plains and Mountain nation originally inhabiting the Upper Plains…
- [[comanche|Comanche]] — The Comanche are a Great Plains and Southwest nation, historically inhabiting Texas, Oklahoma, Colorado, and Kansas, renowned…
- [[iroquois|Iroquois (Haudenosaunee)]] — The Iroquois (Haudenosaunee or Hodenosaunee, meaning "People of the Longhouse") are a confederacy of six nations in the…
- [[lakota-sioux|Lakota / Sioux]] — The Lakota (Sioux) are a Great Plains nation originally spanning the Dakotas, Nebraska, and Montana, renowned for their horse…
- [[navajo|Navajo (Diné)]] — The Navajo (Diné, meaning "the People") are the largest federally recognized Native American nation, inhabiting the Southwest…
- [[nez-perce|Nez Perce]] — The Nez Perce (Nimíipuu, "the People") are a Plateau nation historically inhabiting the Pacific Northwest (present-day Oregon,…
- [[pueblo|Pueblo]] — The Pueblo peoples are a diverse group of Southwestern sedentary cultures inhabiting the Rio Grande Valley and adjacent…
- [[seminole|Seminole]] — The Seminole are a Southeast nation formed in the 18th century from Creek and other Southeastern peoples in the Florida…

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
