---
type: list
category: history
read: false
---

# American murders and murderers

The American murders and murderers most worth knowing for quiz bowl.

## nodes

- [[black-dahlia|Black Dahlia]] — In January 1947, the mutilated body of 22-year-old Elizabeth Short, an aspiring actress in Los Angeles, was discovered in a…
- [[clutter-family-murders|Clutter Family Murders]] — On November 15, 1959, the Clutter family—a wealthy, respected Kansas farming family—were murdered in their home by two…
- [[hall-mills-case|Hall-Mills Case]] — In September 1922, the bodies of Reverend Edward Hall and his lover Eleanor Mills, a choir singer, were found murdered on a…
- [[harry-thaw-stanford-white|Harry Thaw Murder of Stanford White]] — In June 1906, wealthy rail heir Harry Thaw shot and killed renowned architect Stanford White in a public venue over the…
- [[leopold-and-loeb|Leopold and Loeb]] — In 1924, two wealthy Chicago teenagers, Nathan Leopold and Richard Loeb, murdered 14-year-old Bobby Franks in what they…
- [[lindbergh-kidnapping|Lindbergh Kidnapping]] — In March 1932, the 20-month-old son of aviator Charles Lindbergh was abducted from his New Jersey home; despite a ransom…
- [[lizzie-borden|Lizzie Borden]] — In August 1892, two people were killed with an axe in their Fall River, Massachusetts home: Andrew Borden and his wife Abby.
- [[manson-family-murders|Manson Family Murders]] — In August 1969, members of a cult led by Charles Manson committed a series of murders in the Los Angeles area, killing eight…
- [[sacco-and-vanzetti|Sacco and Vanzetti]] — In May 1920, Nicola Sacco and Bartolomeo Vanzetti, Italian immigrant anarchists, were arrested for a payroll robbery and…
- [[sam-sheppard-case|Sam Sheppard Case]] — In July 1954, Marilyn Sheppard, the pregnant wife of osteopathic surgeon Sam Sheppard, was brutally murdered in their suburban…

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
