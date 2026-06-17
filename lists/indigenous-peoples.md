---
type: list
category: history
read: false
---

# indigenous peoples

The indigenous peoples most worth knowing for quiz bowl.

## nodes

- [[aboriginal-australians|Aboriginal Australians]] — The Aboriginal Australians are the indigenous peoples of Australia, with continuous cultural presence spanning at least 65,000…
- [[ainu|Ainu]] — The Ainu are the indigenous people of Hokkaido and surrounding islands in what is now Japan, with a distinct language,…
- [[inuit|Inuit]] — The Inuit are the indigenous circumpolar peoples of the Arctic, inhabiting regions across Alaska, Canada, Greenland, and…
- [[maasai|Maasai]] — The Maasai are a Nilotic pastoralist people of East Africa inhabiting the semi-arid savannas of Kenya and Tanzania, renowned…
- [[maori|Māori]] — The Māori are the indigenous Polynesian people of New Zealand, with origins tracing to migrations from central Polynesia…
- [[quechua|Quechua]] — The Quechua are the largest indigenous people of South America, inhabiting the Andean highlands across Peru, Bolivia, Ecuador,…
- [[roma|Roma]] — The Roma (sometimes called Romani or Gypsies, the latter now considered a slur) are a dispersed ethnic group originating in…
- [[san-bushmen|San (Bushmen)]] — The San, historically called Bushmen, are the indigenous hunter-gatherer peoples of southern Africa, predating the Bantu and…
- [[sami|Sámi]] — The Sámi are the indigenous people of northern Scandinavia and the Kola Peninsula, traditionally inhabiting territories…
- [[yanomami|Yanomami]] — The Yanomami are an indigenous people of the Amazon rainforest inhabiting territories across the Brazil-Venezuela border,…

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
