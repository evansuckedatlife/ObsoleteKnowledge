---
type: concept
category: mathematics
defines: [probability, "probability theory"]
related: ["[[pascal]]", "[[pierre-de-fermat]]", "[[pascal-triangle]]", "[[statistics]]", "[[combinatorics]]"]
requires: []
lists: ["[[mathematics-hubs]]"]
tour_order: 0
read: false
---

# Probability

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Probability** is the mathematical study of chance and uncertainty, quantifying how likely an event is to occur. Born from Pascal and Fermat's correspondence on games of chance in the 1650s, probability theory transformed random phenomena into a rigorous science. It underpins statistics, physics, and modern finance.

## you gotta know

- A probability is a number between 0 and 1 (or 0% to 100%) representing the likelihood of an event; 0 means impossible, 1 means certain.
- For equally likely outcomes, probability = (favourable outcomes) / (total outcomes); this classical definition works for dice rolls, card draws, and symmetric games.
- Blaise Pascal and Pierre de Fermat solved the "problem of points"—dividing stakes in an unfinished game—by calculating expected value, founding the subject in rigorous form.
- The law of large numbers states that as an experiment repeats, the observed frequency approaches the theoretical probability; this connects empirical observation to theory.
- The addition rule: P(A or B) = P(A) + P(B) − P(A and B); the multiplication rule for independent events: P(A and B) = P(A) × P(B).
- Conditional probability P(A|B) = P(A and B) / P(B) models how information updates probability; this leads to Bayes' theorem, which is fundamental to statistics and machine learning.
- The binomial distribution models the number of successes in *n* independent trials with constant probability *p*; its mean is np and variance is np(1−p).
- Expected value is the weighted average of outcomes: E[X] = Σ x·P(x); understanding expected value is essential for rational decision-making under uncertainty.
- The normal distribution, also called the Gaussian distribution, emerges as a limiting case via the central limit theorem and governs many natural phenomena.
- Independent events are those where P(A and B) = P(A)P(B); recognizing independence simplifies calculations and is critical in probability modeling.
- Randomness and determinism coexist in probability; even deterministic systems can exhibit probabilistic behaviour when initial conditions are unknown.

## connections

- [[pascal]] — co-founder of probability theory through his correspondence with Fermat.
- [[pierre-de-fermat]] — co-founder of probability; his work with Pascal on the problem of points was revolutionary.
- [[pascal-triangle]] — a combinatorial structure Pascal studied; its rows give binomial coefficients essential to probability.
- [[statistics]] — applies probability to draw inferences from data.
- [[combinatorics]] — underpins probability by counting outcomes.

## see also

- [[pascal]] · [[pierre-de-fermat]] · [[statistics]] · [[combinatorics]]

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
