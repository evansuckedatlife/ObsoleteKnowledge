---
type: list
category: history
read: false
---

# historical fashions

The historical fashions most worth knowing for quiz bowl.

## nodes

- [[bustle|Bustle]] — The bustle is a framework of steel hoops, petticoats, or padding worn beneath skirts at the rear to create projection and…
- [[codpiece|Codpiece]] — The codpiece is a covering or protrusion added to the front of men's breeches or hose, worn from the 15th through 17th centuries.
- [[corset|Corset]] — The corset is a rigid undergarment designed to shape the torso, particularly to create a pronounced waistline and support the…
- [[crinoline|Crinoline]] — The crinoline is a stiffened petticoat or hoop skirt made of horsehair fabric or flexible steel hoops, worn primarily from the…
- [[farthingale|Farthingale]] — The farthingale is a hooped or structured petticoat that creates a distinctive bell-shaped or cone-shaped silhouette in…
- [[flapper-dress|Flapper Dress]] — The flapper dress is a loose, straight, knee-length or shorter dress worn primarily by young women in the 1920s, embodying a…
- [[peruke|Peruke]] — The peruke (or periwig), a full-bottomed wig made of human or animal hair and often dusted with white or colored powder,…
- [[ruff|Ruff]] — The ruff is an elaborate circular or standing collar made of stiffened linen, worn from the late 16th through early 17th…
- [[toga|Toga]] — The toga is a draped woolen garment worn by male Roman citizens as the formal dress of state, consisting of a large piece of…
- [[zoot-suit|Zoot Suit]] — The zoot suit is a flashy men's outfit featuring high-waisted, wide-legged, tapered trousers and a long coat with wide lapels…

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
