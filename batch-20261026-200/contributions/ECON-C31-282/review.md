# Audit of paired-network information and conditional versus joint identification

**Target:** ECON-C31-282-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** The covariance-class information identity, disjoint-pair optimum, and complete-graph random-count qualification.

**Source identity:** `con_3c1efa7473a04e8e9653720819cbb5f0` / `rev_1a4a1a81addb438a909086df10485713`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/information-and-statistical-power-under-interference/attempt-1/r1/index.html).

For fixed assignment, I checked the worst-case information identity using the variational form rather than assuming the Euclidean and generalized least-squares residuals coincide. Since \(\Sigma\preceq\bar vI\), every residual candidate satisfies \((s-Ab)^\top\Sigma^{-1}(s-Ab)\ge\|s-Ab\|^2/\bar v\). Minimizing in \(b\) gives \(\|r\|^2/\bar v\); the admissible covariance \(\bar vI\) attains it. This justifies the exact worst-case value without incorrectly commuting covariance and projection.

For \(n\) disjoint pairs with exactly \(n\) treated vertices, both treatment and neighbor exposure have \(n\) ones. Their centered squared norms equal \(n/2\). A mixed pair contributes \(-1/2\) to their inner product and an unmixed pair contributes \(+1/2\), so the residual sum of squares is \(2m(1-m/n)\). I checked the integer feasibility condition: the number of remaining pairs must be split equally into types 00 and 11, so \(n-m\) is even. Maximizing over all integers without this parity restriction would give unattainable optima for some network sizes. The displayed \(N=8k\) construction satisfies it and gives \(N/4\).

The two zero-information endpoints have distinct structural meanings. If every pair is mixed, exposure equals \(1-W\); if none is mixed, exposure equals \(W\). Both are absorbed by intercept and own treatment, despite different treatment assignments.

Finally, the complete-graph qualification is necessary and correct. With a fixed count \(k\), \(S=[k\mathbf1-W]/(N-1)\) uses the same coefficients under every draw, permitting a single nuisance reparameterization for the joint experiment. With two supported nonconstant assignment counts, matching mean vectors forces \(\Delta\beta=\Delta\delta/(N-1)\) at both counts and two inconsistent intercept shifts unless \(\Delta\delta=0\). Conditional nonidentification at each individual assignment therefore does not automatically imply joint nonidentification.

**Finding:** Supports these stated results. Expected information alone does not supply a uniform conditional power guarantee. This review does not resolve general graph optimization or estimation of the covariance class from dependent network replicates.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.
