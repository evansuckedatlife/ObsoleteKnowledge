---
type: list
category: sports
read: false
---

# Olympics

The Olympics most worth knowing for quiz bowl.

## nodes

- [[1896-athens-olympics|1896 Summer Olympics]] — The first modern Olympic Games, held in Athens, Greece, revived the ancient Greek athletic competition as an international event.
- [[1912-stockholm-olympics|1912 Summer Olympics]] — The 1912 Summer Olympics in Stockholm, Sweden, marked a expansion of the Games' scale and included the rise of American…
- [[1936-berlin-olympics|1936 Summer Olympics]] — The 1936 Summer Olympics in Berlin were seized by Nazi Germany as propaganda for racial superiority—yet the Games became…
- [[1968-mexico-city-olympics|1968 Summer Olympics]] — The 1968 Summer Olympics in Mexico City became a watershed moment when African American sprinters Tommie Smith and John Carlos…
- [[1972-munich-olympics|1972 Summer Olympics]] — The 1972 Summer Olympics in Munich, West Germany, were overshadowed by the Munich massacre, when Palestinian terrorists took…
- [[1980-moscow-olympics|1980 Summer Olympics]] — The 1980 Summer Olympics in Moscow were marked by a major geopolitical boycott led by the United States and more than 60…
- [[1980-lake-placid-winter-olympics|1980 Winter Olympics]] — The 1980 Winter Olympics in Lake Placid, New York, are remembered for the "Miracle on Ice"—when the U.S.
- [[1984-los-angeles-olympics|1984 Summer Olympics]] — The 1984 Summer Olympics in Los Angeles were boycotted by the Soviet Union and its allies in retaliation for the U.S.-led…
- [[1994-lillehammer-winter-olympics|1994 Winter Olympics]] — The 1994 Winter Olympics in Lillehammer, Norway, are remembered for figure skating drama centered on American skaters Tonya…
- [[1996-atlanta-olympics|1996 Summer Olympics]] — The 1996 Summer Olympics in Atlanta, Georgia, marked the centennial of the modern Olympic Games and became a symbol of the…

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
