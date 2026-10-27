# Complete-market sharing strictly lowers the stated three-country log variance

The source gives exact finite sums for the constant-predictor log-consumption variance in its three-country complete-market benchmark. Those sums imply a strict variance reduction for every \(0<h<1\), not merely in a small-shock approximation. The ratio has different small-shock and extreme-shock limits.

Maintain the equal-weight symmetric complete-market allocation, with consumption \(1+h(s_U+s_A+s_E)/3\). Define
\[
d=\tfrac12\log\frac{1+h}{1-h},\quad
e=\tfrac12\log\frac{1+h/3}{1-h/3},
\]
and the pair means
\[
m=\tfrac12\log(1-h^2),\qquad
n=\tfrac12\log(1-h^2/9).
\]
Autarky log consumption has mean \(m\) and variance \(v_0=d^2\). Integrated log consumption is a mixture: with probability \(1/4\), the outer pair has mean \(m\) and within-pair variance \(d^2\); with probability \(3/4\), the inner pair has mean \(n\) and within-pair variance \(e^2\). The law of total variance gives the compact exact expression
\[
v_1=\frac14d^2+\frac34e^2+\frac3{16}(m-n)^2.
\]
The last term is important: averaging within-pair variances alone would miss a between-pair mean effect created by the logarithm.

Now \(0<e<d\), and \(q=n-m>0\) satisfies
\[
q<d-e.
\]
To verify the latter, exponentiate twice each side:
\[
e^{2q}=\frac{(1-h/3)(1+h/3)}{(1-h)(1+h)},\qquad
e^{2(d-e)}=\frac{(1+h)(1-h/3)}{(1-h)(1+h/3)}.
\]
Canceling common positive factors reduces the desired inequality to \((1+h/3)^2<(1+h)^2\), which holds strictly.

It follows that
\[
v_0-v_1
=\frac34\left[d^2-e^2-\frac14q^2\right]>0.
\]
Indeed \(q^2<(d-e)^2\), while \(d^2-e^2=(d-e)(d+e)>(d-e)^2/4\). Thus the source's complete-market allocation strictly reduces this specific log-growth residual variance for every permitted positive shock amplitude. No claim about arbitrary predictors or arbitrary complete-market economies is needed.

The exact formula also describes two informative limits. As \(h\downarrow0\), \(d=h+O(h^3)\), \(e=h/3+O(h^3)\), and \(q=O(h^2)\). Hence \(v_1/v_0\to1/3\), the familiar linear averaging result. As \(h\uparrow1\), \(d\to\infty\), \(e\to\frac12\log2\), and \(q/d\to1\), because both \(q\) and \(d\) have leading divergence \(-\frac12\log(1-h)\). Therefore
\[
\lim_{h\uparrow1}v_1/v_0=\frac14+\frac3{16}=\frac7{16}.
\]
The finite-sum formula therefore does not preserve the small-shock factor one third near vanishing adverse-state consumption. At \(h=0\), both variances vanish and their ratio is undefined; the stated one-third value is a limit.

This variance result complements the source's separate strict expected-log-utility improvement. It does not make variance generally interchangeable with welfare: the utility improvement uses resource feasibility, symmetry and concavity, whereas the variance comparison above uses the particular independent sign distribution and constant-predictor convention. If all functions of aggregate endowment are projected out, the integrated residual instead vanishes exactly as the source states.

Checked locations: complete-market theorem and equations (3)–(4); full manuscript/YAML read. CARA asymmetry, nominal rigidities, empirical integration effects and external bibliography are not independently verified. Original prose: CC BY 4.0.

Pinned source: [ECON-F36-407-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/84/prb_84d40a55e23245e788c04f5ad601f4ab/contributions/con_1396849dcdf44ff2a46c8979373537b9/files/F36-407.tex). Canonical revision: `rev_a569e333e19d4cdc9c7f35e0a2f1d9f2`.

