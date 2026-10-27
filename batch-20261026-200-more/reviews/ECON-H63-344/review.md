# A larger optimal spread can accompany a higher pricing premium

The manuscript's adoption and optimum formulas are correct. They also reveal a potentially misleading comparative static: an increase in the ambiguity-plus-liquidity premium can increase the chosen repayment spread. The interior optimum moves in the opposite direction, but nonnegative repayment constraints can dominate. This is a boundary phenomenon inside the source's fixed-funding model.

Write \(q=1-p\), \(a=q-\kappa>0\), \(b=p+\kappa\), and \(x_s=y_s-B\). For fixed spread \(d\), the marginal expected utility is
\[
V_\kappa'(d)=\frac{pa}{x_L+ad}-\frac{qb}{x_H-bd}.
\]
Differentiating this marginal utility with respect to \(\kappa\), while keeping \(d\) fixed, gives
\[
\partial_\kappa V_\kappa'(d)
=-\frac{px_L}{(x_L+ad)^2}
-\frac{qx_H}{(x_H-bd)^2}<0.
\tag{A}
\]
Strict concavity then implies that a feasible interior optimum decreases with the premium. The adoption condition can also be written
\[
\kappa<
\frac{pq(x_H-x_L)}{px_H+qx_L}.
\tag{B}
\]
Thus the premium weakens the marginal incentive to introduce insurance.

Nevertheless, nonnegative low-state repayment requires
\[
g_L=B-ad\ge0,\qquad d\le B/a.
\tag{C}
\]
Unlike the interior optimum and the incentive bound, this upper bound increases with \(\kappa\). If it binds, the optimal spread may increase.

Here is an exact example. Take \(p=q=1/2\), \((y_L,y_H)=(3,7)\), \(B=1\), and \(k_H=\log10\). Impose no additional repayment caps. First set \(\kappa=0\). Then \(a=b=1/2\), \((x_L,x_H)=(2,6)\), and the unconstrained optimum is
\[
d_{\rm unc}=
\frac{pa x_H-qb x_L}{ab}=4.
\]
The nonnegative-payment bound is two. The truth-telling bound is \(54/(1+9/2)=108/11>2\), so the unique optimum is \(d^*=2\). It gives repayments \((0,2)\), consumptions \((3,5)\), and expected utility \(\tfrac12\log15\).

Now increase the premium to \(\kappa=1/20\). Choose the source's ambiguity component equal to zero and liquidity coefficient \(1/20\), so the interval restriction on lender probabilities is satisfied. We have
\[
a=9/20,\quad b=11/20,\quad
d_{\rm unc}=320/99,\quad B/a=20/9.
\]
The incentive bound is \(54/(1+99/20)=1080/119>20/9\). Since \(320/99>20/9\), the unique optimum is \(d^*=20/9\), strictly larger than two. Its repayments and consumptions are
\[
(g_L,g_H)=(0,20/9),\qquad
(c_L,c_H)=(3,43/9).
\]
Pricing checks exactly:
\[
\tfrac12(20/9)-\tfrac1{20}(20/9)=1=B.
\]
Both consumptions are positive, and high-state truth-telling holds by the computed incentive bound. The low-state false report demands a larger payment and cannot improve utility, as in the source.

Expected utility now equals \(\tfrac12\log(43/3)\), strictly below \(\tfrac12\log15\). The larger spread therefore does not indicate better insurance or welfare: low-state consumption is unchanged, while the increased spread finances the premium by lowering high-state consumption. Measuring contract contingency solely by \(d\) would miss this distinction.

Equation (A) explains the interior force, while (C) explains why clipping the optimum can reverse its sign. The source makes no blanket monotonicity claim, so this is a substantive comparative-static caution, not an error finding. It retains no default, fixed proceeds, log utility, fixed output probabilities and exogenous reporting costs. Dynamic default, endogenous issuance and the resource cost of verification remain outside the calculation.

Source: [ECON-H63-344-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/40/prb_400e08b5067748318657d93e7e12563e/contributions/con_379c0c5ac80945918337d4aef35d65f1/files/H63-344.tex), canonical revision `rev_677e1c452cc54ec0804819517201d1ae`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
