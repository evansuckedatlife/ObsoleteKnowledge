---
type: list
category: pop-culture
read: false
---

# pre-1960s movies

The pre-1960s movies most worth knowing for quiz bowl.

## nodes

- [[casablanca|Casablanca]] — Casablanca is a 1942 wartime romance and espionage thriller set in French Morocco, where an embittered American barkeep named…
- [[citizen-kane|Citizen Kane]] — Citizen Kane is Orson Welles's 1941 directorial debut, a revolutionary biographical drama about the rise and moral decay of…
- [[gone-with-the-wind|Gone with the Wind]] — Gone with the Wind is an epic historical drama set during the American Civil War and Reconstruction, following the headstrong…
- [[it-s-a-wonderful-life|It's a Wonderful Life]] — It's a Wonderful Life is a 1946 fantasy drama directed by Frank Capra, following a desperate man named George Bailey on…
- [[on-the-waterfront|On the Waterfront]] — On the Waterfront is a 1954 gritty social drama about labor corruption and redemption, following Terry Malloy, a washed-up…
- [[singin-in-the-rain|Singin' in the Rain]] — Singin' in the Rain is a 1952 musical comedy set in 1920s Hollywood during the transition from silent to talking pictures.
- [[some-like-it-hot|Some Like It Hot]] — Some Like It Hot is a 1959 comedy masterpiece directed by Billy Wilder, following two musicians who go undercover as women in…
- [[sunset-boulevard|Sunset Boulevard]] — Sunset Boulevard is a 1950 noir masterpiece directed by Billy Wilder that exposes the dark underbelly of Hollywood through the…
- [[the-wizard-of-oz|The Wizard of Oz]] — The Wizard of Oz is a 1939 fantasy musical following a Kansas farm girl named Dorothy who is transported by tornado to the…
- [[vertigo|Vertigo]] — Vertigo is Alfred Hitchcock's 1958 psychological thriller starring James Stewart as a detective struggling with acrophobia and…

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
