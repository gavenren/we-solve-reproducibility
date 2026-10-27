# Audit of the exponential history-information barrier

**Target:** ECON-C23-251-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** The finite-history weighting identity, simultaneous-risk lower bound and low-rank nonidentification example.

**Source identity:** `con_1834a6eb088743bd8a9a8322537d8756` / `rev_4693928af0e64e1597c43752896b646c`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/causal-effects-of-treatment-histories-in-panel-data/attempt-1/r1/index.html).

I checked the backward conditioning in the history weight. On the selected treatment path, consistency replaces the observed outcome by the fixed potential outcome \(Y(h)\). The stipulated randomization condition holds even after conditioning on the entire potential-outcome vector, so the last assignment factor has conditional mean one. Repeating backward removes all factors. This proves \(E[L_hY(h)]=E[Y(h)]\) and \(E[L_h]=1\); merely assuming marginal randomization at each date would not justify the same argument.

The second-moment bound uses \(L_h^2\le\varepsilon^{-k}L_h\), yielding variance order \(\varepsilon^{-k}\), not \(\varepsilon^{-2k}\). The union over \(J=2^k\) histories introduces \(\log J\). To check that logarithm is not solely an artifact, consider the manuscript's alternatives with one elevated history mean. Each observation lands in that history with probability \(1/J\), so the KL of \(n\) observations is at most \(4n\delta^2/J\). The alternatives are separated in sup norm by \(\delta\), and Fano's argument with \(J\) alternatives supplies the additional \(\log J\). This correctly distinguishes simultaneous recovery from one prescribed contrast, whose two-point lower bound has only the \(J/n\) factor.

The saturation regime also matters. Choosing a fixed bounded \(\delta\) when \(n\lesssim J\log J\) keeps the alternatives admissible and gives a constant lower risk; one cannot extrapolate the unsaturated formula to a risk larger than the bounded parameter diameter. The separate \(J=2\) two-point treatment avoids a degenerate small-alphabet entropy argument.

For the low-rank example, both models observe \(D_t=Y_t=U\), but one has potential outcome equal to assigned current treatment and the other always equal to \(U\). The untreated panels are respectively zero and a time-constant unit effect, each rank at most one. Thus the causal effect differs while every observed panel agrees. This directly verifies the claim that low rank alone cannot replace assignment information.

**Finding:** Supports these claims in the strong sequentially randomized experiment and the separate observational counterexample. The review does not extend weighting to latent-confounded panels or establish an optimal compression scheme for structured history interactions.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.
