---
type: list
category: history
read: false
---

# Napoleonic battles

The Napoleonic battles most worth knowing for quiz bowl.

## nodes

- [[battle-of-austerlitz|Battle of Austerlitz]] — The Battle of Austerlitz on December 2, 1805, was one of Napoleon's greatest tactical masterpieces, in which he defeated a…
- [[battle-of-borodino|Battle of Borodino]] — The Battle of Borodino on September 7, 1812, was the largest and bloodiest engagement of the Napoleonic Wars, fought between…
- [[battle-of-friedland|Battle of Friedland]] — The Battle of Friedland on June 14, 1807, was Napoleon's decisive victory over the Russian army under General Levin Bennigsen…
- [[battle-of-jena-auerstedt|Battle of Jena-Auerstedt]] — The Battle of Jena-Auerstedt on October 14, 1806, was actually two simultaneous battles fought by Napoleon's army against the…
- [[battle-of-leipzig|Battle of Leipzig]] — The Battle of Leipzig, fought October 16–19, 1813, was called the "Battle of the Nations" and is considered the largest land…
- [[battle-of-marengo|Battle of Marengo]] — The Battle of Marengo on June 14, 1800, was one of Napoleon's most celebrated early victories, fought in the Piedmont region…
- [[battle-of-the-nile|Battle of the Nile]] — The Battle of the Nile (also called the Battle of Aboukir Bay) on August 1, 1798, was a crushing naval defeat for the French…
- [[battle-of-trafalgar|Battle of Trafalgar]] — The naval Battle of Trafalgar on October 21, 1805, off the coast of Spain, was fought between the combined French and Spanish…
- [[battle-of-wagram|Battle of Wagram]] — The Battle of Wagram on July 5–6, 1809, was Napoleon's hard-fought victory over the Austrian army under Archduke Charles near…
- [[battle-of-waterloo|Battle of Waterloo]] — The decisive defeat of Napoleon on June 18, 1815, near the village of Waterloo in present-day Belgium, ended his Hundred Days…

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
