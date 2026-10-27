# Audit of finite-horizon stopping barriers and terminal-boundary claims

**Target:** ECON-C61-246-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** The sign of the verification inequality and the two horizon-uniform quadratic barriers.

**Source identity:** `con_2a90b56e83ba43c2beb703e3ae436bfb` / `rev_5a0cb8d4ef09405ca310c0284c5fef14`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/finite-horizon-drift-control-with-discretionary-stopping/attempt-1/r1/index.html).

For an infimum control problem, I checked the verification direction by completing the square. The candidate's generator plus running cost equals the minimized HJB expression plus \(r(u+\mu v_x/r)^2/2\). If both terms are nonnegative, Itô integration gives \(v(t,x)\) below the expected candidate terminal value plus costs. Replacing the candidate terminal value by the larger stopping payoff preserves the inequality. Thus the stated subsolution is a **lower** bound for the value. Reversing that sign would invalidate the stopping-core argument.

For the tangent-line function \(w\), its slope outside the core has magnitude \(A=\kappa b_-\), and \(\mu^2A^2/(2r)=c\). This makes the exterior minimized generator exactly zero. Inside, the drift-control term is largest in magnitude at the endpoints, where it cancels \(c\), leaving the positive diffusion term \(\sigma^2\kappa/2\). The derivative matches at both joins, so the generalized Itô formula has no derivative-jump local-time term. The bounded slope also supplies the martingale integrability used in the argument. Its terminal value is only required to be below the obstacle, as the manuscript explicitly notes.

For the outer bound, I recomputed the exact short deterministic-delay cost under constant \(u_0=-\mu\kappa x/r\). The linear coefficient is \(c+\sigma^2\kappa/2-\mu^2\kappa^2x^2/(2r)\); the only remaining term is the positive quadratic-in-delay drift displacement cost. Outside \(b_+\), the linear coefficient is negative, so some sufficiently short delay improves on immediate stopping for every strictly positive remaining horizon.

This validates the distinction between the limit of preterminal stopping slices and the terminal slice itself. The preterminal stopping set remains inside the fixed interval \([-b_+,b_+]\), while at maturity every state must stop. Evenness and time monotonicity do not prove interval connectedness, which the author correctly leaves conditional.

**Finding:** Supports the barrier conclusions. The review does not supply a value-solution existence theorem, optimal-feedback admissibility in the general coefficient class, or regularity of an actual moving boundary.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.
