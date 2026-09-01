---
type: list
category: pop-culture
read: false
---

# Pop Culture hubs

Formats, genres and phenomena the individual titles belong to.

## nodes

- [[billy-wilder|Billy Wilder]] — Billy Wilder was an Austrian-American film director and screenwriter who became one of Hollywood's most versatile and acclaimed filmmakers of the mid-…
- [[camera-movement|Camera Movement]] — Camera movement refers to the deliberate motion of the film camera — pans, tilts, tracking shots, zooms, and crane movements — used to guide the viewe…
- [[counter-strike|Counter-Strike]] — Counter-Strike is a team-based tactical first-person shooter developed by Valve, originally released as a Half-Life mod in 2000 before becoming a stan…
- [[first-person-shooter|First-Person Shooter]] — First-person shooter (FPS) is a video game genre defined by gameplay presented from the player's perspective looking through the protagonist's eyes, w…
- [[james-stewart|James Stewart]] — James Stewart was an American actor and military pilot who became one of Hollywood's most beloved stars through his portrayal of ordinary, decent men …
- [[laurel-and-hardy|Laurel and Hardy]] — Laurel and Hardy were a British-American comedy duo consisting of Stan Laurel and Oliver Hardy, whose partnership from 1926 through the 1940s became t…
- [[nintendo|Nintendo]] — Nintendo is a Japanese entertainment company founded in 1889 that evolved into one of the world's most influential video game publishers.
- [[romance|Romance]] — Romance is a narrative genre centered on the emotional and often physical relationship between two or more characters, typically culminating in commit…
- [[science-fiction-television|Science-Fiction Television]] — Science-fiction television encompasses TV series that explore speculative futures, alternate realities, or scientific premises as central to their nar…
- [[soviet-montage|Soviet Montage]] — Soviet montage is a film theory and technique that emerged from 1920s Russian cinema, asserting that meaning is created not within individual shots bu…
- [[television-drama|Television Drama]] — Television drama represents narrative-driven TV series built around character arcs, ongoing conflicts, and serialized storytelling rather than comedy …
- [[typography|Typography]] — Typography is the art and technique of arranging letterforms and text, treating type not merely as a neutral vehicle for language but as a visual and …
- [[western-television|Western Television]] — Western television is a genre of serialized TV dramas set in the American frontier or Old West, emphasizing lawlessness, justice, and individualism wi…
- [[worker-placement-mechanics|Worker-Placement Mechanics]] — Worker-placement mechanics represent a core board game system in which players assign limited agent tokens (often representing workers, officials, or …

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
