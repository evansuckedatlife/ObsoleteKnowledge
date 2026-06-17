---
type: list
category: history
read: false
---

# presidential inaugurations

The presidential inaugurations most worth knowing for quiz bowl.

## nodes

- [[andrew-johnson-inauguration|Andrew Johnson's Inauguration]] — Andrew Johnson's assumption of the presidency on April 15, 1865, occurred amid the wreckage of Lincoln's assassination and the…
- [[fdr-first-inauguration|FDR's First Inauguration]] — Franklin Delano Roosevelt's inaugural address on March 4, 1933, occurred at the nadir of the Great Depression, with…
- [[jefferson-first-inauguration|Jefferson's First Inauguration]] — Thomas Jefferson's inauguration on March 4, 1801, occurred during the intensely partisan aftermath of the disputed 1800…
- [[jfk-inauguration|JFK's Inauguration]] — John F.
- [[lincoln-first-inauguration|Lincoln's First Inauguration]] — Abraham Lincoln's inaugural address on March 4, 1861, came as the nation teetered on the brink of dissolution, with seven…
- [[lincoln-second-inauguration|Lincoln's Second Inauguration]] — Abraham Lincoln's second inaugural address on March 4, 1865, stands as one of the greatest political speeches in American…
- [[reagan-inauguration|Reagan's Inauguration]] — Ronald Reagan's inaugural address on January 20, 1981, marked a decisive political realignment toward conservatism and…
- [[theodore-roosevelt-inauguration|Theodore Roosevelt's Inauguration]] — Theodore Roosevelt's second inauguration on March 4, 1905, confirmed his ascent to the presidency in his own right after…
- [[washington-first-inauguration|Washington's First Inauguration]] — George Washington's first inauguration in April 1789 marked the inauguration of the first president of the United States.
- [[william-henry-harrison-inauguration|William Henry Harrison's Inauguration]] — William Henry Harrison's inauguration on March 4, 1841, was the longest presidential inaugural address in American history,…

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
