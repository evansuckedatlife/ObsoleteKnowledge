---
type: list
category: sports
read: false
---

# Tennis Grand Slams

The four Grand Slam tournaments — tennis's most prestigious annual championships.

## nodes

- [[australian-open|Australian Open]] — The Australian Open is one of tennis's four Grand Slam tournaments, held annually in January at Melbourne Park in Melb…
- [[french-open|French Open]] — The French Open, officially known as Roland-Garros, is one of tennis's four Grand Slam tournaments, held annually in M…
- [[wimbledon|Wimbledon]] — The Wimbledon Championships is the oldest and most prestigious Grand Slam tennis tournament in the world, held annuall…
- [[us-open|US Open]] — The US Open is one of the four Grand Slam tennis tournaments and one of golf's five major championships, held annually…

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
