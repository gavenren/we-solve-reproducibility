# Independent review of ECON-C78-369-A1, revision r1

**Finding:** Supports the claim.

**Checked scope:** The length-two-list characterization of all reachable allocations and the requirement to output a legal sequence.

## Independent reachable-set characterization
When each acceptable list has length at most two and the endowment is acceptable, an applicant can improve at most once. After a legal swap it holds its unique first choice and can never participate again. Therefore every participant in a later swap has not previously moved and still holds its original house. Any legal pair at any time must already have been a legal pair at the initial allocation.

An initially dissatisfied applicant desires one specific house, which has one initial owner. Hence that applicant belongs to at most one initially mutually beneficial pair. The initially legal pairs are therefore vertex-disjoint. Performing one cannot alter any other pair's houses or preferences. Every subset of these pairs can be performed in any order and is reachable; no other swap can appear.

This yields a slightly sharper check on the manuscript: if there are k initially legal pairs, the reachable set has exactly 2^k allocations. Distinct subsets change different endowed houses, so no two subsets coincide. The all-swaps allocation is the unique allocation in this reachable set that weakly Pareto dominates every member; every omitted pair is strictly improved by adding its swap. Any maximal legal-swap schedule must perform all k pairs. Thus both the outcome and a legal path are available by scanning initial network edges.

## Boundary test at list length three
The reasoning genuinely uses the two-house restriction. Take three applicants A,B,C endowed with a,b,c. Let A rank c>b>a, B rank a>b, and C rank b>c. Include network edges AB and AC. First AB swaps: A obtains b and B obtains a, strictly improving both. Then AC swaps: A obtains c and C obtains b, strictly improving both. Applicant A moves twice, and the second legal pair was not improving at the initial allocation because A initially held a, which C does not accept.

This explicit instance confirms why the disjoint-pair proof cannot be reused unchanged at maximum list length three. It is not a hardness proof for that case. I did not verify treewidth tractability or a general parameterized classification; the manuscript does not claim those. The reviewed result is stronger than mere termination because it identifies all reachable states and the dominating one on its stated subclass.

## Evidence and limits

The [complete prior manuscript](https://we-solve.github.io/contributions/parameterized-computation-of-a-reachable-pareto-optimal-allocation/attempt-1/r1/) and [current statement](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/main/prompts/ECON-C78-369.txt) were retrieved and read. The reasoning above is an independent mathematical check of the specified scope. References merely listed in the manuscript were not treated as independently verified sources. No empirical replication, formal verification, human review, or full solution of the catalogue problem is claimed.

Reviewer: Codex (GPT-6), `/root/econ_c`; exact serving revision and thinking setting unknown. Gaven (@gavenren) requested the review. This review is original CC BY 4.0 exposition.
