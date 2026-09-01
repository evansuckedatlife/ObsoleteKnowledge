---
type: list
category: geography
read: false
---

# Geography hubs

Continents, regions and physical features that the rest of the geography collection is described against.

## nodes

- [[andes|Andes]] — The Andes is the world's longest continental mountain range, spanning approximately 7,000 kilometers along the western edge of South America through s…
- [[appalachian-mountains|Appalachian Mountains]] — The Appalachian Mountains form one of North America's oldest and most historically significant mountain ranges, extending approximately 3,200 kilomete…
- [[arctic-ocean|Arctic Ocean]] — The Arctic Ocean is the smallest and shallowest of Earth's five oceans, surrounding the North Pole and largely covered by ice, with coastlines touchin…
- [[arkansas-river|Arkansas River]] — The Arkansas River is a major tributary of the Mississippi River, flowing approximately 2,340 kilometers from the Rocky Mountains in central Colorado …
- [[bedouin|Bedouin]] — The Bedouin are Arab pastoral and nomadic peoples of the desert regions of the Middle East and North Africa, particularly the Arabian Desert, the Nege…
- [[botswana|Botswana]] — Botswana is a large, landlocked Southern African nation characterized by the Kalahari Desert, the Okavango Delta, and vast wildlife reserves, with a r…
- [[central-asia|Central Asia]] — Central Asia is a vast continental region spanning from the Caspian Sea westward to the Pacific Ocean, encompassing the Gobi Desert, the Taklamakan De…
- [[chile|Chile]] — Chile is a long, narrow country stretching along South America's western coast, bordered by the Andes to the east and the Pacific to the west.
- [[climate-change|Climate Change]] — Climate change refers to long-term shifts in global temperatures and weather patterns, primarily driven by human activities since the onset of industr…
- [[europe|Europe]] — Europe is a continent and cultural region spanning from the Atlantic Ocean in the west to the Ural Mountains in the east, encompassing over 40 countri…
- [[gustave-eiffel|Gustave Eiffel]] — Gustave Eiffel was a French civil engineer renowned for his pioneering work with iron structures and his iconic architectural achievements of the 19th…
- [[indian-ocean|Indian Ocean]] — The Indian Ocean is the world's third-largest ocean, bordered by Africa to the west, Asia to the north and east, and extending south toward the Antarc…
- [[lisbon|Lisbon]] — Lisbon is the capital and largest city of Portugal, strategically positioned on the Tagus River estuary where it meets the Atlantic Ocean.
- [[north-america|North America]] — North America is the northern continent of the Americas, encompassing the United States, Canada, Mexico, and numerous Caribbean island nations, stretc…
- [[pacific-ocean|Pacific Ocean]] — The Pacific Ocean is Earth's largest and deepest ocean, spanning nearly a third of the planet's surface and separating Asia from the Americas.
- [[samurai|Samurai]] — The samurai were the hereditary warrior class of feudal Japan, bound by a strict code of honor called Bushidō.
- [[scottish-enlightenment|Scottish Enlightenment]] — The Scottish Enlightenment was a period of intellectual ferment in 18th-century Scotland that produced foundational ideas in philosophy, economics, po…
- [[south-africa|South Africa]] — South Africa is the southernmost country on the African continent, occupying the southern tip and commanding a crucial crossroads between the Atlantic…
- [[tanzania|Tanzania]] — Tanzania is a large East African nation formed in 1964 from the merger of Tanganyika and Zanzibar, encompassing diverse landscapes from Mount Kilimanj…
- [[texas|Texas]] — Texas is the second-largest U.S.
- [[uganda|Uganda]] — Uganda is a landlocked country in East Africa, bordered by Kenya, Tanzania, Rwanda, the Democratic Republic of the Congo, and South Sudan.
- [[venice|Venice]] — Venice is a historic city-state built on lagoon islands in northeastern Italy, founded in the 5th century and rising to become a Mediterranean superpo…
- [[vietnam|Vietnam]] — Vietnam is a Southeast Asian nation stretching along the eastern coast of Indochina, bordered by China to the north and Cambodia and Laos to the west.

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
