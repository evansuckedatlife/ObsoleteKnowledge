---
type: list
category: visual-art
read: false
---

# skyscrapers

The skyscrapers most worth knowing for quiz bowl.

## nodes

- [[burj-khalifa|Burj Khalifa]] — The Burj Khalifa is a 828-meter (2,717-foot) supertall skyscraper completed in 2010 in Dubai, holding the record as the…
- [[chrysler-building|Chrysler Building]] — The Chrysler Building is a 77-story Art Deco masterpiece completed in 1930 in Manhattan, rising to 1,046 feet and briefly…
- [[empire-state-building|Empire State Building]] — The Empire State Building is a 102-story Art Deco skyscraper completed in 1931 in Manhattan, rising 1,250 feet to the roof and…
- [[flatiron-building|Flatiron Building]] — The Flatiron Building is a 22-story triangular office building completed in 1902 in Manhattan, located at the intersection of…
- [[home-insurance-building|Home Insurance Building]] — The Home Insurance Building is a ten-story office building completed in 1885 in Chicago, widely recognized as the world's…
- [[one-world-trade-center|One World Trade Center]] — One World Trade Center (also known as the Freedom Tower) is a 94-story supertall skyscraper completed in 2014 in lower…
- [[petronas-towers|Petronas Twin Towers]] — The Petronas Twin Towers are a pair of 88-story skyscrapers completed in 1998 in Kuala Lumpur, Malaysia, each rising 1,482…
- [[shanghai-tower|Shanghai Tower]] — The Shanghai Tower is a 128-story supertall skyscraper completed in 2015 in Shanghai, China, rising 2,073 feet and currently…
- [[taipei-101|Taipei 101]] — Taipei 101 is a 101-story supertall skyscraper completed in 2004 in Taipei, Taiwan, rising 1,667 feet and holding the world's…
- [[willis-tower|Willis Tower]] — The Willis Tower (formerly the Sears Tower) is a 110-story skyscraper completed in 1973 in Chicago, rising 1,450 feet and…

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
