# Audit of the discounted quadratic first integral and stopping transition

**Target:** ECON-C61-288-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** The quadratic subclass's first integral, unique positive boundary, and discounted transversality argument.

**Source identity:** `con_b663853611f94c5aab6242783e6c8c37` / `rev_9f4c970932c44354906ce972e501394e`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/discounted-drift-control-with-discretionary-stopping/attempt-1/r1/index.html).

I checked the first integral independently. With \(C=c/\rho\) and \(U=C-v\), the continuation HJB becomes \(\sigma^2U''+a(U')^2-2\rho U=0\). If \(F(U)=(U')^2\), then \(U''=F'(U)/2\), so \(F\) solves \(\sigma^2F'+2aF=4\rho U\). Direct differentiation of the manuscript's explicit \(F\) satisfies this identity. Its Taylor expansion at zero has leading term \(2\rho U^2/\sigma^2\), which makes the quadrature diverge logarithmically as \(U\downarrow0\). Thus the proposed continuation branch extends to arbitrarily large states rather than ending at a finite location.

The boundary equation equates an increasing \(q^2b^2\) with a strictly decreasing \(F(L-qb^2/2)\) on \(0<b<\sqrt{2L/q}\), with opposite endpoint inequalities. This verifies both existence and uniqueness in the asserted interval and excludes a spurious second root. Value matching and this equation give smooth fit.

On the continuation side, \(v''=-F'(U)/2<0\), while the obstacle is strictly convex. Starting with equal value and slope at \(b\), their slope difference immediately becomes negative; hence \(v<k\) everywhere outside, not merely locally. Inside the proposed stopping region, the HJB residual decreases with \(|x|\) and is positive at the boundary because it replaces the negative continuation curvature by \(q>0\). This checks the obstacle inequality on the whole region.

The threshold case \(K_0=c/\rho\) is also handled correctly: never stopping with zero control attains \(C\), while immediate stopping at zero also has that value. An equality set is not a uniqueness assertion about the optimal strategy. For \(K_0>C\), the equality set is empty.

**Finding:** Supports the displayed construction under its explicit admissibility and generalized-Itô conditions. Bounded \(v\) makes discounted transversality sufficient even without a finite expected hitting time. I did not verify extensions to nonquadratic costs or nonconstant diffusion coefficients, where this first integral need not survive.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.
