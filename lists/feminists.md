---
type: list
category: history
read: false
---

# feminists

The feminists most worth knowing for quiz bowl.

## nodes

- [[bell-hooks|bell hooks]] — bell hooks (1952–2023), born Gloria Jean Watkins, was an American writer and critical theorist who brought rigorous analysis…
- [[betty-friedan|Betty Friedan]] — Betty Friedan (1921–2006) was an American feminist writer whose The Feminine Mystique (1963) ignited second-wave feminism by…
- [[elizabeth-cady-stanton|Elizabeth Cady Stanton]] — Elizabeth Cady Stanton (1815–1902) was an American women's rights pioneer whose Declaration of Sentiments at the 1848 Seneca…
- [[emmeline-pankhurst|Emmeline Pankhurst]] — Emmeline Pankhurst (1858–1928) was a British suffragist and leader of the Women's Social and Political Union (WSPU), which…
- [[germaine-greer|Germaine Greer]] — Germaine Greer (born 1939) is an Australian-British writer and cultural critic whose The Female Eunuch (1970) became a…
- [[gloria-steinem|Gloria Steinem]] — Gloria Steinem (born 1934) is an American feminist activist, writer, and editor whose career spanned grassroots organizing,…
- [[judith-butler|Judith Butler]] — Judith Butler (born 1956) is an American philosopher whose Gender Trouble (1990) fundamentally transformed feminist and queer…
- [[margaret-sanger|Margaret Sanger]] — Margaret Sanger (1879–1966) was an American birth control activist who devoted her life to making contraception legal,…
- [[mary-wollstonecraft|Mary Wollstonecraft]] — Mary Wollstonecraft (1759–1797) was an English writer and philosopher whose A Vindication of the Rights of Woman (1792) became…
- [[simone-de-beauvoir|Simone de Beauvoir]] — Simone de Beauvoir (1908–1986) was a French existentialist philosopher whose The Second Sex (1949) became the canonical text…
- [[sojourner-truth|Sojourner Truth]] — Sojourner Truth (c.
- [[susan-b-anthony|Susan B. Anthony]] — Susan B.

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
