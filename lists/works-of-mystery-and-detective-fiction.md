---
type: list
category: literature
read: false
---

# works of mystery and detective fiction

The works of mystery and detective fiction most worth knowing for quiz bowl.

## nodes

- [[and-then-there-were-none|And Then There Were None]] — Agatha Christie's 1939 novel is considered her masterpiece: ten strangers are lured to an island, each accused of a past…
- [[gaudy-night|Gaudy Night]] — Dorothy L.
- [[in-cold-blood|In Cold Blood]] — Truman Capote's 1966 novel is a true-crime narrative account of the 1959 murder of a Kansas farm family and the investigation…
- [[murder-on-the-orient-express|Murder on the Orient Express]] — Agatha Christie's 1934 novel features detective Hercule Poirot aboard a snowbound luxury train where a wealthy American is…
- [[the-adventures-of-sherlock-holmes|The Adventures of Sherlock Holmes]] — Arthur Conan Doyle's 1892 collection of twelve short stories featuring detective Sherlock Holmes and his companion Dr.
- [[the-big-sleep|The Big Sleep]] — Raymond Chandler's 1939 debut novel introduces Philip Marlowe, a Los Angeles private detective hired by an ailing millionaire…
- [[the-final-problem|The Final Problem]] — Arthur Conan Doyle's 1893 short story in which Sherlock Holmes pursues his nemesis, Professor Moriarty, to the edge of a Swiss…
- [[the-hound-of-the-baskervilles|The Hound of the Baskervilles]] — Arthur Conan Doyle's 1901–1902 serial novel in which Sherlock Holmes investigates a family curse on the English moors—the…
- [[the-maltese-falcon|The Maltese Falcon]] — Dashiell Hammett's 1930 novel introduces Sam Spade, a hard-boiled San Francisco private detective caught in a tangle of lies…
- [[the-moonstone|The Moonstone]] — Wilkie Collins's 1868 novel, considered the first detective novel in English literature, centers on the theft of a valuable…
- [[the-murders-in-the-rue-morgue|The Murders in the Rue Morgue]] — Edgar Allan Poe's 1841 short story about a seemingly impossible double murder in Paris—a mother and daughter killed in a…
- [[the-name-of-the-rose|The Name of the Rose]] — Umberto Eco's 1980 novel is a sophisticated mystery set in a medieval monastery where a series of seemingly unrelated deaths…
- [[the-purloined-letter|The Purloined Letter]] — Edgar Allan Poe's 1844 short story in which C.

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
