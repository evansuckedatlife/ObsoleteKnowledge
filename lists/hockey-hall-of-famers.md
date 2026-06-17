---
type: list
category: sports
read: false
---

# Hockey Hall of Famers

The Hockey Hall of Famers most worth knowing for quiz bowl.

## nodes

- [[bobby-hull|Bobby Hull]] — Bobby Hull, known as The Golden Jet, was a Canadian left-winger and one of hockey's most electrifying scorers.
- [[bobby-orr|Bobby Orr]] — Bobby Orr is a Canadian defenseman and arguably the greatest blue-liner in hockey history.
- [[eddie-shore|Eddie Shore]] — Eddie Shore was a Canadian defenseman and one of hockey's earliest superstars, dominating the sport from the 1920s through the…
- [[gordie-howe|Gordie Howe]] — Gordie Howe, nicknamed Mr.
- [[ken-dryden|Ken Dryden]] — Ken Dryden is a Canadian goaltender and Harvard graduate who rose to dominance in the 1970s with the Montreal Canadiens,…
- [[mario-lemieux|Mario Lemieux]] — Mario Lemieux, known as The Magnificent One, is a Canadian centre regarded as the second-greatest player in hockey history…
- [[maurice-richard|Maurice Richard]] — Maurice Richard, nicknamed The Rocket, was a Canadian right-winger and icon of the Montreal Canadiens who dominated the NHL…
- [[terry-sawchuk|Terry Sawchuk]] — Terry Sawchuk was a Ukrainian-Canadian goaltender and one of the greatest netminders in hockey history.
- [[vladislav-tretiak|Vladislav Tretiak]] — Vladislav Tretiak is a Soviet goaltender widely regarded as one of the greatest net minders of all time.
- [[wayne-gretzky|Wayne Gretzky]] — Wayne Gretzky, known as The Great One, is widely regarded as the greatest ice hockey player of all time.

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
