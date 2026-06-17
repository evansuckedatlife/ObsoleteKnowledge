---
type: list
category: pop-culture
read: false
---

# sandbox and open-world video games

The sandbox and open-world video games most worth knowing for quiz bowl.

## nodes

- [[grand-theft-auto-v|Grand Theft Auto V]] — Grand Theft Auto V is a crime-sandbox developed by Rockstar Games, released in 2013 and set in the sprawling fictional…
- [[minecraft|Minecraft]] — Minecraft is a sandbox survival game released by Mojang in 2011 where players explore infinitely procedurally generated…
- [[no-mans-sky|No Man's Sky]] — No Man's Sky is a space exploration sandbox developed by Hello Games, released in 2016 for PC and PlayStation 4.
- [[red-dead-redemption-2|Red Dead Redemption 2]] — Red Dead Redemption 2 is an open-world Western developed by Rockstar Games, released in 2018 for PlayStation 4 and Xbox One.
- [[stardew-valley|Stardew Valley]] — Stardew Valley is a pastoral sandbox developed by Eric Barone and released in 2016 for PC, later ported to numerous platforms.
- [[subnautica|Subnautica]] — Subnautica is an underwater survival sandbox developed by Unknown Worlds Entertainment, released in early access in 2014 and…
- [[terraria|Terraria]] — Terraria is a 2D sandbox survival game developed by Re-Logic, released in 2011 for PC.
- [[skyrim|The Elder Scrolls V: Skyrim]] — The Elder Scrolls V: Skyrim is a fantasy role-playing game developed by Bethesda Game Studios, released in 2011 for…
- [[breath-of-the-wild|The Legend of Zelda: Breath of the Wild]] — The Legend of Zelda: Breath of the Wild is an action-adventure game developed by Nintendo, released in 2017 for Nintendo…
- [[the-witcher-3-wild-hunt|The Witcher 3: Wild Hunt]] — The Witcher 3: Wild Hunt is an action role-playing game developed by CD Projekt Red, released in 2015 for PC, PlayStation 4,…

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
