---
type: list
category: history
read: false
---

# Revolutionary War generals

The Revolutionary War generals most worth knowing for quiz bowl.

## nodes

- [[anthony-wayne|Anthony Wayne]] — Anthony Wayne, nicknamed "Mad Anthony" for his fearlessness and aggressive tactics, was one of the Continental Army's most…
- [[baron-von-steuben|Baron von Steuben]] — Baron Friedrich von Steuben was a Prussian officer who arrived at Valley Forge in 1778 and transformed the Continental Army…
- [[benedict-arnold|Benedict Arnold]] — Benedict Arnold was a trusted American general during the Revolutionary War who secretly negotiated with the British to…
- [[charles-cornwallis|Charles Cornwallis]] — Charles Cornwallis was the senior British general in the later stages of the American Revolution and the commander of British…
- [[george-washington|George Washington]] — George Washington was the commander-in-chief of the Continental Army and the central figure of the American Revolution.
- [[henry-knox|Henry Knox]] — Henry Knox rose from a Boston bookseller to become the chief artillery officer of the Continental Army and one of the war's…
- [[horatio-gates|Horatio Gates]] — Horatio Gates was a British-born officer who became a major American general and won the pivotal victory at Saratoga in 1777,…
- [[marquis-de-lafayette|Marquis de Lafayette]] — The Marquis de Lafayette (1757–1834), born Gilbert du Motier, was a noble reformer and military hero who championed both the…
- [[nathanael-greene|Nathanael Greene]] — Nathanael Greene was the commander of the Continental Army's southern department and one of the war's most brilliant strategists.
- [[william-howe|William Howe]] — William Howe was the commander-in-chief of British forces during the pivotal years of the American Revolution (1775–1778),…

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
