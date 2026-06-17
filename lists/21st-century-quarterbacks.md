---
type: list
category: sports
read: false
---

# 21st-century quarterbacks

The 21st-century quarterbacks most worth knowing for quiz bowl.

## nodes

- [[aaron-rodgers|Aaron Rodgers]] — Aaron Rodgers is an American football quarterback widely praised for his exceptional arm talent and clutch performances…
- [[ben-roethlisberger|Ben Roethlisberger]] — Ben Roethlisberger is an American football quarterback who spent his entire 18-season career with the Pittsburgh Steelers,…
- [[colin-kaepernick|Colin Kaepernick]] — Colin Kaepernick is an American football quarterback whose seven-season NFL career was defined by both athletic excellence as…
- [[drew-brees|Drew Brees]] — Drew Brees is an American football quarterback recognized as one of the most accurate and prolific passers in NFL history.
- [[michael-vick|Michael Vick]] — Michael Vick is an American football quarterback revolutionary for his running ability and athleticism at the position,…
- [[patrick-mahomes|Patrick Mahomes]] — Patrick Mahomes is an American football quarterback who emerged as the dominant force of the 2020s, leading the Kansas City…
- [[peyton-manning|Peyton Manning]] — Peyton Manning is an American football quarterback celebrated for his intelligence, accuracy, and record-breaking performances…
- [[philip-rivers|Philip Rivers]] — Philip Rivers is an American football quarterback who spent 16 of his 17 seasons with the San Diego/Los Angeles Chargers…
- [[russell-wilson|Russell Wilson]] — Russell Wilson is an American football quarterback who spent ten seasons with the Seattle Seahawks before moving to the Denver…
- [[tom-brady|Tom Brady]] — Tom Brady is an American football quarterback widely regarded as the greatest to ever play the position.

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
