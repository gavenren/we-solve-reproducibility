# Audit of feedback-selection equivalence and diagnostic conditioning

**Target:** ECON-C23-305-A1, revision r1. **Finding:** Supports the claim. **Checked scope:** The opposite-ATT observational-equivalence construction and estimator-independent conditional error bound.

**Source identity:** `con_c7be81932853446586f94237e6c25196` / `rev_3a541db54e094c8bac06e2562b3a9cf9`. [Pinned manuscript](https://raw.githubusercontent.com/We-Solve/we-solve.github.io/8fae5b83d055c1c430c74c1ca52472de0fea79f3/contributions/validation-of-panel-estimators-under-feedback-selection/attempt-1/r1/index.html).

I checked the two panel models by substitution rather than by relying on their labels. Before treatment, \(\alpha_i=-Z_i\) and \(u_{it}=Z_i\) cancel, so every observed preperiod outcome is zero. Selection \(D_i=1\{Z_i=1\}\) depends on the lagged shock. In model A the untreated post outcome is \(-aZ_i\); adding treatment effect \(a\) gives observed outcome zero for treated units and \(a\) for controls. In model B the untreated outcome is \(a\) for both groups; adding effect \(-a\) gives the identical observed pair. ATT is nevertheless \(a\) versus \(-a\), and errors have mean zero as claimed. Independence of individual effects and shocks is deliberately absent, so this is not a counterexample to a model that adds that restriction.

For any accepted diagnostic event of positive probability, observational equivalence implies the estimator has the same **conditional** distribution in both models, even when the diagnostic and estimator use the same data. If targets differ by more than \(2\epsilon\), their success intervals are disjoint; the two conditional success probabilities sum to at most one. Hence at least one conditional error is at least one half. The manuscript correctly uses a strict target-separation inequality: at equality, the closed success intervals share one point and that elementary argument would need modification.

For difference-in-differences itself, with both groups represented the observed estimate equals \(-a\). It therefore has deterministic error \(2a\) in A, a stronger conclusion than the estimator-independent half-probability statement. Distinguishing these two claims is essential.

Finally \(P(E\mid A)\le P(E)/P(A)\) gives the \(1/\eta\) penalty, and nested events of probabilities \(\delta\le\eta\) attain it. Genuine independent-sample diagnostics remove this selection penalty for each fixed model, but do not remove structural bias or allow the diagnostic to choose an estimator using shared information.

**Finding:** Supports these results under the stated broad feedback class. No practical pretreatment diagnostic is thereby certified, and the review does not establish identification under extra serial or latent-factor restrictions.

This is an independent LLM mathematical review of the named scope, not human peer review or formal verification. Sources and exact revision identifiers are recorded in metadata.json. Reviewer: `/root/econ_b`; exact serving version and reasoning setting unknown. Gaven (@gavenren) requested the review batch. Original review text: CC BY 4.0.
