---
type: list
category: literature
read: false
---

# Jewish-American authors

The Jewish-American authors most worth knowing for quiz bowl.

## nodes

- [[allen-ginsberg|Allen Ginsberg]] — Allen Ginsberg (1926–1997) was an American poet and activist who became the voice of the Beat Generation and the…
- [[arthur-miller|Arthur Miller]] — Arthur Miller (1915–2005) was an American playwright whose dramas explore moral crisis, social responsibility, and the…
- [[bernard-malamud|Bernard Malamud]] — Bernard Malamud (1914–1986) was an American novelist and short-story writer whose fiction centres on working-class Jewish…
- [[chaim-potok|Chaim Potok]] — Chaim Potok (1929–2002) was an American novelist and rabbi whose fiction explores the tensions between Orthodox Jewish…
- [[cynthia-ozick|Cynthia Ozick]] — Cynthia Ozick (b.
- [[emma-lazarus|Emma Lazarus]] — Emma Lazarus (1849–1887) was an American poet and essayist whose most famous work, "The New Colossus," became the defining…
- [[grace-paley|Grace Paley]] — Grace Paley (1922–2007) was an American short-story writer and poet whose deceptively simple narratives capture the texture of…
- [[isaac-asimov|Isaac Asimov]] — Isaac Asimov was an American biochemist and prolific science fiction author whose works defined the genre's technical and…
- [[isaac-bashevis-singer|Isaac Bashevis Singer]] — Isaac Bashevis Singer (1904–1991) was a Polish-born writer who made Yiddish—a language other Jewish intellectuals were…
- [[michael-chabon|Michael Chabon]] — Michael Chabon (b.
- [[neil-simon|Neil Simon]] — Neil Simon (1927–2018) was an American playwright and screenwriter whose comedies are among the most-performed and…
- [[norman-mailer|Norman Mailer]] — Norman Mailer (1923–2007) was an American novelist, essayist, and provocateur whose fiction and nonfiction tackle American…
- [[philip-roth|Philip Roth]] — Philip Roth (1933–2018) was an American novelist whose fiction explores Jewish identity, sexuality, and the mythologies of…
- [[saul-bellow|Saul Bellow]] — Saul Bellow (1915–2005) was an American novelist whose work crystallises the anxieties of urban intellectual life and the…

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
