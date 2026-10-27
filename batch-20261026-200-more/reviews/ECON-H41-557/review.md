# Finite Nash behavior does not guarantee a bounded endogenous-identity planner problem

The source's condition \(n\kappa\gamma^2<1\) gives a unique finite Nash equilibrium. A planner maximizing the sum of its stated cardinal utilities faces a stronger feedback condition. There is a nonempty parameter region with a well-defined Nash outcome but unbounded aggregate welfare over feasible actions.

Keep the same nonnegative contributions, real-valued identity choices, fixed anchor \(s\ge0\), and all utility primitives. Define \(f=\kappa\gamma^2>0\) and \(A=\sum_iv_i+n\gamma s>0\). For any fixed contribution vector with total \(Q\), maximizing each identity term gives \(I_i=s+\kappa\gamma Q\), exactly as in the source. The sum of utilities after these identity choices is
\[
\sum_i u_i=AQ+\frac{nf}{2}Q^2-\frac12\sum_ic_i^2.
\]
For a fixed \(Q\ge0\), Cauchy–Schwarz gives \(\sum_ic_i^2\ge Q^2/n\), attained uniquely by equal contributions \(c_i=Q/n\). Thus the complete planner problem reduces to
\[
\max_{Q\ge0}\left\{AQ-\frac12\left(\frac1n-nf\right)Q^2\right\}.
\]

If \(n^2f<1\), the reduced objective is strictly concave and coercive. Its unique maximizer and implementing actions are
\[
Q^P=\frac{nA}{1-n^2f},\qquad
c_i^P=Q^P/n,\qquad I_i^P=s+\kappa\gamma Q^P.
\]
The maximum aggregate utility is \(nA^2/[2(1-n^2f)]\). Strict concavity of the reduced problem and uniqueness of both conditional minimizations prove global uniqueness, not merely stationary optimality.

If \(n^2f=1\), the objective equals \(AQ\), whose positive slope makes its supremum infinite. If \(n^2f>1\), its quadratic coefficient is positive and the same supremum is infinite. Both claims are attained along the feasible ray \(c_i=Q/n\), with the corresponding optimized identities. No negative contribution, changed ancestry or hidden transfer is needed.

Therefore the interval
\[
1/n^2\le f<1/n
\]
has a unique finite Nash equilibrium by the source's theorem, while this particular planner objective is unbounded. For example \(n=2,f=3/10\) satisfies \(2f<1\) but \(4f>1\). This is a boundary of the cardinal bilinear utility specification, not an error in the source, which explicitly presents welfare as a separate declared evaluator rather than proving planner boundedness.

Below the stronger threshold, compare its Nash aggregate \(Q^N=A/(1-nf)\) with the planner aggregate:
\[
\frac{Q^P}{Q^N}=\frac{n(1-nf)}{1-n^2f}>n.
\]
The inequality is strict because \(n\ge2\) and \(f>0\). Standard public-good underprovision is amplified by endogenous identity feedback. Heterogeneous \(v_i\) also make Nash contributions unequal, whereas the planner equalizes contributions because their quadratic effort costs are identical and every \(v_i\) multiplies the common total output.

Finite physical contribution bounds or a sufficiently strong concave benefit specification can eliminate unboundedness, but those are additional primitives. Subtracting a cost depending only on the fixed anchor \(s\) cannot bound the action problem at that anchor. Likewise the mathematical planner is not automatically a feasible institution implementing its actions voluntarily.

Checked locations: utility (1), condition (2), unique-equilibrium theorem and residual welfare discussion. Full source/YAML were read. This clarifies a restricted welfare boundary without asserting an empirical institutional ranking or a general statement about ethnicity. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-H41-557-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/a7/prb_a7d3cb3971e34364800c839a442c612c/contributions/con_0e6997a06acc4a6c8962a9dc46e2c3a8/files/H41-557.tex). Canonical revision: `rev_0fd0a490d6914a0793f6f4b1e37f0ac1`.

