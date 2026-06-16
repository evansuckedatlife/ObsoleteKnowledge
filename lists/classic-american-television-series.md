---
type: list
category: pop-culture
read: false
---

# classic American television series

The classic American television series most worth knowing for quiz bowl.

## nodes

- [[60-minutes|60 Minutes]] — 60 Minutes is the longest-running primetime television program in American history, an investigative news magazine that…
- [[dragnet|Dragnet]] — Dragnet is a pioneering police procedural television series that debuted on NBC in 1951 and ran for eight seasons,…
- [[gunsmoke|Gunsmoke]] — Gunsmoke is a landmark television western that aired on CBS from 1955 to 1975, becoming one of the longest-running dramatic…
- [[saturday-night-live|Saturday Night Live]] — Saturday Night Live is a groundbreaking sketch-comedy and music television show that debuted on NBC in 1975 and has become the…
- [[star-trek-the-original-series|Star Trek (The Original Series)]] — Star Trek is a visionary science-fiction series that imagines a future in which humanity, alongside multiple alien species,…
- [[the-ed-sullivan-show|The Ed Sullivan Show]] — The Ed Sullivan Show is a legendary variety television program that aired on CBS from 1948 to 1971, becoming the nation's…
- [[the-tonight-show|The Tonight Show]] — The Tonight Show is a foundational late-night television institution that premiered on NBC in 1954 and became the template for…
- [[the-twilight-zone|The Twilight Zone]] — The Twilight Zone is a groundbreaking science-fiction and fantasy anthology series that explores the strange, unsettling, and…
- [[the-x-files|The X-Files]] — The X-Files is a science-fiction television series that aired on Fox from 1993 to 2018 (with intermittent breaks), becoming…
- [[twin-peaks|Twin Peaks]] — Twin Peaks is a groundbreaking television drama that aired on ABC from 1990 to 1991 and later returned in limited form,…

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
