---
type: list
category: performance
read: false
---

# musicals

The musicals most worth knowing for quiz bowl.

## nodes

- [[carousel|Carousel]] — Carousel is a 1945 musical by Richard Rodgers (music) and Oscar Hammerstein II (lyrics) adapted from Ferenc Molnár's play Liliom.
- [[fiddler-on-the-roof|Fiddler on the Roof]] — Fiddler on the Roof is a 1964 musical by Jerry Bock (music) and Sheldon Harnick (lyrics) set in the Jewish village of Anatevka…
- [[guys-and-dolls|Guys and Dolls]] — Guys and Dolls is a 1950 musical by Frank Loesser (music and lyrics) based on Damon Runyon's short stories about Broadway,…
- [[hello-dolly|Hello, Dolly!]] — Hello, Dolly!
- [[my-fair-lady|My Fair Lady]] — My Fair Lady is a 1956 musical by Alan Jay Lerner (lyrics) and Frederick Loewe (music) adapted from George Bernard Shaw's…
- [[oklahoma|Oklahoma!]] — Oklahoma!
- [[show-boat|Show Boat]] — Show Boat is a 1927 musical by Jerome Kern (music) and Oscar Hammerstein II (lyrics) based on Edna Ferber's novel, set along…
- [[the-king-and-i|The King and I]] — The King and I is a 1951 musical by Richard Rodgers (music) and Oscar Hammerstein II (lyrics) based on Margaret Landon's novel…
- [[the-sound-of-music|The Sound of Music]] — The Sound of Music is a 1959 musical by Richard Rodgers (music) and Oscar Hammerstein II (lyrics) that tells the true story of…
- [[west-side-story|West Side Story]] — West Side Story is a 1957 musical by Leonard Bernstein (music), Stephen Sondheim (lyrics), and Arthur Laurents (book) that…

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
