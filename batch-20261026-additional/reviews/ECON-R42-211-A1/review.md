# Unequal-route extension of the robust transport allocation reversal

Reviewed source: [Pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/7e/prb_7e494f546ec74122884712ae935bb2d1/contributions/con_ae7b37a95a8847698e1321b71a7d3ffc/files/R42-211.tex), revision `rev_1c942caaf9b24b34bf7cd0dbef4afa35`, repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

**Finding: Supports the claim.** The manuscript's two-route economic-loss calculation and its independence-versus-ambiguity reversal are correct under their stated assumptions. The contribution is recorded as an unresolved exploration, not a general solution of climate-resilient network investment. An independent extension below determines exactly how unequal route costs affect the reversal; this also clarifies why the source isolates the equal-cost case.

With \(S(\tau)=(A-\tau)_+^2/2\), a failure of link 1 alone loses \(R\), a joint failure loses \(L\), and failure of link 2 alone loses zero. Hence expected loss is \(Rp_1+(L-R)h\). The nonnegative coefficient \(L-R\) makes maximal intersection probability worst for every investment. Under the investment-independent common-uniform hazard construction, the intersection is exactly \(\min(p_1,p_2)\). This verifies both the value formula and its common-law attainment: there is no hidden exchange of minimization and maximization.

Retain the manuscript's marginal hardening curves, fixed budget, and common engineering parameter,

\[
p_i(k_i)=\frac{p_0}{1+k_i},\qquad k_1+k_2=B>0,
\]

but now allow \(0\le R\le L\), with \(L>0\). Put \(x=k_1\), so \(k_2=B-x\). Robust loss becomes

\[
F_{\rm rob}(x)=p_0\left[
\frac{R}{1+x}+\frac{L-R}{1+\max(x,B-x)}\right].
\tag{A}
\]

Every denominator in (A) is at most \(1+B\), so

\[
F_{\rm rob}(x)\ge\frac{Lp_0}{1+B}.
\]

The allocation \(x=B\) attains equality. If \(R>0\), equality in the first term requires \(x=B\), making it the unique optimum, including the endpoint \(R=L\). If \(R=0\), either endpoint attains equality and every interior allocation is strictly worse. Thus unequal route costs preserve robust concentration in this benchmark and select the faster route whenever its survival has positive incremental value. The source's theorem is the symmetric special case, not the strongest possible concentration statement.

Under known independent failures, the objective instead is

\[
F_{\rm ind}(x)=\frac{Rp_0}{1+x}
 +\frac{(L-R)p_0^2}{(1+x)(1+B-x)}.
\tag{B}
\]

For \(0<R<L\), write \(a=1+x\), \(b=1+B-x\), \(a+b=B+2=C\), and \(Q=(L-R)p_0\). Differentiating (B), its derivative has the sign of

\[
Q(a-b)-Rb^2=Q(C-2b)-Rb^2.
\tag{C}
\]

This expression is strictly increasing with \(x\): its derivative is \(2Q+2Rb>0\). At \(x=B/2\) it is negative, so the independent optimum lies strictly toward the faster route. At \(x=B\), its sign is \(QB-R\). It follows that the unique optimum is

\[
x^*_{\rm ind}=B\quad\text{if }R\ge (L-R)p_0B,
\]

and otherwise is strictly between \(B/2\) and \(B\), with

\[
b^*=\frac{\sqrt{Q^2+RQC}-Q}{R},\qquad
x^*_{\rm ind}=B+1-b^*.
\tag{D}
\]

At equality the derivative is negative throughout the interior and zero only at the endpoint, so the endpoint optimum remains unique. The omitted boundary cases are also clear: \(R=0\) gives the manuscript's balanced optimum, while \(R=L\) eliminates the joint-failure term and gives \(x=B\).

Consequently the robust-versus-independent allocation discrepancy persists for unequal route costs precisely when \(0<R<(L-R)p_0B\); it disappears when maintaining the faster route alone is sufficiently valuable. For instance, \(L=1\), \(R=0.1\), \(p_0=1/2\), and \(B=2\) give robust allocation \((2,0)\), whereas (D) gives approximately \((1.31534,0.68466)\) under independence. This comparison changes neither engineering curves nor total investment expenditure. Its only changed primitive is the dependence restriction on hazards.

The derivation supports the source's economic interpretation while identifying the boundary of the striking symmetric reversal. A pointwise common worst-case law exists because there are only two relevant nested-threshold failure events and a nonnegative intersection coefficient. That argument would not automatically select a single copula for an arbitrary collection of cuts in a larger network. Likewise, congestion, heterogeneous hardening technologies, endogenous investment totals, and different engineering curves can alter (A) and (B). The review makes no statement about their optima or about a calibrated transport policy. The unresolved broader catalogue objectives are accurately acknowledged in the manuscript.
