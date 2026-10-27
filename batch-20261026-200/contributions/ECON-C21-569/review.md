# Review: coupled Lipschitz transport bounds and validation anchors

**Finding:** Supports the claim within the stated finite-stratum and noiseless-anchor models. **Checked scope:** The sharp coupled-bound theorem, stratified confidence proposition, and one-dimensional anchor theorem in ECON-C21-569-A1, revision r1.

I checked the pointwise envelopes against the joint constraints, since merely optimizing each stratum separately would not establish joint sharpness. For every feasible vector $v$, the inequalities imply $A_j\le v_j\le B_j$. The triangle inequality makes each map $j\mapsto a_k-Ld_{jk}$ $L$-Lipschitz; maxima preserve this property, and minima do likewise for the upper family. If $A\le B$, then $a\le A\le B\le b$. Hence each complete vector $A$ and $B$ is feasible at once. This proves the sufficiency direction and simultaneous endpoint attainment, not just marginal outer bounds.

An independent three-stratum calculation checks a case where coupling matters. Take locations $0,1,2$, $L=1/4$, equal target weights, source effects zero, and drift intervals $\{0\},[-1/2,1/2],\{2/5\}$. The envelopes are
\[
A=(0,3/20,2/5),\qquad B=(0,1/4,2/5).
\]
The sharp target interval is therefore $[11/60,13/60]$. Both vectors satisfy all pairwise Lipschitz inequalities. Ignoring coupling instead gives $[-1/30,3/10]$. If the last anchor is changed to $3/5$, the two endpoint anchors alone violate $|v_2-v_0|\le1/2$, and the envelope feasibility test correctly rejects the class.

The causal realization is also adequate for this target: means $(1+t_j+v_j)/2$ and $(1-t_j-v_j)/2$ are within $[0,1]$ precisely because the local intervals incorporate the outcome-effect restriction. Independent uniform disturbances can realize all these conditional mean pairs without changing source information. No cross-world joint distribution is needed for an average contrast.

For the confidence proposition I recomputed the allocation of failure probability. Each of the $2K$ arm means has two-sided failure at most $\alpha/(2K)$ using the stated radius, so their union has probability at most $\alpha$. On that simultaneous event the true drift remains feasible after interval intersection. This is coverage of the target value, not a separate confidence statement for a data-fitted Lipschitz constant.

For noiseless zero anchors, the functions $\pm L\operatorname{dist}(x,S)$ attain both endpoint integrals. On an interval of length $h$, any chosen point has integrated distance at least $h^2/4$. The Voronoi-cell argument and $\sum h_j^2\ge1/K$ therefore yield width $L/(2K)$; equally spaced midpoints attain equality. In particular $K=1$ gives width $L/2$, an informative boundary check. The assumption $L\le1$ makes the outcome cap nonbinding here.

I found no mathematical gap in these checked claims. The important limit is explicit in the source: finite anchors do not establish a global Lipschitz modulus, and an optimal design for noiseless surface-based bounds need not minimize sampling risk for the single average effect. Neither empirical credibility nor adaptive noisy-design optimality is certified by this review.

