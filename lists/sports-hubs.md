---
type: list
category: sports
read: false
---

# Sports hubs

Competitions, structures and concepts the individual athletes compete within.

## nodes

- [[1920s-sports|1920s Sports]] — The 1920s marked a transformative era in sport known as the Golden Age of Sports, when athletics ascended from a regional pastime to a dominant cultur…
- [[american-culture|American Culture]] — American culture encompasses the shared values, practices, and artistic traditions that define identity in the United States, from mass entertainment …
- [[american-football|American Football]] — American football is a collision sport played primarily in united-states|North America, featuring two teams of eleven players competing to advance an …
- [[ancient-greek-athletics|Ancient Greek Athletics]] — Ancient Greek athletics encompassed the sporting practices, competitions, and traditions that permeated classical Greek civilization from the archaic …
- [[baseball|Baseball]] — Baseball is a bat-and-ball sport played between two teams of nine players, typically across nine innings on a diamond-shaped field with four bases.
- [[boston-bruins|Boston Bruins]] — The Boston Bruins are one of the National Hockey League's oldest and most storied franchises, founded in 1924 as the league's first American team.
- [[defenseman|Defenseman]] — A defenseman is the primary position responsible for preventing the opposing team from scoring in ice hockey.
- [[denver-broncos|Denver Broncos]] — The Denver Broncos are a professional American football franchise based in Denver, Colorado, competing in the National Football League.
- [[detroit-red-wings|Detroit Red Wings]] — The Detroit Red Wings are one of the oldest and most successful franchises in professional ice hockey, founded in 1926 and competing continuously in t…
- [[goaltender|Goaltender]] — A goaltender is the ice hockey player responsible for defending the goal and preventing the opposing team from scoring.
- [[golf|Golf]] — Golf is an individual sport played over a course of 9 or 18 holes, where players use clubs to strike a ball into a hole in the fewest strokes possible.
- [[grand-slam-tournaments|Grand Slam Tournaments]] — The Grand Slam tournaments are the four most prestigious tennis competitions in the world, held annually across different continents and surfaces.
- [[hockey-physical-play|Hockey Physical Play]] — Hockey physical play refers to the body-checking and contact-based style of hockey that emphasizes physicality, intimidation, and physical dominance a…
- [[ice-hockey|Ice Hockey]] — Ice hockey is a professional sport played on ice between two teams of six players, where competitors use sticks to control a puck and score by shootin…
- [[los-angeles-chargers|Los Angeles Chargers]] — The Los Angeles Chargers are a professional american-football|football franchise that relocated to Los Angeles in 2017 after 56 years in san-diego-cha…
- [[montreal-canadiens|Montreal Canadiens]] — The Montreal Canadiens are one of ice hockey's most storied and successful franchises, founded in 1909 and competing continuously in the National Hock…
- [[national-football-league|National Football League]] — The National Football League (NFL) is the premier professional American football league in the United States and one of the world's most profitable sp…
- [[new-orleans-saints|New Orleans Saints]] — The New Orleans Saints are a professional american-football|football franchise competing in the national-football-league|NFL's NFC South, founded in 1…
- [[nfl-accuracy-records|NFL Accuracy Records]] — NFL accuracy records encompass the statistical achievements that quarterback-led teams accomplish through passing precision, completion percentage, an…
- [[nhl-scoring-records|NHL Scoring Records]] — NHL scoring records document the achievements of hockey's greatest offensive players, measuring goals, assists, and points across single seasons, care…
- [[olympic-amateurism-rules|Olympic Amateurism Rules]] — Olympic amateurism rules were strict eligibility codes that governed participation in the Olympic Games from their modern inception through the late t…
- [[san-diego-chargers|San Diego Chargers]] — The San Diego Chargers were an American football franchise based in San Diego, California, competing in the NFL from 1961 to 2016.
- [[san-francisco-49ers|San Francisco 49ers]] — The San Francisco 49ers are one of professional american-football|football's most storied franchises, competing in the national-football-league|NFL si…
- [[world-series|World Series]] — The World Series is the championship series of Major League Baseball, contested annually between the American League and National League champions.

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
