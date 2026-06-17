---
type: list
category: music
read: false
---

# arias

The arias most worth knowing for quiz bowl.

## nodes

- [[casta-diva|Casta diva]] — Casta diva (Chaste goddess) is the solemn, ethereal soprano aria sung by Norma, the high priestess, in Vincenzo Bellini's…
- [[che-gelida-manina|Che gelida manina]] — Che gelida manina (What a cold little hand) is the achingly tender tenor aria sung by Rodolfo in Act I of Giacomo Puccini's…
- [[der-holle-rache|Der Hölle Rache]] — Der Hölle Rache kocht in meinem Herzen (Hell's vengeance boils in my heart) is the infamous coloratura soprano aria sung by…
- [[habanera|Habanera]] — The Habanera (Love is a rebel bird) is the seductive entrance aria sung by Carmen in Act I of Georges Bizet's opera Carmen.
- [[la-donna-e-mobile|La donna è mobile]] — La donna è mobile (Woman is fickle) is the swaggering tenor aria sung by the Duke of Mantua in Act III of Giuseppe Verdi's…
- [[largo-al-factotum|Largo al factotum]] — Largo al factotum (Make way for the factotum) is the swaggering baritone aria sung by Figaro in Act I of Gioachino Rossini's…
- [[nessun-dorma|Nessun dorma]] — Nessun dorma (None shall sleep) is the triumphant final aria sung by Prince Calàf in Giacomo Puccini's opera Turandot.
- [[o-mio-babbino-caro|O mio babbino caro]] — O mio babbino caro (Oh my dear father) is the tender soprano aria sung by Lauretta in Giacomo Puccini's one-act comic opera…
- [[una-furtiva-lagrima|Una furtiva lagrima]] — Una furtiva lagrima (A furtive tear) is the rapturous tenor aria sung by Nemorino in Gaetano Donizetti's comic opera L'elisir…
- [[vesti-la-giubba|Vesti la giubba]] — Vesti la giubba (Put on the costume) is the heart-wrenching tenor aria sung by Canio in Ruggero Leoncavallo's opera Pagliacci…

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
