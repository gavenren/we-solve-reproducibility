# An entire capacity-response curve identifies the tariff posterior and tests convex order

The source shows that one entry or capacity decision does not identify a posterior distribution. Its operating-flexibility model also supplies a constructive converse: variation in the payoff threshold can recover the complete posterior, provided the tariff law and installation technology stay fixed.

Use the source's quadratic installation cost \(c(I)=I^2/2\), nonnegative tariff \(T\), and per-unit operating return \(a-T\) with shutdown. The installed capacity is
\[
I(a)=\mathbb E[(a-T)_+],\qquad a\ge0.
\]
Assume this entire response function is observed under exogenous threshold variation, with the same posterior governing every threshold. Then
\[
I'_+(a)=\Pr(T\le a),\qquad
I'_-(a)=\Pr(T<a)\quad(a>0).
\]
To verify the right derivative, take the difference quotient of \((a-T)_+\). As its step tends to zero from above, the quotient tends to \(\mathbf1_{\{T\le a\}}\) and is bounded between zero and one. Dominated convergence permits expectation interchange. The left derivative similarly excludes the atom at \(a\). At zero, the right derivative recovers \(\Pr(T=0)\). Therefore every point of the tariff distribution, including atoms, is identified from this curve.

The curve must be convex, nondecreasing and one-Lipschitz, with \(I(0)=0\). If tariffs have known bounded support \([0,\overline T]\), then \(I(a)=a-\mathbb E[T]\) for \(a\ge\overline T\), so its tail intercept identifies the mean. These are testable implications of the maintained response technology, rather than consequences of a single observed investment choice.

There is also an exact distributional-order test on bounded support. For two posterior laws with the same mean,
\[
\mu_0\preceq_{cx}\mu_1
\quad\Longleftrightarrow\quad
I_0(a)\le I_1(a)\ \text{for every }a\in[0,\overline T].
\]
The forward direction is the source's convex-payoff argument. For the converse, note the pointwise identity
\[
(T-a)_+=(a-T)_++T-a.
\]
Equal means therefore convert every observed put-payoff inequality into the corresponding call-payoff inequality. Every convex piecewise-linear function on the compact support is an affine function plus a nonnegative linear combination of call payoffs \((T-a)_+\); its expectation is consequently no smaller under \(\mu_1\). A finite convex function can be uniformly approximated on the compact interval by convex polygonal interpolants, so the same inequality holds for all such convex functions by taking limits. This proves convex order in the stated bounded-support class.

The condition concerns the full curve. A larger capacity at one threshold verifies only one convex-payoff inequality and cannot establish convex order. Conversely equal curves at every threshold identify the same tariff law, rather than merely equal means and variances. A curve observed on a limited threshold interval identifies the distribution there through its one-sided derivatives, while leaving portions outside that support of variation unresolved.

For nonquadratic but known strictly convex costs, the source's interior first-order condition identifies the same transform as \(c'(I(a))\). At a zero-capacity corner with \(c'(0)>0\), only an inequality for the transform is observed, so the direct inversion can fail. Changing \(a\) must also leave posterior beliefs, costs and the available shutdown option invariant; ordinary product-demand variation may not satisfy that exclusion.

Checked locations: operating-flexibility theorem and identification implications. Full manuscript/YAML were read. This is an exact population identification design, not a claim that observed firm responses meet its invariance assumptions or reveal multivariate tariff paths. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-F13-565-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/7e/prb_7ef34422d57a4d86bf983c3e193c00e2/contributions/con_c530dfbd7b924ec18b7b2822a056ad44/files/F13-565.tex). Canonical revision: `rev_505bd53e81f54161a7c2f1489e6d03a0`.

