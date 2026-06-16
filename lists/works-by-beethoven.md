---
type: list
category: music
read: false
---

# Works by Beethoven

The landmark symphonies, concertos, sonatas, and choral works of Ludwig van Beethoven, which bridged the Classical and Romantic eras.

## nodes

- [[appassionata-sonata|Appassionata Sonata]] — Piano Sonata No. 23 in F minor, marked by its intense dramatic sweep and stormy finale.
- [[fidelio|Fidelio]] — Beethoven's only opera, depicting Leonore's rescue of her husband Florestan under the guise of the guard Fidelio.
- [[missa-solemnis|Missa solemnis]] — A massive, deeply personal setting of the Catholic Mass ordinary in D major.
- [[moonlight-sonata|Moonlight Sonata]] — Piano Sonata No. 14 in C-sharp minor, famous for its dreamlike Adagio sostenuto movement.
- [[piano-concerto-no-5-beethoven|Piano Concerto No. 5 ("Emperor")]] — Beethoven's final completed piano concerto, celebrated for its heroic E-flat major grandeur.
- [[symphony-no-3-beethoven|Symphony No. 3 ("Eroica")]] — The revolutionary symphony originally dedicated to Napoleon, marking the birth of musical Romanticism.
- [[symphony-no-5-beethoven|Symphony No. 5 in C minor]] — Famous for its iconic four-note fate motif and journey from minor to major.
- [[symphony-no-6-beethoven|Symphony No. 6 ("Pastoral")]] — A program symphony depicting rural nature, flowing water, birdcalls, and a thunderstorm.
- [[symphony-no-9-beethoven|Symphony No. 9 ("Choral")]] — Beethoven's final symphony, introducing vocal soloists and chorus to sing the Ode to Joy.
- [[wellingtons-victory|Wellington's Victory]] — A highly popular battle symphony commemorating the British victory at Vitoria.

## progress

Live read-status for this list (requires the **Bases** core plugin).

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
