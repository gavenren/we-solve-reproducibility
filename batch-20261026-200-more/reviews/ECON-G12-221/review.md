# Exact identified set for aggregation weights from one cross-section

The unrestricted-market proposition in “Even observed portfolios need not identify response weights” is correct. Its three-investor example extends to an exact characterization for any finite population. This identifies precisely which observations recover the response weights and which observations leave an open family of counterfactual responses.

Keep the source's unrestricted CARA-normal economy, with positive risk tolerances \(\tau_i=(\gamma_i\sigma_i^2)^{-1}\), fixed supply \(Q\), and observed means \(\mu_i\), clearing price \(p\), and final holdings \(q_i\). Assume \(\sum_iq_i=Q\). Define
\[
I=\{i:\mu_i\ne p\},\qquad J=\{i:\mu_i=p\}.
\]
Compatibility with this economy requires \(q_j=0\) for every \(j\in J\), and
\[
r_i:=q_i/(\mu_i-p)>0\quad(i\in I).
\]
These conditions are also sufficient. In fact, all compatible primitive vectors, with no omitted restrictions, are
\[
\tau_i=r_i\ (i\in I),\qquad \tau_j=t_j>0\ (j\in J).
\tag{A}
\]

To prove necessity, use the demand equation \(q_i=\tau_i(\mu_i-p)\). For sufficiency, choose variances equal to one and risk aversions \(1/\tau_i\). The demand equation then reproduces each holding at the observed price. Since the observed holdings sum to supply, the market clears. The strictly decreasing aggregate demand gives its unique price. Thus (A) describes actual economies, rather than merely formal candidate coefficients.

Write \(S=\sum_{i\in I}r_i\) and \(T=\sum_{j\in J}t_j\). Holding the primitive tolerances and supply fixed during a mean perturbation, the response weights are
\[
w_i=\frac{r_i}{S+T}\quad(i\in I),\qquad
w_j=\frac{t_j}{S+T}\quad(j\in J).
\tag{B}
\]
These formulas completely describe the identified set.

If \(J\) is empty, all tolerances and therefore all weights are point identified. If both \(I\) and \(J\) are nonempty, the relative weights of the observed nonzero-spread traders remain identified:
\[
w_i/w_\ell=r_i/r_\ell\quad(i,\ell\in I).
\]
Their total weight \(\alpha=\sum_{i\in I}w_i=S/(S+T)\), however, ranges over exactly \((0,1)\). Conversely, every choice of \(\alpha\in(0,1)\) and strictly positive weights on \(J\) summing to \(1-\alpha\), together with \(w_i=\alpha r_i/S\), is attained: set \(t_j=Sw_j/\alpha\). In particular the individual range for a trader \(i\in I\) is exactly \((0,r_i/S)\). None of these open endpoints is attained with finite strictly positive tolerances.

There is one important boundary case. If \(I\) is empty, compatibility forces every holding to zero and hence \(Q=0\). The admissible response vectors are then the entire strictly positive probability simplex. For a single investor that simplex consists of the single weight one. With at least two investors, each coordinate can approach zero or one but cannot equal either. If the data violate a compatibility condition, the identified set is empty; one should not interpret this as partial identification.

For the manuscript's example, \(I=\{1,3\}\), \(r_1=r_3=1\), and \(J=\{2\}\), recovering exactly \(w_1=1/(2+t)\). The general result additionally shows that a zero current position is not intrinsically uninformative: a zero position with a nonzero observed mean-price spread actually contradicts the unrestricted benchmark. The unidentified cases arise specifically at zero spreads.

This is an independent identification result inside the declared terminal-dividend model. It neither identifies trading volume without initial portfolios nor extends the weight formulas across position constraints or active-set changes. It makes no empirical calibration or external-literature claim. The constrained theorem, dynamic learning, survey errors and wealth-dependent preferences require separate analysis.

Source: [ECON-G12-221-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/a8/prb_a80ceab2b371496397fb87a70cfffefb/contributions/con_adddb2faaf8344f7a43d8572773cc4ef/files/G12-221.tex), canonical revision `rev_ede4c20eb3f547c2a22eb91603f0ba4a`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
