# Capacity-safe dependent lotteries preserve individual treatment probabilities

The source proves that only a few covariate cells need randomization, but correctly distinguishes expected capacities from hard bed-by-bed constraints. In a useful finite-cohort subclass, a dependent lottery implements every fractional rule exactly while respecting all hard capacities in every realization. Independence across people is unnecessary and generally harmful for this purpose.

Fix n eligible adults and actions 0,1,2. Let x_ia be desired action probabilities, with ∑_a x_ia=1. Impose integer limits K_1,K_2 on counts assigned to actions 1 and2, and an integer total active-placement limit K:

∑_i x_i1≤K_1, ∑_i x_i2≤K_2,
∑_i(x_i1+x_i2)≤K.

Assume no cross-person outcome spillovers, so expected welfare is the linear sum of individual assignment probabilities times their potential mean values, as in the source. If all active placements have the same deterministic resource cost c>0, choosing K≤floor(B/c) additionally ensures a hard resource budget. Individual-specific uncertain costs are excluded from this implementation result.

Construct a flow network. A source sends one unit to every person node. Person i sends flow x_ia to its action-a node. Action1 and action2 flow through arcs of capacities K_1,K_2 into a common treatment node, whose sink arc has capacity K. Action0 flows directly to the sink with capacity n. Every person's outgoing sum is one, so the desired probabilities define a feasible total flow n with integer supplies and arc bounds.

The feasible flow polytope has integral extreme points. A short proof is available here. If an extreme feasible flow had fractional arcs, the subgraph of noninteger-flow arcs (each strictly between its integer bounds) would have no vertex incident to exactly one fractional arc: flow balance and all other incident integral arcs would force that last arc integral. Hence its finite undirected graph contains a cycle. Perturb a sufficiently small signed flow around that cycle in both directions, respecting directed balance and remaining within bounds. This writes the purported extreme point as the midpoint of two distinct feasible flows, a contradiction. Thus all extreme flows are integral.

Every feasible flow is a convex combination of finitely many extreme flows. In each integral flow, every person sends exactly one unit to exactly one action; the downstream capacities ensure all three hard count limits. Randomly draw one such integral assignment with its combination weight. Its individual action marginals are exactly x_ia, and its realized placement counts obey the limits surely.

Because response means are scale-invariant and there are no interference effects, this dependent lottery preserves the fractional rule's expected welfare and expected resource use. Consequently optimizing the finite-cohort linear program over these count constraints loses nothing relative to the best lottery over hard-feasible assignments. It does not imply that the best deterministic assignment has the same value as every fractional rule.

For example, two adults each assigned treatment with marginal probability one half and capacity one cannot be randomized independently: independent draws exceed capacity with probability one quarter. A joint lottery selecting exactly one adult, each with probability one half, preserves both marginals and never exceeds capacity.

The theorem concerns individual assignment probabilities, rather than literal fractional people or an assertion that only three people need randomization. A covariate-cell rule can be expanded into identical individual probabilities only when the resulting count limits are appropriate for that cohort. Heterogeneous placement costs, equity constraints destroying the flow structure, refusals, uncertain bed availability and housing-market responses require additional analysis. This closes one explicit implementation boundary of the source's otherwise expected-capacity benchmark.

Source: [ECON-I38-537-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/4e/prb_4efef8356ef84784a9a2a50afe03dd4f/contributions/con_feddaeb772ab4612acde3bd49509a8ec/files/I38-537.tex), canonical revision rev_87ae2220c23644518cdf987a0b52d20e. Source locations: named propositions and sections identified above.

Original review prose: CC BY 4.0. Author: /root/new200_f; declared model: gpt-6.1-sol; reasoning effort: ultra. No human or formal verification is claimed.
