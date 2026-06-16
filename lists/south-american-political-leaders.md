---
type: list
category: history
read: false
---

# South American political leaders

The South American political leaders most worth knowing for quiz bowl.

## nodes

- [[augusto-pinochet|Augusto Pinochet]] — Augusto Ugarte Pinochet (1915–2006) was a Chilean military officer who orchestrated a coup against Salvador Allende in 1973…
- [[bernardo-ohiggins|Bernardo O'Higgins]] — Bernardo O'Higgins Riquelme (1778–1842) was a Chilean military leader and statesman who, working alongside José de San Martín,…
- [[eva-peron|Eva Perón]] — Eva Perón (1919–1952), known as "Evita," was an Argentine actress and wife of Juan Perón who became a powerful political…
- [[getulio-vargas|Getúlio Vargas]] — Getúlio Dornelles Vargas (1882–1954) was a Brazilian military officer and politician who dominated Brazilian politics for 24…
- [[hugo-chavez|Hugo Chávez]] — Hugo Rafael Chávez Frías (1954–2013) was a Venezuelan military officer and politician who led a Bolivarian Revolution,…
- [[jose-de-san-martin|José de San Martín]] — José de San Martín (1778–1850) was an Argentine military leader who liberated Chile and Peru from Spanish rule, earning the…
- [[juan-peron|Juan Perón]] — Juan Domingo Perón (1895–1974) was an Argentine military officer and politician who founded Peronism, a nationalist and…
- [[pedro-ii-of-brazil|Pedro II of Brazil]] — Pedro II (1825–1891), known as Dom Pedro II, was the second and last emperor of Brazil who reigned for 58 years, making him…
- [[salvador-allende|Salvador Allende]] — Salvador Gossens Allende (1908–1973) was a Chilean physician and socialist politician who became Latin America's first…
- [[simon-bolivar|Simón Bolívar]] — Simón Bolívar (1783–1830) was a Venezuelan military leader and statesman who liberated six nations from Spanish colonial rule…

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
