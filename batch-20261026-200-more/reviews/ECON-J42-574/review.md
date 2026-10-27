# Global optimality with positive recruitment costs

The source correctly restricts its sharp global construction to zero recruitment resource cost. With positive cost, its flow-corrected first-order identity remains necessary but needs an operating-profit condition. In the same constant-elasticity family, that condition is exact and sufficient for a global optimum.

Fix observed \(w_0,n_0,s_0>0\), separation elasticity \(b>0\), recruitment elasticity \(a\ge0\), and cost per recruit \(h\ge0\). Define
\[
R(w)=s_0n_0(w/w_0)^a,\qquad
s(w)=s_0(w/w_0)^{-b},\qquad e=a+b.
\]
Employment is \(n(w)=n_0(w/w_0)^e\). Choose productivity according to the source's corrected identity:
\[
m=w_0(1+1/e)+hs_0a/e.
\tag{A}
\]
Then \(w_0\) is stationary for steady-state profit
\(\Pi(w)=(m-w)n(w)-hR(w)\).

The exact condition for \(w_0\) to be a global maximizing operating wage, weakly preferred to not operating, is
\[
hs_0b\le w_0.
\tag{B}
\]
At strict inequality it strictly beats nonoperation and is the unique overall optimum. At equality it is the unique positive operating-wage maximizer but ties the zero-profit nonoperation option.

Necessity follows by evaluating profit at \(w_0\). Substitution of (A) gives
\[
\Pi(w_0)=\frac{n_0}{e}(w_0-hs_0b).
\tag{C}
\]
A negative value cannot maximize when not operating yields zero.

For sufficiency, first take \(a>0\) and \(h>0\). The sign of \(\Pi'(w)\) is the sign of
\[
F(w)=em-(e+1)w-hs_0a(w/w_0)^{-b}.
\]
It is strictly concave on positive wages, tends to minus infinity at both ends, and vanishes at \(w_0\). Its derivative there is
\[
F'(w_0)=-(e+1)+hs_0ab/w_0.
\]
Under (B), \(F'(w_0)\le-(e+1)+a=-(b+1)<0\). Therefore \(w_0\) is the larger root. There is exactly one smaller root: strict concavity, the negative endpoint limits and the negative derivative at \(w_0\) imply that \(F\) is positive just below \(w_0\) and crosses zero once before that. Profit decreases, then increases, then decreases across these two roots. Its only candidate global maximum is consequently \(w_0\) or the limiting value at zero. That limit is zero, approached from below because the negative recruitment term has exponent \(a<e\). Equation (C) makes \(w_0\) at least as good, proving sufficiency and uniqueness among positive wages.

If \(h=0\), the source's direct unimodality proof applies. If \(a=0\), recruitment expenditure is constant and profit's variable part is proportional to \((m-w)w^b\), uniquely maximized at \(w_0\); condition (C) again handles nonoperation. Thus all declared corners are covered.

This also sharpens partial identification with known \(h\). If recruitment elasticity lies in a supplied interval and (B) holds, every \(a\) in that interval generates a globally optimal observed wage with productivity (A). Its derivative is
\[
\frac{dm}{da}=\frac{hs_0b-w_0}{(a+b)^2}\le0.
\]
At the participation boundary, inferred productivity is constant across recruitment elasticities; below it, higher recruitment elasticity lowers the required productivity. If (B) fails, no member of this stationary family can explain an operating global optimum at \(w_0\).

The conclusion remains about steady-state partial-equilibrium profit. It does not solve a discounted workforce control problem, identify recruitment costs from quits, or include competitor reactions. It extends the source's constructive optimization guarantee while respecting those limits.

Source: [ECON-J42-574-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/20/prb_20ad6203eaad46fd8c789522586c2092/contributions/con_c8a48949e4334cc88144d09ed0cf22b4/files/J42-574.tex), canonical revision `rev_cfbca6d1b5904ec9ba9f16af2bb57978`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
