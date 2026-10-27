# Finite forgiveness after false monitoring alarms

The source shows that its grim-trigger equilibrium ends almost surely when false alarms occur. A finite-punishment strategy repairs that persistence issue within the same repeated game. Its incentive threshold and long-run support frequency can be derived exactly.

Keep \(d>0,R>0\), discount \(\delta\in(0,1)\), prescribed benefit \(b\le\bar b\), and \(0\le q_1<q_0\le1\). Choose an integer punishment length \(L\ge1\). In the good state the party pays \(b\), the voter supports, and a bad signal starts \(L\) punishment periods at the next date. During punishment the party pays zero and the voter opposes; broker signals are ignored, the counter decreases deterministically, and cooperation resumes afterward. A payment deviation in the good state causes immediate opposition and starts \(L\) punishment periods next date. Nonprescribed payments during punishment do not change the countdown.

Let \(V,P\) be start-of-period good-state voter and party values. Starting a punishment spell has values \(\delta^LV,\delta^LP\), since current punishment payoffs are zero for both sides. Define
\[
D_L=1-\delta+\delta q_1(1-\delta^L)>0.
\]
The good-state Bellman equations give
\[
V=(b-d)/D_L,\qquad P=(R-b)/D_L.
\tag{A}
\]

After receiving \(b\), the voter's support incentive is exactly
\[
d\le\delta(q_0-q_1)(1-\delta^L)V.
\]
Substitution from (A) yields the threshold
\[
b\ge b_L:=
d\left[
\frac{q_0}{q_0-q_1}
+\frac{1-\delta}{\delta(q_0-q_1)(1-\delta^L)}
\right].
\tag{B}
\]
The party's best good-state payment deviation is zero, followed by immediate opposition and delayed return to cooperation. Its deviation value is \(\delta^{L+1}P\). Hence compliance is optimal exactly when \(P\ge0\), or \(b\le R\).

During punishment the voter gains nothing from support because the countdown is action-independent, so opposition is strictly optimal. The party obtains no support from any payment there and optimally pays zero. These one-period conditions therefore hold at every public history; bounded discounted payoffs make the one-deviation principle applicable. The specified finite strategy is sequentially implementable if and only if
\[
b_L\le b\le\min(R,\bar b)
\]
within this strategy class.

The threshold decreases strictly with \(L\), and
\[
\lim_{L\to\infty}b_L
=\frac{d(1-\delta+\delta q_0)}
       {\delta(q_0-q_1)},
\]
the source's grim-trigger threshold. Finite forgiveness sacrifices punishment severity and thus requires a larger benefit. If the resource cap lies strictly above the grim threshold, some finite \(L\) is feasible; if it equals the grim threshold exactly, no finite \(L\) reaches that equality.

When \(q_1>0\), the induced public-state chain has a good spell of expected length \(1/q_1\), followed by exactly \(L\) punishment periods. Its stationary good-state fraction is
\[
\pi_G=\frac1{1+Lq_1}.
\tag{C}
\]
This can also be checked from stationary flows: every punishment state has probability \(q_1\pi_G\), and the \(L+1\) state probabilities sum to one. The finite irreducible chain returns to cooperation infinitely often almost surely. Consequently support has a positive long-run frequency, unlike the source's grim strategy, which eventually ends permanently. If \(q_1=0\), the equilibrium path stays good forever.

Longer punishments lower the required benefit in (B) but lower the stationary support fraction in (C). This gives a precise incentive-versus-false-alarm tradeoff. Perfect secrecy still defeats this monitoring mechanism: at \(q_0=q_1\), a support deviation changes no signal distribution, so no finite benefit paid before voting can compensate its current cost through future sanctions.

This is an additional equilibrium construction, not a characterization of every repeated-game outcome. It retains the source's observable payments, broker technology, no competing party and no reciprocity preference. It neither identifies actual monitoring nor makes transfers themselves a social resource gain.

Source: [ECON-D72-545-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/b6/prb_b68821ef0ee34326b0e9444c9733f00b/contributions/con_b98c8f27b4b04e1b9f978bb6ebaecc86/files/D72-545.tex), canonical revision `rev_ecb1a5e329db432582c6e58f9b1e5413`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
