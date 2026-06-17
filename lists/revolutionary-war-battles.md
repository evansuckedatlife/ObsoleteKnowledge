---
type: list
category: history
read: false
---

# Revolutionary War battles

The Revolutionary War battles most worth knowing for quiz bowl.

## nodes

- [[battle-of-brandywine|Brandywine]] — On September 11, 1777, British general William Howe outmaneuvered George Washington's Continental Army near Brandywine Creek…
- [[bunker-hill|Bunker Hill]] — On June 17, 1775, American militia fortified Breed's Hill (near Bunker Hill) overlooking Boston Harbor.
- [[battle-of-cowpens|Cowpens]] — On January 17, 1781, American general Daniel Morgan defeated British cavalry colonel Banastre Tarleton at the Cowpens, South…
- [[lexington-and-concord|Lexington and Concord]] — On April 19, 1775, British regulars marched from Boston to seize colonial munitions stored in Concord, Massachusetts.
- [[battle-of-long-island|Long Island]] — On August 27, 1776, the first major engagement of the Revolutionary War saw British general William Howe crush an American…
- [[battle-of-monmouth|Monmouth]] — On June 28, 1778, the Continental Army and British forces clashed at Monmouth Courthouse, New Jersey.
- [[battle-of-princeton|Princeton]] — On January 3, 1777, George Washington's Continental Army routed a British force at Princeton, New Jersey.
- [[battle-of-saratoga|Saratoga]] — In September-October 1777, American forces commanded by Horatio Gates defeated British general John Burgoyne's army near…
- [[battle-of-trenton|Trenton]] — On December 26, 1776, after a devastating campaign and retreat across New Jersey, George Washington led approximately 2,400…
- [[battle-of-yorktown|Yorktown]] — In September-October 1781, American and French forces under George Washington surrounded British general Lord Cornwallis at…

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
