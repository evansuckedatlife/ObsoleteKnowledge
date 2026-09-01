---
type: process
category: science
defines: [Nerve transmission, action potential, synaptic transmission, neural signaling]
related: ["[[muscle-contraction]]", "[[potassium]]", "[[sodium]]", "[[neurotransmitter]]", "[[ion-channel]]"]
requires: ["[[ion]]", "[[potassium]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Nerve transmission

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Nerve transmission** is the propagation of electrical and chemical signals along neurons, enabling rapid communication throughout the nervous system. The process relies on ion gradients maintained across the cell membrane (high potassium inside, high sodium outside) and on gated ion channels that open and close in response to voltage changes. An electrical impulse (action potential) travels along the axon at high speed; at the synapse, the impulse triggers neurotransmitter release, which bridges the gap to the next neuron, regenerating the electrical signal downstream. This mechanism underlies all sensation, movement, and thought.

## you gotta know

- The *resting potential* (typically −70 mV) arises from the Na/K pump maintaining a concentration gradient: ~140 mM [[potassium|K⁺]] inside, ~5 mM outside; ~10 mM [[sodium|Na⁺]] inside, ~145 mM outside.
- *Depolarization* begins when a stimulus (sensory input or input from another neuron) opens sodium channels; Na⁺ floods in, driving the membrane voltage positive, reaching peak depolarization (~+30 mV).
- The **action potential** is a stereotyped all-or-nothing voltage spike: depolarization opens more sodium channels (positive feedback); inactivation gates then close sodium channels while delayed potassium channels open, allowing K⁺ efflux to restore negative voltage.
- The *refractory period* (absolute and relative) prevents backward signal propagation: sodium channels remain inactivated for ~2 ms (absolute), making the neuron temporarily unresponsive; potassium channels remain open slightly longer (relative), hyperpolarizing the neuron and requiring stronger stimuli to fire.
- *Propagation* along the axon is fastest in myelinated axons, where myelin insulation (formed by glial cells) allows voltage changes to depolarize distant segments directly, jumping between nodes of Ranvier at speeds up to 120 m/s.
- **Synaptic transmission** converts electrical signals to chemical: the action potential opens calcium channels at the axon terminal, Ca²⁺ influx triggers exocytosis of neurotransmitter-filled vesicles into the synaptic cleft.
- *Neurotransmitter* molecules bind receptors on the postsynaptic cell, opening ion channels there and either exciting (depolarizing) or inhibiting (hyperpolarizing) the downstream neuron.
- Neurotransmitter recycling and [[muscle-contraction|motor control]] depend on this cascade: each synapse sums excitatory and inhibitory inputs, determining whether the postsynaptic neuron fires.

## connections

- [[muscle-contraction]] — nerve signals at the neuromuscular junction trigger muscle contraction via acetylcholine release.
- [[potassium]] — an intracellular ion whose efflux repolarizes the neuron after depolarization.
- [[sodium]] — an extracellular ion whose influx depolarizes the neuron during the action potential.
- [[ion-channel]] — the molecular gates controlling ion flow during nerve transmission.
- [[neurotransmitter]] — the chemical messenger released at synapses to signal downstream neurons.

## see also

[[muscle-contraction]] · [[potassium]] · [[sodium]] · [[neurotransmitter]]

<!-- crosslinks -->
```dataviewjs
dv.view("_dv/crosslinks")
```
<!-- /crosslinks -->

<!-- tournav -->
```dataviewjs
dv.view("_dv/tournav")
```
<!-- /tournav -->

<!-- footer -->

---

Lists: [[science-hubs]] · Mark read: `INPUT[toggle:read]`
