---
type: concept
category: science
defines: [Back-EMF, counter-electromotive force, back electromotive force]
related: ["[[resistor]]", "[[electron]]", "[[central-processing-unit]]", "[[motherboard]]", "[[industrial-revolution]]", "[[barrier-penetration]]", "[[backtracking]]"]
requires: ["[[resistor]]", "[[electron]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Back-EMF

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Back-EMF**, also termed **counter-electromotive force** or **back electromotive force**, is the induced voltage in an electrical circuit or electromechanical system that opposes the driving voltage or the instantaneous change in current. Governed fundamentally by *Faraday's law of induction* and *Lenz's law*, it develops whenever magnetic flux linkages vary within an inductive coil or rotating armature. The phenomenon acts as an inherent negative feedback mechanism in electric motors and generators, limiting the operational current drawn under steady state while generating an extreme inductive voltage spike when an inductor's current is forced to change rapidly.

## you gotta know

- Arises directly from *Lenz's law*, which dictates that the direction of any induced electromotive force opposes the change in magnetic flux that generated it, thereby satisfying the physical principle of conservation of energy.
- Quantified in an ideal inductor by the relationship $\mathcal{E} = -L (dI/dt)$, where self-inductance $L$ scales the magnitude of the opposing potential created by the temporal derivative of current.
- Generates high-voltage transients called inductive kickback when an inductive circuit is abruptly opened with a mechanical switch or transistor, causing severe electrical arcing or dielectric breakdown if not suppressed.
- Suppressed in modern electronics by connecting a flyback diode, also called a snubber diode or freewheeling diode, antiparallel across the inductive coil to route decaying currents safely through a [[resistor]].
- Regulates the armature current in electric motors, where the magnitude of the counter-voltage scales proportionally with rotor angular velocity; at zero rotational velocity during startup or rotor stall, the absence of this opposing voltage causes the motor to draw its highest current, known as the stall current.
- Enables sensorless motor commutation in modern electronics, where microcontrollers in a [[central-processing-unit]] monitor the zero-crossing points of the counter-voltage in unenergized motor coils to infer rotor orientation without physical sensors.
- Demonstrated classically through the *jumping ring experiment* devised by *Elihu Thomson*, where alternating currents in an iron-core solenoid project an aluminum ring into the air through mutual inductive repulsion.
- Causes counter-torque in electrical generators according to *Fleming's right-hand rule*, requiring mechanical prime movers such as steam turbines developed during the [[industrial-revolution]] to supply continuous mechanical power.

## connections

- [[resistor]] — placed alongside flyback diodes in snubber circuits to dissipate inductive kickback energy as heat.
- [[electron]] — the charged subatomic particles whose acceleration produces varying magnetic fields that induce the opposing electric field.
- [[central-processing-unit]] — relies on complex power management and filtration stages to isolate sensitive silicon transistors from motor inductive spikes.
- [[motherboard]] — features dedicated choke filters and suppression diodes to prevent transient kickback voltages from corrupting bus lines.
- [[industrial-revolution]] — transformed by dynamos and heavy electric traction motors whose operating limits and torque curves are dictated by counter-electromotive force.
- [[barrier-penetration]] — high-voltage inductive kickback spikes can exceed dielectric insulation limits, precipitating breakdown via quantum tunneling and avalanche conduction.
- [[backtracking]] — utilized in automated circuit board routing algorithms to optimize trace geometries and minimize parasitic loop inductance.

## see also

- [[resistor]] · [[motherboard]] · [[central-processing-unit]] · [[barrier-penetration]] · [[backtracking]]

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
