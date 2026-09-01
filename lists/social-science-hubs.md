---
type: list
category: social-science
read: false
---

# Social Science hubs

Concepts and frameworks the individual studies and thinkers apply.

## nodes

- [[authority|Authority]] — Authority is the recognized right of an individual or institution to make decisions, issue commands, and expect compliance from others.
- [[business-cycle|Business Cycle]] — The business cycle describes the alternating pattern of expansion and contraction in economic activity — periods of growth and rising confidence follo…
- [[culture|Culture]] — Culture encompasses the shared beliefs, values, practices, artifacts, and meanings that a group of people collectively create and transmit across gene…
- [[deadweight-loss|Deadweight Loss]] — Deadweight loss is the reduction in total economic surplus (the sum of consumer and producer benefit) caused by market inefficiencies.
- [[developmental-psychology|Developmental Psychology]] — Developmental psychology is the study of how psychological processes and behaviour change across the lifespan, from infancy through old age.
- [[economic-growth|Economic Growth]] — Economic growth is the sustained increase in the total productive output of an economy over time, typically measured by real gross-domestic-product gr…
- [[endangered-languages|Endangered Languages]] — Endangered languages are languages with so few remaining speakers that they face extinction within one to three generations.
- [[ethics-in-psychology|Ethics in Psychology]] — Ethics in psychology is the field of moral and professional standards governing research on human and animal subjects, including requirements for info…
- [[human-evolution|Human Evolution]] — Human evolution is the process by which anatomically and behaviourally modern humans emerged from non-human primate ancestors over millions of years.
- [[humanistic-psychology|Humanistic Psychology]] — Humanistic psychology emerged in the 1950s-60s as a reaction against both behaviourism and psychoanalysis, emphasizing human potential, creativity, an…
- [[inca-empire|Inca Empire]] — The Inca Empire (Tawantinsuyu) was the largest pre-Columbian state in the Americas, spanning much of western South America from around 1400 to 1533.
- [[indigenous-languages-americas|Indigenous Languages of the Americas]] — The indigenous languages of the Americas comprise the languages spoken by the diverse pre-Columbian civilizations and their descendants, ranging from …
- [[indus-valley-civilization|Indus Valley Civilization]] — The Indus Valley Civilization (circa 3300–1300 BCE) was one of the world's three great ancient urban societies, alongside Egypt and Mesopotamia.
- [[island-languages|Island Languages]] — Island languages are languages that develop or persist in relative geographic isolation on islands, leading to unique linguistic features shaped by sm…
- [[kinship-systems|Kinship Systems]] — Kinship systems are the culturally determined frameworks through which societies organize relationships between family members and define rights, obli…
- [[linguistic-typology|Linguistic Typology]] — Linguistic typology is the classification of languages by their recurrent structural features—how they form words (morphology), arrange them (syntax),…
- [[magic|Magic]] — Magic is the belief and practice that thoughts, words, or ritual actions can directly influence the physical world through supernatural means—a univer…
- [[market-mechanism|Market Mechanism]] — The Market Mechanism is the economic process by which prices adjust to balance the quantity of goods supplied with the quantity demanded, without cent…
- [[motivation|Motivation]] — Motivation is the force that initiates, directs, and sustains behavior toward achieving goals or satisfying needs.
- [[operant-conditioning|Operant Conditioning]] — Operant Conditioning is the learning process through which behavior is shaped by its consequences—rewards that increase behavior and punishments that …
- [[philip-zimbardo|Philip Zimbardo]] — Philip Zimbardo is an American social psychologist best known for conducting the Stanford Prison Experiment in 1971, a shocking study that demonstrate…
- [[psychoanalysis|Psychoanalysis]] — Psychoanalysis is a psychological theory and therapeutic method pioneered by Sigmund Freud, emphasizing the role of the unconscious mind, repressed co…
- [[psychology-as-science|Psychology as Science]] — The establishment of Psychology as Science marks the late-19th-century transition of psychology from philosophical speculation to controlled laborator…
- [[rite-of-passage|Rite of Passage]] — A Rite of Passage is a ritualized ceremony or series of ceremonies through which individuals transition between defined social statuses—from childhood…
- [[semiotics|Semiotics]] — Semiotics is the study of signs and how meaning is created, communicated, and interpreted through sign systems.
- [[sociolinguistics|Sociolinguistics]] — Sociolinguistics is the study of language in its social context—how language varies across groups, regions, and social circumstances, and how language…
- [[solomon-asch|Solomon Asch]] — Solomon Asch was a Polish-American social psychologist famous for the Asch Conformity Experiments, a series of studies conducted in the 1950s that rev…
- [[thomas-malthus|Thomas Malthus]] — Thomas Robert Malthus was an English clergyman and economist whose "Essay on the Principle of Population" (1798) argued that human population grows ge…
- [[turkey|Turkey]] — Turkey, located at the crossroads of Europe and Asia in the region historically called Anatolia, has been a crucial site of human civilization for mil…

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
