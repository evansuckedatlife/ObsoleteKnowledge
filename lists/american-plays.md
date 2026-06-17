---
type: list
category: literature
read: false
---

# American plays

The American plays most worth knowing for quiz bowl.

## nodes

- [[a-raisin-in-the-sun|A Raisin in the Sun]] — Lorraine Hansberry's 1959 play follows the African American Younger family in Chicago as they await a life insurance check…
- [[a-streetcar-named-desire|A Streetcar Named Desire]] — Tennessee Williams' 1947 play depicts the collision between Blanche DuBois, a fading Southern belle seeking refuge with her…
- [[angels-in-america|Angels in America]] — Tony Kushner's 1991-1993 two-part play, subtitled "A Gay Fantasia on National Themes," interweaves the personal collapse of…
- [[death-of-a-salesman|Death of a Salesman]] — Arthur Miller's tragedy follows Willy Loman, an aging traveling salesman whose mental and financial decline culminates in suicide.
- [[long-days-journey-into-night|Long Day's Journey into Night]] — Eugene O'Neill's 1956 play (published posthumously) is a four-act family tragedy set over a single day in a Connecticut summer…
- [[our-town|Our Town]] — Thornton Wilder's 1938 play is a three-act meditation on small-town American life, set in the fictional Groves Corners, New…
- [[the-crucible|The Crucible]] — Arthur Miller's 1953 play dramatizes the 1692 Salem witch trials, depicting a community consumed by fear, accusation, and…
- [[the-glass-menagerie|The Glass Menagerie]] — Tennessee Williams' 1944 "memory play" is narrated retrospectively by Tom Wingfield, who recounts his family's struggles in a St.
- [[the-iceman-cometh|The Iceman Cometh]] — Eugene O'Neill's 1946 play is set in Harry Hope's saloon, a refuge for derelicts, failed dreamers, and alcoholics waiting for…
- [[whos-afraid-of-virginia-woolf|Who's Afraid of Virginia Woolf?]] — Edward Albee's 1962 play depicts a brutal evening between two married couples—the intellectual George and his acerbic,…

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
