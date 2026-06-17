---
type: list
category: geography
read: false
---

# mountains

The mountains most worth knowing for quiz bowl.

## nodes

- [[denali|Denali]] — Denali (formerly Mount McKinley) is North America's highest peak at 20,310 feet, located in the Alaska Range of interior Alaska.
- [[k2|K2]] — K2 is the world's second-highest mountain at 28,251 feet, located in the Karakoram Range on the Pakistan-China border.
- [[mont-blanc|Mont Blanc]] — Mont Blanc is the highest peak in the Alps at 15,774 feet, straddling the border of France, Italy, and Switzerland in the…
- [[mount-aconcagua|Mount Aconcagua]] — Mount Aconcagua is the highest peak in South America at 22,838 feet, located in the Andes on the Argentina-Chile border.
- [[mount-elbrus|Mount Elbrus]] — Mount Elbrus is the highest peak in the Caucasus Range at 18,510 feet, straddling the Russia-Georgia border in the southern…
- [[mount-everest|Mount Everest]] — Mount Everest is the world's highest mountain at 29,032 feet, located in the Himalayas on the Nepal-Tibet border.
- [[mount-fuji|Mount Fuji]] — Mount Fuji is Japan's highest peak at 12,388 feet and an iconic symbol of Japanese culture and landscape.
- [[mount-kenya|Mount Kenya]] — Mount Kenya is Africa's second-highest peak at 17,057 feet, located in central Kenya near the equator.
- [[mount-kilimanjaro|Mount Kilimanjaro]] — Mount Kilimanjaro is Africa's highest peak at 19,341 feet, located in Tanzania near the Kenyan border.
- [[mount-kosciuszko|Mount Kosciuszko]] — Mount Kosciuszko is the highest peak in Australia at 7,310 feet, located in the Great Dividing Range in New South Wales.
- [[the-matterhorn|The Matterhorn]] — The Matterhorn is an iconic Alpine peak at 14,692 feet on the Switzerland-Italy border, famous for its distinctive pyramidal…

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
