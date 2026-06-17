---
type: list
category: history
read: false
---

# spies

The spies most worth knowing for quiz bowl.

## nodes

- [[aldrich-ames|Aldrich Ames]] — Aldrich Ames was a CIA analyst and Moscow station chief who became the most damaging mole in American intelligence history.
- [[benedict-arnold|Benedict Arnold]] — Benedict Arnold was a trusted American general during the Revolutionary War who secretly negotiated with the British to…
- [[julius-and-ethel-rosenberg|Julius and Ethel Rosenberg]] — Julius and Ethel Rosenberg were American Communist spies who passed atomic bomb secrets to the Soviet Union during the Cold War.
- [[kim-philby|Kim Philby]] — Kim Philby was a high-ranking officer in British intelligence who was secretly recruited by Soviet intelligence while at…
- [[klaus-fuchs|Klaus Fuchs]] — Klaus Fuchs was a German-born British physicist who worked on the Manhattan Project and transmitted atomic bomb secrets to the…
- [[mata-hari|Mata Hari]] — Mata Hari was a Dutch exotic dancer and courtesan who became a German spy during World War I, though her true allegiances…
- [[nathan-hale|Nathan Hale]] — Nathan Hale was an American patriot and spy for the Continental Army during the Revolutionary War.
- [[robert-hanssen|Robert Hanssen]] — Robert Hanssen was an FBI counterintelligence officer who spied for the Soviet Union and Russia for over twenty years, making…
- [[the-cambridge-five|The Cambridge Five]] — The Cambridge Five were a ring of British intelligence officers and diplomats who were secretly recruited by Soviet…
- [[virginia-hall|Virginia Hall]] — Virginia Hall was an American intelligence officer and spy who worked for the OSS (Office of Strategic Services) during World…

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
