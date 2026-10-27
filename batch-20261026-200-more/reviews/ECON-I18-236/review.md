# Removing regularity by ironing virtual readiness costs

The “Optimal regular readiness contract” theorem is sound under its stated monotonicity assumption. That assumption can be removed within the same one-dimensional model. The correction is an ironed virtual cost, with an explicit optimality proof; it is not a claim that the source's regular theorem contains an error.

Retain the source's positive continuous density on a compact type interval, its bounded readiness \(0\le k\le\bar k\), increasing concave \(C^1\) benefit \(B\), \(\kappa>0\), and financing parameter \(\lambda>0\). Let \(q=F(\theta)\), \(\theta(q)=F^{-1}(q)\), and
\[
v(q)=(1+\lambda)\theta(q)+\lambda q/f(\theta(q)),\qquad
C(q)=\int_0^qv(s)\,ds.
\]
These functions are continuous. Let \(\bar C\) be the greatest convex function lying below \(C\) on \([0,1]\), and let \(\bar v\) be its almost-everywhere derivative. Endpoint values of the derivative do not affect expected welfare. Standard one-dimensional convexity here can also be obtained by taking the lower convex hull of the graph: \(\bar C\) touches \(C\) at both endpoints, and on each connected component of \(\{C>\bar C\}\) it is affine.

Define
\[
k^I(q)=\arg\max_{0\le k\le\bar k}
\left\{B(k)-(1+\lambda)\kappa k^2/2-\bar v(q)k\right\}.
\tag{A}
\]
The maximizer exists and is unique because of the strictly concave quadratic term. Since \(\bar v\) is nondecreasing, the elementary two-maximizer inequality used in the source shows that \(k^I\) is nonincreasing. Choose its values at jumps monotonically. Consequently \(k^I(F(\theta))\) is implementable by the source lemma, with
\[
U(\theta)=\int_\theta^{\bar\theta}k^I(F(s))\,ds,\quad
t(\theta)=\theta k^I(F(\theta))+\kappa k^I(F(\theta))^2/2+U(\theta).
\tag{B}
\]

For completeness, the key inequality establishing optimality is as follows. For any feasible nonincreasing allocation \(k(q)\), put \(D=C-\bar C\ge0\). Both endpoints of \(D\) are zero. Integration by parts against the bounded-variation function \(k\) yields
\[
\int_0^1(v-\bar v)k\,dq
=-\int_{[0,1]}D\,dk\ge0,
\tag{C}
\]
because \(dk\) is a nonpositive measure. Thus replacing the original virtual cost by its ironed version weakly raises the objective of every implementable allocation. The source's Fubini calculation converts the original expected objective, after minimizing transfers, into
\[
\int_0^1\{B(k)-(1+\lambda)\kappa k^2/2-vk\}\,dq.
\]
Equation (C) bounds it above by the corresponding ironed objective. Equation (A) maximizes that upper bound pointwise.

This bound is attained by \(k^I\). On every open interval where \(D>0\), the convex minorant is affine, so \(\bar v\) is constant almost everywhere. Uniqueness of the maximizer in (A) makes \(k^I\) constant on that interval. Hence the measure \(-dk^I\) charges no point where \(D>0\); where it may charge, \(D=0\). The right side of (C) is therefore zero for \(k^I\). Its original welfare equals its ironed upper bound, proving global optimality among truthful, individually rational contracts.

For quadratic benefits \(B(k)=bk-dk^2/2\), \(d\ge0\), implementation is especially transparent:
\[
k^I(q)=\left[\frac{b-\bar v(q)}
 {d+(1+\lambda)\kappa}\right]_0^{\bar k}.
\]
Intervals on which the cumulative virtual cost lies strictly above its lower convex hull are pooling intervals. At a regular distribution, \(C\) is already convex, so \(\bar C=C\), and the construction reduces to the source theorem. Zero readiness and full-capacity portions are permitted, including types at allocation jumps; changes on probability-zero endpoint types do not alter expected welfare.

This is a substantial restricted extension, not a solution of the broader preparedness problem. It retains verifiable readiness, risk neutrality, commitment and the absence of a binding hard budget. It does not address unobservable innovation effort, correlated platform failures or competition. The source's separate hold-up game and outbreak-ambiguity claim are outside this extension. No external references or empirical quantities are certified here.

Source: [ECON-I18-236-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/d7/prb_d790a8e74e5c4e319d158bff46e0dd1e/contributions/con_40f6fa7da07d4764afbf6b0f95e88c57/files/I18-236.tex), canonical revision `rev_b3a5b4048a884a96a2d2c761e95703c3`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
