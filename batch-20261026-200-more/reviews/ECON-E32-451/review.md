# Exact temporal allocation of permanent repair

The source's least-cost repair theorem handles arbitrary positive definite stacked costs. A useful specialization separates which instruments repair the permanent state from when they should be used. It also reveals a boundary of the financing model: with only quadratic costs, spreading repair over an unrestricted horizon can drive its infimum to zero.

Let \(C_0=PG\), \(b=-Pv\), and suppose \(b\in{\rm range}(C_0)\), as required for feasibility. Retain signed instruments and a finite horizon \(T\ge1\). Specialize the cost to
\[
J(U)=\frac12\sum_{s=0}^{T-1}w_su_s^\top R_0u_s,\qquad
w_s>0,\quad R_0\succ0,
\]
with repair constraint \(C_0\sum_su_s=b\). Put
\[
H_T=\sum_{s=0}^{T-1}w_s^{-1},\qquad
M=C_0R_0^{-1}C_0^\top.
\]

For any fixed aggregate instrument vector \(a=\sum_su_s\), the unique least-cost timing is
\[
u_s=\frac{a}{w_sH_T},
\qquad
J_{\min}(a)=\frac{a^\top R_0a}{2H_T}.
\tag{A}
\]
One can prove this without matrix differentiation. Set \(e_s=u_s-a/(w_sH_T)\), so \(\sum_se_s=0\). Expanding the cost yields
\[
\sum_sw_su_s^\top R_0u_s
=\frac{a^\top R_0a}{H_T}
+\sum_sw_se_s^\top R_0e_s.
\]
The cross terms cancel because their sum is proportional to \(\sum_se_s\). Positive definiteness makes the remainder nonnegative, with equality only when every \(e_s=0\). This proves both optimality and uniqueness.

It remains to choose the aggregate \(a\) subject to \(C_0a=b\). The source's single-period quadratic argument gives
\[
a^*=R_0^{-1}C_0^\top M^+b.
\]
Combining with (A), the full unique solution and cost are
\[
u_s^*=\frac{R_0^{-1}C_0^\top M^+b}{w_sH_T},
\qquad
J_T^*=\frac{b^\top M^+b}{2H_T}.
\tag{B}
\]
The pseudoinverse is required if some permanent-state coordinates are redundant. Feasibility still means \(b\) belongs to the range; (B) does not repair an unreachable displacement. If \(b=0\), the unique minimum is zero controls.

With equal date costs \(w_s=1\), each date uses \(a^*/T\), and cost is the one-date minimum divided by \(T\). Thus, whenever nonzero repair is feasible, \(J_T^*>0\) for each finite horizon but \(J_T^*\to0\) as \(T\to\infty\). This is an infimum across different finite-horizon problems. No finite sequence attains zero cost for nonzero \(b\), because positive definite costs make zero cost require every control to vanish.

If date-zero costs are discounted at factor \(\delta\in(0,1)\), so \(w_s=\delta^s\), the optimal timing weights are proportional to \(\delta^{-s}\): later instruments are cheaper in the stated accounting. The same aggregate permanent repair is achieved, but this least-cost criterion favors postponement. That observation is conditional on disregarding the welfare cost of living with the damage while repair is delayed.

This matters for interpreting the source's distinction between permanent repair and discounted welfare. Permanent-state effects depend only on the sum of controls, whereas its equation (4) values their timing and transitory responses. Adding linear resource costs, deadlines, intensity caps, discount-weighted capacity benefits or irreversible exit can prevent the vanishing-cost comparison. None can be inferred from the quadratic minimum alone.

The result is an exact timing refinement within the finite-dimensional invariant accumulation model. It does not identify the permanent projection, establish that observed recessions have permanent effects, or extend signed-control feasibility to nonnegative instruments. No empirical or external-literature claim is used.

Source: [ECON-E32-451-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/b4/prb_b4b9bb617c12430b85ddeb2733c8bc25/contributions/con_3d373fe7d4d1489d9b90a3ecb3025278/files/E32-451.tex), canonical revision `rev_c050ab11f8264069bfa86eb3275cc895`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
