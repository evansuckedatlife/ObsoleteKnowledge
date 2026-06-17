---
type: list
category: social-science
read: false
---

# linguists

The linguists most worth knowing for quiz bowl.

## nodes

- [[benjamin-lee-whorf|Benjamin Lee Whorf]] — Benjamin Lee Whorf was an American linguist best known for developing the theory of linguistic relativity, which proposes that…
- [[edward-sapir|Edward Sapir]] — Edward Sapir was an American linguist and anthropologist who pioneered the study of Native American languages and language's…
- [[ferdinand-de-saussure|Ferdinand de Saussure]] — Ferdinand de Saussure was a Swiss linguist whose Course in General Linguistics (published posthumously in 1916) established…
- [[george-lakoff|George Lakoff]] — George Lakoff is an American linguist and cognitive scientist who pioneered cognitive linguistics by arguing that language…
- [[leonard-bloomfield|Leonard Bloomfield]] — Leonard Bloomfield was an American linguist whose rigorous methodological approach to language description and whose…
- [[noam-chomsky|Noam Chomsky]] — Noam Chomsky is an American linguist and cognitive scientist whose theory of generative grammar revolutionised linguistics in…
- [[panini|Panini]] — Panini was an ancient Indian grammarian and linguistic theorist, likely active in the 4th century BCE, who compiled an…
- [[paul-grice|Paul Grice]] — Paul Grice was a British philosopher of language whose theory of conversational implicature and the cooperative principle…
- [[steven-pinker|Steven Pinker]] — Steven Pinker is a Canadian-American cognitive psychologist and linguist who has brought generative grammar and cognitive…
- [[william-jones|William Jones]] — William Jones was a British philologist and judge in 18th-century India whose 1786 proposal of a genetic relationship between…
- [[william-labov|William Labov]] — William Labov is an American sociolinguist who founded the systematic study of linguistic variation and change, demonstrating…

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
