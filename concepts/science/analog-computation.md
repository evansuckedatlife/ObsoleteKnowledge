---
type: concept
category: science
defines: [analog-computation, analog computer, differential analyzer]
related: ["[[amplifier]]", "[[analog-to-digital]]", "[[algorithm]]", "[[central-processing-unit]]", "[[cold-war]]", "[[world-war-ii]]", "[[resistor]]"]
requires: ["[[resistor]]", "[[central-processing-unit]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# analog-computation

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Analog-computation** is a computational paradigm that models dynamic mathematical systems by exploiting the continuous physical properties of electrical, mechanical, or hydraulic media rather than manipulating symbolic discrete bits. Peaking in utility between the 1930s and 1970s, an **analog computer** maps continuous variables directly onto voltages, currents, or shaft rotations to solve complex systems of ordinary differential equations in real time. Though largely displaced by general-purpose digital computers, the paradigm remains historically vital for engineering simulations and is currently seeing renewed research interest in neuromorphic hardware.

## you gotta know

- Computes by constructing direct physical analogies of mathematical models, allowing equations describing physics, fluid dynamics, and mechanics to be solved instantaneously without step-by-step numerical approximation.
- Traces its mechanical origins to nineteenth-century devices like *James Thomson's* ball-and-disk integrator and *Vannevar Bush's* electromechanical **differential analyzer**, developed at *MIT* to compute firing tables and network power distributions.
- Relies in electronic implementations on the operational **amplifier**, which can be configured with external passive components like a precision **resistor** or capacitor to perform addition, inversion, scaling, and calculus operations like continuous time integration.
- Configured physically by human operators using patch cords, potentiometers, and plugboards to wire together functional blocks into a feedback topology representing a specific system of differential equations.
- Excels at real-time closed-loop simulation of dynamic systems, seeing extensive deployment in aerospace engineering, flight simulators, ballistic missile trajectories, and nuclear reactor control.
- Suffers from fundamental physical limitations compared to digital machines, including thermal noise, component drift, contact resistance, and calibration error, which restrict typical computational precision to three or four significant figures.
- Gradually phased out through the advent of high-speed digital processors and accurate **analog-to-digital** converters, which offered exact software programmability and arbitrary mathematical precision.

## connections

- [[amplifier]] — the primary active building block that carries out mathematical operations like integration and summing through negative feedback.
- [[analog-to-digital]] — the interface technology that allowed hybrid systems to bridge continuous analog setups with discrete digital processors.
- [[resistor]] — forms calibrated input and feedback paths that set the mathematical coefficients of analog summing and scaling stages.
- [[central-processing-unit]] — the discrete digital architecture whose exponential growth in performance and programmability rendered general-purpose analog machines obsolete.
- [[algorithm]] — digital numerical integration techniques eventually replaced direct circuit emulation of differential equations.
- [[cold-war]] — fueled massive government and military investment in analog simulators for supersonic aerodynamics, radar, and rocketry.
- [[world-war-ii]] — saw widespread deployment of mechanical and electromechanical analog computers for naval gun directors and artillery fire control.

## see also

- [[amplifier]] · [[analog-to-digital]] · [[central-processing-unit]]

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
