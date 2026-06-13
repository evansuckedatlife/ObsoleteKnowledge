---
type: list
category: geography
read: false
---

# deserts

The deserts most worth knowing for quiz bowl.

## nodes

- [[antarctica|Antarctica]] — Antarctica is the world's southernmost continent, an ice-bound polar desert surrounding the South Pole and covering roughly…
- [[arabian-desert|Arabian Desert]] — The Arabian Desert spans roughly 900,000 square miles across the Arabian Peninsula, encompassing parts of Saudi Arabia, Yemen,…
- [[atacama-desert|Atacama Desert]] — The Atacama is the driest non-polar desert on Earth, stretching roughly 600 miles along the western edge of the Andes in…
- [[gobi-desert|Gobi Desert]] — The Gobi is a large cold desert spanning roughly 500,000 square miles across Mongolia and northern China, notable for its…
- [[great-sandy-desert|Great Sandy Desert]] — The Great Sandy Desert is a large hot desert occupying roughly 75,000 square miles of northwestern Australia, spanning parts…
- [[great-victoria-desert|Great Victoria Desert]] — The Great Victoria Desert is Australia's largest desert, sprawling roughly 134,000 square miles across the border of Western…
- [[kalahari-desert|Kalahari Desert]] — The Kalahari is a large semi-arid sandy savanna covering roughly 360,000 square miles across Botswana, Namibia, and South Africa.
- [[namib-desert|Namib Desert]] — The Namib is one of Africa's most ancient deserts, extending roughly 1,200 miles along the southwestern coast of Namibia.
- [[negev-desert|Negev Desert]] — The Negev is a triangular arid desert region comprising roughly 4,700 square miles of southern Israel, extending southward…
- [[painted-desert|Painted Desert]] — The Painted Desert is a semi-arid badlands region in northeastern Arizona, stretching roughly 100 miles east to west across…
- [[rub-al-khali|Rub' al-Khali]] — The Rub' al-Khali, or "Empty Quarter," is the world's largest continuous sand desert, spanning roughly 250,000 square miles…
- [[sahara-desert|Sahara Desert]] — The Sahara is the world's largest hot desert, spanning roughly 3.6 million square miles across North Africa from the Atlantic…
- [[taklamakan-desert|Taklamakan Desert]] — The Taklamakan is a large hot desert in northwestern China, covering roughly 130,000 square miles in the Xinjiang region…

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
