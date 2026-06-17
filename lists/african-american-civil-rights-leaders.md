---
type: list
category: history
read: false
---

# African-American civil rights leaders

The African-American civil rights leaders most worth knowing for quiz bowl.

## nodes

- [[booker-t-washington|Booker T. Washington]] — Booker T.
- [[ella-baker|Ella Baker]] — Ella Baker was a legendary grassroots organizer who spent over 50 years building democratic movements from the ground up,…
- [[frederick-douglass|Frederick Douglass]] — Frederick Douglass was a formerly enslaved person who became one of the most influential orators and intellectuals of the 19th…
- [[john-lewis|John Lewis]] — John Lewis (1940–2020) was a towering figure of the civil rights movement who transitioned from Freedom Rider and march…
- [[malcolm-x|Malcolm X]] — Malcolm X was a Muslim minister and human rights activist who challenged the integrationist strategy of the Civil Rights…
- [[martin-luther-king-jr|Martin Luther King Jr.]] — Martin Luther King Jr.
- [[medgar-evers|Medgar Evers]] — Medgar Evers was a field organizer for the NAACP in Mississippi and one of the most effective civil rights leaders of the…
- [[rosa-parks|Rosa Parks]] — Rosa Parks was an African-American civil rights activist whose refusal to surrender her bus seat to a white passenger in…
- [[shirley-chisholm|Shirley Chisholm]] — Shirley Chisholm (1924–2005) was the first Black woman elected to Congress, representing Brooklyn from 1969 to 1983.
- [[thurgood-marshall|Thurgood Marshall]] — Thurgood Marshall was a pioneering civil rights lawyer who became the first African-American Supreme Court Justice, using the…
- [[w-e-b-du-bois|W.E.B. Du Bois]] — W.E.B.

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
