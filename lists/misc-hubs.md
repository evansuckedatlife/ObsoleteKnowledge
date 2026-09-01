---
type: list
category: misc
read: false
---

# Misc hubs

Cross-cutting concepts that belong to no single field.

## nodes

- [[african-diaspora|African Diaspora]] — The African diaspora refers to the dispersal of African peoples across the globe, most significantly through the forced migration of enslaved Africans…
- [[architecture|Architecture]] — Architecture is the art and science of designing and constructing buildings and physical structures that serve human needs while embodying aesthetic, …
- [[art-nouveau|Art Nouveau]] — Art Nouveau was an international design movement (1890–1910) that revolutionized decorative arts, architecture, and graphic design by drawing inspirat…
- [[astronomy|Astronomy]] — Astronomy is the scientific discipline that studies celestial objects, phenomena, and the structure of the universe itself.
- [[belle-epoque|Belle Époque]] — The Belle Époque (French for "Beautiful Era") was a period of European cultural and economic flourishing spanning roughly 1870 to 1914, centered prima…
- [[buckminster-fuller|Buckminster Fuller]] — Buckminster Fuller (1895–1983) was an American visionary inventor, architect, and systems theorist who pioneered the geodesic dome and championed holi…
- [[caribbean-culture|Caribbean Culture]] — Caribbean culture is the distinctive fusion of African, European, Indigenous, and Asian traditions forged in the islands of the Caribbean through cent…
- [[daniel-burnham|Daniel Burnham]] — Daniel Burnham (1846–1912) was an American architect and urban planner whose visionary leadership transformed Chicago into a modern metropolis and est…
- [[engineering|Engineering]] — Engineering is the practical discipline of designing, building, and improving structures, machines, and systems using mathematics and science.
- [[geodesic-dome|Geodesic Dome]] — The geodesic dome is an architectural structure composed of triangular panels arranged over a sphere or hemisphere, designed to span large distances w…
- [[geometry|Geometry]] — Geometry is the branch of mathematics concerned with the properties, relationships, and measurements of points, lines, planes, and solid shapes.
- [[gilded-age|Gilded Age]] — The Gilded Age was the period of rapid industrialization and economic growth in the United States, roughly from the 1870s through the 1900s, marked by…
- [[gregorian-calendar|Gregorian Calendar]] — The Gregorian calendar is the solar calendar adopted by the Catholic Church in 1582 and gradually adopted worldwide as the standard civil calendar.
- [[human-anatomy|Human Anatomy]] — Human anatomy is the scientific study of the body's structure—its bones, muscles, organs, and systems—and how these components are organized and inter…
- [[indian-removal|Indian Removal]] — Indian Removal was the U.S.
- [[islamic-calendar|Islamic Calendar]] — The Islamic calendar (also called the Hijri calendar) is a purely lunar calendar used throughout the Islamic world to date events and determine religi…
- [[john-keats|John Keats]] — John Keats (1795–1821) was an English Romantic poet whose lyrical genius earned him rapid fame and has only grown since his death from tuberculosis at…
- [[lord-byron|Lord Byron]] — Lord Byron (George Gordon, 1788–1824) was an English Romantic poet whose outrageous personal life and stirring verse made him one of the most famous w…
- [[lunar-calendar|Lunar Calendar]] — A lunar calendar is a timekeeping system based on the cycles of the moon, marking months by lunar phases (typically 29–30 days per month) rather than …
- [[marcus-brutus|Marcus Brutus]] — Marcus Junius Brutus (85–42 BCE) was a Roman senator and general whose participation in the assassination of Julius Caesar made him one of history's m…
- [[mary-queen-of-scots|Mary Queen of Scots]] — Mary Queen of Scots was a Scottish monarch (1542–1587) and the tragic focal point of religious and political turmoil in Renaissance Britain.
- [[new-year-s-day|New Year's Day]] — New Year's Day, celebrated on January 1st in much of the world, marks the beginning of the calendar year and is observed as a holiday in the Gregorian…
- [[oliver-wendell-holmes-jr|Oliver Wendell Holmes Jr.]] — Oliver Wendell Holmes Jr.
- [[percy-bysshe-shelley|Percy Bysshe Shelley]] — Percy Bysshe Shelley was an English Romantic poet and political radical whose visionary work explored freedom, love, and social justice.
- [[robert-louis-stevenson|Robert Louis Stevenson]] — Robert Louis Stevenson was a Scottish author and adventurer whose imaginative tales of mystery, adventure, and psychological terror defined Victorian …
- [[sequoyah|Sequoyah]] — Sequoyah was a Cherokee polymath who single-handedly created a syllabary for the Cherokee language in the early 19th century, enabling his people to a…
- [[space-age|Space Age]] — The Space Age was a cultural and design movement spanning roughly the 1950s through 1970s, born from humanity's ventures into space exploration and Co…
- [[spring-equinox|Spring Equinox]] — The spring equinox (or vernal equinox) marks the astronomical moment when the sun crosses the celestial equator, making day and night nearly equal len…
- [[symmetry|Symmetry]] — Symmetry is the quality of being unchanged when subjected to a transformation—a rotation, reflection, or translation.
- [[ten-commandments|Ten Commandments]] — The Ten Commandments are the foundational moral and religious laws given by God to Moses on Mount Sinai, according to Hebrew scripture.
- [[theravada-buddhism|Theravada Buddhism]] — Theravada Buddhism is the oldest surviving school of Buddhism, emphasizing adherence to the original teachings preserved in the Pali Canon scriptures.
- [[urbanism|Urbanism]] — Urbanism is the discipline of designing and organizing cities and urban spaces—neighborhoods, streets, parks, transit systems, and civic buildings.
- [[visual-art|Visual Art]] — Visual art encompasses creative works made primarily for aesthetic contemplation and to be perceived through the eye: painting, sculpture, drawing, pr…
- [[western-new-year-s-day|Western New Year's Day]] — Western New Year's Day is the annual celebration of January 1st, marking the beginning of the year according to the Gregorian calendar adopted through…

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
