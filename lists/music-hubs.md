---
type: list
category: music
read: false
---

# Music hubs

Forms, eras and concepts underlying the individual composers and works.

## nodes

- [[bach|Johann Sebastian Bach]] — Johann Sebastian Bach (1685–1750) was a German Baroque composer and organist whose mastery of counterpoint and fugal form stands unmatched in Western …
- [[bali|Bali]] — Bali is an Indonesian island and province known for its distinctive cultural traditions, particularly its music and performance arts.
- [[baritone|Baritone]] — A baritone is a male singing voice ranging roughly from the A below middle C to the A one octave above, sitting between the higher tenor and the lower…
- [[bel-canto-opera|Bel Canto Opera]] — Bel canto (Italian: "beautiful singing") refers to an operatic tradition and vocal aesthetic emphasizing pure, elegant melody and brilliant vocal tech…
- [[canon|Canon]] — In music, a canon is a polyphonic compositional form in which two or more voices enter successively, each singing or playing the same melodic line at …
- [[castrato|Castrato]] — A castrato (plural: castrati) is a male singer castrated before puberty to preserve a high, soprano or alto register while retaining the physical stre…
- [[catholic-liturgy|Catholic Liturgy]] — Catholic liturgy refers to the formal worship practices of the Roman Catholic Church, centered on the Mass—a ritualistic reenactment and commemoration…
- [[chapel-royal|Chapel Royal]] — The Chapel Royal is the collective name for the royal chapel institutions of the English monarchy, most prominently at the palaces of Westminster and …
- [[classical-music|Classical Music]] — Classical music refers to the musical period and aesthetic that emerged in the mid-18th century as a reaction against the complexity and ornamentation…
- [[cool-jazz|Cool Jazz]] — Cool jazz emerged in the late 1940s as a deliberate reaction against bebop's frenetic intensity and harmonic complexity.
- [[count-basie|Count Basie]] — Count Basie (1904–1984), born William James Basie, was an American pianist and bandleader whose orchestra became one of the defining engines of the sw…
- [[donizetti|Gaetano Donizetti]] — Gaetano Donizetti (1797–1848) was an Italian composer and master of the bel canto vocal tradition, one of the most prolific opera composers of the 19t…
- [[gregorian-mode|Gregorian Mode]] — Gregorian modes (also called church modes or ecclesiastical modes) are a system of eight melodic scales used in Gregorian chant and medieval liturgica…
- [[harmony|Harmony]] — Harmony refers to the combination of simultaneous notes and the system governing which note combinations create coherence, tension, and resolution in …
- [[indian-music|Indian Music]] — Indian classical music encompasses two major regional traditions: Hindustani (North Indian) and Carnatic (South Indian), each with distinct histories,…
- [[leoncavallo|Ruggero Leoncavallo]] — Ruggero Leoncavallo was an Italian composer central to the verismo movement, which brought stark realism to the opera stage.
- [[literature|Literature and Music]] — Literature and music have been intertwined since antiquity, but operatic composers from the 18th century onward made literary adaptation a central cre…
- [[liturgical-music|Liturgical Music]] — Liturgical music encompasses all musical compositions created for use in religious services and worship.
- [[luciano-pavarotti|Luciano Pavarotti]] — Luciano Pavarotti was an Italian tenor whose extraordinary voice and charismatic stage presence made him the most famous opera singer of the late twen…
- [[major-minor-tonality|Major-Minor Tonality]] — Major-minor tonality is the system of organizing pitch and harmony that dominated Western music from roughly 1650 to 1900 and persists widely today.
- [[medieval-drama|Medieval Drama]] — Medieval drama emerged from the church's need to make scripture vivid and memorable to illiterate congregations.
- [[medieval-music|Medieval Music]] — Medieval music encompasses the musical traditions of Europe from roughly the 6th to the 15th centuries, a period defined by the dominance of the Catho…
- [[mezzo-soprano|Mezzo-Soprano]] — Mezzo-soprano (literally "half-soprano" in Italian) is the female voice type between soprano and alto, commanding a warm, robust middle-to-lower range…
- [[modal-music|Modal Music]] — Modal music is a system of melody and improvisation organized around modes—recurring melodic and harmonic frameworks distinct from Western major and m…
- [[mozart|Wolfgang Amadeus Mozart]] — Wolfgang Amadeus Mozart was an Austrian composer who, in his tragically short life of thirty-five years, created a body of work unmatched in its scope…
- [[opera-buffa|Opera Buffa]] — Opera buffa is a comic operatic form that flourished in 18th and 19th-century Italy, characterized by witty, often farcical plots, popular appeal, and…
- [[roman-numeral-analysis|Roman Numeral Analysis]] — Roman numeral analysis is the standard notational system for identifying chords and their harmonic functions within a tonal key.
- [[romantic-era|Romantic Era]] — The Romantic era (roughly 1820–1900) in music and dance was a period of revolutionary expansion: composers and choreographers pursued emotional intens…
- [[rossini|Gioachino Rossini]] — Gioachino Rossini was an Italian composer who, in the early nineteenth century, became the defining voice of comic opera and a founder of bel canto, t…
- [[sacred-music|Sacred Music]] — Sacred music encompasses all compositions created for worship, prayer, and spiritual contemplation across religions and cultures.
- [[soprano|Soprano]] — Soprano is the highest standard female voice classification in Western classical and operatic music, characterized by brightness, agility, and project…
- [[tabla|Tabla]] — The tabla is a pair of hand drums central to Indian classical music, consisting of a smaller, higher-pitched drum (dayan) and a larger, lower-pitched …
- [[verismo-opera|Verismo Opera]] — Verismo opera is an operatic movement that emerged in late 19th-century Italy, emphasizing realism, contemporary settings, and raw emotional directnes…

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
