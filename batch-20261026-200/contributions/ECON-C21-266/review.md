# Scoped review of metric-cell geometry and the doubly robust error bound

**Target:** ECON-C21-266-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** Voronoi construction, exact conditional-score bias, finite-sample risk constants and nuisance norm requirement

**Source identity:** `con_b21100abfc484676aa1384e90fd65d23` / `rev_fd3bc4991c304c3f8be47fab18097d2d`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/heterogeneous-causal-effects-on-metric-covariate-spaces/attempt-1/r1/index.html).

The metric partition argument can be checked without any Euclidean dimension assumption. For centers separated by more than \(h\), their closed \(h/3\)-balls are disjoint: intersection would imply distance at most \(2h/3\). Each such ball lies in its center's Voronoi cell, since another center is more than \(2h/3\) away from its points. Maximality supplies coverage by radius-\(h\) balls, hence cell diameter at most \(2h\). The lower small-ball mass assumption bounds the number of centers and proves termination. A fixed deterministic tie rule gives measurable cells.

Conditioning on the independent training sample and \(X=x\), I expanded the proposed score directly. Subtracting \(\tau=m_1-m_0\) gives
\[
b(x)=(\widehat e-e)\left\{
 \frac{\widehat m_1-m_1}{\widehat e}
 +\frac{\widehat m_0-m_0}{1-\widehat e}\right\}.
\]
Both signs are positive inside the brackets; confusing the control residual sign would change this identity. Clipping the propensity away from zero and one yields a deterministic score bound. Known propensity makes this conditional bias exactly zero even if the outcome regressions are misspecified.

For a cell of mass \(p\), its count \(N\) is binomial. The inequalities
\[
\frac{\mathbf1\{N>0\}}N\le\frac2{N+1},
\qquad
E\frac1{N+1}\le\frac1{(n+1)p},
\qquad
p(1-p)^n\le\frac1{n+1}
\]
give the stated factor three for the cell-mean stochastic and empty-cell contributions. Applying \((a+b)^2\le2a^2+2b^2\), then the cell Hölder diameter and Jensen's inequality for conditional averages of \(b\), reproduces the reported coefficients \(6,4,4\). Clipping the final estimator cannot increase squared error because the true contrast lies in the clipping interval.

Finally, the displayed bias involves a product. Hölder's inequality controls its \(L^2\) norm by \(L^4\) errors of the two factors; two \(L^2\) consistency claims alone do not supply that bound. The manuscript explicitly retains this distinction.

This review supports the geometry and finite-sample risk statement in the split-sample bounded experiment. It does not establish minimax lower bounds or verify every learned-metric and confidence-band assertion.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.

