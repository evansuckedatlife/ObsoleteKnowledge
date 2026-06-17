---
type: list
category: literature
read: false
---

# Shakespearean villains

The Shakespearean villains most worth knowing for quiz bowl.

## nodes

- [[aaron-the-moor|Aaron the Moor]] — Aaron is the moor in Shakespeare's Titus Andronicus, a sadistic servant and lover of the queen who orchestrates a cascade of…
- [[claudius-hamlet|Claudius]] — Claudius, King of Denmark, is the regicidal uncle who murders his brother (Prince Hamlet's father) with poison, marries the…
- [[don-john|Don John]] — Don John, the illegitimate brother of the Prince of Aragon, is a malcontent plotter whose sole ambition is to disrupt the…
- [[edmund|Edmund]] — Edmund, the bastard son of the Earl of Gloucester, is a schemer who exploits his illegitimate status as an excuse for…
- [[goneril|Goneril]] — Goneril, the eldest daughter of King Lear, is a ruthless, ambitious woman who begins the play by falsely professing limitless…
- [[iago|Iago]] — Iago is the master manipulator of Othello, a military ensign who destroys a general and his beloved wife through calculated…
- [[lady-macbeth|Lady Macbeth]] — Lady Macbeth is Macbeth's wife and the architect of Duncan's murder, a woman of steel who suppresses her own humanity to drive…
- [[macbeth|Macbeth]] — Macbeth is the ambitious Scottish thane whose murders transform him from a celebrated warrior into a paranoid tyrant.
- [[regan|Regan]] — Regan, the younger of King Lear's two cruel daughters, matches her sister Goneril in callousness but surpasses her in pure…
- [[richard-iii|Richard III]] — Richard III, the hunchbacked Duke of Gloucester, is Shakespeare's most self-aware villain—a man who owns his malevolence even…

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
