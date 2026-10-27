# Scoped review of weighted-star nucleoli and arrangement enumeration

**Target:** ECON-C71-299-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** Star formula, symmetry/empty-core example and finite exact algorithm's exponential bound

**Source identity:** `con_3ab7fe6eab9a474088349ac216efa33a` / `rev_0d8ac6ae49e747309f828fa2e5b03371`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/a-combinatorial-polynomial-time-nucleolus-algorithm-for-matching-games/attempt-1/r1/index.html).

I checked the weighted-star formula by reducing the entire core, not just balancing two selected edge inequalities. Efficiency and the highest-weight edge force \(x_0+x_1=W\) and all other leaves' allocations to zero. The remaining edge constraints give \(x_0\ge W_2\); these suffice for all coalitions because a star matching uses at most one edge. With a unique maximum, the core is exactly \(x_0=t\), \(x_1=W-t\), \(W_2\le t\le W\).

Along that segment, center-free coalitions have excess zero or \(t-W\). Coalitions containing the center and highest-weight leaf have constant excess zero when proper. Other center-containing coalitions have excess \(w_j-t\), or \(-t\). Thus the largest variable excess is precisely \(\max(t-W,W_2-t)\). Balancing these terms uniquely gives \(t=(W+W_2)/2\). For weights \(8,5,2\), this gives center \(6.5\), top leaf \(1.5\), and others zero; either directional perturbation increases the largest variable excess above \(-1.5\). The fixed zero excesses remain ahead of it and cannot remove that lexicographic comparison. Multiple top leaves force the core to the center-only allocation. The one-leaf case separately balances the singleton excesses and gives \(W/2\), including \(W=0\).

The uniqueness proof's midpoint argument also supports automorphism invariance: if two minimizers differ in the coalition sets attaining the highest differing excess level, their midpoint strictly reduces the multiplicity at that level after preserving all earlier levels. If every level set agrees, singleton excesses identify every allocation coordinate. For an odd cycle, transitivity consequently gives the equal allocation, while summing edge-core inequalities contradicts its total matching worth. This checks the empty-core example without treating the nucleolus as a core selection in that case.

For the exact finite algorithm, a cell of the excess-equality arrangement has a fixed excess ordering. Successive linear minimization over that bounded cell reaches a face containing a vertex. Boundary hyperplanes \(x_i=0\) and excess-equality hyperplanes therefore suffice to enumerate candidates with \(N-1\) independent constraints plus efficiency. With \(O(4^N+N)\) hyperplanes this gives \(2^{O(N^2)}\) systems, as stated.

The formulas and finite reduction are supported. Enumeration is exponential and does not supply the requested general polynomial combinatorial algorithm; I did not independently verify the cited literature's polynomial-time result.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.

