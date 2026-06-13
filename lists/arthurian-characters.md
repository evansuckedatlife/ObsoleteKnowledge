---
type: list
category: mythology
read: false
---

# Arthurian characters

The knights, ladies, and wizards of the legend of King Arthur and Camelot.

## nodes

- [[galahad|Galahad]] — Sir Galahad stands as the purest and most virtuous knight of the Round Table, destined from birth to achieve what no other…
- [[gawain|Gawain]] — Sir Gawain stands as one of Arthur's most formidable and loyal knights, celebrated for strength that waxes and wanes with the sun.
- [[guinevere|Guinevere]] — Queen of Britain and wife to King Arthur, Guinevere embodies the tragic contradiction between duty and desire.
- [[king-arthur|King Arthur]] — The legendary king of Britain who united the realm and established the Round Table as a symbol of chivalric equality and justice.
- [[lancelot|Lancelot]] — Sir Lancelot du Lac stands as the greatest knight of the Round Table—unmatched in courage and martial prowess—yet his love for…
- [[merlin|Merlin]] — The legendary wizard and advisor to King Arthur, credited with orchestrating Arthur's birth and rise to power through magic…
- [[mordred|Mordred]] — Mordred emerges as the dark shadow of Arthur's reign—a prince of ambiguous parentage whose ambition and betrayal precipitate…
- [[percival|Percival]] — Sir Percival (also Perceval or Parzival) embodies the knight as everyman—humble, flawed, and ultimately enlightened through…
- [[lady-of-the-lake|The Lady of the Lake]] — The Lady of the Lake stands as one of Arthurian legend's most powerful and enigmatic figures—a mystical enchantress dwelling…
- [[tristan-and-iseult|Tristan and Iseult]] — The tragic lovers Tristan and Iseult (also Isolde) represent one of medieval literature's greatest love stories—a passionate…

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
