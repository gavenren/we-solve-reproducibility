# Sharp recovery-rate bounds and a two-horizon identification design

The source shows that an adult outcome reflects a convolution of disruption sensitivity and recovery. That ambiguity can be made exact. A single adult horizon with age-specific causal impulse losses generally does not identify recovery; externally bounded sensitivities give a sharp interval, and two comparable adult horizons can identify it.

Work inside the linear human-capital stock model, with recovery coefficient \(0<\rho\le1\), common adult measurement age \(A\), and an additional unit disruption at chronological age \(t\). Allow its net sensitivity to be \(g_t>0\), so its stock decrement on entry is \(g_t\). Suppose causal adult stock losses \(L_t>0\) are known for a finite collection of ages \(t<A\). The source's stock identity gives
\[
L_t=g_t\rho^{e_t},\qquad e_t=A-1-t.
\]
No earnings-price or labor-supply mapping is inferred from these stock measurements.

If sensitivities are otherwise unrestricted positive numbers, every \(\rho\in(0,1]\) is compatible: choose \(g_t=L_t/\rho^{e_t}\) at each observed age. Thus even a perfectly measured age profile cannot distinguish persistence from age sensitivity. This is exact nonidentification within the structural class, not sampling uncertainty.

Now suppose independent external restrictions give \(0<\underline g_t\le g_t\le\overline g_t<\infty\), with every combination allowed. For each \(e_t>0\), the sharp recovery restriction is
\[
(L_t/\overline g_t)^{1/e_t}\le\rho\le
(L_t/\underline g_t)^{1/e_t}.
\]
Intersect these intervals with \((0,1]\). At \(e_t=0\), the observation requires \(L_t\in[\underline g_t,\overline g_t]\) and imposes no further restriction on \(\rho\). If any such condition fails or the intersection is empty, the benchmark is incompatible with the observations.

Necessity follows by dividing the positive equation for \(L_t\) and taking an increasing positive root. For sufficiency, every \(\rho\) in the intersection gives \(g_t=L_t/\rho^{e_t}\) inside every stipulated interval. These choices reproduce the complete impulse-loss profile simultaneously, proving sharpness and showing that no unlisted cross-age restriction has been imposed. Positive losses and finite upper sensitivity bounds keep feasible lower recovery bounds away from zero whenever a positive exponent is observed.

A second outcome horizon can separate the mechanisms under a different, explicit design. Consider the same initial unit disruption at age \(t\), measure its causal stock loss at ages \(A_1<A_2\), and assume that after the initial disruption there are no further regime differences in investment, support or other disruption. Require the same recovery coefficient and comparable stock measurement scale. Then
\[
\frac{L_{t,A_2}}{L_{t,A_1}}=\rho^{A_2-A_1},
\qquad
\rho=\left(\frac{L_{t,A_2}}{L_{t,A_1}}\right)^{1/(A_2-A_1)}.
\]
The sensitivity follows from either horizon equation. Ratios above one reject this positive-decay subclass; ratios at one imply \(\rho=1\). Additional horizons or impulse ages must deliver the same inferred \(\rho\), providing overidentifying restrictions.

For example, losses four and one observed two years apart imply \(\rho=1/2\), whereas a single loss of four could reflect any permitted recovery coefficient paired with an appropriate initial sensitivity. Longitudinal follow-up supplies information different from another cross-sectional age cell.

Checked locations: stock calculation (1), its age-gradient proposition and convolution discussion. Full manuscript/YAML were read. The argument assumes identified causal impulse losses; chronological-age regressions, selective tracing, changing later support and survivor selection do not automatically supply them. External references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-J24-515-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/ee/prb_eee04b41eef448c29471e63873e31fe7/contributions/con_2e33d053e73949feb3d67052ca969e81/files/J24-515.tex). Canonical revision: `rev_c47fd2d466a346a487c53ab60345c28e`.

