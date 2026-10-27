# Scoped review of posterior-mean compactness and the Gaussian boundary

**Target:** ECON-D82-301-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** Feasible-coupling attainment, covariance realization, and strict Gaussian-gap counterexample

**Source identity:** `con_c525442df8164164a6b79ab626f70478` / `rev_9614eb7def3d40599b3794ad66504852`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/general-cost-strategic-disclosure-on-continuous-type-spaces/attempt-1/r1/index.html).

I checked the compactness argument's tail control because the Gaussian prior is unbounded. Conditional Jensen gives
\[
E_\pi\|M\|^4\le E\|\omega\|^4
\]
uniformly over feasible couplings. Together with the fixed state marginal, this yields joint tightness and uniform integrability of joint squared norms. Under weak convergence, bounded continuous truncations pass the conditional-mean identity to the limit; the uniform moment bound removes their tails. Vanishing integrals against every bounded continuous test function imply that the finite signed conditional-mean measure is zero. Thus the limiting coupling is feasible.

For continuous running costs with at most quadratic absolute growth, the same fourth-moment bound makes the tail contribution uniformly small, so their expectations are continuous along feasible weakly convergent sequences. Adding a lower-semicontinuous functional bounded below and finite somewhere gives attainment. Disintegration on the stated standard Borel spaces implements the optimizing coupling by sending its posterior-mean coordinate. This reasoning depends on the kernel cost being invariant under replacement by the joint law of state and posterior mean; extra independent message content can otherwise change that cost.

I recomputed the quadratic cross term using
\(E[\omega M^{\mathsf T}]=E[MM^{\mathsf T}]=T\).
Expanding \(\|A\omega-DM\|^2\) gives the manuscript's affine trace expression. After whitening, observing a unit-variance Gaussian coordinate with independent noise variance \((1-t)/t\) produces posterior-mean variance \(1/(1+(1-t)/t)=t\). Omitting the coordinate at \(t=0\) and observing it exactly at \(t=1\) covers both boundary eigenvalues. Hence every \(0\preceq T\preceq\Sigma_0\) is realized, including singular cases; no positive-noise restriction may be silently imposed at the endpoints.

Finally, revealing the sign of a standard normal produces posterior mean \(\pm\sqrt{2/\pi}\), each with probability one half. The cost zero at its coupling and one elsewhere is lower semicontinuous because the exceptional singleton is closed. A linear Gaussian signal's posterior mean is Gaussian, possibly degenerate, and cannot have that two-point law. This proves the stated strict gap of one. It is a counterexample within the deliberately broad cost class, not evidence against Gaussian sufficiency for conventional covariance costs.

The scoped mathematical statements are supported. Lower semicontinuity alone does not supply convergence from above under finite-signal approximation, and covariance matching does not preserve general nonquadratic objectives.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.

