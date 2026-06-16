---
type: list
category: history
read: false
---

# World War II battles

The World War II battles most worth knowing for quiz bowl.

## nodes

- [[battle-of-anzio|Battle of Anzio]] — The Battle of Anzio (January–May 1944), codenamed Operation Shingle, was an Allied amphibious assault on the Italian coast…
- [[battle-of-britain|Battle of Britain]] — The Battle of Britain (July–October 1940) was an aerial campaign in which the German Luftwaffe sought to achieve air…
- [[battle-of-el-alamein|Battle of El Alamein]] — The Battle of El Alamein (October–November 1942) was a desert warfare engagement in Egypt between the British Eighth Army and…
- [[battle-of-kursk|Battle of Kursk]] — The Battle of Kursk (July–August 1943) was the largest tank engagement in history, fought in southern Russia over a bulging…
- [[battle-of-monte-cassino|Battle of Monte Cassino]] — The Battle of Monte Cassino (January–May 1944) was a four-month campaign by Allied forces to capture the strategic height…
- [[battle-of-normandy|Battle of Normandy]] — The Battle of Normandy (June–August 1944), codenamed Operation Overlord, was the largest amphibious invasion in history: over…
- [[battle-of-stalingrad|Battle of Stalingrad]] — The Battle of Stalingrad (August 1942 – February 1943) was a sprawling urban combat between Nazi Germany and the Soviet Union…
- [[battle-of-the-atlantic|Battle of the Atlantic]] — The Battle of the Atlantic (September 1939 – May 1945) was a prolonged naval and aerial struggle for control of the sea lanes…
- [[battle-of-the-bulge|Battle of the Bulge]] — The Battle of the Bulge (December 1944 – January 1945), Germany's last major offensive, was a desperate winter assault through…
- [[operation-barbarossa|Operation Barbarossa]] — Operation Barbarossa (June 1941 – November 1942) was Nazi Germany's massive invasion of the Soviet Union, the largest military…

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
