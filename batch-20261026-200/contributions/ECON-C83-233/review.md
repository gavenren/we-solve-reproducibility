# Audit of the sampling–outcome covariance decomposition and sharp cluster example

**Target:** ECON-C83-233-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** The variance identity, simple-random-sampling specialization, cluster counterexample and local-transport proviso.

**Source identity:** `con_3329d9c4c71e45aea90e955b9759a8dd` / `rev_45f287b113da466e8b84cc9b00cf6f20`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/network-population-validity-without-independent-unit-sampling/attempt-1/r1/index.html).

I recomputed the covariance of two weighted terms using the manuscript's independence of the **whole sampling vector** from the **whole score vector**. It is
\[
\frac{\pi_{ij}}{\pi_i\pi_j}E[Z_iZ_j]-\mu_i\mu_j
=\frac{\pi_{ij}}{\pi_i\pi_j}\operatorname{Cov}(Z_i,Z_j)
+\left(\frac{\pi_{ij}}{\pi_i\pi_j}-1\right)\mu_i\mu_j.
\]
Coordinatewise marginal independence would not justify the first equality. The explicit vector-level assumption is therefore essential, and the review supports the identity only under that assumption.

For simple random sampling, the off-diagonal ratio equals \(N(n-1)/[n(N-1)]\), while the diagonal is \(N/n\). Direct summation of the absolute deviations from one gives \(2(N-n)/(nN)\) after dividing by \(N^2\), including the census boundary \(n=N\), where that entire sampling term vanishes. The remaining outcome-covariance term need not vanish at a census.

The equal-cluster random-sign example makes this distinction exact. For \(h=d+1\), each unit has variance one and covariance one with its \(d\) cluster mates. Inserting these into the identity yields \(1/n+(n-1)d/[n(N-1)]\); at \(n=N\) this equals \(h/N\), the variance of the average of \(N/h\) independent cluster signs. Thus replacing the number of independent clusters by the number of sampled vertices would produce a false consistency claim. The deterministic two-half-population sampling example independently isolates sampling dependence without score dependence.

The transport inequality also has a valid coupling proof, but its common response map and approximation error are substantive assumptions. A single long cycle and two disjoint long cycles share fixed-radius rooted neighborhoods while differing in global connectedness. This verifies the manuscript's warning that local graph convergence cannot control arbitrary global outcomes.

**Finding:** Supports these precisely stated calculations and counterexamples. The displayed absolute-covariance upper bound can be loose, especially with cancellation; the review does not turn that sufficient condition into a necessary-and-sufficient criterion or a general minimax rate.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.
