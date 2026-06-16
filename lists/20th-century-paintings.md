---
type: list
category: visual-art
read: false
---

# 20th-century paintings

The 20th-century paintings most worth knowing for quiz bowl.

## nodes

- [[american-gothic|American Gothic]] — American Gothic is Grant Wood's 1930 painting of a farmer and his daughter standing before a Gothic Revival farmhouse, their…
- [[black-square|Black Square]] — Black Square is Kazimir Malevich's austere 1915 painting of a pure black square on a white background, representing the…
- [[campbells-soup-cans|Campbell's Soup Cans]] — Campbell's Soup Cans is Andy Warhol's provocative 1962 installation of 32 silk-screened canvases, each depicting a slightly…
- [[composition-with-red-blue-and-yellow|Composition with Red, Blue and Yellow]] — Composition with Red, Blue and Yellow is Piet Mondrian's austere 1921 geometric abstraction comprising primary colors, black…
- [[guernica|Guernica]] — Guernica is Pablo Picasso's monumental 1937 anti-war mural painting depicting the bombing of the Basque town of Guernica…
- [[les-demoiselles-d-avignon|Les Demoiselles d'Avignon]] — Les Demoiselles d'Avignon is Pablo Picasso's groundbreaking 1907 painting that shattered European artistic tradition by…
- [[nighthawks|Nighthawks]] — Nighthawks is Edward Hopper's 1942 quintessential American painting depicting a handful of solitary figures in a late-night…
- [[the-persistence-of-memory|The Persistence of Memory]] — The Persistence of Memory is Salvador Dalí's iconic 1931 Surrealist painting featuring melting pocket watches draped across a…
- [[the-treachery-of-images|The Treachery of Images]] — The Treachery of Images is René Magritte's 1929 conceptual painting depicting a meticulously rendered pipe beneath the French…
- [[the-weeping-woman|The Weeping Woman]] — The Weeping Woman is Pablo Picasso's 1937 portrait of a fragmented female figure with distorted features, clutching a…

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
