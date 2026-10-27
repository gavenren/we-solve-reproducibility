# Exact compensation frontier with clipped Nash policies

This independently extends the manuscript's stringent-cap example to all its heterogeneous parameters, including binding individual bounds. The result characterizes exactly which forest caps admit compensation. It concerns the reduced-equilibrium model, not structural trade responses.

Write \(S=\sum_i d_i\), \(C=\sum_i c_i\), and let \(n_i=\min(A_i,c_id_i\theta)\) be the manuscript's Nash policy (equation (2)). Define \(N=\sum_i n_i\), \(Q=\sum_i n_i^2/c_i\), and the nonnegative allocation inefficiency \(E=Q-N^2/C\). Nonnegativity follows by the same weighted Cauchy inequality used in the first theorem; equality holds precisely when the Nash allocation is proportional to \(c_i\). The clipped Nash policies need not have that proportionality.

For a cooperative aggregate \(A\in[0,A_{\max}]\), cost minimization gives \(a_i=c_iA/C\). Summing equation (1) and subtracting welfare at the actual, possibly clipped Nash allocation gives
\[
G(A)=-\frac{A^2}{2C}+\theta S A+\frac Q2-\theta SN
=\frac E2+\frac{(C\theta S-N)^2-(A-C\theta S)^2}{2C}.
\]
The common environmental constant cancels; the baseline cost remains \(Q/2\), rather than \(N^2/(2C)\). Replacing it by the latter would incorrectly erase the gains from reallocating a fixed aggregate.

Consequently the exact weak-participation interval is
\[
A_-\le A\le A_+,\qquad
A_\pm=C\theta S\pm\sqrt{(C\theta S-N)^2+CE},
\]
intersected with the physically feasible interval. The square root is real even when some countries hit their upper bounds. Also \(n_i\le c_id_i\theta\) implies \(N\le C\theta S\), and \(A_-\le N\le A_+\). Thus a proportional reallocation at the Nash aggregate always admits compensation, with gain \(E/2\).

Now impose the manuscript's cap lower bound \(L=(D_0-\bar D)/\theta\). Put \(A_0=\min(C\theta S,A_{\max})\). If \(L\le A_0\), its cooperative optimum is \(A_0\), whose welfare is at least Nash welfare because the unconstrained planner can choose the Nash vector. If \(L>A_0\), feasibility forces \(A_0=C\theta S<A_{\max}\), and the cooperative optimum is \(A=L\). Therefore **a feasible cap admits budget-balanced weak participation if and only if \(L\le A_+\)**. If \(A_+\ge A_{\max}\), every feasible cap passes; otherwise the maximal compensable requirement is exactly \(A_+\). This also proves the policy comparison does not depend merely on how stringent the cap looks in absolute units.

At an endpoint with \(G=0\), budget balance and nonnegative country gains force every compensated gain to be zero. The transfer vector is then uniquely \(t_i=W_i(n)-W_i(a)\). For \(G>0\), any division of aggregate surplus yields feasible transfers as in the second theorem, including strict gains for all. No unrestricted transfer can help when \(G<0\).

For the symmetric numerical example, \(C=2,S=2,\theta=1,N=2,Q=2,E=0\). The roots are \(2\) and \(6\); the stringent-cap region begins at \(4\), recovering its threshold without assuming the example in the derivation. When \(E>0\), the upper root strictly increases relative to the proportional-baseline calculation: eliminating inefficient Nash cost creates additional compensation capacity.

Checked locations: equation (1), both theorems, and the stringent-cap example. I checked the full manuscript and YAML. External bibliography, empirical leakage, and political transfer constraints are not verified. This is an exact conditional extension, with no assertion that the broad catalogue problem is solved.

Original prose: CC BY 4.0.

Pinned source: [ECON-F18-222-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/74/prb_74fac30499d745e39764ceefb51b24c9/contributions/con_eb353d381b8f490c86c4b554831d6870/files/F18-222.tex). Canonical revision: `rev_b70a89e8b7714b5c833f0b7cd0d264ae`.

