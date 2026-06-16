---
type: list
category: literature
read: false
---

# Japanese authors

The Japanese authors most worth knowing for quiz bowl.

## nodes

- [[akutagawa-ryunosuke|Akutagawa Ryūnosuke]] — Akutagawa Ryūnosuke (1892–1927) was a seminal figure in early twentieth-century Japanese literature who pioneered the modern…
- [[chikamatsu-monzaemon|Chikamatsu Monzaemon]] — Chikamatsu Monzaemon (1653–1724) was the preeminent playwright of the Edo period who wrote for both bunraku (puppet theatre)…
- [[endo-shusaku|Endō Shusaku]] — Endō Shusaku (1923–1996) was a major post-war novelist and Japan's most celebrated Christian writer, whose work explored the…
- [[kawabata-yasunari|Kawabata Yasunari]] — Kawabata Yasunari (1899–1972) was Japan's first Nobel Prize winner in Literature whose delicate, lyrically controlled prose…
- [[matsuo-basho|Matsuo Bashō]] — Matsuo Bashō (1644–1694) was Japan's preeminent master of haiku and poet of the Edo period whose spare, nature-inflected verse…
- [[mishima-yukio|Mishima Yukio]] — Mishima Yukio (1925–1970) was a prolific and controversial post-war novelist, playwright, and essayist who fused classical…
- [[murasaki-shikibu|Murasaki Shikibu]] — Murasaki Shikibu (973–1025 CE) was a noblewoman of the Heian court who authored The Tale of Genji, widely regarded as the…
- [[sei-shonagon|Sei Shōnagon]] — Sei Shōnagon (966–1017 CE) was a Heian court noblewoman and lady-in-waiting whose Makura no Soshi (The Pillow Book) is one of…
- [[zeami|Zeami]] — Zeami Motokiyo (1363–1443) was a transformative theatre artist and theorist who perfected and codified Nō theatre during the…
- [[oe-kenzaburo|Ōe Kenzaburō]] — Ōe Kenzaburō (1935–2023) was a Nobel Prize–winning novelist and essayist whose experimental, intellectually demanding fiction…

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
