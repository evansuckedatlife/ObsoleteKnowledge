---
type: list
category: misc
read: false
---

# world's fairs

The world's fairs most worth knowing for quiz bowl.

## nodes

- [[1851-great-exhibition-london|1851 Great Exhibition, London]] — The Great Exhibition of 1851, held in London's Hyde Park, was the first major international exposition showcasing industrial…
- [[1889-paris-worlds-fair|1889 Paris Exposition Universelle]] — The 1889 Paris Exposition Universelle, held in celebration of the centennial of the French Revolution, introduced the world to…
- [[1893-chicago-worlds-fair|1893 Chicago World's Columbian Exposition]] — The 1893 World's Columbian Exposition in Chicago celebrated the 400th anniversary of Columbus's voyage while showcasing…
- [[1900-paris-worlds-fair|1900 Paris Exposition Universelle]] — The 1900 Paris Exposition Universelle, held from April to November, was the second major world's fair in Paris and one of the…
- [[1904-st-louis-worlds-fair|1904 St. Louis Louisiana Purchase Exposition]] — The 1904 Louisiana Purchase Exposition in St.
- [[1939-new-york-worlds-fair|1939 New York World's Fair]] — The 1939 New York World's Fair, held in Flushing Meadows, Queens, was a celebration of progress and technological optimism…
- [[1962-seattle-worlds-fair|1962 Seattle World's Fair (Century 21 Exposition)]] — The 1962 Seattle World's Fair, officially titled Century 21 Exposition, celebrated humanity's optimism about space exploration…
- [[1964-new-york-worlds-fair|1964 New York World's Fair]] — The 1964 New York World's Fair returned to Flushing Meadows, Queens, a quarter-century after the 1939 exposition, celebrating…
- [[1967-montreal-expo-67|1967 Montreal Expo 67]] — Expo 67 in Montreal celebrated Canada's centennial year as a young nation and established the fair as a spectacular showcase…
- [[1970-osaka-expo|1970 Osaka Exposition (Expo 70)]] — Expo 70 in Osaka was the first world's fair held in Asia, marking Japan's emergence as a postwar economic and technological…

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
