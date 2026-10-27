# A structural-shock correlation bound gives an exact additional income-effect interval

The source leaves contemporaneous structural innovations arbitrarily correlated, obtaining the sharp income-effect interval \([0,d_{\max}]\). A declared bound on that correlation produces another exact sensitivity interval. Its center is an innovation regression coefficient, distinct from the descriptive health-on-income regression in levels.

Write the identified innovation covariance as
\[
\Sigma=\begin{pmatrix}v_Y&c_{YH}\\c_{YH}&v_H\end{pmatrix},
\quad v_Y>0,\quad
v_\perp=v_H-c_{YH}^2/v_Y>0.
\]
Define \(q=c_{YH}/v_Y\). The source's observational-equivalence construction uses \(U=\varepsilon_Y\), \(V=\varepsilon_H-d\varepsilon_Y\). Impose the additional substantive restriction
\[
|\operatorname{Corr}(U,V)|\le r,\qquad0\le r<1.
\]
Then its exact compatible contemporaneous income-effect set becomes
\[
[0,d_{\max}]\cap
\left[
q-r\sqrt{\frac{v_\perp}{v_Y(1-r^2)}},\
q+r\sqrt{\frac{v_\perp}{v_Y(1-r^2)}}
\right].
\]

For proof, set \(x=d-q\). Direct covariance calculation gives
\[
\operatorname{Cov}(U,V)=-v_Yx,\qquad
\operatorname{Var}(V)=v_\perp+v_Yx^2.
\]
Thus
\[
\operatorname{Corr}(U,V)^2
=\frac{v_Yx^2}{v_\perp+v_Yx^2}.
\]
The denominator is strictly positive for every \(d\), by positive definiteness of \(\Sigma\). Multiplying by it and rearranging yields \((1-r^2)v_Yx^2\le r^2v_\perp\), exactly the stated interval. Intersecting the source's coefficient nonnegativity restrictions supplies necessity.

For sufficiency, choose any \(d\) in that intersection and use the source's equations (4): \(\eta=g-da\), \(c=h-db\), with the innovation transformation above. These coefficients satisfy all original restrictions and reproduce the entire observed Gaussian panel law. The calculated correlation obeys the added bound by construction. Therefore every retained value is attained, and no omitted feature of the baseline panel can narrow this sensitivity set under the stated class.

At \(r=0\), uncorrelated structural innovations force \(d=q\), provided that value belongs to \([0,d_{\max}]\); otherwise the combined model is rejected. As \(r\uparrow1\), the extra radius diverges and its intersection approaches the source's original interval. An empty intersection at a given bound is an incompatibility result, not a point estimate.

For the manuscript's example \(\Sigma=I\), the innovation slope is \(q=0\), even though the regression slope of health on income levels is \(1/5\). With \(r=1/5\), the extra upper bound is \(1/\sqrt{24}\), so the sharp set is \([0,1/\sqrt{24}]\), smaller than \([0,1/2]\). Once \(r\ge1/\sqrt5\), every original \(d\le1/2\) is allowed. Exact zero contemporaneous effect here does not eliminate later income-to-health effects, since its lagged structural coefficient \(\eta\) can remain positive.

If the imperfect-exclusion experiment in equation (7) is also available, intersect all three intervals. The same construction proves joint sharpness: for each retained \(d\), choose the experiment's direct effect \(h_0-df\) and the structural innovations above. Subsequent pure-income path effects remain the affine image in equation (5), evaluated at the final interval endpoints.

Checked locations: baseline covariance assumptions, observational-equivalence equations (3)–(5), covariance-share example and experiment (7). Full source/YAML were read. The correlation limit is external identifying content, not estimable from the unchanged reduced-form panel alone. Nonlinear pathways, mortality and external references remain unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-I14-603-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/24/prb_24c983ffc4ef4850bf341092d4f52a79/contributions/con_9d318dc0889f4f3599b9a797ca6a393b/files/I14-603.tex). Canonical revision: `rev_a675e27f46074112b0d7c7fa4e0d4746`.

