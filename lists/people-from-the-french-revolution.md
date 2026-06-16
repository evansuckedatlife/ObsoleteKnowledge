---
type: list
category: history
read: false
---

# people from the French Revolution

The people from the French Revolution most worth knowing for quiz bowl.

## nodes

- [[charlotte-corday|Charlotte Corday]] — Charlotte Corday (1768–1793), a noblewoman and royalist sympathizer, assassinated the radical journalist Jean-Paul Marat in…
- [[danton|Danton]] — Georges Danton (1759–1794) was a charismatic revolutionary leader who rose to prominence during the early radical phase of the…
- [[louis-xvi|Louis XVI]] — Louis XVI (1754–1793), the last Bourbon king of France, inherited the throne at a moment of fiscal crisis and deep social…
- [[marat|Marat]] — Jean-Paul Marat (1743–1793) was a radical journalist and physician whose inflammatory publications and fiery speeches drove…
- [[marie-antoinette|Marie Antoinette]] — Marie Antoinette (1755–1793), wife of Louis XVI, was an Austrian-born queen whose perceived extravagance and foreign origins…
- [[marquis-de-lafayette|Marquis de Lafayette]] — The Marquis de Lafayette (1757–1834), born Gilbert du Motier, was a noble reformer and military hero who championed both the…
- [[mirabeau|Mirabeau]] — Honoré-Gabriel Riqueti, Comte de Mirabeau (1749–1791) was the French Revolution's most brilliant and charismatic orator in its…
- [[napoleon-bonaparte|Napoleon Bonaparte]] — Napoleon Bonaparte (1769–1821) rose from Corsican obscurity to become the French Revolution's greatest military hero and…
- [[robespierre|Robespierre]] — Maximilien Robespierre (1758–1794) was the architect of the Reign of Terror, wielding unprecedented power during the French…
- [[saint-just|Saint-Just]] — Louis-Antoine de Saint-Just (1767–1794) was a radical revolutionary and Robespierre's closest political ally, serving as a key…

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
