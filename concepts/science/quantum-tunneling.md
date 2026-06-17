---
type: concept
category: science
defines: [Quantum tunneling, tunneling]
related: ["[[wavefunction]]", "[[uncertainty-principle]]", "[[barrier-penetration]]"]
requires: ["[[wavefunction]]", "[[uncertainty-principle]]", "[[schrodinger-equation]]"]
lists: ["[[quantum-mechanics-concepts]]"]
tour_order: 3
read: false
---

# Quantum tunneling


<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

Quantum tunneling is the phenomenon where a particle penetrates a potential barrier even when its total energy is less than the barrier height—classically impossible. The [[wavefunction]] does not vanish abruptly at a barrier edge but decays exponentially into the forbidden region, with a small but nonzero amplitude on the far side. This permits a probability of escape proportional to exp(−2κW), where κ depends on particle mass and W is barrier width.

## you gotta know

- A particle can escape a potential well or penetrate a barrier with energy E < V₀
- The tunneling probability is exponentially sensitive to barrier width and particle mass
- Electrons (small mass) tunnel readily; macroscopic objects (large mass) tunnel with vanishingly small probability
- Alpha decay of nuclei proceeds via tunneling through the Coulomb barrier
- Scanning tunneling microscopes exploit electron tunneling to image surfaces at atomic resolution
- Tunneling time is not well-defined; the particle does not "exist" in the barrier region
- [[uncertainty-principle]] permits energy violation for times Δt ~ ℏ/ΔE, which is relevant inside the barrier

## context

Tunneling results directly from the [[wavefunction]] description: the Schrödinger equation yields exponentially decaying solutions in classically forbidden regions (E < V). The probability of finding the particle beyond the barrier is small but never zero. Historically, tunneling explained radioactive decay (Gamow) and ionization rates in atoms. It is essential for semiconductor physics (tunnel diodes), quantum computing (tunneling rates set decoherence timescales), and biochemistry (enzyme-catalyzed reactions). The exponential sensitivity makes tunneling a precision probe of particle mass and barrier structure.

## connections

- [[wavefunction]] — extends into classically forbidden regions with exponential decay
- [[schrodinger-equation]] — yields tunneling solutions automatically
- [[uncertainty-principle]] — permits transient energy violations allowing barrier crossing
- [[alpha-decay]] — radioactive nuclei decay via alpha-particle tunneling
- [[barrier-penetration]] — quantifies tunneling probability vs. energy and width
- [[planck-constant]] — sets the scale of exponential decay rate
- [[quantum-mechanics]] — foundational: no tunneling in classical mechanics

## see also

- [[wavefunction]] · [[uncertainty-principle]] · [[schrodinger-equation]]

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

Lists: [[quantum-mechanics-concepts]] · Mark read: `INPUT[toggle:read]`
