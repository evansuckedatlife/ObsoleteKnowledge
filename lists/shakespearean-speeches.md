---
type: list
category: literature
read: false
---

# Shakespearean speeches, monologues, and soliloquies

The Shakespearean speeches, monologues, and soliloquies most worth knowing for quiz bowl.

## nodes

- [[all-the-worlds-a-stage|All the world's a stage]] — Jacques's meditation on the seven ages of human life, spoken in As You Like It as he observes the world as a stage and all…
- [[friends-romans-countrymen|Friends, Romans, countrymen]] — Mark Antony's funeral oration for Julius Caesar, a masterpiece of rhetorical manipulation in Julius Caesar.
- [[is-this-a-dagger-which-i-see-before-me|Is this a dagger which I see before me]] — Macbeth's soliloquy immediately before murdering King Duncan, in which he confronts a vision of a floating dagger—real or…
- [[now-is-the-winter-of-our-discontent|Now is the winter of our discontent]] — Richard III's opening soliloquy, in which the deformed, ambitious duke announces his intention to manipulate, seduce, and…
- [[once-more-unto-the-breach|Once more unto the breach]] — King Henry V's rallying cry to his soldiers as they assault the breach in the walls of Harfleur, demanding they harden their…
- [[st-crispins-day|Saint Crispin's Day speech]] — King Henry V's rousing address to his outnumbered troops before the Battle of Agincourt, transforming despair into glory by…
- [[the-quality-of-mercy|The quality of mercy]] — Portia's eloquent appeal to Shylock to show mercy in The Merchant of Venice, delivered in the courtroom as Antonio faces the…
- [[to-be-or-not-to-be|To be or not to be]] — The most celebrated soliloquy in English literature, spoken by Hamlet as he contemplates suicide while wrestling with inaction…
- [[tomorrow-and-tomorrow-and-tomorrow|Tomorrow and tomorrow and tomorrow]] — Macbeth's bleak soliloquy after learning of Lady Macbeth's death, in which he articulates the meaninglessness of life and the…
- [[what-a-piece-of-work-is-a-man|What a piece of work is a man]] — Hamlet's eloquent meditation on human dignity and potential in Hamlet, in which he praises mankind as "noble in reason,"…

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
