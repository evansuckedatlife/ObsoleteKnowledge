---
type: concept
category: mathematics
defines: [Extreme Value Theorem, EVT]
related: ["[[continuous-functions]]", "[[continuity]]", "[[closed-interval]]", "[[limit]]", "[[topology]]", "[[compactness]]"]
requires: ["[[continuous-functions]]"]
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Extreme Value Theorem

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

The **Extreme Value Theorem** (EVT) asserts that a continuous function on a closed and bounded interval *[a, b]* attains both a maximum and a minimum value. This seemingly obvious fact is profound: it connects the algebraic property of continuity to the geometric existence of extreme points, and it is false in weaker settings (e.g., on open intervals or for discontinuous functions). The EVT is a cornerstone of calculus, enabling existence proofs and optimization algorithms.

## you gotta know

- *Statement*: If f is continuous on [a, b], then f achieves a maximum value M and minimum value m on [a, b].
- Requires both *continuity* (the function has no jumps or discontinuities) and *closure* (the interval must include its endpoints [a, b], not just open endpoints); EVT fails if either is absent.
- On an open interval (a, b), a continuous function may not achieve its supremum or infimum—e.g., f(x) = x on (0, 1) approaches but never reaches 1, and approaches but never reaches 0.
- The proof relies on the *Heine-Borel theorem*: closed and bounded sets in ℝ are compact, and continuous images of compact sets are compact; this compactness preserves the existence of extrema.
- EVT guarantees that optimization problems have solutions: no need to worry that a function merely approaches a bound without reaching it; the maximum and minimum actually occur at some points.
- The proof essentially combines compactness (closed/bounded sets in ℝ) with continuity (functions preserve the topological property of compactness), ensuring image sets are compact and thus bounded and closed.
- Used in the proof of the *Intermediate Value Theorem* and in analysis of critical points for calculus; both depend on the existence properties that EVT establishes.
- Generalizes to compact sets in any metric space or topological space: continuous functions on compact spaces are bounded and attain their extrema, making EVT a cornerstone of topology and analysis.
- Applications span optimization (calculus, economics), numerical analysis (finding global minima), and physics (principle of least energy).

## connections

- [[continuous-functions]] — continuity is necessary; discontinuous functions may fail to attain extrema.
- [[continuity]] — the fundamental property enabling the theorem's conclusion.
- [[closed-interval]] — closure is essential; open intervals do not suffice.
- [[intermediate-value-theorem]] — related existence result, also grounded in continuity.
- [[compactness]] — the topological property that underlies EVT in the most general setting.
- [[limit]] — limits formalize the continuity assumption on which EVT depends.

## see also

[[continuous-functions]] · [[intermediate-value-theorem]] · [[compactness]] · [[closed-interval]]

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

Lists: [[mathematics-hubs]] · Mark read: `INPUT[toggle:read]`
