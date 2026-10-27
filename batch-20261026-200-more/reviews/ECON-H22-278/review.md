# The formal-to-informal welfare jump has a complete sign classification

The source derives a correct welfare-jump expression at the monopolist's legal-status switch. That expression has an unexpectedly sharp sign classification. Output necessarily falls when the firm becomes informal, yet real surplus can rise because the resource compliance cost disappears. The result below identifies exactly which force dominates.

Use the separate endogenous-status model, with \(D=A-c>0\), \(B>0\), \(0<e<D\), and
\[
0<F<F_{\max}:=\frac{D^2-(D-e)^2}{4B}.
\]
Put \(q_F=(D-\tau^*)/(2B)\), \(q_I=(D-e)/(2B)\), where the source's threshold is \(\tau^*=D-\sqrt{(D-e)^2+4BF}\in(0,e)\). Write \(d=q_F-q_I>0\). Equality of branch profits at the switch gives the useful identity
\[
F=B(q_F^2-q_I^2).
\]
Substituting this into the source's aggregate equivalent-variation jump yields
\[
\begin{aligned}
J&=D(q_I-q_F)-\frac B2(q_I^2-q_F^2)+F\\
 &=d\left[-D+\frac{3B}{2}(q_F+q_I)\right]
 =d\left[\frac D2-\frac34(\tau^*+e)\right].
\end{aligned}
\]
Because \(d>0\), the switch raises real surplus exactly when \(\tau^*+e<2D/3\), lowers it when the inequality reverses, and is welfare-neutral at equality. This is a complete criterion, not merely examples of either sign.

It can be expressed entirely in primitive regions. As \(F\) ranges from zero to \(F_{\max}\), the threshold \(\tau^*\) decreases continuously and strictly from \(e\) to zero.

* If \(0<e\le D/3\), then \(\tau^*+e<2e\le2D/3\), so every admissible switch has \(J>0\).
* If \(2D/3\le e<D\), then \(\tau^*+e>e\ge2D/3\), so every admissible switch has \(J<0\).
* If \(D/3<e<2D/3\), define
\[
F_{\mathrm{crit}}=\frac{2D}{3B}\left(e-\frac D3\right).
\]
Then \(J<0\) for \(F<F_{\mathrm{crit}}\), \(J=0\) at equality, and \(J>0\) for \(F>F_{\mathrm{crit}}\).

For the middle case, solve \(\tau^*=2D/3-e\): squaring the positive equation \(\sqrt{(D-e)^2+4BF}=D/3+e\) gives the displayed \(F_{\mathrm{crit}}\). The right-hand threshold lies strictly between zero and \(e\), so the solution lies strictly inside \((0,F_{\max})\); there is no extraneous squared root. At the enforcement boundaries the strict signs above follow from the open restrictions on \(F\).

Exact numerical instances illustrate both outcomes. With \(D=B=1,e=0.3,F=0.0375\), the switch has \(\tau^*=0.2,q_F=0.4,q_I=0.35\), and \(J=0.00625>0\). With \(D=B=1,e=0.8,F=0.03\), it has \(\tau^*=0.6,q_F=0.2,q_I=0.1\), and \(J=-0.055\). These are analytic parameter choices, not estimates. Both satisfy every source restriction and have positive informal profits, excluding entry as an intervening choice.

Profit continuity at the threshold means the discontinuous ownership-income term is zero; the surplus comparison comes from consumers, government receipts, and saved real compliance resources. Counting \(F\) as a tax receipt would eliminate this mechanism incorrectly. The tie convention chooses the formal branch exactly at \(\tau^*\); \(J\) is the right-hand jump from that branch to the informal limit.

Checked locations: the separate endogenous-status model and exact-status-threshold theorem; the Cournot model was also read but is not extended here. Full manuscript/YAML were checked. This does not infer household-level signs, endogenous employment incidence, or empirical enforcement effects. External references are unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-H22-278-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/70/prb_70dbd8333c0f4672b5cde4c2647028e9/contributions/con_97e6705d065a4cc9b3bbff2e9742eccb/files/H22-278.tex). Canonical revision: `rev_0aaa6442c9484b57bbebd46689d69fe2`.

