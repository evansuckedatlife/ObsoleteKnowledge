---
type: list
category: pop-culture
read: false
---

# Pop Culture hubs

Formats, genres and phenomena the individual titles belong to.

## nodes

- [[alfred-hitchcock|Alfred Hitchcock]] — Alfred Hitchcock was a British-American film director who redefined the thriller genre and became synonymous with suspense cinema.
- [[billy-wilder|Billy Wilder]] — Billy Wilder was an Austrian-American film director and screenwriter who became one of Hollywood's most versatile and acclaimed filmmakers of the mid-…
- [[camera-movement|Camera Movement]] — Camera movement refers to the deliberate motion of the film camera — pans, tilts, tracking shots, zooms, and crane movements — used to guide the viewe…
- [[counter-strike|Counter-Strike]] — Counter-Strike is a team-based tactical first-person shooter developed by Valve, originally released as a Half-Life mod in 2000 before becoming a stan…
- [[doom|Doom]] — Doom (1993) is the seminal first-person shooter that defined the genre's core grammar: run, aim, shoot, advance.
- [[esports|Esports]] — Esports encompasses competitive video gaming organized at professional, televised, and international scales.
- [[film-editing|Film Editing]] — Film editing is the art of assembling shot sequences into a coherent narrative and emotional experience.
- [[first-person-shooter|First-Person Shooter]] — First-person shooter (FPS) is a video game genre defined by gameplay presented from the player's perspective looking through the protagonist's eyes, w…
- [[frank-capra|Frank Capra]] — Frank Capra was an Italian-American director who championed the moral courage of ordinary people against institutional corruption and social indiffere…
- [[industrialization|Industrialization]] — Industrialization is the transformation of economic production from craft and agriculture to machine-based factory systems, and its profound cultural,…
- [[james-stewart|James Stewart]] — James Stewart was an American actor and military pilot who became one of Hollywood's most beloved stars through his portrayal of ordinary, decent men …
- [[laurel-and-hardy|Laurel and Hardy]] — Laurel and Hardy were a British-American comedy duo consisting of Stan Laurel and Oliver Hardy, whose partnership from 1926 through the 1940s became t…
- [[mise-en-scene|Mise-en-scène]] — Mise-en-scène refers to everything placed before the camera: set design, actor positioning, lighting, props, and composition within the frame.
- [[mystery-television|Mystery Television]] — Mystery television encompasses dramatic series structured around criminal investigation, suspense, and revelation.
- [[nintendo|Nintendo]] — Nintendo is a Japanese entertainment company founded in 1889 that evolved into one of the world's most influential video game publishers.
- [[romance|Romance]] — Romance is a narrative genre centered on the emotional and often physical relationship between two or more characters, typically culminating in commit…
- [[science-fiction-television|Science-Fiction Television]] — Science-fiction television encompasses TV series that explore speculative futures, alternate realities, or scientific premises as central to their nar…
- [[sergei-eisenstein|Sergei Eisenstein]] — Sergei Eisenstein was a Soviet filmmaker and theorist who redefined cinema as a medium of intellectual collision rather than narrative continuity.
- [[soviet-montage|Soviet Montage]] — Soviet montage is a film theory and technique that emerged from 1920s Russian cinema, asserting that meaning is created not within individual shots bu…
- [[television-drama|Television Drama]] — Television drama represents narrative-driven TV series built around character arcs, ongoing conflicts, and serialized storytelling rather than comedy …
- [[typography|Typography]] — Typography is the art and technique of arranging letterforms and text, treating type not merely as a neutral vehicle for language but as a visual and …
- [[visual-metaphor|Visual Metaphor]] — Visual metaphor in cinema uses image, composition, and camera movement to express abstract concepts, emotional states, and thematic meanings without d…
- [[western-film|Western Film]] — Western film encompasses movies set in the American frontier (typically 1865–1900) that explore themes of lawlessness, civilization, masculinity, and …
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
