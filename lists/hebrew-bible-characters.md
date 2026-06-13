---
type: list
category: religion
read: false
---

# Hebrew Bible Characters

Major figures of the Hebrew Bible (Old Testament), from the patriarchs to the prophets.

## nodes

- [[abraham|Abraham]] — Abraham is the founding patriarch of Judaism, Christianity, and Islam, revered across all three Abrahamic faiths as the father…
- [[daniel|Daniel]] — Daniel was an Israelite prophet and statesman who served foreign kings during the Babylonian exile.
- [[david|David]] — King David is arguably the most revered figure in the Hebrew Bible and Jewish tradition—a shepherd who became Israel's…
- [[elijah|Elijah]] — Elijah the Tishbite was one of the most powerful prophets in Hebrew scripture, known for his dramatic confrontations with…
- [[jacob|Jacob]] — The grandson of Abraham and son of Isaac, Jacob is remembered as the patriarch whose name was changed to Israel, meaning "he…
- [[jonah|Jonah]] — Jonah was a reluctant prophet whose story explores themes of divine mercy, human prejudice, and the universal scope of God's…
- [[moses|Moses]] — The greatest prophet and lawgiver in Hebrew scripture, Moses is credited with leading the Israelites out of slavery in Egypt…
- [[samson|Samson]] — Samson was an Israelite judge whose extraordinary physical strength made him a folk hero and champion against Philistine…
- [[samuel|Samuel]] — Samuel was a prophet and judge who marked a pivotal transition in Israelite history from the era of judges to the era of kings.
- [[solomon|Solomon]] — King Solomon was the son and successor of King David, renowned for his wisdom, wealth, and architectural grandeur.

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
