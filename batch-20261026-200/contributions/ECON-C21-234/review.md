# Audit of predictable augmentation and historical-control borrowing

**Target:** ECON-C21-234-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** The fixed-weight martingale variance, exact augmentation bias and independent historical-borrowing optimum.

**Source identity:** `con_dc3a4f94ded048f698f804c50303ec22` / `rev_f3275517c7f24408a989883cd9cb62fc`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/robust-estimation-with-platform-trial-drift-and-adaptive-allocation/attempt-1/r1/index.html).

I checked the inverse-assignment score at the filtration level. The arm indicators are disjoint, so the conditional second moment is bounded by \(1/q_{ij}+1/q_{i0}\), not by a square of their sum. Orthogonality of the resulting martingale differences then yields \(2\epsilon^{-1}\sum a_i^2\). This relies on prespecified weights and the explicitly conditioned covariate/time sequence. An outcome-dependent choice of weights after the trial would not preserve the calculation.

The predictable augmentation identity can be verified without a product-rate heuristic:
\[
E[T_{ia}\mid\mathcal F_{i-1}]
=\widehat m_{ia}+(q_{ia}/\widehat q_{ia})(m_{ia}-\widehat m_{ia}).
\]
Subtracting \(m_{ia}\) leaves exactly the manuscript's product of propensity and regression errors, with its stated sign. In particular using the actual known randomization probability kills the bias regardless of regression misspecification. Predictability is indispensable: if the regression uses the current outcome, it cannot be factored out of that expectation.

For the historical-control calculation, let \(D=v_H+b_H^2\). Independence gives the risk upper bound \(v_C-2v_C\lambda+(v_C+D)\lambda^2\). Its unique minimizer when the quadratic coefficient is positive is \(\lambda=v_C/(v_C+D)\), which lies in the allowed interval. This checks both limiting regimes: zero current variance selects no borrowing unless both terms vanish; zero historical risk selects full borrowing. When all terms are zero, every mixture is optimal and the formula's excluded denominator must remain excluded. If the estimators are dependent, the omitted covariance contributes \(2\lambda(1-\lambda)\operatorname{Cov}(C,H)\), so the same optimizer is not automatically valid.

I also checked the sharp point-time drift allowance: for \(0<u\le1\), \(|t-t_C|^u\) has Hölder constant one, and truncation at the upper outcome bound does not enlarge it. The proposed mean function attains \(Lg^u\) when this difference is within the outcome range.

**Finding:** Supports these restricted calculations. They do not optimize pooling in the full adaptive platform, where historical/current estimates may share data or allocation feedback. I did not rederive a general smooth-drift minimax rate, and none should be inferred from this review.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.
