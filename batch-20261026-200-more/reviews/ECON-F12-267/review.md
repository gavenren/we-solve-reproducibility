# Exact productivity directions and sharper network error certificates

The uniform approximation theorem is valid, but its bound can be sharpened by exploiting an exact direction of the nonlinear equilibrium. A shock proportional to the vector of primary-factor shares produces an exactly common log-price change, regardless of the intermediate substitution elasticities.

Use the source's notation \(a=(a_i)\), \(F\), \(A_{ij}=(1-a_i)b_{ij}\), \(\rho=\max_i(1-a_i)<1\), and \(M=\max_i(1-a_i)|r_i|\). Let \(x(\varepsilon)\) be its unique equilibrium and \(x^{\rm lin}(\varepsilon)=(I-A)^{-1}\varepsilon\). For every real \(c\),
\[
F(x+c\mathbf1)=F(x)+c(\mathbf1-a).
\tag{A}
\]
For \(r_i\ne0\), factor \(e^{r_ic}\) out of the sum defining \(F_i\); for \(r_i=0\), the displayed equality follows from the row sum. This proves (A) for every source technology.

Consequently
\[
x(\varepsilon+ca)=x(\varepsilon)+c\mathbf1.
\tag{B}
\]
Indeed substitution using (A) verifies the fixed-point equation, and uniqueness completes the proof. Since \((I-A)\mathbf1=a\), the same shift identity holds for the linear approximation. Their difference is therefore invariant under adding \(ca\) to the shock vector.

Apply the manuscript's uniform theorem to \(\varepsilon-ca\), then use (B). This gives the improved certificate
\[
\|x(\varepsilon)-x^{\rm lin}(\varepsilon)\|_\infty
\le\frac{M}{2(1-\rho)^3}
\left(\min_{c\in\mathbb R}\|\varepsilon-ca\|_\infty\right)^2.
\tag{C}
\]
The minimum exists because every \(a_i>0\), making the residual norm tend to infinity with \(|c|\). It is never larger than the original shock norm, since \(c=0\) is feasible. It can be zero for a nonzero shock: if \(\varepsilon=ca\), both exact and linear prices equal \(c\mathbf1\). This substantially distinguishes network-relative shocks from common price movements.

The scalar minimization is itself explicit as an interval-feasibility problem. A candidate residual radius \(E\ge0\) is feasible exactly when
\[
\max_i\frac{\varepsilon_i-E}{a_i}
\le
\min_i\frac{\varepsilon_i+E}{a_i}.
\]
This follows by solving \(|\varepsilon_i-ca_i|\le E\) for each \(c\) and intersecting the intervals. Thus (C) does not require solving another nonlinear equilibrium.

One can additionally determine the direction of the price error when elasticities are on the same side of one. The manuscript's Hessian formula shows that \(F_i\) is convex when \(r_i\ge0\) and concave when \(r_i\le0\). Because \(F_i(0)=0\) and \(DF(0)=A\), all \(r_i\ge0\) imply \(F(x)\ge Ax\) coordinatewise. Therefore
\[
x-x^{\rm lin}=(I-A)^{-1}[F(x)-Ax]\ge0,
\]
using the inverse's nonnegative Neumann series. If all \(r_i\le0\), the inequality reverses. This holds for signed shocks as well as adverse shocks. If signs differ, no uniform coordinatewise ranking follows from this argument.

For equal primary shares \(a_i=a_0\), there is a further dispersion bound. Every \(F_i(x)\) lies between \((1-a_0)\min_jx_j\) and \((1-a_0)\max_jx_j\). Thus \({\rm osc}(x)\le{\rm osc}(\varepsilon)/(1-\rho)\). The variance bound \({\rm Var}(x_j)\le{\rm osc}(x)^2/4\), inserted into the source's Taylor proof, gives
\[
\|x-x^{\rm lin}\|_\infty
\le\frac{M\,{\rm osc}(\varepsilon)^2}{8(1-\rho)^3}.
\]
For one sector the dispersion vanishes and exactness follows as expected.

These are analytical refinements of the fixed-link price benchmark. They do not extend smoothness through inventory depletion or endogenous link changes, and they do not equate gross output with welfare or value added. No computational or empirical reproduction is claimed.

Source: [ECON-F12-267-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/44/prb_443d9ab6ee434658bc1f0f854ad5d7c7/contributions/con_9d3bb31e34cb4379a108eb913c15df58/files/F12-267.tex), canonical revision `rev_8946d4316e2f4c95823c9c6d054b2847`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
