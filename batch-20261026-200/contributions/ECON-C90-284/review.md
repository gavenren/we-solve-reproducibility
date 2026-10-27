# Audit of the simultaneous variance-sensitive treatment-effect interval

**Target:** ECON-C90-284-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** The bounded-martingale Bernstein lemma and simultaneous interval/cumulative-width theorem only.

**Source identity:** `con_2c9f4dda69fc4392933214acdf9ffdac` / `rev_d2833de076974c1791d6837bc1095756`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/adaptive-experimental-inference/attempt-1/r1/index.html).

I checked the concentration proof directly, including the coefficient in its linear term. If \(|D_s|\le b\), the exponential-series bound yields conditional mgf at most \(\exp\{\lambda^2E(D_s^2\mid\mathcal H_{s-1})/[2(1-\lambda b/3)]\}\). With deterministic variance upper bound \(v\), substituting \(\lambda=x/(v+bx/3)\) gives exponent exactly \(-x^2/[2(v+bx/3)]\). Solving the resulting quadratic tail inequality gives \(bL/3+\sqrt{2vL+b^2L^2/9}\), which is bounded by the displayed \(\sqrt{2vL}+2bL/3\). Thus the lemma uses a safe upper cutoff, not an unjustified exact inversion.

For the inverse-probability treatment contrast, conditional randomization gives the predictable difference in means even when both means depend on the past. Its centered absolute value is at most \(1/\epsilon+1\le2/\epsilon\). Because the two assignment indicators cannot both be one, the conditional second moment is at most \(1/p_t+1/(1-p_t)=1/[p_t(1-p_t)]\le1/[\epsilon(1-\epsilon)]\). No cross term needs to be bounded, and the variance itself is no larger.

Using \(L=\log(2T/\alpha)\) assigns failure probability at most \(\alpha/T\) to each date. The union bound therefore covers the random predictable running target at all dates up to the declared horizon. Intersecting with \([-1,1]\) retains the target on this event; it does not require the empirical center to lie there. Summing \(2r_t\) with the elementary square-root and harmonic-series bounds reproduces the manuscript's cumulative-width constants. The separate bound \(2T\) follows pathwise, including the author's explicit treatment of an empty intersection on the failure event.

**Finding:** Supports this theorem. The calculation does not use the drift budget, so it does not by itself establish an improved drift-dependent inference frontier. I did not audit the separate restarted-weights regret theorem or claim that the displayed width bound is sharp. Coverage for a fixed declared \(T\) must not be presented as an infinite-horizon confidence sequence without an additional argument.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.
