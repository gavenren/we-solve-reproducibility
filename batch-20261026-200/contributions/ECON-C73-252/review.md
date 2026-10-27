# Audit of reset-tolerant regret and the last-iterate counterexample

**Target:** ECON-C73-252-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** The epoch/block regret summation, adaptive-action concentration and empirical-versus-current-play distinction.

**Source identity:** `con_89fd02117b3947e49aac6fa3cba56fff` / `rev_70f7cfdbe64e4a18abd13ac406aae8dc`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/learning-in-games-and-convergence/attempt-1/r1/index.html).

I checked truncation of the final doubling epoch, where a hidden horizon assumption can enter. If its scheduled length is \(L\), entering it required \(L-1\) earlier rounds in the block and at least one current round, so the actual block length satisfies \(\ell\ge L\). The epoch guarantee \(\log m/\eta+\eta l/8\), with \(l\le L\), is bounded by \(\sqrt{L\log m/2}\). Summing scheduled square roots and using \(L\le\ell\) yields the author's constant \(4\) safely, including a block of one round.

Across at most \(K+1\) blocks, Cauchy–Schwarz gives \(\sum_j\sqrt{\ell_j}\le\sqrt{(K+1)T}\). The switch rule must be predictable, as stated. The pathwise exponential-weights comparison is with each realized full-feedback vector, so opponents may adapt to the past; the stochastic conversion to realized payoffs separately needs independent current draws conditional on that past. Conditioning additionally on opponents' current actions then gives mean-zero payoff-sampling error with range length at most one. This validates the Hoeffding constant and playerwise union bound.

The limiting equilibrium notion is coarse correlated equilibrium because the learner controls fixed-action external deviations. No swap-regret conclusion follows without the extra assumed blockwise swap guarantee. The manuscript keeps that extension conditional.

For the four-profile matching-pennies cycle, I checked every full-cycle deviation: each fixed action wins twice, and conditional on either own action the opponent plays each action once, so every swap map also wins twice. Any residual prefix has at most three rounds, bounding regret by three. Yet each current marginal is a point mass, at \(\ell_1\) distance one from the unique uniform Nash marginal. This is a valid counterexample to inference from realized regret alone, not a claim that the constructed path is a universally no-regret algorithm.

**Finding:** Supports these scoped claims. The review does not establish last-iterate convergence under arbitrary switching, partial feedback, or a game-uniform metric-distance constant. Those require additional assumptions beyond the incentive bounds checked here.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.
