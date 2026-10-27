# Equal-revenue tax reforms have strictly different worker burdens

The open-economy theorem's incidence formula admits a global comparison that is useful when revenue is the policy target. Two positive tax rates raising the same revenue generally impose different domestic worker burdens. The higher-rate reform is strictly worse for workers for every recycling fraction allowed by the source.

Keep \(0<\alpha<1\), \(a=\alpha/(1-\alpha)\), \(g\in[0,1]\), and baseline output \(Y_0>0\). The source gives
\[
T(\tau)=\alpha Y_0\tau(1-\tau)^a,\quad
CV(\tau)=(1-\alpha)Y_0[1-(1-\tau)^a]-gT(\tau).
\tag{A}
\]
The domain is \(0<\tau<1\), with the baseline at zero.

First, receipts have exactly one peak:
\[
T'(\tau)=\alpha Y_0(1-\tau)^{a-1}[1-(a+1)\tau].
\]
Thus the maximizing rate is \(\tau^*=1/(a+1)=1-\alpha\), and
\[
T_{\max}=\alpha(1-\alpha)Y_0\alpha^a.
\tag{B}
\]
Receipts increase strictly before \(\tau^*\), decrease strictly afterward, and converge to zero at either end. Continuity and these strict inequalities imply that every target \(t\in(0,T_{\max})\) has exactly two implementing rates \(\tau_L<\tau^*<\tau_H\). The peak has exactly one rate; targets above the peak are infeasible in this benchmark.

For the two rates implementing the same positive target, transfers \(gt\) cancel from the compensation difference:
\[
CV(\tau_H)-CV(\tau_L)
=(1-\alpha)Y_0[(1-\tau_L)^a-(1-\tau_H)^a]>0.
\tag{C}
\]
Dividing by the common \(t\) proves the same strict ranking for incidence. The sign does not require estimating or fixing a special recycling fraction: it holds for each common \(g\). Economically, equal receipts imply equal transfers, while the high-rate equilibrium has lower capital, output and wage income.

A stronger property is that compensation itself is strictly increasing throughout the positive-rate domain. Direct differentiation gives
\[
CV'(\tau)=\alpha Y_0(1-\tau)^{a-1}
\{(1-g)(1-\tau)+ga\tau\}>0.
\tag{D}
\]
At \(g=0\) the first summand is strictly positive; at \(g=1\) the second is strictly positive; intermediate values preserve positivity. Complete recycling therefore does not reverse the global welfare ranking, even on the decreasing-revenue branch. At zero its first derivative vanishes when \(g=1\), consistently with the manuscript's second-order distortion.

Normalized incidence is also strictly increasing. Set \(f(\tau)=(1-\tau)^{-a}\). Equation (1) in the source is
\[
\iota(\tau)+g=\frac{f(\tau)-f(0)}{a\tau}
=\frac1{a\tau}\int_0^\tau f'(s)\,ds.
\]
Because \(f'\) is strictly increasing, its average over \([0,\tau]\) increases strictly as the upper endpoint increases. This proves monotonicity without a fragile sign expansion. The lower limit is \(1-g\); as \(\tau\uparrow1\), incidence diverges to infinity while compensation converges to the finite lost baseline wage bill \((1-\alpha)Y_0\). The divergence comes from the vanishing denominator \(T(\tau)\), not from an unbounded household loss.

These are conditional global comparative statics, not an empirical tax-rate recommendation. They hold with perfectly elastic foreign capital supply, quasilinear domestic workers who own no capital, fixed labor and the specified revenue use. The source's fixed-capital redistribution and announcement-wealth propositions concern different environments and are not combined with (A). No external references or actual ownership and mobility parameters are verified.

Source: [ECON-H22-245-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/c5/prb_c5bcf3e537024841af5a6fef126cc2ce/contributions/con_3ce486475e7144588576b6b79bf408f7/files/H22-245.tex), canonical revision `rev_8e64e25ce1c14ed29ac89097d283b8f7`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
