---
type: list
category: science
read: false
---

# circuit components

The circuit components most worth knowing for quiz bowl.

## nodes

- [[capacitor|Capacitor]] — A capacitor is a two-terminal passive component that stores electrical energy in an electric field between two conducting…
- [[diode|Diode]] — A diode is a two-terminal semiconductor device constructed from a PN junction (p-type and n-type silicon fused together) that…
- [[fuse-circuit-breaker|Fuse and Circuit Breaker]] — Fuses and circuit breakers are safety devices that interrupt current flow when it exceeds a rated threshold, protecting…
- [[ground|Ground]] — Ground is an arbitrary reference point in a circuit assigned zero volts, against which all other voltages are measured.
- [[inductor|Inductor]] — An inductor is a two-terminal passive component that stores electrical energy in a magnetic field created by current flowing…
- [[led|LED]] — An LED (light-emitting diode) is a semiconductor diode that emits light when forward-biased, converting electrical current…
- [[op-amp|Op-Amp]] — An op-amp (operational amplifier) is an integrated circuit containing a high-gain differential amplifier with very high input…
- [[rectifier|Rectifier]] — A rectifier is a circuit that converts alternating current (AC) into direct current (DC) using one or more diodes to allow…
- [[resistor|Resistor]] — A resistor is a two-terminal passive component that opposes the flow of electric current, dissipating electrical energy as heat.
- [[source|Source]] — A source is an active circuit element that supplies electrical energy to a circuit.
- [[switch|Switch]] — A switch is a mechanical or electronic component that opens or closes a circuit path, controlling whether current can flow.
- [[transformer|Transformer]] — A transformer is a passive component consisting of two or more inductively coupled coils wound on a shared magnetic core, used…

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
