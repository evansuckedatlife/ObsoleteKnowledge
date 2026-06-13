---
type: list
category: geography
read: false
---

# western European rivers

The western European rivers most worth knowing for quiz bowl.

## nodes

- [[danube-river|Danube River]] — The Danube is Europe's second-longest river, flowing 1,771 miles from Germany's Black Forest through ten countries to the…
- [[elbe-river|Elbe River]] — The Elbe is a 724-mile river flowing from the Czech Republic through eastern Germany to the North Sea, passing through major…
- [[loire-river|Loire River]] — The Loire is France's longest river, flowing 625 miles from the Massif Central through the Loire Valley to the Atlantic Ocean.
- [[po-river|Po River]] — The Po is northern Italy's longest river, flowing 405 miles from the Alps westward across the Padana plain to the Adriatic Sea.
- [[rhine-river|Rhine River]] — The Rhine is western Europe's most important waterway, flowing 765 miles from the Swiss Alps through Germany, France, and the…
- [[rhone-river|Rhône River]] — The Rhône is a major western European river flowing 505 miles from the Swiss Alps through Lake Geneva and eastern France into…
- [[seine-river|Seine River]] — The Seine is France's second-longest river, flowing 485 miles from Burgundy through Paris and Normandy to the English Channel.
- [[tagus-river|Tagus River]] — The Tagus is the Iberian Peninsula's longest river, flowing 645 miles from central Spain through Portugal to the Atlantic Ocean.
- [[thames-river|Thames River]] — The Thames is England's most important river, flowing 215 miles through south-central England to the North Sea.
- [[tiber-river|Tiber River]] — The Tiber is the river on which Rome was founded and grew into the capital of the ancient Mediterranean world.

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
