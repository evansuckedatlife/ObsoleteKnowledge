---
type: list
category: mythology
read: false
---

# Hindu gods and heroes

Central deities and heroes of Hinduism, including the Trimurti and Vishnu's avatars.

## nodes

- [[agni|Agni]] — Agni is the god of fire and one of the most ancient and revered deities in Hindu and Vedic tradition.
- [[arjuna|Arjuna]] — Arjuna is one of the five Pandava princes and a central hero of the Mahabharata, the world's longest epic poem.
- [[brahma|Brahma]] — Brahma is the creator god of the Hindu trinity, responsible for bringing the universe into being at the start of each cosmic…
- [[ganesha|Ganesha]] — Ganesha is the elephant-headed god of beginnings, wisdom, and the remover of obstacles in Hindu tradition.
- [[hanuman|Hanuman]] — Hanuman is the monkey god and one of the most beloved figures in Hindu mythology, revered for his unwavering devotion,…
- [[indra|Indra]] — Indra is the king of the gods and the lord of storms, thunder, and rain in Hindu and Vedic tradition.
- [[krishna|Krishna]] — Krishna is a central figure in Hindu mythology, an avatar of Vishnu who played a pivotal role in the Mahabharata.
- [[lakshmi|Lakshmi]] — Lakshmi is the goddess of wealth, fortune, abundance, and prosperity in Hindu tradition.
- [[parvati|Parvati]] — Parvati is the goddess of love, fertility, beauty, and cosmic power in Hindu tradition.
- [[rama|Rama]] — Rama is a legendary prince and an avatar of Vishnu, revered as the exemplar of righteousness (dharma) and virtue in Hindu…
- [[shiva|Shiva]] — Shiva is the destroyer and transformer of the Hindu trinity, embodying the cycles of death, renewal, and cosmic destruction…
- [[vishnu|Vishnu]] — Vishnu is the preserver god of the Hindu trinity, responsible for maintaining cosmic order and protecting the universe from chaos.

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
