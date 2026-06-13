---
type: list
category: geography
read: false
---

# African bodies of water

The African bodies of water most worth knowing for quiz bowl.

## nodes

- [[congo-river|Congo River]] — The Congo is Africa's second-longest river and by far its largest by discharge, carrying more water to the ocean than any…
- [[lake-chad|Lake Chad]] — Lake Chad is a shallow freshwater lake in the Sahel region of West-Central Africa, bordered by Nigeria, Niger, Chad, and Cameroon.
- [[lake-malawi|Lake Malawi]] — Lake Malawi (also called Lake Nyasa) is an East African lake spanning approximately 11,400 square miles along the borders of…
- [[lake-tanganyika|Lake Tanganyika]] — Lake Tanganyika is Africa's deepest and second-largest lake by volume, stretching approximately 420 miles along the border of…
- [[lake-victoria|Lake Victoria]] — Lake Victoria is Africa's largest lake by surface area, spanning approximately 26,600 square miles across the borders of…
- [[lake-volta|Lake Volta]] — Lake Volta is the world's largest artificial reservoir by surface area, created by the Akosombo Dam on the Volta River in Ghana.
- [[limpopo-river|Limpopo River]] — The Limpopo is a major southern African river flowing approximately 1,100 miles from the highlands of South Africa and…
- [[niger-river|Niger River]] — The Niger is West Africa's principal river, flowing approximately 2,600 miles in a distinctive boomerang arc through nine…
- [[nile-river|Nile River]] — The Nile is Africa's longest river, flowing approximately 4,130 miles through eleven countries before emptying into the…
- [[okavango-river|Okavango River]] — The Okavango is a southern African river approximately 1,000 miles long that flows from Angola through Botswana, terminating…
- [[zambezi-river|Zambezi River]] — The Zambezi is southern Africa's most important river, flowing approximately 1,650 miles from northwestern Zambia across eight…

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
