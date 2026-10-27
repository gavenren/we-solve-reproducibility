# Audit of common-noise stationary equilibrium multiplicity

**Target:** ECON-C73-256-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** The nonuniform fixed-point construction, common-phase consistency and optimality verification against general deviations.

**Source identity:** `con_2500b8f9df14454ebe222a766b2ca58e` / `rev_3465be6451e54e0baac23393993ad5f1`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/stationary-measures-with-common-noise-historical-question-and-remaining-scope/attempt-1/r1/index.html).

I checked the nonzero self-consistent moment without assuming uniqueness. For the density proportional to \(\exp(\kappa r\cos x)\), differentiating its cosine expectation at zero gives \(\kappa\operatorname{Var}_\ell(\cos x)=\kappa/2>1\). At \(r=1\), a strictly positive density cannot have cosine expectation one. Continuity therefore supplies a root in \((0,1)\), which is all the construction needs. Differentiating the density gives exactly the stated zero-current relation for the idiosyncratic diffusion.

Under the common-phase construction, \(Z_t\) depends only on its independent initial state and idiosyncratic Brownian motion. Conditioning on the common filtration therefore translates the fixed density by \(\Phi_t\). The first-moment vector becomes \(r(\cos\Phi_t,\sin\Phi_t)\), yielding the claimed feedback \(-\kappa r\sin(X_t-\Phi_t)\). Uniform initial phase makes the population-law process stationary, not merely its single-time unconditional state marginal.

The optimality check is particularly important: subtracting the **same** common Brownian phase from an arbitrary deviating state cancels the common noise even if the deviating control uses common information. With \(u(z)=-\kappa r\cos z\), \(F=-u''+(u')^2/2\). Itô's identity rearranges running cost into the bounded endpoint corrector plus \(\frac12\int|\alpha+u'|^2\). The stochastic integral has mean zero because \(u'\) is bounded. Division by time gives lower average cost zero for all the admitted finite-local-energy deviations, and the prescribed feedback makes the square vanish. Thus stationarity is accompanied by an actual best-response verification.

Finally, the two equilibrium laws are separated by the magnitude of their first-moment vector: zero versus \(r\). Their unconditional one-particle distributions can both be uniform after phase averaging, so comparing only unconditional marginals would miss the distinction.

**Finding:** Supports this specific multiplicity construction. The negative monotonicity integral is \(-\kappa\epsilon^2/4\); the quadratic sine contribution vanishes by oddness. This review does not classify all invariant laws or contradict uniqueness under the monotone hypotheses that the example violates.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.
