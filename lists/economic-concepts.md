---
type: list
category: social-science
read: false
---

# economic concepts

The economic concepts most worth knowing for quiz bowl.

## nodes

- [[comparative-advantage|Comparative Advantage]] — Comparative advantage is the ability of one party (country, firm, or individual) to produce a good at a lower opportunity cost…
- [[elasticity|Elasticity]] — Elasticity measures the responsiveness of quantity demanded or supplied to changes in price (or income, or other factors).
- [[factors-of-production|Factors of Production]] — The factors of production are the resources or inputs that an economy uses to produce goods and services.
- [[gross-domestic-product|Gross Domestic Product]] — Gross Domestic Product (GDP) is the total monetary value of all final goods and services produced within a country's borders…
- [[inflation|Inflation]] — Inflation is the general and sustained increase in the price level of goods and services in an economy over time.
- [[interest-rate|Interest Rate]] — An interest rate is the cost of borrowing money, expressed as a percentage of the principal per unit time (usually per year).
- [[invisible-hand|Invisible Hand]] — The invisible hand is the metaphor by economist Adam Smith (1776) for how self-interested individuals, pursuing their own…
- [[monopoly|Monopoly]] — A monopoly is a market structure in which a single firm is the sole supplier of a good with no close substitutes.
- [[supply-and-demand|Supply and Demand]] — Supply and demand is the foundational framework describing how prices are determined in a market economy.
- [[tariff|Tariff]] — A tariff is a tax imposed on imported goods when they cross a nation's border.
- [[unemployment|Unemployment]] — Unemployment is the condition of being without a job despite actively seeking employment.

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
