---
type: list
category: history
read: false
---

# campaigns in the Pacific Theater of World War II

The campaigns in the Pacific Theater of World War II most worth knowing for quiz bowl.

## nodes

- [[attack-on-pearl-harbor|Attack on Pearl Harbor]] — On December 7, 1941, the Japanese Imperial Navy launched a surprise attack on the United States naval base at Pearl Harbor,…
- [[bataan-death-march|Bataan Death March]] — Following the fall of the Bataan Peninsula in the Philippines in April 1942, Japanese forces conducted a brutal forced march…
- [[battle-of-guadalcanal|Battle of Guadalcanal]] — Fought August 1942 to February 1943, Guadalcanal was the first major ground offensive launched by the Allies in the Pacific.
- [[battle-of-iwo-jima|Battle of Iwo Jima]] — Fought February–March 1945, the Battle of Iwo Jima saw American forces assault one of the most heavily fortified Japanese…
- [[battle-of-leyte-gulf|Battle of Leyte Gulf]] — Fought October 23–26, 1944 in the waters around the Philippine island of Leyte, this battle ranks as the largest naval…
- [[battle-of-midway|Battle of Midway]] — Fought June 4–7, 1942, the Battle of Midway stands as the turning point of the Pacific War.
- [[battle-of-okinawa|Battle of Okinawa]] — The longest and costliest of the Pacific island campaigns, Okinawa (April–June 1945) saw American forces battle a Japanese…
- [[battle-of-saipan|Battle of Saipan]] — Fought June–July 1944 in the Mariana Islands, the Battle of Saipan saw American forces capture a strategic island within…
- [[battle-of-tarawa|Battle of Tarawa]] — Fought November 20–23, 1943, the Battle of Tarawa was the first major amphibious assault by American forces against a heavily…
- [[battle-of-the-coral-sea|Battle of the Coral Sea]] — Fought in May 1942 between American and Japanese naval forces in the Coral Sea east of Australia, this battle marked the first…

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
