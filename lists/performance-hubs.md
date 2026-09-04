---
type: list
category: performance
read: false
---

# Performance hubs

Forms and traditions behind the individual productions and performers.

## nodes

- [[19th-century-france|19th-Century France]] — 19th-Century France serves as one of the most prominent historical and atmospheric backdrops in musical theatre, opera, and classical dance, spanning …
- [[alain-boublil|Alain Boublil]] — Alain Boublil is a French musical theatre lyricist and librettist celebrated for co-creating several of the most commercially triumphant and culturall…
- [[alan-jay-lerner|Alan Jay Lerner]] — Alan Jay Lerner was an American lyricist and librettist who defined the literate, witty, and romantic golden age of mid-century musical-theatre.
- [[all-that-jazz|All That Jazz]] — All That Jazz is a 1979 American musical drama film directed and co-written by Bob Fosse, offering an unflinching, semi-autobiographical portrait of h…
- [[american-folk-culture|American Folk Culture]] — American folk culture encompasses the oral lore, vernacular melodies, social dances, and communal religious hymns created by rural and immigrant pione…
- [[american-racism|American Racism]] — American racism is the enduring system of racial hierarchy, institutional disenfranchisement, and white supremacy directed primarily against African A…
- [[andrew-lloyd-webber|Andrew Lloyd Webber]] — Andrew Lloyd Webber is a British composer who revolutionized musical theatre in the 1980s with a series of commercially colossal productions that blen…
- [[ashton|Frederick Ashton]] — Frederick Ashton, later knighted as Sir Frederick Ashton, was the premier twentieth-century choreographer of england and the creative architect of the…
- [[ballet-theatre|Ballet Theatre]] — Ballet Theatre, officially known today as American Ballet Theatre (ABT), is a premier classical dance institution founded in New York City in 1939 by …
- [[ballets-russes|Ballets Russes]] — The Ballets Russes was a groundbreaking ballet company founded by impresario Sergei Diaghilev in 1909 that revolutionized dance and art through radica…
- [[billy-joel|Billy Joel]] — Billy Joel, known universally as The Piano Man, is one of the most successful American singer-songwriters, pianists, and composers of the 20th century.
- [[bohemian-culture|Bohemian Culture]] — Bohemian Culture is a countercultural ethos and social practice centered on voluntary poverty, artistic devotion, nonconformist lifestyles, and anti-m…
- [[broadway-dancers|Broadway Dancers]] — Broadway Dancers, traditionally known inside the theatrical community as the ensemble or affectionately as gypsies, form the technical backbone of Ame…
- [[broadway-musicals|Broadway Musicals]] — Broadway Musicals constitute the commercial and artistic pinnacle of theatrical entertainment staged within the Theater District of Manhattan in new-y…
- [[brothers-grimm|Brothers Grimm]] — Jacob Grimm (1785–1863) and Wilhelm Grimm (1786–1859) were two German brothers whose collection and curation of European fairy tales became the canoni…
- [[cabaret-musical|Cabaret]] — Cabaret, often indexed as Cabaret (musical), is a landmark 1966 stage musical featuring music by John Kander, lyrics by Fred Ebb, and a book by Joe Ma…
- [[carol-channing|Carol Channing]] — Carol Channing, born Carol Elaine Channing, was an iconic American actress, singer, and comedienne whose outsized stage persona and unmistakable raspi…
- [[chance-procedure|Chance Procedure]] — Chance Procedure, also known across modern arts as aleatoric composition and indeterminacy, is an avant-garde creative technique in which elements of …
- [[cinderella|Cinderella]] — Cinderella, known in classic international variations as Cendrillon and Aschenputtel, is an archetypal folk narrative recounting the unjust persecutio…
- [[damon-runyon|Damon Runyon]] — Damon Runyon, born Alfred Damon Runyan, was an iconic American newspaperman, sports journalist, and short-story writer celebrated for his comedic port…
- [[dance|Dance]] — Dance, together with the universal human act of rhythmic dancing, is an expressive performing art defined by purposefully structured bodily movements …
- [[edna-ferber|Edna Ferber]] — Edna Ferber was a prominent American novelist, short-story author, and dramatist whose sweeping historical panoramas captured the vibrant social, raci…
- [[evita-musical|Evita]] — Evita is a 1978 musical by composer Andrew Lloyd Webber and lyricist Tim Rice that chronicles the rise of Eva Perón from illegitimate poverty to First…
- [[fairy-tale|Fairy Tale]] — A fairy tale is a narrative genre featuring magical elements, archetypal characters (princes, witches, enchanted forests), and moral lessons wrapped i…
- [[fancy-free|Fancy Free]] — Fancy Free is a landmark 1944 American ballet choreographed by Jerome Robbins to a vivid symphonic jazz score composed by Leonard Bernstein.
- [[fokine|Michel Fokine]] — Michel Fokine was a Russian-born choreographer and dancer who revolutionized ballet in the early 20th century by rejecting rigid classical conventions.
- [[folk-traditions|Folk Traditions]] — Folk Traditions encompass the inherited customs, oral narratives, ceremonial dances, and vernacular songs passed down orally across generations within…
- [[frank-loesser|Frank Loesser]] — Frank Loesser was a master American songwriter, lyricist, and composer whose verbal dexterity and melodic range shaped the Golden Age of the Broadway …
- [[fred-ebb|Fred Ebb]] — Fred Ebb was an acclaimed American musical theatre lyricist who formed one of Broadway's most enduring and influential writing partnerships alongside …
- [[german-literature|German literature]] — German literature encompasses the written and oral traditions of the German-speaking world, evolving from medieval heroic epics and the intellectual f…
- [[hans-christian-andersen|Hans Christian Andersen]] — Hans Christian Andersen was a nineteenth-century Danish author and poet whose original literary fairy tales transformed storytelling and became lastin…
- [[imperial-ballet|Imperial Ballet]] — The Imperial Ballet was the state ballet company of Imperial Russia, centered at the Mariinsky Theatre in St.
- [[literature-genre|Literature Genre]] — A literature genre is a systematic classification of written works based on shared formal, thematic, or structural characteristics that readers recogn…
- [[minkus|Ludwig Minkus]] — Ludwig Minkus was an Austrian composer whose ballets scores became pillars of classical ballet repertoire in 19th-century Russia.
- [[musical-theatre|Musical Theatre]] — Musical theatre is a theatrical form that synthesizes dramatic narrative, music, choreography, and elaborate spectacle into a live performance.
- [[new-york-city-ballet|New York City Ballet]] — New York City Ballet (NYCB) is an American ballet company founded in 1948 by choreographer George Balanchine and Lincoln Kirstein, establishing New Yo…
- [[nijinsky|Vaslav Nijinsky]] — Vaslav Nijinsky was a Russian dancer and choreographer of unparalleled technical virtuosity and artistic daring whose brief but revolutionary career r…
- [[russian-folklore|Russian Folklore]] — Russian folklore encompasses the mythology, fairy tales, folk customs, and carnival traditions of Russian culture stretching back centuries.
- [[the-sleeping-beauty|The Sleeping Beauty]] — The Sleeping Beauty is a grand three-act ballet with a prologue composed by Pyotr Ilyich Tchaikovsky and choreographed by Marius Petipa, which premier…
- [[tim-rice|Tim Rice]] — Tim Rice (born 1944) is an acclaimed English lyricist and author who transformed modern musical-theatre through celebrated collaborations with compose…

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
