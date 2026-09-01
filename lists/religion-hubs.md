---
type: list
category: religion
read: false
---

# Religion hubs

Traditions, movements and ideas that the specific figures and texts belong to.

## nodes

- [[adam-and-eve|Adam and Eve]] — Adam and Eve are the first human beings in biblical tradition, created by God and placed in the Garden of Eden.
- [[apostle|Apostle]] — An apostle is one of the twelve (or sometimes more) followers of Jesus chosen to be his closest companions and primary witnesses to his ministry.
- [[aramaic|Aramaic]] — Aramaic is an ancient Semitic language closely related to Hebrew that became the lingua franca of the Near East by the first millennium BCE.
- [[augustine|Augustine]] — Augustine of Hippo (354–430 CE) was an influential North African theologian and bishop whose ideas profoundly shaped Christian doctrine for over a tho…
- [[bathsheba|Bathsheba]] — Bathsheba was the wife of Uriah the Hittite who became the mother of Solomon after King David seduced her and orchestrated her husband's death.
- [[bible|Bible]] — The Bible is the central sacred text of Christianity, comprising the Hebrew Bible (also called the Old Testament) and the New Testament.
- [[book-of-job|Book of Job]] — The Book of Job is a biblical wisdom text exploring the problem of human suffering and divine justice through the story of a righteous man afflicted w…
- [[brahman|Brahman]] — Brahman is the ultimate, transcendent reality at the heart of Hindu metaphysics—the infinite, formless, eternal principle that underlies and permeates…
- [[council-of-trent|Council of Trent]] — The Council of Trent (1545–1563) was the Roman Catholic Church's major ecumenical council convened to address the theological challenges posed by the …
- [[counter-reformation|Counter-Reformation]] — The Counter-Reformation (16th–17th centuries) was the Catholic Church's comprehensive response to the Protestant Reformation, combining internal Churc…
- [[covenant-of-abraham|Covenant of Abraham]] — The Covenant of Abraham is the foundational agreement between God and Abraham in Jewish tradition, establishing Abraham as the father of a chosen peop…
- [[gospel-of-john|Gospel of John]] — The Gospel of John (or Fourth Gospel) is the final of the four canonical Gospels in the New Testament, traditionally attributed to John the Apostle.
- [[hebrew|Hebrew]] — Hebrew is an ancient Semitic language, the sacred and spoken language of Jewish tradition and the original language of most of the Hebrew Bible (Tanak…
- [[herod|Herod]] — Herod the Great (73–4 BCE) was the Roman-backed king of Judea who ruled during the time of Jesus's birth and early ministry.
- [[high-holy-days|High Holy Days]] — The High Holy Days (or High Holidays) are the most solemn period in the Jewish calendar, consisting primarily of Rosh Hashanah and Yom Kippur, observa…
- [[hijra|Hijra]] — The Hijra (also spelled Hegira) was Prophet Muhammad's migration from Mecca to Medina in 622 CE, fleeing persecution and establishing the first Islami…
- [[judges|Judges]] — Judges is the seventh book of the Hebrew Bible, recounting the period between Joshua's conquest of Canaan and the establishment of the monarchy under …
- [[laozi|Laozi]] — Laozi (literally "Old Master") is the legendary author traditionally credited with composing the Tao Te Ching, the foundational text of Taoism and phi…
- [[saul|Saul]] — Saul was the first King of Israel, anointed by the prophet Samuel around 1050 BCE to lead Israel against Philistine invasion.
- [[st-peters-basilica|St. Peter's Basilica]] — St.
- [[trinity|Trinity]] — The Trinity is the foundational Christian doctrine asserting that God exists as a single being in three distinct persons: the Father, the Son (Jesus),…
- [[wu-wei|Wu-wei]] — Wu-wei (literally Non-action or Effortless action) is the central principle in Taoism and the Tao Te Ching, describing a state of perfect alignment wi…
- [[yin-yang|Yin-yang]] — Yin-yang is the fundamental Taoist symbol and cosmological principle representing the dynamic balance of complementary opposites: yin (dark, receptive…
- [[yoga|Yoga]] — Yoga is a comprehensive philosophical and physical discipline rooted in Hindu and Indian traditions, aimed at achieving spiritual liberation (moksha) …

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
