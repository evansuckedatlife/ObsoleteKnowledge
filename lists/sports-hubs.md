---
type: list
category: sports
read: false
---

# Sports hubs

Competitions, structures and concepts the individual athletes compete within.

## nodes

- [[american-culture|American Culture]] — American culture encompasses the shared values, practices, and artistic traditions that define identity in the United States, from mass entertainment …
- [[goaltender|Goaltender]] — A goaltender is the ice hockey player responsible for defending the goal and preventing the opposing team from scoring.
- [[grand-slam-tournaments|Grand Slam Tournaments]] — The Grand Slam tournaments are the four most prestigious tennis competitions in the world, held annually across different continents and surfaces.
- [[nhl-scoring-records|NHL Scoring Records]] — NHL scoring records document the achievements of hockey's greatest offensive players, measuring goals, assists, and points across single seasons, care…

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
