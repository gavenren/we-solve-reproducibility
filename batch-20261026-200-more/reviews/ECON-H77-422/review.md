# Financing shares and the gross grant flow required for implementation

The manuscript derives the correct grant \(t_j^*=(A_j-b_j)/(1-\eta_j)\) for fixed financing shares. If financing shares can themselves be selected, one can solve exactly which constitution implements the same social service allocation with the smallest gross central grant budget. This is a flow-minimization result; grants remain transfers in the source's welfare boundary.

Restrict to \(J\ge2\) jurisdictions with strictly positive incentive gaps
\[
d_j=A_j-b_j>0,\qquad g_j^*=A_j/c_j>0,
\]
and put \(w_j=d_jg_j^*>0\). Choose shares \(\eta_j\ge0\), \(\sum_j\eta_j=1\), \(\eta_j<1\), then use the source's implementing grants. At optimal services the gross central outlay is
\[
T^*(\eta)=\sum_jt_j^*g_j^*
=\sum_j\frac{w_j}{1-\eta_j}.
\tag{A}
\]
The equilibrium quantities and real welfare stay fixed as \(\eta\) varies; what changes is the amount circulated through grants and offsetting central taxes.

Set \(s_j=1-\eta_j\). The problem becomes
\[
\min_{0<s_j\le1,\ \sum_js_j=J-1}\sum_jw_j/s_j.
\tag{B}
\]
Its unique solution has the form
\[
s_j^*=\min\{1,\sqrt{w_j/\lambda}\},\qquad
\sum_j\min\{1,\sqrt{w_j/\lambda}\}=J-1.
\tag{C}
\]
Thus \(\eta_j^*=1-s_j^*\) and \(t_j^*=d_j/s_j^*\).

For a complete proof, the feasible set permits a finite candidate, for example equal shares. As any \(s_j\downarrow0\), its positive term \(w_j/s_j\) diverges. Hence a minimizing sequence stays away from zero, and compactness on that restricted set yields attainment. The objective has diagonal Hessian \(2w_j/s_j^3>0\), proving strict convexity and uniqueness.

The scalar equation in (C) has a solution: its left side is continuous, equals \(J\) for sufficiently small positive \(\lambda\), and tends to zero as \(\lambda\to\infty\). On the region where the sum is below \(J\), at least one term is unsaturated and decreases strictly, so the solution for \(J-1\) is unique. For a fixed \(\lambda\), minimizing \(w_j/s+\lambda s\) over \(0<s\le1\) gives exactly the displayed clipped square root. Summing these pointwise inequalities and using the common total \(J-1\) proves global optimality of (C), including jurisdictions whose upper bound \(s_j=1\) is active. Those jurisdictions have zero financing share, which the source allows.

For two jurisdictions no upper bound binds, and the solution is especially simple:
\[
s_j^*=\frac{\sqrt{w_j}}{\sqrt{w_1}+\sqrt{w_2}},
\qquad
T_{\min}=(\sqrt{w_1}+\sqrt{w_2})^2.
\]
Equal financing shares instead produce \(T_{\rm equal}=2(w_1+w_2)\). The exact excess gross flow is
\[
T_{\rm equal}-T_{\min}=(\sqrt{w_1}-\sqrt{w_2})^2.
\]
It vanishes exactly when the two implementation-weighted incentive gaps coincide.

High-\(w_j\) jurisdictions receive larger \(s_j\), hence lower own financing shares, because financing their own grant strongly dilutes a costly required incentive. This allocation is about the response to marginal central taxation. It does not presume that residents have changed their social valuations.

The objective in (B) could matter under a separate gross-flow capacity constraint or administrative consideration. Within the manuscript's original lump-sum, costless-transfer welfare accounting, reducing \(T^*\) alone is not an additional real welfare gain. Negative incentive gaps, upper grant caps, mobility and endogenous political representation require separate treatment. The result retains the declared political objectives and proves a financing-design frontier rather than a universal argument for centralization or decentralization.

Source: [ECON-H77-422-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/7e/prb_7e382267a194403ebc426d297ebb0d78/contributions/con_8b85f936b5e24d7b8ec3dff0b9442f27/files/H77-422.tex), canonical revision `rev_56bcb41409f8447492396116e51d37f5`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
