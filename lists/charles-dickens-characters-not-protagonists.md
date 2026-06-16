---
type: list
category: literature
read: false
---

# Charles Dickens characters who aren’t protagonists

The Charles Dickens characters who aren’t protagonists most worth knowing for quiz bowl.

## nodes

- [[bill-sikes|Bill Sikes]] — Bill Sikes is the brutal, violent burglar in Oliver Twist who serves as Fagin's enforcer and Nancy's abuser, embodying brute…
- [[ebenezer-scrooge|Ebenezer Scrooge]] — Ebenezer Scrooge is the miser and misanthrope in A Christmas Carol who is transformed by supernatural visitation on Christmas…
- [[fagin|Fagin]] — Fagin is the calculating criminal mastermind in Oliver Twist who directs a gang of child pickpockets from a squalid London…
- [[madame-defarge|Madame Defarge]] — Madame Defarge is the implacable revolutionary avenger in A Tale of Two Cities who knits coded death lists and presides over…
- [[miss-havisham|Miss Havisham]] — Miss Havisham is a wealthy, deeply wounded woman in Great Expectations who was abandoned at the altar and has since lived in…
- [[mr-bumble|Mr. Bumble]] — Mr.
- [[mr-micawber|Mr. Micawber]] — Mr.
- [[sydney-carton|Sydney Carton]] — Sydney Carton is the dissolute, brilliant barrister in A Tale of Two Cities whose life of dissipation is redeemed through his…
- [[uriah-heep|Uriah Heep]] — Uriah Heep is the obsequious and hypocritical clerk in David Copperfield whose false humility and greasy manner conceal…
- [[wackford-squeers|Wackford Squeers]] — Wackford Squeers is the brutish headmaster of Dotheboys Hall in Nicholas Nickleby, a Yorkshire boarding school where he…

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
