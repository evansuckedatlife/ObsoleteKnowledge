---
type: list
category: science
read: false
---

# space missions

The space missions most worth knowing for quiz bowl.

## nodes

- [[apollo-1|Apollo 1]] — A crewed Apollo capsule test scheduled for launch on February 21, 1967, that ended in catastrophic fire during a ground test…
- [[apollo-11|Apollo 11]] — The first crewed lunar landing, on July 20, 1969, when Apollo 11 carried Neil Armstrong, Buzz Aldrin, and Michael Collins to…
- [[apollo-13|Apollo 13]] — A crewed lunar mission launched by NASA on April 11, 1970, that suffered a catastrophic oxygen tank failure two days into the…
- [[apollo-soyuz-test-project|Apollo-Soyuz Test Project]] — A symbolic crewed space mission flown in July 1975 by the United States and Soviet Union, in which an Apollo command module…
- [[hubble-space-telescope-servicing|Hubble Space Telescope Servicing Missions]] — A series of five Space Shuttle missions (1993–2009) to repair, upgrade, and maintain the Hubble Space Telescope.
- [[space-shuttle-challenger|Space Shuttle Challenger]] — The Space Shuttle Challenger was destroyed 73 seconds after launch on January 28, 1986, killing all seven crew members aboard…
- [[spacex-crs-1|SpaceX CRS-1]] — The first Commercial Resupply Services mission to the International Space Station, launched by SpaceX on May 22, 2012.
- [[sputnik-1|Sputnik 1]] — The first artificial satellite, launched by the Soviet Union on October 4, 1957, marking the beginning of the Space Age and…
- [[voskhod-1|Voskhod 1]] — The first spacecraft to carry a multi-person crew, launched by the Soviet Union on October 12, 1964.
- [[vostok-1|Vostok 1]] — The first crewed spaceflight, launched by the Soviet Union on April 12, 1961, with Yuri Gagarin aboard.

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
