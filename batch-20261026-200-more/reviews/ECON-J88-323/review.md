# Joint employment and wage responses identify the portable-benefit frontier

The source's competitive one-task benchmark gives a complete frontier at a known portable-benefit valuation \(\nu\). Because that valuation is common across policies, uncertainty produces only two possible frontier sets in this benchmark. A joint wage-and-employment response identifies which set applies under its supply restriction.

Fix a common closed feasible interval of contribution rates \(t\in[0,\bar t]\), with \(\bar t>0\), on which every model under consideration has positive cash wages and interior employment. Retain \(k>0\), linear supply, demand and the same baseline worker population. Let the only uncertain parameter be the common \(\nu\in[\nu_L,\nu_U]\subset[0,\infty)\). All other primitives are known for this first calculation.

The source derives
\[
N_\nu(t)=N_0+\frac{sB(\nu-1)}{B+s}t,\quad
S_\nu(t)=N_\nu(t)^2/(2s),\quad C(t)=kt^2.
\]
Since employment stays positive, worker welfare is strictly increasing in employment. For \(\nu\le1\), rate zero dominates every positive rate: employment and worker welfare weakly decrease, while implementation cost strictly increases. The entire frontier is therefore \(\{0\}\). For \(\nu>1\), both worker outcomes strictly rise with the rate while cost strictly rises, so the entire interval is the frontier.

Consequently the sharp identified set of frontier *sets* is exactly:

* \(\{\{0\}\}\) when \(\nu_U\le1\);
* \(\{[0,\bar t]\}\) when \(\nu_L>1\);
* \(\{\{0\},[0,\bar t]\}\) when \(\nu_L\le1<\nu_U\).

Every listed set is attained by a single admissible common valuation, and no intermediate subset is possible. Taking independent coordinate bounds policy by policy would overlook this restriction and invent frontier shapes inconsistent with the structural family. For a finite rate menu containing zero, replace the interval by that entire menu. If the menu contains only zero, the two possibilities coincide.

Now allow \(s,B,A,\nu\) initially unknown, but observe the baseline cash wage \(w_0>0\), employment \(N_0>0\), and the causal local responses \(\dot w,\dot N\) to the contribution. At \(t=0\), effective compensation equals cash wage, so the source's exact supply relation identifies
\[
s=N_0/w_0.
\]
Differentiating \(N=s(w+\nu t)\), holding the model primitives invariant, gives
\[
\nu=\frac{\dot N}{s}-\dot w
=\frac{w_0}{N_0}\dot N-\dot w.
\]
Thus the combined wage and employment experiment identifies the valuation and, within this benchmark, the frontier. It does not require separately identifying buyer demand first.

Demand provides an overidentification calculation when \(\dot p=\dot w+1\ne0\):
\[
B=-\dot N/\dot p,\qquad A=N_0+Bw_0.
\]
The inferred \(B\) must be positive. At the special case \(\nu=1\), the model instead predicts \(\dot N=\dot p=0,\dot w=-1\); the displayed ratio cannot identify \(B\), but the valuation formula still identifies \(\nu=1\). If \(\dot p=0\) with \(\dot N\ne0\), the fixed-demand benchmark is rejected.

This sharpens rather than contradicts the source's warning about a wage response alone. The identifying addition is the employment response plus the maintained baseline supply relation. Rationing, changing worker composition, search costs or nonlinear local supply invalidate that shortcut unless separately modeled. Even correctly identified insurance value here is not an empirical estimate of classification effects elsewhere.

Checked locations: competitive one-task model, baseline-worker welfare, and finite-menu identification sections. Full manuscript/YAML were read. Broader platform power, cross-platform substitution, waiting time and external literature remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-J88-323-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/fa/prb_fa8d168233584e8299a75e80e7f5902c/contributions/con_cd9850841ef843f780ddc7c1937b62f7/files/J88-323.tex). Canonical revision: `rev_b2862443186e4f9aa1c2469e48bed8e4`.

