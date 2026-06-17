---
type: term
category: mathematics
defines: [Sorting algorithm, comparison sort, merge sort, quicksort, stability]
related: ["[[algorithm]]", "[[big-o-notation]]", "[[divide-and-conquer]]", "[[recursion]]", "[[binary-search]]", "[[tree-data-structure]]", "[[time-complexity]]"]
lists: []
read: false
---

# Sorting Algorithm

## summary

A *sorting algorithm* is a procedure that arranges elements of a list into a specified order—usually ascending or descending. Sorting is one of the most fundamental and well-studied problems in computer science; dozens of algorithms exist, trading off time complexity, space complexity, stability (preserving relative order of equal elements), and cache behavior. Efficient sorting is essential for search (binary search requires sorted input), data analysis, and countless applications. The best comparison-based sorting algorithms achieve O(n log n) time; non-comparative sorting (counting sort, radix sort) can achieve O(n) under restrictive assumptions about the data.

## you gotta know

### Classic Comparison-Based Sorts
- *Merge sort*: divide-and-conquer; O(n log n) time, O(n) extra space, stable. Splits list in half recursively, merges sorted halves.
- *Quicksort*: divide-and-conquer; O(n log n) average, O(n²) worst-case, O(log n) space (for recursion stack), usually in-place. Partitions via a pivot; prone to worst-case on already-sorted input unless pivot selection is randomized.
- *Heap sort*: uses a heap; O(n log n) time, O(1) extra space, not stable. Builds a max-heap, repeatedly extracts maximum.
- *Insertion sort*: O(n²) time, O(1) space, stable, in-place. Efficient on small arrays and nearly-sorted data; used as a sub-algorithm in hybrid sorts like Timsort.
- *Bubble sort*: O(n²) time, O(1) space, stable, in-place. Repeatedly swaps adjacent out-of-order elements; rarely used in practice due to poor performance.

### Non-Comparative Sorts
- *Counting sort*: O(n + k) time where k is the range of input values; requires integer inputs in a small range; stable.
- *Radix sort*: O(n·d) where d is the number of digits; sorts by each digit position from least to most significant; stable; used for strings and large integers.
- *Bucket sort*: O(n + k) average case; distributes elements into buckets, sorts each bucket, concatenates results.

### Key Concepts
- *Stability*: a sort is stable if equal elements retain their original relative order; important for multi-key sorting (e.g., sort by name, then by age).
- *In-place*: a sort uses only O(1) extra space besides the input; merge sort requires O(n) space; quicksort is typically in-place.
- *Adaptive*: a sort is adaptive if its running time improves on nearly-sorted input (insertion sort is highly adaptive; Timsort exploits runs).
- *Comparison sorting lower bound*: any comparison-based sort requires Ω(n log n) comparisons in the worst case (information-theoretic argument: n! orderings require log₂(n!) ≈ n log n bits to distinguish).

### Modern Practice
- *Timsort*: hybrid of merge sort and insertion sort, used in Python and Java; O(n log n) worst-case, O(n) best-case on nearly-sorted data; stable.
- *Introsort*: hybrid of quicksort and heap sort; starts with quicksort, switches to heap sort if depth exceeds 2 log n; used in C++ std::sort.
- Most practical systems use adaptive, hybrid algorithms tuned for real-world distributions and cache behavior.

## context

Sorting is a canonical problem in computer science: it teaches fundamental algorithmic thinking, Big O analysis, and divide-and-conquer strategy. The problem is so well-studied that it serves as a benchmark for new algorithmic techniques and hardware: the first practical analog computers, the earliest electronic computers (ENIAC), and modern GPUs are all measured partly on their sorting throughput. The transition from O(n²) algorithms (bubble sort, insertion sort) to O(n log n) optimal algorithms (merge sort, quicksort) illustrates how algorithmic insight can provide exponential speedup as data sizes grow. Sorting has deep connections to other domains: sorting networks (specialized circuits for parallel sorting), external sorting (for data larger than RAM), parallel sorting algorithms, and specialized sorts for strings and integers all require distinct insights. In job interviews, coding interviews, and algorithm competitions, sorting is ubiquitous: not just "implement quicksort," but rather "solve this problem efficiently using sorting" or "derive a sorting algorithm adapted to this constraint." Understanding the tradeoffs between sorts—time, space, stability, adaptivity—is essential for choosing the right tool in practice.

## connections

- [[algorithm]] — sorting is one of the fundamental algorithmic problems.
- [[big-o-notation]] — sorting algorithms are analyzed via Big O: merge sort is Θ(n log n), bubble sort is Θ(n²).
- [[divide-and-conquer]] — merge sort and quicksort are canonical divide-and-conquer algorithms.
- [[recursion]] — recursive sorts like merge sort and quicksort naturally decompose into recursive calls on smaller arrays.
- [[binary-search]] — requires sorted input; binary search on a sorted array is O(log n), enabling fast lookup.
- [[tree-data-structure]] — heap sort uses a heap (binary tree); merge sort trees have depth log n.
- [[time-complexity]] — sorting algorithms exemplify the major complexity classes: O(n), O(n log n), O(n²), O(n·d).
- [[polynomial-function]] — sorting time is polynomial in n; O(n log n) is polynomial, making sorting tractable.

## see also

- [[algorithm]] · [[divide-and-conquer]] · [[big-o-notation]] · [[time-complexity]]

<!-- footer -->

---

Lists: · Mark read: `INPUT[toggle:read]`
