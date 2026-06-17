---
type: list
category: history
read: false
---

# Black American legislators

The Black American legislators most worth knowing for quiz bowl.

## nodes

- [[adam-clayton-powell-jr|Adam Clayton Powell Jr.]] — Adam Clayton Powell Jr.
- [[barbara-jordan|Barbara Jordan]] — Barbara Jordan (1936–1996) was the first Black woman elected to Congress from the South, representing Texas from 1973 to 1979.
- [[blanche-bruce|Blanche Bruce]] — Blanche Kelso Bruce (1841–1898) was the first African American elected to a full six-year term in the United States Senate,…
- [[carol-moseley-braun|Carol Moseley Braun]] — Carol Moseley Braun (1947–) was the first Black woman elected to the United States Senate, representing Illinois from 1993 to…
- [[charles-rangel|Charles Rangel]] — Charles Rangel (1930–2016) was a Long Island politician and longtime Harlem congressman who chaired the House Ways and Means…
- [[hiram-revels|Hiram Revels]] — Hiram Rhodes Revels (1827–1901) was the first African American to serve in the United States Senate, representing Mississippi…
- [[john-lewis|John Lewis]] — John Lewis (1940–2020) was a towering figure of the civil rights movement who transitioned from Freedom Rider and march…
- [[p-b-s-pinchback|P.B.S. Pinchback]] — Pinckney Benton Stewart Pinchback (1837–1921) was Louisiana's most prominent Black Reconstruction politician, serving as…
- [[robert-smalls|Robert Smalls]] — Robert Smalls (1839–1915) was an enslaved maritime pilot who became a Civil War hero, Reconstruction congressman, and…
- [[shirley-chisholm|Shirley Chisholm]] — Shirley Chisholm (1924–2005) was the first Black woman elected to Congress, representing Brooklyn from 1969 to 1983.

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
