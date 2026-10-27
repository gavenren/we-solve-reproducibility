# Allocation regret depends only on relative coefficient error and is quadratic

The source gives a general \(2\epsilon\) regret guarantee from a uniform response band. In its strictly concave quadratic funding model, known curvatures permit a sharper certificate based on estimation error in relative marginal returns. A common error in every use has exactly zero allocation cost.

Retain the feasible set \(X=\{x:0\le x_j\le u_j,\sum_jx_j=b\}\), and suppose the positive curvature matrix \(C=\operatorname{diag}(c_j)\) is known. Let true and estimated objectives be
\[
F_a(x)=a^{\mathsf T}x-\tfrac12x^{\mathsf T}Cx,\qquad
F_{\widehat a}(x)=\widehat a^{\mathsf T}x-\tfrac12x^{\mathsf T}Cx.
\]
Their unique optimizers are \(x^*,\widehat x\). Put \(e=\widehat a-a\). Then the exact deterministic certificate is
\[
0\le F_a(x^*)-F_a(\widehat x)
\le\frac12\min_{\eta\in\mathbb R}
\sum_j\frac{(e_j-\eta)^2}{c_j}.
\]
The minimizing shift is
\[
\eta^*=\frac{\sum_je_j/c_j}{\sum_j1/c_j}.
\]
The bound applies with binding capacities and zero allocations, not only interior solutions.

For proof, the quadratic expansion and first-order optimality of \(\widehat x\) over the convex set give
\[
F_{\widehat a}(\widehat x)-F_{\widehat a}(x^*)
\ge\tfrac12(\widehat x-x^*)^{\mathsf T}C(\widehat x-x^*).
\]
Set \(d=\widehat x-x^*\), whose coordinate sum is zero. Subtract the coefficient-error term to obtain
\[
F_a(x^*)-F_a(\widehat x)
\le(e-\eta\mathbf1)^{\mathsf T}d-\tfrac12d^{\mathsf T}Cd
\le\tfrac12(e-\eta\mathbf1)^{\mathsf T}C^{-1}(e-\eta\mathbf1).
\]
The final inequality is completion of a square. Minimizing its positive quadratic in \(\eta\) proves the displayed formula. No stochastic independence or differentiability of the clipped optimizer is used.

The allocation itself satisfies
\[
\|\,\widehat x-x^*\,\|_C
\le\min_\eta\|e-\eta\mathbf1\|_{C^{-1}},
\]
where \(\|v\|_C^2=v^{\mathsf T}Cv\). Add the two optimizer variational inequalities to get \(d^{\mathsf T}Cd\le e^{\mathsf T}d\), remove the common shift using \(\sum_jd_j=0\), and apply weighted Cauchy–Schwarz. If \(d=0\), the conclusion is immediate.

Sharpness is attained whenever both optimizers are interior and the perturbation is small enough to preserve capacities. The equality-constrained first-order equations then give
\[
d=C^{-1}(e-\eta^*\mathbf1),
\]
and the true regret is exactly half its squared \(C\)-norm. A sufficiently interior baseline and sufficiently small nonconstant error therefore attain the certificate.

For common error \(e_j=q\), the right side is zero. Indeed estimated welfare differs from true welfare by the constant \(qb\) on the funding simplex, leaving every allocation ranking unchanged. This formalizes the source's observation that a common linear coefficient can be absorbed at a fixed budget. With \(c_j\ge c_{\min}>0\) and \(\|e\|_2\le\delta\), the simpler bound is \(\delta^2/(2c_{\min})\), showing quadratic rather than linear small-error regret in this subclass.

Checked locations: capacity-constrained model (1), water-filling proposition, feature-rank discussion and regret inequality (4). Full exact source/YAML were read. The certificate requires the same known curvatures and feasible set; uncertain capacities, teacher spillovers, nonseparable returns or curvature errors need additional terms. External references are unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-I22-533-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/ea/prb_ea6716ecfdd64ec681603fc393e02111/contributions/con_1d399e63a8ec42c5975341e26a7f01f2/files/I22-533.tex). Canonical revision: `rev_4d07d45c112b4a429a68662c160e610c`.

