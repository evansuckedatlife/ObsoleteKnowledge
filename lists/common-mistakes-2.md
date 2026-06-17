---
type: list
category: misc
read: false
---

# common mistakes

The common mistakes most worth knowing for quiz bowl.

## nodes

- [[daniel-shays|Daniel Shays]] — Daniel Shays (1747–1825) was a Massachusetts militia officer and farmer who led a rebellion (1786–1787) against debt…
- [[enharmonic-notes|Enharmonic Notes]] — Enharmonic notes are two different pitch notations that sound identical on a piano or most instruments but have different…
- [[immaculate-conception|Immaculate Conception]] — The Immaculate Conception is the Catholic and Eastern Orthodox Christian doctrine that Mary, the mother of Jesus, was born…
- [[name-order|Name Order]] — Name order refers to the sequence in which given names and family names appear in a person's full name, which varies…
- [[painting-titles|Painting Titles]] — The titling of famous paintings creates confusion because artworks are often known by multiple names—popular titles differ…
- [[revelation-book|Revelation]] — Revelation is the final book of the New Testament, a visionary apocalyptic text attributed to John the Apostle, describing…
- [[the-man-that-corrupted-hadleyburg|The Man That Corrupted Hadleyburg]] — The Man That Corrupted Hadleyburg is a short story (1899) by Mark Twain satirizing small-town American hypocrisy,…
- [[tom-wolfe-thomas-wolfe|Tom Wolfe and Thomas Wolfe]] — Two distinct American authors often confused due to their nearly-identical names: Thomas Wolfe (1900–1938), a Southern…
- [[united-kingdom|United Kingdom]] — The United Kingdom is a political union comprising England, Scotland, Wales, and Northern Ireland.

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
