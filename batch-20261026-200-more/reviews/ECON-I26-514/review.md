# Exact joint transport sensitivity of Shapley mechanisms

The manuscript correctly states that coordinate transport bounds need not describe the joint mechanism set. Under its independently bounded intervention-mean shifts, that joint set can be characterized exactly as a finite zonotope. Fixing the endpoint means additionally tightens the coordinate sensitivity bound.

Let \(K\) have four mechanisms and write the Shapley map as \(\phi=Av\), where columns correspond to subsets \(S\subseteq K\). Its coefficients are
\[
A_{kS}=
\begin{cases}
(|S|-1)!(4-|S|)!/4!,&k\in S,\\
-|S|!(3-|S|)!/4!,&k\notin S.
\end{cases}
\tag{A}
\]
Only applicable branches are used, so no negative factorial occurs. This follows directly by collecting each \(v(S)\) in the source's predecessor-set formula.

Suppose the target-minus-source conditional mean shifts obey
\[
|d_S(x)|\le\delta_S(x)
\]
under the target covariate law. Assume these shifts may vary independently across subsets, with no additional monotonicity or common structural restriction, and that the bounds are integrable. Put \(\bar\delta_S=E_T\delta_S(X)\). The exact joint region for the mean mechanism error \(e\) is
\[
\mathcal E=
\left\{Az:|z_S|\le\bar\delta_S\text{ for all }S\right\}.
\tag{B}
\]
Necessity follows by integrating each bounded shift and using linearity of the fixed Shapley map. For sufficiency, any \(z_S\) in the displayed interval can be realized by
\(d_S(x)=z_S\delta_S(x)/\bar\delta_S\) when \(\bar\delta_S>0\), and zero otherwise. These choices satisfy every bound simultaneously and have the desired means. This proves sharpness for the declared mean-function uncertainty class.

For a direction \(t\in\mathbb R^4\), the exact support function is
\[
h_{\mathcal E}(t)=
\sum_{S\subseteq K}\bar\delta_S
\left|\sum_kt_kA_{kS}\right|.
\tag{C}
\]
Each box coordinate maximizes its own linear term by choosing the matching sign. Hence (C) supplies sharp bounds on every linear combination of mechanism errors, not merely four separate intervals. The entire compact convex region is the intersection of the corresponding supporting halfspaces.

Efficiency appears explicitly. Summing (A) across mechanisms gives column sum zero for each intermediate subset, minus one for the empty subset, and plus one for the full subset. Thus
\[
\sum_ke_k=z_K-z_\varnothing.
\tag{D}
\]
If the source and target endpoint means are known to agree, set both endpoint shift bounds to zero. Every admissible error vector then lies on the three-dimensional efficiency hyperplane \(\sum_ke_k=0\). Choosing separate coordinate extrema that do not sum to zero is impossible.

For a common bound \(\delta\) on every intervention mean, the coordinate support radius is the source's \(2\delta\), because the positive and negative Shapley weights each sum to one. If the two endpoint means are fixed and only intermediate shifts have that bound, each coordinate radius improves to
\[
\delta\sum_{S\ne\varnothing,K}|A_{kS}|=3\delta/2.
\]
The removed empty and full columns each had absolute coefficient \(1/4\). This improved radius is sharp individually: choose each allowed shift with the sign of its coefficient in row \(k\). Those choices generally do not attain the other coordinates' extrema simultaneously, precisely as (B) records.

This result formalizes joint uncertainty for well-defined modular interventions. If the mean functions must also obey monotonicity, outcome-range limits or a shared structural parameter, the box in (B) must be intersected with those restrictions before mapping it; (B) is then only an outer region. It does not make schooling randomization identify unobserved mechanism interventions, or establish population overlap and invariance empirically.

Source: [ECON-I26-514-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/08/prb_0831cf465f9f426bad3ffc3803f74f77/contributions/con_1ba319ceddeb4826841e685a34a6a38e/files/I26-514.tex), canonical revision `rev_95ac0f106b8240c1b350864fb8c23a1d`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
