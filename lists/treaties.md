---
type: list
category: history
read: false
---

# treaties

The treaties most worth knowing for quiz bowl.

## nodes

- [[camp-david-accords|Camp David Accords]] — The Camp David Accords (1978) were two frameworks negotiated at the U.S.
- [[peace-of-westphalia|Peace of Westphalia]] — The Peace of Westphalia (1648) consisted of two treaties that ended the devastating Thirty Years' War in Europe, signed in the…
- [[treaty-of-brest-litovsk|Treaty of Brest-Litovsk]] — The Treaty of Brest-Litovsk (1918) withdrew Russia from World War I, signed by the nascent Soviet Union and Germany in…
- [[treaty-of-ghent|Treaty of Ghent]] — The Treaty of Ghent (1814) ended the War of 1812 between the United States and Britain, signed in Ghent, Belgium, after two…
- [[treaty-of-guadalupe-hidalgo|Treaty of Guadalupe Hidalgo]] — The Treaty of Guadalupe Hidalgo (1848) ended the Mexican-American War, transferring roughly half of Mexico's territory to the…
- [[treaty-of-nanking|Treaty of Nanking]] — The Treaty of Nanking (1842) ended the First Opium War between Britain and China, signed aboard a British warship in Nanking…
- [[treaty-of-paris-1783|Treaty of Paris (1783)]] — The Treaty of Paris (1783) formally ended the American Revolutionary War, signed between Britain and the newly formed United…
- [[treaty-of-tordesillas|Treaty of Tordesillas]] — The Treaty of Tordesillas (1494) partitioned the non-European world between Spain and Portugal, drawn at the behest of Pope…
- [[treaty-of-utrecht|Treaty of Utrecht]] — The Treaty of Utrecht (1713) ended the War of the Spanish Succession, a major European conflict fought over the inheritance of…
- [[treaty-of-versailles|Treaty of Versailles]] — The Treaty of Versailles (1919) formally ended World War I, signed in the Palace of Versailles in France by the Allied powers…

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
