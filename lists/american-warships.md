---
type: list
category: history
read: false
---

# American warships

The American warships most worth knowing for quiz bowl.

## nodes

- [[css-virginia|CSS Virginia]] — CSS Virginia, the Confederate ironclad built from the salvaged hull of the Union frigate USS Merrimack, devastated Union…
- [[uss-arizona|USS Arizona]] — USS Arizona (BB-39), a Pennsylvania-class battleship, sank in 102 seconds during the Japanese attack on Pearl Harbor on…
- [[uss-constellation|USS Constellation]] — USS Constellation (CV-64), a Kitty Hawk-class aircraft carrier commissioned in 1961, served through the Vietnam War and Cold…
- [[uss-constitution|USS Constitution]] — USS Constitution, the oldest naval vessel still in commission, is a 44-gun wooden frigate launched in 1797 that earned the…
- [[uss-enterprise-cv-6|USS Enterprise (CV-6)]] — USS Enterprise (CV-6), the legendary Yorktown-class aircraft carrier nicknamed "Big E," was the most-decorated ship of World…
- [[uss-indianapolis|USS Indianapolis]] — USS Indianapolis (CA-35), a heavy cruiser, sank on July 30, 1945, after delivering atomic bomb components to Tinian Island…
- [[uss-maine|USS Maine]] — USS Maine, an American armored cruiser that exploded in Havana harbor in February 1898, became the catalyst for the…
- [[uss-missouri|USS Missouri]] — USS Missouri (BB-63), the last Iowa-class battleship, served as the flagship where Japan formally surrendered on September 2,…
- [[uss-monitor|USS Monitor]] — USS Monitor was the first ironclad warship built for the Union Navy, a revolutionary vessel with a rotating gun turret and low…
- [[uss-nautilus|USS Nautilus]] — USS Nautilus (SSN-571), the world's first nuclear-powered submarine, launched in 1954 and revolutionized undersea warfare with…

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
