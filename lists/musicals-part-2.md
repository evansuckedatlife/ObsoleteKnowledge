---
type: list
category: performance
read: false
---

# musicals

The musicals most worth knowing for quiz bowl.

## nodes

- [[a-chorus-line-musical|A Chorus Line]] — A Chorus Line is a 1975 Pulitzer Prize-winning musical that documents the lives of dancers auditioning for a Broadway chorus.
- [[cats-musical|Cats]] — Cats is a 1981 musical by composer Andrew Lloyd Webber, based on T.
- [[chicago-musical|Chicago]] — Chicago is a cynical 1996 musical revival by John Kander and Fred Ebb, originally written in 1975, that captures the sleaze…
- [[hamilton-musical|Hamilton]] — Hamilton: An American Musical is a 2015 hip-hop and pop musical by Lin-Manuel Miranda that reimagines the life of founding…
- [[into-the-woods-musical|Into the Woods]] — Into the Woods is a 1987 musical by Stephen Sondheim that interweaves and subverts classic Grimm fairy tales—Cinderella,…
- [[les-miserables-musical|Les Misérables]] — Les Misérables is an epic musical adaptation of Victor Hugo's 1862 novel, composed by Claude-Michel Schönberg with lyrics by…
- [[rent-musical|Rent]] — Rent is a 1996 musical by Jonathan Larson that reimagines La Bohème in contemporary New York, following bohemian artists…
- [[sweeney-todd-musical|Sweeney Todd]] — Sweeney Todd: The Demon Barber of Fleet Street is a 1979 musical by Stephen Sondheim that blends Grand Guignol horror with…
- [[the-phantom-of-the-opera-musical|The Phantom of the Opera]] — The Phantom of the Opera is an Andrew Lloyd Webber musical adaptation of Gaston Leroux's gothic novel, which premiered in…
- [[wicked-musical|Wicked]] — Wicked is a 2003 musical by composer-lyricist Stephen Schwartz, based on Gregory Maguire's 1995 novel, that retells the story…

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
