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
- [[baroque-art|Baroque Art]] — Baroque is the exuberant artistic and architectural style that emerged in late 16th-century Europe, particularly in Catholic regions responding to the…
- [[bathsheba|Bathsheba]] — Bathsheba was the wife of Uriah the Hittite who became the mother of Solomon after King David seduced her and orchestrated her husband's death.
- [[bible|Bible]] — The Bible is the central sacred text of Christianity, comprising the Hebrew Bible (also called the Old Testament) and the New Testament.
- [[book-of-job|Book of Job]] — The Book of Job is a biblical wisdom text exploring the problem of human suffering and divine justice through the story of a righteous man afflicted w…
- [[brahman|Brahman]] — Brahman is the ultimate, transcendent reality at the heart of Hindu metaphysics—the infinite, formless, eternal principle that underlies and permeates…
- [[council-of-trent|Council of Trent]] — The Council of Trent (1545–1563) was the Roman Catholic Church's major ecumenical council convened to address the theological challenges posed by the …
- [[counter-reformation|Counter-Reformation]] — The Counter-Reformation (16th–17th centuries) was the Catholic Church's comprehensive response to the Protestant Reformation, combining internal Churc…
- [[covenant-of-abraham|Covenant of Abraham]] — The Covenant of Abraham is the foundational agreement between God and Abraham in Jewish tradition, establishing Abraham as the father of a chosen peop…
- [[goliath|Goliath]] — Goliath is the legendary giant of the Philistines, famous not for his own deeds but for being the unlikely victim of a shepherd boy's victory.
- [[gospel-of-john|Gospel of John]] — The Gospel of John (or Fourth Gospel) is the final of the four canonical Gospels in the New Testament, traditionally attributed to John the Apostle.
- [[hebrew|Hebrew]] — Hebrew is an ancient Semitic language, the sacred and spoken language of Jewish tradition and the original language of most of the Hebrew Bible (Tanak…
- [[herod|Herod]] — Herod the Great (73–4 BCE) was the Roman-backed king of Judea who ruled during the time of Jesus's birth and early ministry.
- [[high-holy-days|High Holy Days]] — The High Holy Days (or High Holidays) are the most solemn period in the Jewish calendar, consisting primarily of Rosh Hashanah and Yom Kippur, observa…
- [[hijra|Hijra]] — The Hijra (also spelled Hegira) was Prophet Muhammad's migration from Mecca to Medina in 622 CE, fleeing persecution and establishing the first Islami…
- [[incarnation|Incarnation]] — The Incarnation is the core Christian doctrine affirming that God became flesh in the person of Jesus Christ, uniting the infinite divine nature with …
- [[isaac|Isaac]] — Isaac is the second of the Hebrew Bible's three great patriarchs and the son of Abraham and Sarah.
- [[jewish-law|Jewish Law]] — Jewish law, or halakhah (Hebrew "the way to walk"), is the comprehensive system of religious, civil, and ethical obligations derived from the Torah an…
- [[joshua|Joshua]] — Joshua is the military leader and judge who succeeded Moses and led the Israelites into the Promised Land of Canaan after forty years of wilderness wa…
- [[judges|Judges]] — Judges is the seventh book of the Hebrew Bible, recounting the period between Joshua's conquest of Canaan and the establishment of the monarchy under …
- [[karma-and-dharma|Karma and Dharma]] — Karma and dharma are interlocking concepts central to Hindu and Buddhist understanding of existence: karma is the law of moral causality—actions gener…
- [[laozi|Laozi]] — Laozi (literally "Old Master") is the legendary author traditionally credited with composing the Tao Te Ching, the foundational text of Taoism and phi…
- [[medina|Medina]] — Medina is the second holiest city in Islam and the sanctuary that received Muhammad and his followers during the Hijra (migration) from Mecca.
- [[noah|Noah]] — Noah is the patriarch chosen by God to preserve humanity and animal life through a catastrophic flood that wiped the slate clean after the corruption …
- [[original-sin|Original Sin]] — Original sin is the Christian theological doctrine that humanity inherits a fallen, sinful nature from the transgression of Adam and Eve in the Garden…
- [[philistines|Philistines]] — The Philistines were an ancient Mediterranean people who settled on the coastal plains of Canaan (modern-day southern Israel) during the Iron Age, rou…
- [[repentance|Repentance]] — Repentance is the spiritual act of turning away from wrongdoing, acknowledging sin, and seeking restoration through transformation and restitution.
- [[saul|Saul]] — Saul was the first King of Israel, anointed by the prophet Samuel around 1050 BCE to lead Israel against Philistine invasion.
- [[st-peters-basilica|St. Peter's Basilica]] — St.
- [[suffering|Suffering]] — Suffering stands as one of humanity's central existential and theological preoccupations: the experience of pain, loss, and anguish, and the meaning —…
- [[theodicy|Theodicy]] — Theodicy is the philosophical and theological effort to justify the existence of evil and suffering in a world governed by an omnipotent, omniscient, …
- [[trinity|Trinity]] — The Trinity is the foundational Christian doctrine asserting that God exists as a single being in three distinct persons: the Father, the Son (Jesus),…
- [[vatican-city|Vatican City]] — Vatican City is the world's smallest independent state and the spiritual and administrative center of the Roman Catholic Church.
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
