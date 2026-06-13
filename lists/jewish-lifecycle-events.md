---
type: list
category: religion
read: false
---

# Jewish Lifecycle Events

The rites marking birth, coming of age, marriage, death, and conversion in Judaism.

## nodes

- [[bar-bat-mitzvah|Bar/bat mitzvah]] — Bar mitzvah (son of commandment) and bat mitzvah (daughter of commandment) are coming-of-age ceremonies marking a young…
- [[brit-milah|Brit milah]] — Brit milah is the circumcision ceremony that welcomes a newborn Jewish boy into the covenant community.
- [[jewish-baby-naming|Jewish baby naming]] — Jewish baby naming refers to the ceremonies that formally welcome a newborn into the Jewish community and assign a Hebrew name.
- [[jewish-confirmation|Jewish confirmation]] — Jewish confirmation is a ceremony reaffirming religious commitment and Jewish identity, typically held in Reform and…
- [[jewish-conversion|Jewish conversion]] — Jewish conversion (giyur) is the formal process by which a non-Jew becomes a member of the Jewish people, adopting Jewish…
- [[jewish-death|Jewish death and burial]] — Jewish death and burial practices reflect values of dignity, simplicity, and respect for the deceased.
- [[jewish-divorce|Jewish divorce]] — Jewish divorce (gerushin) is the legal dissolution of a Jewish marriage according to halakha (Jewish law).
- [[jewish-marriage|Jewish marriage]] — Jewish marriage (kiddushin) is a covenant between two partners sanctified by Jewish law and ritual.
- [[jewish-mourning|Jewish mourning]] — Jewish mourning is a structured system of rituals and practices honoring the deceased and supporting the bereaved.
- [[pidyon-haben|Pidyon ha-ben]] — Pidyon ha-ben (redemption of the firstborn) is a ceremony in which the parents of a firstborn son symbolically "redeem" him…

## progress

Live read-status for this list (requires the **Bases** core plugin). Flip a node's `read` from its footer toggle and it moves here.

```base
filters:
  and:
    - lists.containsLinkTo(this.file.asLink())
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

## source

Scoped from NAQT's *You Gotta Know* topic [`jewish-lifecycle-events`](https://www.naqt.com/you-gotta-know/jewish-lifecycle-events.html). Content authored originally; NAQT used as a topic map only.
