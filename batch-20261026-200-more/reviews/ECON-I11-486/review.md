# Sharp health-completion bounds with bounded annual changes

The manuscript's missing-health bounds allow each unobserved live quality index to range independently over \([0,1]\). If a substantive annual-change restriction is available, the longitudinal structure can tighten those bounds while preserving sharpness. It must be imposed explicitly; it does not follow from missingness or from complete vital-status records.

For a beneficiary and regime, let \(\mathcal T\subseteq\{1,\ldots,5\}\) be the dates alive, with survival fully observed. Let \(\mathcal O\subseteq\mathcal T\) be dates with observed health indices \(q_s\). Fix a supplied \(L\ge0\) and require
\[
0\le q_t\le1,\qquad |q_t-q_s|\le L|t-s|
\quad(t,s\in\mathcal T).
\tag{A}
\]
There is no restriction linking a post-death zero health contribution to the pre-death quality index. Death remains an outcome, not an imputed quality measurement.

Observed values must satisfy (A) among themselves. If they do not, the maintained completion class is empty. If \(\mathcal O\ne\varnothing\), define for each live date
\[
\ell_t=\max\{0,\max_{s\in\mathcal O}(q_s-L|t-s|)\},\qquad
u_t=\min\{1,\min_{s\in\mathcal O}(q_s+L|t-s|)\}.
\tag{B}
\]
If no live quality value is observed, use \(\ell_t=0,u_t=1\). Every admissible trajectory lies between these envelopes, by comparison with every observation.

Both entire envelope trajectories are themselves admissible. Each function \(t\mapsto q_s\pm L|t-s|\) is \(L\)-Lipschitz; maxima and minima of finitely many functions sharing that constant retain it, as does clipping to the constant range endpoints. The observed consistency inequalities make both envelopes equal \(q_s\) at each observed date. Hence their values simultaneously satisfy all cross-date restrictions. This is stronger than separately reporting a feasible interval at each date.

Since the health target uses nonnegative discount weights, the exact beneficiary-level completion interval is
\[
\left[\sum_{t\in\mathcal T}\beta^t\ell_t,\
      \sum_{t\in\mathcal T}\beta^tu_t\right].
\tag{C}
\]
Both endpoints are attained by the corresponding full trajectory. Convex mixtures of those trajectories obey (A) and attain intermediate totals. The same conclusion holds at \(L=0\): all live indices must coincide with any observed value, or may take a common arbitrary value if none is observed.

Let \(L_a^L,U_a^L\) be the regime-specific population expectations of the endpoints in (C), using the source's fixed cohort weights and identified observed-data law. Selecting the lower or upper envelope separately for each observed history is measurable in this finite horizon. These choices preserve every observed variable, including survival, utilization and travel. With no additional cross-beneficiary or cross-regime health restrictions, the sharp health contrast is
\[
\Delta H\in[L_1^L-U_0^L,\ U_1^L-L_0^L].
\]
Combining with the source's common unit-resource-cost class gives the sharp welfare interval
\[
\left[
\lambda(L_1^L-U_0^L)-\rho\Delta T-h_{\mathcal C}(\Delta Q),\
\lambda(U_1^L-L_0^L)-\rho\Delta T+h_{\mathcal C}(-\Delta Q)
\right].
\tag{D}
\]
Sharpness uses the source's independence between health completions and the shared cost-vector restriction. If scientific restrictions link latent health to utilization, further joint feasibility work is required.

For example, an observed live score \(q_2=0.8\) and bound \(L=0.1\) restrict a missing live year-three score to \([0.7,0.9]\), rather than \([0,1]\); other observed years may tighten it further through (B). This is an illustrative envelope calculation, not a clinical assertion about actual annual quality changes.

The extension supplies an exact sensitivity family indexed by a declared trajectory bound. It does not validate that bound, identify acquisition assignment, or infer mediation from the ownership-payment factorial. It preserves the cohort across moves and death and makes no empirical or medical recommendation.

Source: [ECON-I11-486-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/9c/prb_9c7f348ade4941f2b332eda622b6eaa4/contributions/con_bd4511545ec743978a2ba6f6f7fe6b86/files/I11-486.tex), canonical revision `rev_3f2b7ce39e724c6dbcef25c9b65ebf31`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
