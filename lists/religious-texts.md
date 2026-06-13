---
type: list
category: religion
read: false
---

# Religious Texts

The core scriptures and classic texts of the world's religious traditions.

## nodes

- [[analects|Analects]] — The Analects is a collection of sayings and conversations attributed to Confucius and his disciples, compiled in China around…
- [[apocrypha|Apocrypha]] — The Apocrypha is a collection of religious texts written between the Hebrew Bible and the New Testament, primarily during the…
- [[avesta|Avesta]] — The Avesta is the sacred scripture of Zoroastrianism, an ancient Persian religion founded by the prophet Zoroaster (Zarathustra).
- [[bhagavad-gita|Bhagavad Gita]] — The Bhagavad Gita is a 700-verse philosophical dialogue embedded within the epic Mahabharata, where the god Krishna counsels…
- [[book-of-mormon|Book of Mormon]] — The Book of Mormon is a sacred text of The Church of Jesus Christ of Latter-day Saints (LDS), purportedly translated by Joseph…
- [[hadith|Hadith]] — The Hadith is a collection of reports documenting the sayings, deeds, and approvals of the Prophet Muhammad, compiled in the…
- [[quran|Qur'an]] — The Qur'an is the central religious text of Islam, believed by Muslims to be the literal word of God (Allah) revealed orally…
- [[talmud|Talmud]] — The Talmud is a vast body of Jewish law, theology, and commentary compiled over centuries, consisting of the Mishnah (3rd…
- [[tao-te-ching|Tao Te Ching]] — The Tao Te Ching (or Daodejing) is a foundational text of Taoism, attributed to the sage Laozi and composed around the 4th–6th…
- [[upanishads|Upanishads]] — The Upanishads are a collection of philosophical texts forming the foundation of Advaita Vedanta and Hindu metaphysics,…
- [[vedas|Vedas]] — The Vedas are the oldest and most authoritative scriptures of Hinduism, composed in Vedic Sanskrit between approximately…
- [[yijing|Yijing]] — The Yijing (or I Ching, "Book of Changes") is an ancient Chinese divination text and philosophical classic, compiled over…

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

Scoped from NAQT's *You Gotta Know* topic [`religious-texts`](https://www.naqt.com/you-gotta-know/religious-texts.html). Content authored originally; NAQT used as a topic map only.
