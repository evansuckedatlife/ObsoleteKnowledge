---
type: concept
category: science
defines: [Backtracking, backtrack search]
related: ["[[algorithm]]", "[[central-processing-unit]]", "[[motherboard]]", "[[bacteriophage]]", "[[barrier-penetration]]", "[[back-emf]]"]
requires: ["[[algorithm]]"]
lists: ["[[science-hubs]]"]
tour_order: 0
read: false
---

# Backtracking

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**Backtracking**, often referred to as **backtrack search**, is an algorithmic paradigm that systematically searches for solutions to combinatorial and constraint satisfaction problems by constructing candidate solutions incrementally and abandoning each candidate as soon as it determines it cannot be extended to a valid final solution. Coined by American mathematician *D. H. Lehmer* in the 1950s and formalized by *Solomon W. Golomb* and *Leonard D. Baumert*, it conceptualizes the search space as an implicit decision tree explored via recursive depth-first traversal. The method is fundamental to computer science, powering satisfiability solvers, logic programming engines, automated planning, and operations research.

## you gotta know

- Operates via recursive exploration of solution spaces, traversing down a state-space tree by making tentative assignments and immediately retreating to the preceding decision point when a constraint violation is detected.
- Prunes entire subtrees of the state space that cannot yield feasible completions, making it drastically more efficient than naive brute-force exhaustive enumeration.
- Illustrated classically through the *N-queens puzzle*, in which $N$ non-attacking chess queens are placed on an $N \times N$ board column-by-column, backtracking to reposition previous queens whenever a newly placed queen is threatened.
- Underpins modern conflict-driven clause learning (*CDCL*) solvers for the *Boolean satisfiability* (*SAT*) problem, which implement non-chronological backtracking (backjumping) to bypass multiple tree levels upon discovering a logical conflict.
- Combines with bounding functions in the *branch-and-bound* paradigm, which solves combinatorial optimization problems like the *traveling salesperson problem* and the *knapsack problem* by pruning subtrees whose theoretical bound cannot exceed the best known solution.
- Forms the execution engine of logic programming languages such as *Prolog*, where automatic goal resolution relies on unification and depth-first search with backtracking to query relation databases.
- Extensively employed in compiler design to implement predictive recursive descent parsers and syntax analyzers that must roll back when a grammar production rule fails to match input tokens.
- Deployed in computational genomics and bioinformatics to trace optimal alignment paths across dynamic programming matrices, as when mapping sequence matches in a [[bacteriophage]] genome.

## connections

- [[algorithm]] — the computational category of formal problem-solving procedures of which backtracking is a foundational search and constraint-satisfaction technique.
- [[central-processing-unit]] — executes recursive search calls, with stack performance and branch prediction efficiency heavily impacting the execution speed of backtracking routines.
- [[motherboard]] — printed circuit board layout tools use backtracking and routing algorithms to determine non-colliding traces across multiple substrate layers.
- [[bacteriophage]] — dynamic programming algorithms utilize backtracking pointers to reconstruct full nucleotide alignments and phylogenetic relationships among phage variants.
- [[barrier-penetration]] — represents a physical process where quantum annealing can explore energy landscapes and tunnel past local maxima that force classical algorithms to backtrack.
- [[back-emf]] — automated circuit synthesis tools run backtrack searches to place snubber networks and inductors that mitigate inductive counter-voltages.

## see also

- [[algorithm]] · [[central-processing-unit]] · [[motherboard]] · [[bacteriophage]] · [[barrier-penetration]] · [[back-emf]]

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
