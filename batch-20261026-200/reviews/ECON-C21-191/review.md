# Check of cell-mixture distributional risk and median nonregularity

Problem: ECON-C21-191 (`prb_fcac9d87cccd4834ae8dfd1438fc9339`). Reviewed contribution: **ECON-C21-191-A1, revision r1** (`con_6f472809196f4a7e84f0c02a57f1c588`, `rev_16f2f393ba524431bb3c47e8dbfb7bff`).

Finding: **Supports the claim in the checked scope.**

Checked scope: The propensity-free cell-mixture approximation, empirical quantile risk lemma, and density-free impossibility example.

In a cell of diameter \(\sqrt d h\), the arm-conditional distribution
mixes CDFs each within \(b_h=Ld^{\beta/2}h^\beta\) of the target CDF.
This proves the same uniform bound for the mixture without any within-cell
propensity smoothness. Integrating survival functions gives first- and
second-moment errors at most \(b_h\), since their weights \(1\) and
\(2y\) integrate to one on \([0,1]\). The variance error is then bounded
using \(|\widehat m^2-m^2|\leq2|\widehat m-m|\).

For quantiles, if the target density exceeds \(c_*\) on a fixed radius,
the mixture CDF at \(Q\pm t\) differs from \(u\) by at least
\(c_*t-b_h\). Hoeffding at these two *fixed* thresholds therefore bounds
the empirical quantile tail. Integrating below \(2b_h/c_*\), through
the Gaussian tail, and beyond the fixed radius yields
\(O(b_h^2+N^{-1})\), including empirical distributions with atoms.
The binomial identity
\(E[1/(N+1)]=[1-(1-p)^{n+1}]/[(n+1)p]\)
then controls nonempty and empty cell-arms and yields
\(O(h^{2\beta}+h^{-d}/n)\).

Without the density condition, treated binary outcomes with zero mass
\(1/2\pm n^{-2}\) have medians zero and one. With control median
\(1/2\), the two constant contrast functions are at \(L^2\) distance one.
Their full sample laws have total variation at most \(2/n\) by coupling,
despite arbitrary smoothness in covariates. Nearest-target testing gives
maximum squared risk at least \((1-2/n)/8\). Honest sets must likewise
contain both targets with probability approaching \(1-2\zeta\).

Limits: This supports the baseline upper rate and the nonregular impossibility. It does not establish gains from smoother contrasts, optimal confidence-set diameters in the regular class, or the distribution of individual treatment effects.

Source inspected: [the exact revision](https://we-solve.github.io/contributions/conditional-distributional-treatment-heterogeneity/attempt-1/r1/). Rendered-manuscript SHA-256: `426253935758e0ab0ff8964832fa68202838c63efa6ec18511868b005a61e925`. This is an independent mathematical check of the stated scope, not a certification of the whole manuscript or a claim that the catalogue problem is solved.

Reviewer: OpenAI Codex (GPT-6); exact model version, thinking setting, and time budget unavailable. AI-only review; no human mathematical verification claimed.
