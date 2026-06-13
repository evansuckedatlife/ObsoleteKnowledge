---
type: list
category: religion
read: false
---

# Biblical Sayings

Everyday English idioms and expressions that originate in the Bible.

## nodes

- [[behemoth|Behemoth]] — Behemoth is an enormous, powerful creature described in the Book of Job as an example of God's incomprehensible creation and…
- [[good-samaritan|Good Samaritan]] — The Good Samaritan is a parable told by Jesus about a Samaritan who stops to help a wounded traveler, while others—a priest…
- [[jezebel|Jezebel]] — Jezebel was a wicked queen of Israel, wife of King Ahab, who opposed the prophet Elijah and persecuted God's followers.
- [[land-of-milk-and-honey|a land of milk and honey]] — This phrase describes the Promised Land—Canaan—that God promised to give the Israelites after their exodus from Egypt.
- [[fire-and-brimstone|fire and brimstone]] — This phrase describes divine destruction and damnation, rooted in the destruction of Sodom and Gomorrah with fire and sulfur…
- [[golden-calf|golden calf]] — The golden calf is an idol made by the Israelites while Moses was receiving the Ten Commandments on Mount Sinai.
- [[pearls-before-swine|pearls before swine]] — This phrase comes from Jesus' teaching in the Sermon on the Mount, warning against sharing precious or sacred things with…
- [[sweat-of-your-brow|the sweat of your brow]] — This phrase comes from Genesis, where God condemns Adam to labor as punishment for eating the forbidden fruit.
- [[writing-on-the-wall|the writing on the wall]] — This phrase comes from Daniel, where mysterious writing appears on a palace wall during a feast, and Daniel must interpret it…
- [[ye-of-little-faith|ye of little faith]] — This phrase, spoken by Jesus to his followers, expresses disappointment or gentle rebuke for lack of trust in God.

## progress

Live read-status for this list (requires the **Bases** core plugin). Flip a node's `read` from its footer toggle and it moves here.

```base
filters:
  and:
    - lists.containsLinkTo(this.file.asLink())
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

## source

Scoped from NAQT's *You Gotta Know* topic [`biblical-sayings`](https://www.naqt.com/you-gotta-know/biblical-sayings.html). Content authored originally; NAQT used as a topic map only.
