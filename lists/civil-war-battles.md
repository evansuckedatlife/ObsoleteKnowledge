---
type: list
category: history
read: false
---

# Civil War battles

The Civil War battles most worth knowing for quiz bowl.

## nodes

- [[battle-of-antietam|Battle of Antietam]] — The Battle of Antietam (September 17, 1862), also known as the Battle of Sharpsburg, was the bloodiest single day in American…
- [[battle-of-chancellorsville|Battle of Chancellorsville]] — The Battle of Chancellorsville (April 30–May 6, 1863) was a Confederate tactical masterpiece in which Robert E.
- [[battle-of-chickamauga|Battle of Chickamauga]] — The Battle of Chickamauga (September 18–20, 1863) was the second-bloodiest battle of the American Civil War, fought in…
- [[battle-of-fredericksburg|Battle of Fredericksburg]] — The Battle of Fredericksburg (December 11–15, 1862) was a major Confederate victory fought in and around the town of…
- [[battle-of-gettysburg|Battle of Gettysburg]] — The Battle of Gettysburg (July 1–3, 1863) was the largest and most significant battle of the American Civil War, fought in and…
- [[battle-of-hampton-roads|Battle of Hampton Roads]] — The Battle of Hampton Roads (March 8–9, 1862) was a pivotal naval engagement fought off the coast of Virginia in which two…
- [[battle-of-shiloh|Battle of Shiloh]] — The Battle of Shiloh (April 6–7, 1862), fought near a small Methodist church in southwestern Tennessee, shocked both North and…
- [[first-battle-of-bull-run|First Battle of Bull Run]] — The First Battle of Bull Run (July 21, 1861), also called the First Battle of Manassas, was the first major land battle of the…
- [[fort-sumter|Fort Sumter]] — Fort Sumter, a federal garrison in Charleston Harbor, South Carolina, was the site of the opening engagement of the American…
- [[siege-of-vicksburg|Siege of Vicksburg]] — The Siege of Vicksburg (May 22–July 4, 1863) was a prolonged Union campaign to capture the fortified city of Vicksburg,…

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
