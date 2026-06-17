---
type: list
category: geography
read: false
---

# North American rivers

The North American rivers most worth knowing for quiz bowl.

## nodes

- [[colorado-river|Colorado River]] — The Colorado River is a major river of the southwestern United States and northwestern Mexico, flowing approximately 1,450…
- [[columbia-river|Columbia River]] — The Columbia River is the longest river in the Pacific Northwest, flowing approximately 1,240 miles from British Columbia…
- [[delaware-river|Delaware River]] — The Delaware River flows approximately 330 miles from the Catskill Mountains of New York to Delaware Bay and the Atlantic…
- [[hudson-river|Hudson River]] — The Hudson River flows approximately 315 miles southward from the Adirondack Mountains in upstate New York to New York Harbor…
- [[mackenzie-river|Mackenzie River]] — The Mackenzie River flows approximately 1,025 miles northwestward from Great Slave Lake to the Arctic Ocean, serving as…
- [[mississippi-river|Mississippi River]] — The Mississippi River is the longest river in North America and the second-longest on the continent after the Missouri,…
- [[missouri-river|Missouri River]] — The Missouri River flows approximately 2,540 miles from the Rocky Mountains in Montana to its confluence with the Mississippi…
- [[ohio-river|Ohio River]] — The Ohio River is a major tributary of the Mississippi River, flowing approximately 980 miles from Pennsylvania to Kentucky,…
- [[potomac-river|Potomac River]] — The Potomac River flows approximately 380 miles from the Appalachian Mountains of West Virginia to Chesapeake Bay, forming the…
- [[red-river-of-the-south|Red River of the South]] — The Red River of the South (distinct from the Red River flowing into Hudson Bay) flows approximately 1,300 miles from the…
- [[rio-grande|Rio Grande]] — The Rio Grande flows approximately 1,900 miles from the San Juan Mountains of Colorado southward through New Mexico and along…
- [[snake-river|Snake River]] — The Snake River flows approximately 1,040 miles through the Pacific Northwest, originating in the Teton Range of Wyoming and…
- [[st-lawrence-river|St. Lawrence River]] — The St.
- [[yukon-river|Yukon River]] — The Yukon River flows approximately 1,980 miles through western Canada and Alaska from the Whitehorse region of the Yukon…

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
