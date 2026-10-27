# A payoff-span criterion exactly characterizes kernel-moment identification

The source constructs a hidden pricing-kernel direction orthogonal to the factual dividend payoff. Its identification obstruction is an instance of an exact finite-state spanning criterion. This criterion states when additional asset prices genuinely identify the dividend-removal price.

Fix one public date-zero state. Suppose the terminal state has \(N\) atoms with known probabilities \(\pi_j>0\). Let \(D^1,\ldots,D^L\in\mathbb R^N\) be known payoff vectors, and observe their prices \(p_\ell=\sum_j\pi_jM_jD^\ell_j\). The admissible kernel vectors \(M\) are strictly positive and otherwise unrestricted; assume at least one such vector matches all observed prices. For a counterfactual payoff \(d\in\mathbb R^N\), holding the kernel fixed as in the source, its price is point identified **if and only if**
\[
d\in\operatorname{span}\{D^1,\ldots,D^L\}.
\]

For sufficiency, write \(d=\sum_\ell\alpha_\ell D^\ell\). Linearity gives its price \(\sum_\ell\alpha_\ell p_\ell\), shared by every compatible kernel. Multiple representations do not cause an ambiguity: their difference is a zero payoff, whose price is zero under the assumed compatible kernel.

For necessity, use the weighted inner product \(\langle x,y\rangle_\pi=\sum_j\pi_jx_jy_j\). If \(d\) is not in the payoff span, its orthogonal projection residual \(h\) is nonzero, satisfies \(\langle h,D^\ell\rangle_\pi=0\) for every traded payoff, and has \(\langle h,d\rangle_\pi=\langle h,h\rangle_\pi>0\). Start from any compatible strictly positive kernel \(M^0\). Because there are finitely many atoms, both \(M^0+\epsilon h\) and \(M^0-\epsilon h\) remain strictly positive for sufficiently small \(\epsilon>0\). Their factual prices agree exactly while their counterfactual prices differ by \(2\epsilon\langle h,h\rangle_\pi>0\). This proves failure of point identification within the admissible economic class, rather than merely failure of a particular estimator.

For the source's intervention, \(d\) is a positive constant payoff. Its price is identified exactly when the constant vector is in the span of observed payoff vectors. Observing a risk-free payoff suffices, as does a synthetic risk-free payoff formed from several risky claims. Observing additional dividend forecasts without another pricing restriction does not generally enlarge this payoff span. The criterion is applied separately at each public state; state-contingent identification of the relevant kernel moment then identifies the removal-price variance under a known public-state law.

For a concrete two-state illustration with equal probabilities, let the factual payoff be \((1,3)\) and the counterfactual payoff \((1,1)\). The vector \(h=(3,-1)\) is orthogonal to the factual payoff but not to the constant payoff. Kernels \((2,2)+\epsilon(3,-1)\), for sufficiently small positive or negative \(\epsilon\), all price the factual payoff at four; their constant-payoff prices equal \(2+\epsilon\). Adding a claim with payoff \((3,1)\) spans the constant vector and removes this freedom.

Strict positivity and finite support are substantive. The perturbation proof uses an interior feasible kernel; identification can change on a boundary where kernels are forced to zero. If one instead closes the class to nonnegative kernels, sharp upper and lower counterfactual prices are linear-program extrema. They are attained whenever the feasible set is compact, for example if an observed payoff is strictly positive in every atom, which bounds every kernel coordinate. For the original strictly positive class those extrema can be limits rather than attained values.

Checked locations: “An unobserved pricing-kernel direction,” its sharp-interval theorem, and additional-observation proposition. Full source and YAML were read. This is a restricted spanning result, not identification of realistic multiperiod channels or empirical kernels. The separate interaction theorem is not extended; external references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-G12-290-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/f2/prb_f24658c1c3f14380b9ea18b9abd01b1f/contributions/con_16678c4588e2484d9fa9318c10f7a9c9/files/G12-290.tex). Canonical revision: `rev_49bc099556ed4daaa3d7bf1b1d4d2bb8`.

