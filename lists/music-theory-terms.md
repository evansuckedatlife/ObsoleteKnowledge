---
type: list
category: music
read: false
---

# music theory terms

The music theory terms most worth knowing for quiz bowl.

## nodes

- [[cadence|Cadence]] — A cadence is a concluding harmonic phrase that signals the end of a musical phrase, section, or entire piece.
- [[circle-of-fifths|Circle of Fifths]] — The circle of fifths is a geometric diagram organizing all twelve pitches (in their major and minor keys) in a circle, ordered…
- [[counterpoint|Counterpoint]] — Counterpoint is the art of combining two or more independent melodic lines that sound simultaneously, each with its own…
- [[fugue|Fugue]] — A fugue is a polyphonic composition where two or more voices develop the same thematic material (the subject) through…
- [[key-signature|Key Signature]] — A key signature is a set of sharps or flats written at the beginning of a staff, immediately after the clef, that identifies…
- [[leitmotif|Leitmotif]] — A leitmotif (German: "leading motif") is a recurring melodic or harmonic phrase associated with a particular character, idea,…
- [[modulation|Modulation]] — Modulation is the act of changing from one key to another within a piece of music, creating harmonic variety and narrative…
- [[polyphony|Polyphony]] — Polyphony is the texture of simultaneous independent melodic lines, each with its own rhythmic and pitch identity, that…
- [[sonata-form|Sonata Form]] — Sonata form is the most important structural principle in instrumental music since the Classical period, organizing a movement…
- [[syncopation|Syncopation]] — Syncopation is the displacement of normal metrical accent, placing emphasis on weak beats or off-beats, creating rhythmic…

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
