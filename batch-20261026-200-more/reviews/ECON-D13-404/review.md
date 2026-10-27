# Sharp welfare-change sets from repeated hours observations

The source shows that one hours observation identifies the product \(\omega a\). Repeated observations with a common labor-preference parameter yield a stronger result: the entire compatible parameter family and the woman's utility-change set can be characterized exactly, even without private consumption observations.

Consider two regimes \(r=1,2\), both with strictly interior labor \(0<l_r<\bar l\), observed wages \(w_r>0\) and nonlabor incomes \(y_r>0\). Maintain the source's utility normalizations and a common unknown \(a>0\), allowing unknown weights \(\omega_r\in(0,1)\). Write
\[
T_r=w_rl_r+y_r,\qquad z_r=\frac{w_r}{l_rT_r},\qquad
z_{\max}=\max(z_1,z_2).
\]
The sharp compatible family is
\[
a\in(z_{\max},\infty),\qquad \omega_r=z_r/a.
\tag{A}
\]
Necessity follows from each regime's interior first-order condition and \(\omega_r<1\). For sufficiency, any \(a\) in that open interval gives admissible positive weights and satisfies both first-order conditions. The source's strictly concave labor objective then makes the observed labor uniquely optimal. Because labor is observed below the cap, no additional cap restriction arises. Thus there are no missing preference or equilibrium restrictions in (A).

Although consumption levels remain unidentified, the first-order condition and sharing rule give
\[
c_{wr}=\omega_rT_r=\frac{w_r}{a l_r},
\qquad
\frac{c_{w2}}{c_{w1}}=\frac{w_2l_1}{w_1l_2}.
\tag{B}
\]
The ratio is point identified under the common-\(a\) restriction. It is not recovered by treating total household consumption as the woman's consumption.

Her utility change is therefore
\[
\Delta U(a)=
\log\frac{w_2l_1}{w_1l_2}
-\frac a2(l_2^2-l_1^2),\qquad a>z_{\max}.
\tag{C}
\]
Equation (C) supplies the exact sharp identified set as the image of an open half-line under an affine map. If \(l_2<l_1\), the set is
\[
\left(
\log\frac{w_2l_1}{w_1l_2}
+\frac{z_{\max}}2(l_1^2-l_2^2),\ \infty
\right).
\]
If \(l_2>l_1\), it is the open half-line below the corresponding threshold in (C). If hours coincide, the utility change is exactly \(\log(w_2/w_1)\). Every included value is attained by a specific \(a\) from (A). Finite endpoints are excluded because attaining \(a=z_{\max}\) would set at least one weight equal to one, outside the source's maintained class.

For a pure bargaining intervention, \(w_1=w_2=w\), \(y_1=y_2=y\), with only the weight changing. If labor falls, (B) says that the woman's consumption rises in the exact proportion \(l_1/l_2\). Moreover the lower endpoint of the utility-change set is
\[
\log(l_1/l_2)+\frac{z_{\max}}2(l_1^2-l_2^2)>0.
\]
Thus welfare improvement has a strictly positive model-implied lower bound, while its magnitude has no finite upper bound without additional preference information. The result strengthens the source's sign comparison and makes the remaining magnitude ambiguity explicit.

With wage or income changes, the same sharp family applies, but a labor response alone need not determine the welfare sign; equation (C) handles the joint intervention. External information \(a\in[a_-,a_+]\) simply intersects that interval with \((z_{\max},\infty)\) before applying (C).

This is a conditional identification result, not an empirical inference from average hours. It relies on common labor preferences, interior choices, known household budgets and the source's logarithmic sharing normalization. Binding caps, childcare expenses, public goods and changing utility scales require separate restrictions. No actual policy effect or external reference is certified.

Source: [ECON-D13-404-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/ce/prb_ce5709498edd418ba8999db09546ce70/contributions/con_dc21e161fcb24c34a0d441f9a74716d1/files/D13-404.tex), canonical revision `rev_a3a706655bb5423dba101902a08fbe58`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
