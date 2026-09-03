---
type: list
category: pop-culture
read: false
---

# Pop Culture hubs

Formats, genres and phenomena the individual titles belong to.

## nodes

- [[1930s-cinema|1930s Cinema]] — 1930s cinema marks the transition from silent to sound film and the artistic and commercial maturation of the medium during the Great Depression.
- [[alfred-hitchcock|Alfred Hitchcock]] — Alfred Hitchcock was a British-American film director who redefined the thriller genre and became synonymous with suspense cinema.
- [[american-cinema|American Cinema]] — American cinema refers to the body of films produced in the United States, and especially the industrial and artistic dominance of Hollywood from the …
- [[billy-wilder|Billy Wilder]] — Billy Wilder was an Austrian-American film director and screenwriter who became one of Hollywood's most versatile and acclaimed filmmakers of the mid-…
- [[camera-movement|Camera Movement]] — Camera movement refers to the deliberate motion of the film camera — pans, tilts, tracking shots, zooms, and crane movements — used to guide the viewe…
- [[cinematography|Cinematography]] — Cinematography is the art and craft of making movies—the technical and creative choices that define what the camera captures.
- [[counter-strike|Counter-Strike]] — Counter-Strike is a team-based tactical first-person shooter developed by Valve, originally released as a Half-Life mod in 2000 before becoming a stan…
- [[documentary-cinema|Documentary Cinema]] — Documentary cinema is filmmaking that purports to record reality rather than fiction—to document actual events, people, and places.
- [[doom|Doom]] — Doom (1993) is the seminal first-person shooter that defined the genre's core grammar: run, aim, shoot, advance.
- [[esports|Esports]] — Esports encompasses competitive video gaming organized at professional, televised, and international scales.
- [[everyman-hero|Everyman Hero]] — The everyman hero is a foundational narrative archetype of american-cinema that emerged prominently during the Great Depression through the populist f…
- [[film-editing|Film Editing]] — Film editing is the art of assembling shot sequences into a coherent narrative and emotional experience.
- [[first-person-shooter|First-Person Shooter]] — First-person shooter (FPS) is a video game genre defined by gameplay presented from the player's perspective looking through the protagonist's eyes, w…
- [[frank-capra|Frank Capra]] — Frank Capra was an Italian-American director who championed the moral courage of ordinary people against institutional corruption and social indiffere…
- [[frontier|Frontier]] — The frontier in pop-culture is the mythological space where civilization meets wilderness and law must be imposed through courage and violence.
- [[golden-age-of-hollywood|Golden Age of Hollywood]] — The Golden Age of Hollywood, often called Classical Hollywood cinema, was a transformative era of American filmmaking spanning from the late 1920s rel…
- [[gunslinger-archetype|Gunslinger Archetype]] — The gunslinger archetype represents the iconic mythical figure of the American frontier in western-film and folklore: a lethal, laconic drifter whose …
- [[industrialization|Industrialization]] — Industrialization is the transformation of economic production from craft and agriculture to machine-based factory systems, and its profound cultural,…
- [[james-stewart|James Stewart]] — James Stewart was an American actor and military pilot who became one of Hollywood's most beloved stars through his portrayal of ordinary, decent men …
- [[laurel-and-hardy|Laurel and Hardy]] — Laurel and Hardy were a British-American comedy duo consisting of Stan Laurel and Oliver Hardy, whose partnership from 1926 through the 1940s became t…
- [[marilyn-monroe|Marilyn Monroe]] — Marilyn Monroe, born Norma Jeane Mortenson (later baptized Norma Jeane Baker), was a mid-twentieth-century actress, model, and singer who became the q…
- [[mise-en-scene|Mise-en-scène]] — Mise-en-scène refers to everything placed before the camera: set design, actor positioning, lighting, props, and composition within the frame.
- [[montage|Montage]] — Montage is the cinematic technique of selecting, editing, and piecing together separate sections of film to form a continuous whole, generating meanin…
- [[mystery-television|Mystery Television]] — Mystery television encompasses dramatic series structured around criminal investigation, suspense, and revelation.
- [[narrative-cinema|Narrative Cinema]] — Narrative cinema is filmmaking that tells a story through visual and temporal sequencing—the techniques by which cinema makes meaning from shots, scen…
- [[nintendo|Nintendo]] — Nintendo is a Japanese entertainment company founded in 1889 that evolved into one of the world's most influential video game publishers.
- [[photojournalism|Photojournalism]] — Photojournalism is the journalistic and artistic practice of visual reporting that uses photographic images to document news events, historical crises…
- [[populism|Populism]] — Populism is a political and cultural impulse built on faith in "the people" and distrust of elites—institutions, experts, and the powerful.
- [[psychological-drama|Psychological Drama]] — Psychological drama is cinema (and theater) focused on the inner emotional and mental life of characters—their fears, desires, traumas, and moral conf…
- [[romance|Romance]] — Romance is a narrative genre centered on the emotional and often physical relationship between two or more characters, typically culminating in commit…
- [[science-fiction-television|Science-Fiction Television]] — Science-fiction television encompasses TV series that explore speculative futures, alternate realities, or scientific premises as central to their nar…
- [[screwball-comedy|Screwball Comedy]] — Screwball comedy is a film genre dominated by rapid-fire dialogue, romantic chaos, and class conflict; it emerged in the 1930s and flourished through …
- [[sergei-eisenstein|Sergei Eisenstein]] — Sergei Eisenstein was a Soviet filmmaker and theorist who redefined cinema as a medium of intellectual collision rather than narrative continuity.
- [[soviet-montage|Soviet Montage]] — Soviet montage is a film theory and technique that emerged from 1920s Russian cinema, asserting that meaning is created not within individual shots bu…
- [[streaming-culture|Streaming Culture]] — Streaming culture encompasses the social practices, interactive entertainment ecosystems, and digital communities centered on the live broadcasting of…
- [[television-drama|Television Drama]] — Television drama represents narrative-driven TV series built around character arcs, ongoing conflicts, and serialized storytelling rather than comedy …
- [[typography|Typography]] — Typography is the art and technique of arranging letterforms and text, treating type not merely as a neutral vehicle for language but as a visual and …
- [[video-game-genre|Video Game Genre]] — Video game genre is the classification system for games based on gameplay mechanics, player objectives, and experiential focus.
- [[video-game-industry|Video Game Industry]] — The video game industry is the global ecosystem of companies, creators, and business models that produce, distribute, and monetize games.
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
