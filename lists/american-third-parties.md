---
type: list
category: history
read: false
---

# American third parties

The American third parties most worth knowing for quiz bowl.

## nodes

- [[anti-masonic-party|Anti-Masonic Party]] — The Anti-Masonic Party was an early U.S.
- [[bull-moose-party|Bull Moose Party]] — The Bull Moose Party, officially the Progressive Party, was a U.S.
- [[dixiecrats|Dixiecrats]] — The Dixiecrats, formally the States' Rights Democratic Party, were Southern Democrats who split from the national Democratic…
- [[free-soil-party|Free Soil Party]] — The Free Soil Party was a short-lived antislavery political movement of the 1848–1854 era, formed by Northern Democrats…
- [[green-party|Green Party]] — The Green Party of the United States, founded in 1991 and formally chartered in 2001, advocates for environmental protection,…
- [[know-nothing-party|Know-Nothing Party]] — The Know-Nothing Party, officially the American Party, was a nativist political movement of the 1850s that opposed immigration…
- [[libertarian-party|Libertarian Party]] — The Libertarian Party, founded in 1971, is the longest-standing active third party in the United States, advocating for…
- [[populist-party|Populist Party]] — The Populist Party, also known as the People's Party, emerged in the 1890s as a radical agrarian and labor movement responding…
- [[reform-party|Reform Party]] — The Reform Party, founded by Texas billionaire Ross Perot in 1995, was a centrist third party focused on federal deficit…
- [[socialist-party-usa|Socialist Party USA]] — The Socialist Party of America, founded in 1901 and formally established as the Socialist Party USA in 1973 (successor to the…

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
