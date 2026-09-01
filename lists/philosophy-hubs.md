---
type: list
category: philosophy
read: false
---

# Philosophy hubs

Branches, problems and positions the individual philosophers argue about.

## nodes

- [[antisthenes|Antisthenes]] — Antisthenes (c.
- [[free-will|Free Will]] — Free will is the philosophical question of whether humans have the capacity to make choices that are not entirely determined by prior causes, natural …
- [[friedrich-nietzsche|Friedrich Nietzsche]] — Friedrich Nietzsche (1844–1900) was a German philosopher whose radical critique of Western morality, reason, and religion fundamentally reshaped moder…
- [[jean-paul-sartre|Jean-Paul Sartre]] — Jean-Paul Sartre (1905–1980) was a French philosopher, novelist, and political activist who became the public face of existentialism in the mid-20th c…
- [[martin-heidegger|Martin Heidegger]] — Martin Heidegger (1889–1976) was a German philosopher who radically transformed the study of Being and human existence through phenomenology and exist…
- [[mathematics|Mathematics]] — Mathematics is the study of abstract entities—numbers, shapes, and logical relationships—governed by proof and axioms rather than empirical observatio…
- [[meaning|Meaning]] — Meaning in philosophy concerns the significance, purpose, or intelligibility that humans perceive in existence, actions, and the world.
- [[medieval-philosophy|Medieval Philosophy]] — Medieval philosophy is the Western philosophical tradition spanning roughly the 5th to 15th centuries, dominated by the integration of Aristotelian lo…
- [[metaphysics|Metaphysics]] — Metaphysics is the philosophical inquiry into the fundamental nature of reality: what exists, what is the relationship between mind and matter, whethe…
- [[mind-body-problem|Mind-body problem]] — The mind-body problem is the central puzzle of modern philosophy of mind: how does consciousness—subjective, private, qualitative experience—relate to…
- [[morality|Morality]] — Morality is the system of principles concerning the distinction between right and wrong, good and bad action.
- [[neoplatonism|Neoplatonism]] — Neoplatonism is a philosophical school that reinterpreted Plato through a mystical, hierarchical lens, emerging in the 3rd century CE and dominating l…
- [[panpsychism|Panpsychism]] — Panpsychism is the philosophical view that consciousness or some form of experience is a fundamental and ubiquitous feature of the physical world—not …
- [[phenomenology|Phenomenology]] — Phenomenology is a philosophical method and discipline that investigates the structure of consciousness from the first-person perspective: what is it …
- [[qualia|Qualia]] — Qualia are the subjective, qualitative features of conscious experience—the way things feel or appear to you.
- [[reason|Reason]] — Reason is the faculty of mind that processes logic, derives conclusions from premises, and aspires to universal truth independent of sensory experienc…
- [[science|Science]] — Science is a systematic, empirical inquiry into the natural world governed by the scientific method: forming hypotheses, conducting experiments, and r…
- [[theology|Theology]] — Theology is the philosophical and rational inquiry into the nature of God, divine revelation, and humanity's relationship to the divine.

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
