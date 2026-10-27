# Sharp multi-instrument exclusion sensitivity

The manuscript's scalar-instrument sensitivity interval extends to multiple historical instruments, but the result is generally an intersection or a convex feasibility problem rather than an average of individual ratios. Instruments can jointly refute a declared direct-channel bound even when each instrument separately admits coefficients.

Let \(Z\in\mathbb R^k\) be centered with finite second moments, and let centered scalar \(D,Y\) satisfy
\[
Y=\beta D+\gamma^\top Z+u,\qquad E[Zu]=0,\qquad
|\gamma_j|\le\Gamma_j.
\tag{A}
\]
The nonnegative bounds \(\Gamma_j\) are prespecified in the chosen instrument coordinates. Define
\[
a=E[ZD],\quad b=E[ZY],\quad \Sigma=E[ZZ^\top],\quad
\mathcal Z=\{\Sigma\gamma:|\gamma_j|\le\Gamma_j\}.
\]
The exact sharp coefficient set is
\[
\mathcal B=\{\beta\in\mathbb R:b-\beta a\in\mathcal Z\}.
\tag{B}
\]
It is a convex closed subset of the real line: an interval, a point, the whole line, or empty, allowing unbounded intervals in principle.

Necessity follows by taking the vector moment of (A). For sufficiency, whenever a pair \((\beta,\gamma)\) satisfies that moment, define \(u=Y-\beta D-\gamma^\top Z\) on the observed probability space. Then \(E[Zu]=0\), and no further restrictions on the disturbance were imposed. Thus every included coefficient reproduces the full observed distribution under the declared moment model. This is the same sharpness logic as the source, now retaining all instruments simultaneously.

When \(\Sigma\) is nonsingular, write \(r=\Sigma^{-1}b\) and \(s=\Sigma^{-1}a\). The test is especially explicit:
\[
|r_j-\beta s_j|\le\Gamma_j\quad\text{for every }j.
\tag{C}
\]
For \(s_j\ne0\), this gives the interval centered at \(r_j/s_j\) with radius \(\Gamma_j/|s_j|\). Intersect all these intervals. For \(s_j=0\), that coordinate either imposes no coefficient restriction if \(|r_j|\le\Gamma_j\), or rejects the model if \(|r_j|>\Gamma_j\). No division by a zero first-stage component is needed.

For singular \(\Sigma\), (B) remains valid without a generalized-inverse shortcut that might lose a nullspace constraint. An equivalent exact characterization is
\[
|v^\top(b-\beta a)|
\le\sum_j\Gamma_j|(\Sigma v)_j|
\quad\text{for every }v\in\mathbb R^k.
\tag{D}
\]
Indeed the right side is the support function of the centrally symmetric compact convex set \(\mathcal Z\). Membership implies every inequality. Conversely, a point outside that set has a separating hyperplane and violates one such inequality. In computation, (B) is simply linear feasibility in \(\beta,\gamma\), and its endpoints can be obtained by linear optimization when bounded.

For an exact incompatibility example, take \(\Sigma=I_2\), \(a=(1,1)\), \(b=(1/2,4/5)\), and \(\Gamma_1=\Gamma_2=1/10\). Equation (C) gives \(\beta\in[2/5,3/5]\) from the first instrument and \(\beta\in[7/10,9/10]\) from the second. Each separate model is nonempty, but the joint set is empty. These moments are realizable: independent mean-zero variance-one instruments, \(D=Z_1+Z_2\), and \(Y=Z_1/2+4Z_2/5\) produce them exactly.

The rectangular bounds are coordinate-specific substantive restrictions. An invertible redefinition of instruments preserves the moment equations, but must transform the allowed direct-channel set as well; imposing the same numerical rectangle after rotation changes the model.

This result addresses exclusion sensitivity in the source population model. It does not supply weak-instrument sampling coverage for the vector problem, validate historical exclusion, or transport a local coefficient to a feasible national reform. The manuscript's separate Lipschitz transport bounds retain their own assumptions.

Source: [ECON-O43-435-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/54/prb_54bccc1b724e4bb08da587693a176565/contributions/con_1c395dd965654d9083bbcc9e88bf2acc/files/O43-435.tex), canonical revision `rev_74aa0098967144988915859da34599cb`, pinned commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

Original review prose: CC BY 4.0. Independent AI mathematical review; no human or formal verification.
