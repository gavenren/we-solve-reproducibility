# Boundary welfare losses and a sharp welfare-safety test in the subsidy benchmark

Finding: **Supports the claim**.

Reviewed source: [ECON-L52-201-A1 manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/5e/prb_5eeb0a20f47c466abad6d9f6c1cf165f/contributions/con_3460964e5b114402bd45a49b72720c59/files/L52-201.tex), revision `rev_bbf9e142cbb7490c84d5776f0e6bd6fb` at pinned repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

The manuscript's declared contribution is a deliberately specified two-country benchmark. Its metadata marks the larger problem unresolved, and the text expressly excludes endogenous world prices, heterogeneous firms, and a derived retaliation mechanism. I checked the benchmark as stated. The equilibrium and interior loss formulas are correct. A useful additional check is to solve the boundary cases and identify when the symmetric subsidy outcome can make both countries worse off than the no-policy allocation.

Let \(d=1+2\lambda>0\), \(L=\bar x\), and \(P(z)=\min\{L,\max\{0,z\}\}\). Define the unconstrained national and cooperative choices
\[
 z_N=(\theta+b-\lambda)/d,\qquad
 z_C=(\theta+\kappa-\lambda)/d.
\]
The national objective is strictly concave in its own action, and the foreign action enters only additively. Thus each country's unique best response is \(P(z_N)\), independently of the other country's choice. This is enough for unique Nash equilibrium; no strategic-complementarity or equilibrium-selection argument is required. Summing the two payoffs cancels the rent account exactly, giving the cooperative choice \(P(z_C)\) separately in each coordinate.

Write \(x_N=P(z_N)\), \(x_C=P(z_C)\), and \(\Delta=x_N-x_C\). The exact world-welfare loss, including all clipped cases, is
\[
 \mathcal L
 =d\{(x_N-z_C)^2-(x_C-z_C)^2\}
 =d\Delta^2+2d(x_C-z_C)\Delta.
\]
The projection inequality \((z_C-x_C)(x_N-x_C)\le0\) shows that the last term is nonnegative. Thus \(\mathcal L\ge d\Delta^2\), with equality when the cooperative optimum is interior, or when its projection residual vanishes. This explains why substituting the clipped policy difference into the manuscript's interior square formula is generally invalid at a binding cooperative constraint.

There is also a global upper bound matching the interior formula:
\[
 0\le\mathcal L\le (b-\kappa)^2/d.
\]
For completeness, put \(\delta=z_N-z_C\) and \(r=x_C-z_C\). Optimality of the projection \(x_N=P(z_C+\delta)\) gives
\((\delta-r-\Delta)\Delta\ge0\). Hence
\[
 \mathcal L/d=\Delta^2+2r\Delta
 \le2\delta\Delta-\Delta^2
 \le\delta^2.
\]
This is a boundary-valid loss bound; it becomes equality in the manuscript's interior case. Clipping can therefore reduce the loss below its unconstrained value, and may make two different incentive wedges produce the same constrained action.

A second independent implication concerns the policy comparison with zero subsidies. At a symmetric action \(x\), country \(i\)'s net welfare is
\[
 W_i(x,x)=(\theta+\kappa-\lambda)x-\frac d2x^2.
\]
The business-stealing term disappears from this expression even though it changes the government's unilateral incentive. For \(x_N>0\), the symmetric Nash outcome weakly improves each country's welfare over no policy exactly when
\[
 x_N\le\frac{2(\theta+\kappa-\lambda)}d.
\]
If the right side is negative, no positive symmetric subsidy passes this comparison. This criterion is distinct from the sign of the Nash/cooperative policy wedge: over-subsidization can still raise welfare relative to zero, while a sufficiently large wedge can destroy all of the attainable gain.

For example, take \(\lambda=0,\theta=1,\kappa=0,b=2,L=4\). The Nash action is \(3\), the cooperative action is \(1\), and each country's Nash welfare is \(3-9/2=-3/2\), compared with zero without subsidies. Cooperative world welfare is \(1\), Nash world welfare is \(-3\), and their difference is \(4=(b-\kappa)^2/d\). These numbers follow from the exact stated primitives; they do not require a trade response omitted from the model. A government still prefers its Nash action holding the other's subsidy fixed.

If \(\theta,\lambda,b\) are known but the only restriction on \(\kappa\) is nonnegativity, this yields a sharp robust safety test: a positive Nash subsidy is weakly welfare-improving for every admissible \(\kappa\) exactly when \(x_N\le2(\theta-\lambda)/d\). Necessity follows by taking \(\kappa=0\); sufficiency follows because welfare increases with \(\kappa\). Under an interior national choice this reduces to \(b\le\theta-\lambda\). Strict improvement for every admissible \(\kappa\) requires the corresponding strict inequality. It reinforces the manuscript's identification point while specifying the exact additional bound needed for this narrower decision.

These are algebraic extensions of the benchmark, not a challenge to its accounting. The subsidy transfer cancels domestically as specified, the fiscal distortion remains a real loss, and the international rent term cancels only in worldwide welfare. I found no error in the theorem. Its limitations concerning spillover identification and richer policy games are acknowledged and remain outside this review's support.
