---
type: list
category: literature
read: false
---

# plot twists

The plot twists most worth knowing for quiz bowl.

## nodes

- [[1984-ending-twist|1984 (Ending Twist)]] — George Orwell's 1984 chronicles the life of Winston Smith in a totalitarian superstate ruled by the Party, where truth,…
- [[an-occurrence-at-owl-creek-bridge|An Occurrence at Owl Creek Bridge]] — Ambrose Bierce's An Occurrence at Owl Creek Bridge is a short story set during the American Civil War, depicting a condemned…
- [[citizen-kane-twist|Citizen Kane]] — Orson Welles' Citizen Kane is a landmark film that chronicles the rise and fall of Charles Foster Kane, a newspaper magnate…
- [[fight-club-twist|Fight Club]] — Fight Club is a 1999 novel (and film adaptation) in which an unnamed office worker befriends the charismatic Tyler Durden and…
- [[jane-eyre-twist|Jane Eyre]] — Charlotte Brontë's Jane Eyre follows an orphaned governess who falls in love with her employer, the brooding Mr.
- [[oedipus-rex|Oedipus Rex]] — Oedipus Rex is Sophocles' masterpiece tragedy, performed around 429 BCE, examining fate, knowledge, and the limits of human…
- [[rebecca-twist|Rebecca]] — Daphne du Maurier's Rebecca is a gothic romance narrated by an unnamed woman who marries the wealthy, aloof Maxim de Winter…
- [[soylent-green-twist|Soylent Green]] — Soylent Green is a 1973 science-fiction film set in an overpopulated, resource-depleted future New York where the masses…
- [[the-murder-of-roger-ackroyd|The Murder of Roger Ackroyd]] — Agatha Christie's The Murder of Roger Ackroyd is a detective novel narrated by Dr.
- [[the-sixth-sense|The Sixth Sense]] — The Sixth Sense is a 1999 psychological thriller about a child psychologist treating a troubled young boy who claims to "see…
- [[the-usual-suspects-twist|The Usual Suspects]] — The Usual Suspects is a 1995 crime thriller in which five career criminals are gathered for an apparent heist, only to…

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
