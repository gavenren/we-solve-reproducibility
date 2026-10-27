# A known mean missing valuation yields sharp quantile welfare bounds

The source obtains sharp welfare bounds when every missing privacy valuation can range independently over \([0,H]\). An external restriction on the mean missing valuation can materially tighten those bounds without assuming missing at random or independence between valuation and exposure.

Retain the fixed-cohort five-year benchmark, the observed joint law of \((R,D,Rh)\), and \(W=G+\mathbb E[hD]\). Suppose \(H>0\), the nonrespondent share \(\pi=\Pr(R=0)>0\), and external information identifies
\[
\mathbb E[h\mid R=0]=\mu\in[0,H].
\]
No other restriction is imposed on the association between \(h\) and signed cumulative avoided exposure \(D\). Let \(Q(u)\), \(0<u<1\), be the generalized quantile of \(D\) conditional on \(R=0\), and set \(\alpha=\mu/H\). Then the sharp welfare interval is
\[
\left[
G+M+\pi H\int_0^\alpha Q(u)\,du,\quad
G+M+\pi H\int_{1-\alpha}^1Q(u)\,du
\right],
\]
where \(M=\mathbb E[RhD]\) is the source's observed respondent contribution.

Here is a direct proof, including discrete exposure distributions. Write \(y(D)=\mathbb E[h/H\mid D,R=0]\). Every admissible completion supplies \(0\le y\le1\) and \(\mathbb E[y]=\alpha\); conversely each such function can be implemented by assigning the missing coefficient its conditional mean \(Hy(D)\). Thus it suffices to optimize \(\mathbb E[Dy(D)]\) over a unit-capacity allocation with fixed mass.

For the upper endpoint, assign \(y=1\) on the highest-exposure fraction \(\alpha\), \(y=0\) below its threshold \(q\), and choose a fractional value on \(D=q\) if an atom must be split. This has the required mean and value \(\int_{1-\alpha}^1Q(u)\,du\). For any competing feasible \(y\), let \(y^*\) denote that assignment. Pointwise,
\[
(D-q)(y-y^*)\le0.
\]
Taking expectations and using equal allocation masses eliminates \(q\), proving \(\mathbb E[Dy]\le\mathbb E[Dy^*]\). Assigning mass to the lowest exposures reverses the argument and gives the lower endpoint. The bounded exposure assumption ensures integrability.

Both endpoint completions leave every observed variable unchanged and satisfy the mean restriction. Convex combinations of their \(y\) functions preserve the mean and fill every intermediate value. This proves sharpness, rather than only valid outer inequalities. Signed exposures require no change to the threshold argument.

For a concrete nonrespondent distribution, suppose \(D=-1\) and \(D=2\) each have probability one half, and \(\mu=H/2\). The sharp conditional privacy-benefit interval is \([-H/2,H]\), obtained by placing all permitted high valuations on the negative or positive half. If instead \(D\equiv d\), the interval collapses to \(\mu d\), even though no individual missing valuation is identified. At \(\mu=0\) all missing coefficients are zero almost surely; at \(\mu=H\) they are all \(H\), and the formulas correctly collapse to a single mean. If \(\pi=0\), missing-data uncertainty disappears and no conditional quantile is needed. If \(H=0\), privacy benefits vanish identically.

The new restriction can exclude source endpoint assignments because their implied mean valuations need not equal \(\mu\). It does not authorize replacing \(h\) by \(\mu\) inside \(\mathbb E[hD]\): that would additionally impose zero covariance. Nor does it recover the paired exposure contrast from ordinary randomized-arm marginals; the source's stronger exposure-identification assumption is retained.

Checked locations: fixed-cohort benchmark, sharp selective-valuation proposition and stable-valuation-over-time discussion. Full source/YAML were read. External mean evidence, actual exposure measurement, producer effects and references are not established here. Original prose: CC BY 4.0.

Pinned source: [ECON-L51-345-A1](https://github.com/We-Solve/research/blob/bd5218964aa5efa77ac062e3600b8cfe70df528c/problems/98/prb_982b116b6f25484b9111bb151e05bef9/contributions/con_ce554cd84f9c4d19892f8de86633195f/files/L51-345.tex). Canonical revision: `rev_f1e0a07ff93f4be7ad1256458c2e7a31`.

