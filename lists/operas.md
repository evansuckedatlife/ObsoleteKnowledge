---
type: list
category: music
read: false
---

# Operas

The landmark dramatic and comic operas of the Western classical canon, from the High Classical era to the early twentieth century.

## nodes

- [[aida|Aida]] — Radamès and the captive Ethiopian princess Aida are buried alive in ancient Egypt.
- [[boris-godunov|Boris Godunov]] — The guilt-ridden Tsar Boris is tormented by Dmitry's murder and the False Dmitry's rebellion.
- [[carmen|Carmen]] — The soldier Don José is seduced by the gypsy cigarette girl Carmen, leading to tragedy in Seville.
- [[don-giovanni|Don Giovanni]] — Leporello keeps a catalogue of the libertine Don Giovanni's conquests before he is dragged to Hell.
- [[la-boheme|La bohème]] — The seamstress Mimì and the poet Rodolfo fall in love but are separated by poverty and consumption in Paris.
- [[madama-butterfly|Madama Butterfly]] — Cio-Cio-San raising the child Dolore commits suicide after US Lieutenant Pinkerton abandons her.
- [[salome|Salome]] — Salome performs the Dance of the Seven Veils for Herod to demand Jokanaan's severed head.
- [[the-barber-of-seville|The Barber of Seville]] — Figaro helps Count Almaviva woo Rosina and escape her elderly guardian Doctor Bartolo.
- [[the-marriage-of-figaro|The Marriage of Figaro]] — The servants Figaro and Susanna outwit Count Almaviva's attempt to assert the droit du seigneur.
- [[william-tell|William Tell]] — The Swiss patriot William Tell is forced by governor Gessler to shoot an apple off his son's head.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
