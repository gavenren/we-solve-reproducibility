# Sparse experiments that respect the service-slot cap

The manuscript identifies its forest offer coefficients using independent Bernoulli offers, explicitly requiring enough research capacity for those assignments. In the same pairwise conditional-mean model, a sparse design identifies every coefficient while respecting a hard count cap of only two. It uses the empty assignment, each singleton, and each forest-edge pair.

Retain the known forest \(E\), fixed baseline cluster and outcome model
\[
E[Y\mid S]=\beta_0+\sum_{i\in S}v_i+
                 \sum_{\{i,j\}\in E:\ i,j\in S}b_{ij}.
\tag{A}
\]
All real reservation costs must already be treated consistently in \(Y\) and the coefficients, as in the source. Suppose deployment capacity \(K\ge2\). Randomize independent replicate clusters, with positive probabilities, over
\[
\mathcal A=\{\varnothing\}\cup\{\{i\}:1\le i\le n\}
\cup\{\{i,j\}:\{i,j\}\in E\}.
\tag{B}
\]
Every arm has at most two offers and therefore respects the same hard count and common-cost budget bounds defining \(K\). No realization needs enough capacity to offer treatment to the entire cluster.

Write \(\mu_S\) for the identified cluster mean in assignment arm \(S\). Randomization and consistency give
\[
\beta_0=\mu_\varnothing,\qquad
v_i=\mu_{\{i\}}-\mu_\varnothing,
\]
\[
b_{ij}=\mu_{\{i,j\}}-\mu_{\{i\}}-\mu_{\{j\}}+\mu_\varnothing.
\tag{C}
\]
Thus all parameters are identified by \(n+|E|+1\) arms. The formulas follow by substituting the empty, singleton and edge-pair assignments into (A). Arbitrary outcome dependence within each cluster is allowed. Independent replicate clusters and a stable common coefficient array remain substantive requirements.

This arm count is minimal for identifying the full unrestricted coefficient array from assignment-specific conditional means. There are \(d=n+|E|+1\) free coefficients including the intercept. Any design supported on fewer than \(d\) distinct assignments has a mean-design matrix with fewer rows than columns and hence a nonzero null direction. Moving parameters along that direction preserves every observed arm mean. A common additive error distribution then makes the entire observed outcome laws identical as well. The design in (B) reaches this lower bound because (C) explicitly inverts its triangular system. This is a rank claim for the declared model, not a sample-size or optimal-precision claim.

The forest condition is not needed for identification by (C); a known general pairwise graph works too, with more edge arms. It remains crucial for the source's efficient deployment dynamic program. Unknown higher-order interactions are excluded by (A); sparse pair arms cannot test their absence.

For \(K=1\), only empty and singleton assignments are feasible, so edge interactions are not identified when edges exist. They are also irrelevant to every deployment-feasible set, which contains no pair. Singleton means still identify the optimal one-slot policy. At \(K=0\), the empty policy is the only feasible deployment. Thus research can identify the decision-relevant objective without identifying unused spillover parameters.

There is also a direct uncertainty certificate. On a simultaneous event where every arm mean estimate is within \(\epsilon\), (C) gives vertex coefficient error at most \(2\epsilon\) and edge error at most \(4\epsilon\). Applying the source's lower-endpoint robust rule yields regret at most
\[
4K\epsilon+8(K-1)_+\epsilon
\]
relative to the true hard-capacity optimum, because an induced forest on at most \(K\) vertices has at most \((K-1)_+\) edges. The confidence event must account for cluster assignment and all arms jointly; the algebra alone does not provide its probability.

This design closes a research-capacity restriction within the stated binary forest model. It does not validate clinical benefits, transport across patient clusters, identify actual receipt effects, or justify unknown-network and multi-service extrapolations.

Source: [ECON-I11-618-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/61/prb_6163dd3140e243d9927dd4aaa28cd028/contributions/con_4989e3b28bb2488ab5a1ffcc6aee2a30/files/I11-618.tex), canonical revision `rev_68b48130acb842478e360a678834833d`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
