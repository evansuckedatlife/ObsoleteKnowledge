---
type: list
category: religion
read: false
---

# Founders of Religious Traditions

The people who founded or decisively shaped the world's major religions.

## nodes

- [[abraham|Abraham]] — Abraham is the founding patriarch of Judaism, Christianity, and Islam, revered across all three Abrahamic faiths as the father…
- [[bahaullah|Baháʼu'lláh]] — Baháʼu'lláh (1817–1892), born Mirza Husayn-Ali, was the founder of the Baháʼí Faith, a modern religion emphasizing the unity…
- [[confucius|Confucius]] — Confucius was a Chinese philosopher and teacher whose ideas about proper conduct, family relationships, and social harmony…
- [[guru-nanak|Guru Nanak]] — Guru Nanak (1469–1539) was the founding guru of Sikhism, a monotheistic religion emphasizing equality, community service, and…
- [[joseph-smith|Joseph Smith]] — Joseph Smith (1805–1844) was the founding prophet of the Church of Jesus Christ of Latter-day Saints (Mormonism), a uniquely…
- [[mahavira|Mahavira]] — Mahavira, meaning "great hero," was the 24th and final Tirthankara (ford-maker) of Jainism, who revitalized and systematized…
- [[mary-baker-eddy|Mary Baker Eddy]] — Mary Baker Eddy (1821–1910) was the founding figure of Christian Science, a uniquely American religion blending Christian…
- [[muhammad|Muhammad]] — Muhammad was the founding prophet of Islam, a religion that emerged in 7th-century Arabia and became one of the world's…
- [[siddhartha-gautama|Siddhartha Gautama]] — Siddhartha Gautama, known as the Buddha ("the Awakened One"), was the founder of Buddhism and one of history's most…
- [[zoroaster|Zoroaster]] — Zoroaster is the founding prophet of Zoroastrianism, one of the world's oldest monotheistic religions originating in ancient…

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

Scoped from NAQT's *You Gotta Know* topic [`founders-of-religious-traditions`](https://www.naqt.com/you-gotta-know/founders-of-religious-traditions.html). Content authored originally; NAQT used as a topic map only.
