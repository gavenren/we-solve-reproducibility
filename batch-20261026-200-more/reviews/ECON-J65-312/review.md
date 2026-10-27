# Asset heterogeneity increases grouped log-insurance benefits and has variance bounds

The source warns that substituting average assets into its homogeneous log-utility benefit formula is generally wrong. Under common welfare weights and interior choices, the direction of that error and the value of observing assets can be characterized exactly.

Work only in the exogenous-employment insurance benchmark. Within one observed group, condition on unemployment, thereby using the source's probability reweighting by \(r_\theta\). Suppose all welfare weights equal \(w>0\), utility is logarithmic, and assets have support \([a_L,a_U]\subset(0,\infty)\). Assume
\[
0<w/\lambda-a_U,\qquad w/\lambda-a_L<\bar b.
\]
These inequalities make every fully informed optimum interior. Set \(b^*(a)=w/\lambda-a\). The common grouped optimum \(b_G\) is also interior and belongs to the interval between the smallest and largest \(b^*(a)\), because the derivative
\[
f'(b)=w\,\mathbb E[(a+b)^{-1}]-\lambda
\]
is continuous, strictly decreasing, nonnegative at the lower endpoint and nonpositive at the upper endpoint. Thus it has a unique zero, with the natural equality cases for constant assets.

Let \(b_M=w/\lambda-\mathbb E[a]\) be the mean-assets plug-in. Jensen's inequality gives
\[
w\,\mathbb E[(a+b_M)^{-1}]
\ge \frac{w}{\mathbb E[a]+b_M}=\lambda.
\]
Since \(f'\) strictly decreases, \(b_G\ge b_M\), strictly if the asset distribution is nondegenerate. Thus heterogeneity raises the optimal common benefit relative to mean substitution in this precisely defined subclass. This statement is conditional on unemployment and on common weights; applying unconditional mean assets or allowing weights correlated with assets changes it.

There is also an exact information-value expression. Write \(f_a(b)=w\log(a+b)-\lambda b\), and let
\[
\mathcal I=\mathbb E[f_a(b^*(a))-f_a(b_G)].
\]
With \(y_a=\lambda(a+b_G)/w>0\), direct subtraction gives
\[
\mathcal I=w\,\mathbb E[y_a-1-\log y_a].
\]
The integrand is nonnegative and vanishes only at \(y_a=1\). Therefore information has strictly positive value exactly when assets are nondegenerate. The grouped first-order condition also implies \(\mathbb E[1/y_a]=1\), providing an independent check on a computed optimum. Population welfare gains multiply this conditional value by the group's unemployment mass.

The value is bounded quantitatively by asset variance:
\[
\frac{w}{2(a_U+\bar b)^2}\operatorname{Var}(a)
\le\mathcal I\le
\frac{w}{2a_L^2}\operatorname{Var}(a).
\]
To prove this, throughout the feasible rectangle the negative second derivative of \(f_a\) lies between \(m=w/(a_U+\bar b)^2\) and \(L=w/a_L^2\). Taylor expansion around the interior individual optimum therefore bounds each individual loss between \(m(b-b^*(a))^2/2\) and \(L(b-b^*(a))^2/2\). At \(b_G\), the expected squared distance is at least \(\operatorname{Var}(b^*(a))=\operatorname{Var}(a)\), proving the lower bound. For the upper bound, grouped optimality says its regret is no larger than regret at the feasible \(b_M=\mathbb E[b^*(a)]\). Expected squared distance there is exactly \(\operatorname{Var}(a)\).

These constants are sufficient, not claimed sharp. If benefit caps bind, the full-information rule clips, and the simple variance and plug-in direction arguments require modification. If unemployment has zero probability the conditional problem is undefined and contributes zero to the original objective.

Checked locations: implementable heterogeneous benchmark, log-utility example and information-refinement section. Full source/YAML were read. Search, endogenous taxes, labor-market equilibrium and the external source are not verified by this extension. Original prose: CC BY 4.0.

Pinned source: [ECON-J65-312-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/85/prb_85a15969023b4be596b496f90e3c5311/contributions/con_0f62907c5e9044c4837ab7dad855c5e5/files/J65-312.tex). Canonical revision: `rev_665c95c0af694912b154ebaba29735f8`.

