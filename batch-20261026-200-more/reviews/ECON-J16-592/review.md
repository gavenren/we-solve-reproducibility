# Monotone fertility identifies sharp interaction bounds for policy-induced births

The source bounds unconditional birth–policy interactions under selection restrictions. An additional monotone-fertility assumption supports a distinct principal-stratum question: what can be learned about that interaction among people whose birth timing is changed by policy? The answer requires two trimming calculations and remains partly unidentified.

Suppress parental group and baseline covariates for clarity. Retain randomized binary policy \(\pi\), bounded earnings \(0\le Y(b,\pi)\le M\), and consistency. Impose \(B(1)\ge B(0)\) almost surely. Let \(p_\pi=\Pr(B=1\mid\pi)\), assume \(0<p_0<p_1<1\), and define the induced-birth stratum \(C=\{B(0)=0,B(1)=1\}\), of identified mass \(c=p_1-p_0>0\).

Seek the stratum interaction
\[
G_C=\mathbb E[Y(1,1)-Y(0,1)-Y(1,0)+Y(0,0)\mid C].
\]
This is a different population from the source's entire baseline cohort and must be labeled accordingly; it is not a replacement estimate of its original normalized target.

Let \(Q_1\) be the quantile function of observed earnings in cell \((B,\pi)=(1,1)\), and \(Q_0\) that in cell \((0,0)\). Within the first cell, the induced-birth stratum occupies fraction \(q_1=c/p_1\); within the second it occupies fraction \(q_0=c/(1-p_0)\). Define trimmed means
\[
L_j=q_j^{-1}\int_0^{q_j}Q_j(u)\,du,\qquad
U_j=q_j^{-1}\int_{1-q_j}^1Q_j(u)\,du,\quad j=0,1.
\]
Then, without additional cross-world earnings restrictions, the sharp interval is
\[
G_C\in[L_1+L_0-2M,\ U_1+U_0].
\]

Monotonicity partitions the population into always-birth mass \(p_0\), induced-birth mass \(c\), and never-birth mass \(1-p_1\). Observed cell \((1,1)\) combines always and induced births; cell \((0,0)\) combines induced and never births. The smallest mean of any unobserved subset occupying fraction \(q\) of an identified distribution is its bottom-\(q\) trimmed mean, and the largest is its top-\(q\) trimmed mean. This follows by comparing a candidate membership probability \(w(y)\) with the threshold assignment: \((y-a)(w-w_{\mathrm{bottom}})\ge0\), and integrating cancels the common membership mass. At atoms, fractional membership attains the cutoff exactly.

Thus \(Y(1,1)\) and \(Y(0,0)\) within \(C\) have the two trimmed intervals. The other two potential outcomes for \(C\) are never factually observed under either policy, so their stratum means remain independently in \([0,M]\). Combining the signed terms gives the stated outer bounds.

For sharpness, select induced-birth members from either extreme tail in each of the two factual mixtures. Couple those selected outcome margins arbitrarily as the same mass-\(c\) stratum, assign the remaining factual mixture margins to always and never births, and reproduce their other observed policy-cell distributions freely. Set the two missing induced-birth potentials to \(M\) for the lower endpoint and zero for the upper. Randomize policy independently. This constructs every observed arm law and monotone birth timing. Mixtures of endpoint constructions preserve those restrictions and attain every intermediate interaction.

The interval can remain wide despite monotone fertility: random policy and knowledge of the induced-birth share do not observe the crossed earnings potentials. No exclusion that policy acts only through birth is imposed; such an exclusion would force a very different interaction problem.

Checked locations: random-policy observation model, observational-equivalence proposition and sharp interaction theorem. Full source/YAML were read. Conditional versions require covariate-specific masses and weighting by induced-birth shares; parental normalizers and aggregate cohort targets remain separate. External references are unverified. Original prose: CC BY 4.0.

Pinned source: [ECON-J16-592-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/ec/prb_ec66f3b172fd431ebece20b4a844a8ab/contributions/con_74e27bc2f5dc48719739ff73b6361f61/files/J16-592.tex). Canonical revision: `rev_fa4efa93705141038faa72a2967727a6`.

