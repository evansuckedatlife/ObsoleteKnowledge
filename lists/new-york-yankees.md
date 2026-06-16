---
type: list
category: sports
read: false
---

# New York Yankees

The New York Yankees most worth knowing for quiz bowl.

## nodes

- [[aaron-judge|Aaron Judge]] — Aaron Judge is an outfielder and one of the Yankees' current superstars, known for his towering home runs and imposing…
- [[alex-rodriguez|Alex Rodriguez]] — Alex Rodriguez was one of baseball's most talented shortstops and third basemen, joining the Yankees in 2004 and anchoring…
- [[babe-ruth|Babe Ruth]] — Babe Ruth revolutionised baseball in the 1920s as the most dominant home-run hitter of his era, transforming the sport from a…
- [[derek-jeter|Derek Jeter]] — Derek Jeter was the Yankees' shortstop and captain for 20 seasons (1995–2014), revitalising the franchise after 18 years…
- [[don-mattingly|Don Mattingly]] — Don Mattingly was a first baseman and the face of the Yankees during the lean years of the 1980s, known for consistent,…
- [[joe-dimaggio|Joe DiMaggio]] — Joe DiMaggio was an outfielder and one of baseball's most complete players, starring for the Yankees from 1936 to 1951.
- [[lou-gehrig|Lou Gehrig]] — Lou Gehrig was a first baseman and American League legend best known for his record 2,130 consecutive games played, earning…
- [[mariano-rivera|Mariano Rivera]] — Mariano Rivera was a closer and one of baseball's most dominant and iconic pitchers, spending nearly his entire 19-season…
- [[mickey-mantle|Mickey Mantle]] — Mickey Mantle was a switch-hitting outfielder and the Yankees' centerpiece from the 1950s through the early 1960s, combining…
- [[reggie-jackson|Reggie Jackson]] — Reggie Jackson was an outfielder and one of baseball's most dominant sluggers, best remembered for his dramatic postseason…
- [[whitey-ford|Whitey Ford]] — Whitey Ford was the Yankees' ace pitcher for 16 seasons (1950–1967), posting one of the most successful records in postseason…
- [[yogi-berra|Yogi Berra]] — Yogi Berra was a Hall of Fame catcher and one of the Yankees' most beloved figures, combining exceptional hitting (.285 career…

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
