---
type: list
category: religion
read: false
---

# New Testament characters

Key figures of the New Testament surrounding Jesus and the early Church.

## nodes

- [[john-the-apostle|John the Apostle]] — One of Jesus's twelve apostles and traditionally credited with authoring the Gospel of John, the Epistles of John, and the…
- [[john-the-baptist|John the Baptist]] — A Jewish preacher who baptized people as a sign of repentance and is best known for baptizing Jesus in the River Jordan.
- [[judas-iscariot|Judas Iscariot]] — One of the twelve apostles of Jesus who became notorious for betraying Jesus to the religious authorities in exchange for…
- [[lazarus|Lazarus]] — A friend of Jesus from the village of Bethany who died and was raised from the dead by Jesus in one of the most dramatic…
- [[mary-magdalene|Mary Magdalene]] — A devoted follower of Jesus often identified as the first witness to the Resurrection.
- [[paul|Paul]] — Originally Saul of Tarsus, a persecutor of early Christians who underwent a dramatic conversion on the road to Damascus after…
- [[peter|Peter]] — One of Jesus's most prominent apostles, originally a fisherman named Simon who became the rock upon which Jesus built his church.
- [[pontius-pilate|Pontius Pilate]] — The Roman prefect of Judea who presided over Jesus's trial and ultimately authorized his crucifixion.
- [[thomas|Thomas]] — One of the twelve apostles of Jesus, best known for his skepticism about the Resurrection until he encountered the risen Jesus…
- [[virgin-mary|Virgin Mary]] — The mother of Jesus, revered in Christian tradition as the Virgin Mary because she conceived Jesus while remaining a virgin.

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
