---
type: list
category: visual-art
read: false
---

# early 20th-century art movements

The early 20th-century art movements most worth knowing for quiz bowl.

## nodes

- [[abstract-expressionism|Abstract Expressionism]] — Abstract Expressionism was an American art movement (roughly 1943–1960s) that combined abstraction's non-representational form…
- [[bauhaus|Bauhaus]] — Bauhaus (Building House) was a German design school and movement (1919–1933) that unified art, craft, and industrial design…
- [[constructivism|Constructivism]] — Constructivism was a Soviet avant-garde movement (1915–1930s) that rejected "art for art's sake" and instead deployed…
- [[cubism|Cubism]] — Cubism is an early-20th-century revolutionary art movement that deconstructed forms into geometric shapes and multiple…
- [[dada|Dada]] — Dada was an anti-art, anarchist movement born during World War I (roughly 1916–1924) that rejected reason, logic, and…
- [[de-stijl|De Stijl]] — De Stijl (The Style) was a Dutch art movement (1917–1931) that pursued universal harmony through pure geometric abstraction,…
- [[expressionism|Expressionism]] — Expressionism was an early-20th-century movement (1905–1925, with roots earlier) that prioritized subjective emotion and inner…
- [[fauvism|Fauvism]] — Fauvism was a short-lived but electrifying early-20th-century movement (1905–1910) that liberated color from descriptive…
- [[futurism|Futurism]] — Futurism was an Italian movement (1909–1944) that celebrated speed, machinery, violence, and modernity as antidotes to what…
- [[surrealism|Surrealism]] — Surrealism emerged in the 1920s as a movement devoted to unleashing the unconscious mind, drawing on Freudian psychoanalysis…

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
