# Independent risk and nuisance-remainder checks for sparse CATE aggregation

Reviewed source: [Pinned manuscript](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/e3/prb_e348afec5b784339a350a9c923a4b598/contributions/con_3686292eec2b447591d74743c7eae940/files/C21-210.tex), revision `rev_1ba8f508247346309fe3b829df3eaa1f`, repository commit `bd5218964aa5efa77ac062e3600b8cfe70df528c`.

**Finding: Supports the claim, within its stated estimation scope.** The contribution metadata calls this an unresolved exploration, and the manuscript distinguishes estimation from honest adaptive inference. The finite-class result and sparse packing argument support that limited claim. An independent calculation below identifies a consequential boundary: ordinary nuisance L2 errors cannot in general be multiplied to control the displayed L2 remainder, even with bounded outcomes, clipping, overlap, and independent training. The manuscript's supremum-error assertion avoids that problem.

Write the doubly robust score, conditionally on independently trained nuisances, as

\[
Z=\widehat m_1-\widehat m_0+
\frac{D(Y-\widehat m_1)}{\widehat e}
-\frac{(1-D)(Y-\widehat m_0)}{1-\widehat e}.
\]

Let \(\delta_d=\widehat m_d-m_d\). Direct conditional expectation gives

\[
E[Z\mid X]-\tau
=\delta_1(1-e/\widehat e)
 +\delta_0\{(1-e)/(1-\widehat e)-1\}
=(\widehat e-e)\left\{
\frac{\delta_1}{\widehat e}+\frac{\delta_0}{1-\widehat e}\right\}.
\]

Thus the signs and denominators of the manuscript's remainder are correct. Independent training makes this an ordinary bounded regression problem conditional on the training sample; it does not by itself change the norm required to control the product. For clipped propensity estimates in \([\epsilon,1-\epsilon]\), Holder's inequality supplies the useful sufficient condition

\[
\|R\|_2\le\epsilon^{-1}\|\widehat e-e\|_4
  (\|\delta_1\|_4+\|\delta_0\|_4).
\tag{A}
\]

The analogous product of two L2 norms is false. To see this inside a bounded CATE model, take an event \(E_q\) of covariate probability \(q\), true propensity \(e=1/2\), true outcome regressions \(m_0=m_1=0\), and deterministic independently supplied nuisance estimates

\[
\widehat e=1/2+(1/4)1_{E_q},\qquad
\widehat m_1=1_{E_q},\qquad \widehat m_0=0.
\]

These satisfy overlap with \(\epsilon=1/4\), and bounded mean-zero outcomes may be chosen independently of treatment and covariates. The exact remainder is \(R=(1/3)1_{E_q}\). Consequently

\[
\|R\|_2=\sqrt q/3,\qquad
\|\widehat e-e\|_2\|\delta_1\|_2=q/4.
\]

Their ratio diverges as \(q\downarrow0\). In squared-risk units the remainder is \(q/9\), whereas a squared product of the L2 errors is \(q^2/16\). This is a boundary example for a possible extension, not a counterexample to the contribution: its proposition retains \(\|R\|_2^2\) exactly and gives a valid supremum-norm sufficient condition. It shows why replacing that exact term by a familiar product rate requires an additional argument.

The aggregation proof also withstands a direct excess-loss check. For \(g=E[Z\mid X]\), the difference of squared losses factors as

\[
D_h=(h-f_0)(h+f_0-2Z).
\]

Boundedness gives \(E D_h^2\le4(A+L)^2\|h-f_0\|_2^2\), which is at most a constant times \(\|h-g\|_2^2+\|f_0-g\|_2^2\). Bernstein concentration therefore has the localized variance needed to absorb a fraction of the candidate risk. The empirical minimizer then has the stated finite-class rate plus approximation and mean-perturbation terms. Rounding toward zero is relevant: it retains the L1 radius, while the sum of at most \(s\) coefficient-rounding errors is at most \(1/n\). No restricted-eigenvalue condition is needed for this finite prediction-class construction, although computational efficiency is not established by enumeration.

For the lower bound, a direct information calculation agrees with the packing scale. If a treated outcome has mean \(t\), its distribution on \(\{-1,1\}\) has probabilities \((1\pm t)/2\). For \(|t|\le1/2\), its relative entropy against mean zero is bounded by a constant times \(t^2\). Since treatment occurs with probability one half and the Rademacher dictionary is orthonormal, the n-observation entropy is at most \(C n\|\beta\|_2^2=Cnsa^2\). Two block-code coefficients differing in \(h\) blocks have squared prediction distance \(2ha^2\); the code separation therefore yields the claimed \(sa^2\) scale. Finally \(sa\le\min(L,1/2)\) explains the sample-size condition proportional to \(s^2\log(p/s)\), rather than only \(s\log(p/s)\).

These checks support the local risk bounds and sharpen their usable nuisance conditions. They do not remove the extra grid logarithm, construct an efficient aggregation algorithm, or establish honest adaptive confidence sets. Those are explicitly unresolved in the source and are not counted as errors here.
